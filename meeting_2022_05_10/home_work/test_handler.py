from hw_handler import get_handler, HandlerInterface


class TestHandler:
    def assertEqual(self, arg1, arg2):
        assert arg1 == arg2

    def setup_method(self):
        self.handler: HandlerInterface = get_handler()

    def test_1(self):
        self.assertEqual("two", self.handler.handle(1))

    def test_2(self):
        self.assertEqual("eine", self.handler.handle(2))

    def test_3(self):
        self.assertEqual("six", self.handler.handle(3))

    def test_4(self):
        self.assertEqual("two", self.handler.handle(4))

    def test_5(self):
        self.assertEqual("ten", self.handler.handle(5))

    def test_6(self):
        self.assertEqual("three", self.handler.handle(6))

    def test_7(self):
        self.assertEqual("teen", self.handler.handle(7))

    def test_8(self):
        self.assertEqual("four", self.handler.handle(8))

    def test_9(self):
        self.assertEqual("teen", self.handler.handle(9))

    def test_10(self):
        self.assertEqual("five", self.handler.handle(10))

    def test_11(self):
        self.assertEqual("ty-two", self.handler.handle(11))

    def test_12(self):
        self.assertEqual("six", self.handler.handle(12))

    def test_13(self):
        self.assertEqual("ty-six", self.handler.handle(13))

    def test_14(self):
        self.assertEqual("ven", self.handler.handle(14))

    def test_15(self):
        self.assertEqual("ty", self.handler.handle(15))

    def test_16(self):
        self.assertEqual("eight", self.handler.handle(16))

    def test_17(self):
        self.assertEqual("ty-four", self.handler.handle(17))

    def test_18(self):
        self.assertEqual("nine", self.handler.handle(18))

    def test_19(self):
        self.assertEqual("ty-eight", self.handler.handle(19))

    def test_20(self):
        self.assertEqual("ten", self.handler.handle(20))

    def test_21(self):
        self.assertEqual("ty-two", self.handler.handle(21))
