import datetime

FORMAT = "%H:%M:%S"
storage_dict = {}


def check_correct_data(data):
    """packet validation"""
    if len(data) != 3:
        print("wrong packet length")
        return False
    elif None in data:
        print("wrong package data")
        return False
    else:
        return True


def get_param_distance():
    """get parametrs of passed way"""
    day_steps = 0
    for key, value in storage_dict.items():
        day_steps += value["steps"]
    dist_km = (day_steps + 0.65) / 1000
    spent_calories = dist_km * 200
    return day_steps, dist_km, spent_calories


def accept_package(data):
    """get data package"""
    if check_correct_data(data):
        print("package is valid")
        time, steps, pulse = data
        pack_time = datetime.datetime.strptime(time, FORMAT)
        if pack_time.time() not in storage_dict and (
            not storage_dict or pack_time.time() > max(storage_dict)
        ):
            storage_dict[pack_time.time()] = {"steps": steps}
            day_steps, dist_km, spent_calories = get_param_distance()
            print(
                f"""
                  Time: {pack_time.time()}.
                  You have completed {day_steps} steps.
                  Your summary distance is {dist_km}. 
                  You burned {spent_calories}.
                  """
            )


package = ("11:00:01", 302, 100)
package1 = ("11:00:02", 302, 100)
accept_package(package)
accept_package(package1)
