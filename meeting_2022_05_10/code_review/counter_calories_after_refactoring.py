""" Don't forget to tell about this way

1. clean/dirty functions : storage_dict
2. magic numbers: 200 and 0.65 
3. long if: accept_package
4. single responsibility: accept_package 
5. naming: check_correct_data
6. typization, show example of useless typization


The refactoring plan : 
1. class instead of sets of functions
2. Magic number to constant 
3. blured responsibility (datetime and checking storage time order in accept should be in validation)
4. long if to logic variables 
5. useless loop in get_param_dict (loop should should have single responsibility <= 2 lines)
   5.1 Ask about how to solve
   5.2.Change value from dict to int and use sum instead of loop
6. Single responsibility print -> in other method 
7. Naming (check_correct_data -> is_data_valid, accept_package -> process_package, get_param_distance -> get_summary_data)

*** 
8. real typing
8.1. class for data package 
8.2 class for data view 
9. validation data package 
10. validation in handler 
11. a view class instead of print
12. a controller class as a glue 
13. abstract classes as an interface
14. project structure (classes in their folders)

*** OUTPUT 
Time: 11:00:01.
You have completed 302 steps.
Your summary distance is 0.502. 
You burned 0.32630000000000003.


Time: 11:00:02.
You have completed 604 steps.
Your summary distance is 0.804. 
You burned 0.5226000000000001.
"""

import datetime
from abc import ABC, abstractmethod
from cgitb import handler
from dataclasses import dataclass, field
from typing import Dict, Optional, Tuple


@dataclass
class DataPackage:
    TIME_FORMAT = "%H:%M:%S"
    MAXIMUM_PULSE_BEATS_SECOND = 250

    time_str: str
    steps: int
    pulse: int
    time_datetime: datetime.time = field(init=False)

    def __post_init__(self):
        self.time_datetime = datetime.datetime.strptime(
            self.time_str, DataPackage.TIME_FORMAT
        ).time()

    def is_valid(self):
        if not self.steps >= 0:
            return False

        if not 0 < self.pulse < DataPackage.MAXIMUM_PULSE_BEATS_SECOND:
            return False

        return True


@dataclass(frozen=True)
class ViewDataPackage:
    time: datetime.time
    completed_steps: int
    traveled_path_km: int
    burned_calories: int


class TrackerView(ABC):
    @abstractmethod
    def print(self, data: ViewDataPackage):
        """provide respresenation of give data"""


class TrackerHandler(ABC):
    @abstractmethod
    def process_package(self, data_package: ViewDataPackage) -> ViewDataPackage:
        """process given data_package to return data for summary representation"""


class TrakerConsoleView(TrackerView):
    def print(self, data: ViewDataPackage):
        print(
            f"Time: {data.time}.\n"
            f"You have completed {data.completed_steps} steps.\n"
            f"Your summary distance is {data.traveled_path_km} km.\n"
            f"You burned {data.burned_calories} calories.\n"
        )


class TrackerController:
    def __init__(self, handler: TrackerHandler, view: TrackerView):
        self.view = view
        self.handler = handler

    def accept_package(self, package: Tuple[str, int, int]):
        data_package = DataPackage(
            time_str=package[0], steps=package[1], pulse=package[2]
        )

        view_data: Optional[ViewDataPackage] = None

        if data_package.is_valid():
            view_data = self.handler.process_package(data_package)

        if view_data is not None:
            self.view.print(view_data)


class TrackerSummaryHandler(TrackerHandler):
    CALORIES_PER_KM = 200
    STEP_LENGTH_M = 0.65
    STORAGE_FORMAT = Dict[datetime.time, int]

    def __init__(self):
        self.storage_dict: TrackerSummaryHandler.STORAGE_FORMAT = {}

    def is_data_valid(self, data: DataPackage):
        """packet validation"""

        if not self.storage_dict:
            return True

        is_next_package = data.time_datetime > max(self.storage_dict)

        is_pacckage_in_storage = data.time_datetime not in self.storage_dict

        if not is_next_package or not is_pacckage_in_storage:
            return False

        return True

    def get_summary_data(self, storage_dict: STORAGE_FORMAT) -> Tuple[int, int, int]:

        """get parametrs of passed way"""
        day_steps = sum(storage_dict.values())
        dist_km = (day_steps + TrackerSummaryHandler.CALORIES_PER_KM) / 1000
        spent_calories = dist_km * TrackerSummaryHandler.STEP_LENGTH_M

        return day_steps, dist_km, spent_calories

    def process_package(self, data_package: DataPackage) -> ViewDataPackage:
        """get data package"""
        if self.is_data_valid(data_package):

            self.storage_dict[data_package.time_datetime] = data_package.steps
            day_steps, dist_km, spent_calories = self.get_summary_data(
                self.storage_dict
            )

            return ViewDataPackage(
                time=data_package.time_datetime,
                completed_steps=day_steps,
                traveled_path_km=dist_km,
                burned_calories=spent_calories,
            )


def main():
    package = ("11:00:01", 302, 100)
    package1 = ("11:00:02", 302, 100)

    controller = TrackerController(TrackerSummaryHandler(), TrakerConsoleView())
    controller.accept_package(package)
    controller.accept_package(package1)


if __name__ == "__main__":
    main()
