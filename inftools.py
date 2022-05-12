import time


class Counter:
    def __init__(self, start=0, step=1, name="Unnamed counter"):
        self._start = start
        self._step = step
        self._value = start
        self._name = name

    def increase(self, multiplier=1, bonus=0):
        self._value += self._step * multiplier + bonus
        return self

    def __repr__(self):
        return f"[{self._name}]: {self._value}"

    def show(self):
        print(self.__repr__())
        return self

    def value(self):
        return self._value


'''
class Log:
    __file = f"{__file__.replace('.py', '').replace('.cpy', '')}-log.txt"

    _ = open(__file, "wt")
    _.close()

    __show_debug = True
    __show_main = True
    __show_important = True

    @classmethod
    def __values_to_str(cls, *values):
        return " ".join(list(values))

    @classmethod
    def debug(cls, *values):
        to_log = f"[Log/Debug]: {cls.__values_to_str(*values)}\n"
        if cls.__show_debug:
            print(to_log, end="")
        f = open(cls.__file, "at", encoding="utf-8")
        f.write(f"{time.strftime('%d.%m.%Y %H:%M:%S')} ")
        f.write(to_log)
        f.close()

    @classmethod
    def log(cls, *values):
        to_log = f"[Log/Main]: {cls.__values_to_str(*values)}\n"
        if cls.__show_main:
            print(to_log, end="")
        f = open(cls.__file, "at", encoding="utf-8")
        f.write(f"{time.strftime('%d.%m.%Y %H:%M:%S')} ")
        f.write(to_log)
        f.close()

    @classmethod
    def important(cls, *values):
        to_log = "-" * 16 + f"\n" \
                            f"\n" \
                            f"[Log/Important]: {cls.__values_to_str(*values)}\n" \
                            f"\n" + \
                 f"-" * 16 + "\n"
        if cls.__show_important:
            print(to_log, end="")
        f = open(cls.__file, "at", encoding="utf-8")
        f.write("-" * 16 + f" {time.strftime('%d.%m.%Y %H:%M:%S')} ")
        f.write(to_log)
        f.close()

    @classmethod
    def enableDebugPrinting(cls):
        cls.__show_debug = True

    @classmethod
    def disableDebugPrinting(cls):
        cls.__show_debug = False

    @classmethod
    def enableMainPrinting(cls):
        cls.__show_main = True

    @classmethod
    def disableMainPrinting(cls):
        cls.__show_main = False

    @classmethod
    def enableImportantPrinting(cls):
        cls.__show_important = True

    @classmethod
    def disableImportantPrinting(cls):
        cls.__show_important = False

    @classmethod
    def enableAllPrinting(cls):
        cls.__show_debug = True
        cls.__show_main = True
        cls.__show_important = True

    @classmethod
    def disableAllPrinting(cls):
        cls.__show_debug = False
        cls.__show_main = False
        cls.__show_important = False
'''


class NumberSystems:
    @classmethod
    def from_base_to_base(cls, number, from_base=10, to_base=10):
        number_10 = int(str(number), from_base)

        if to_base != 10:
            alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            result = ""

            while number_10 > 0:
                result = alphabet[number_10 % to_base] + result
                number_10 //= to_base

            return result
        else:
            return number_10

    @classmethod
    def from_10_to_2(cls, number: int):
        return cls.from_base_to_base(number, 10, 2)

    @classmethod
    def from_2_to_10(cls, number: str):
        return cls.from_base_to_base(number, 2, 10)

    @classmethod
    def from_10_to_3(cls, number: int):
        return cls.from_base_to_base(number, 10, 3)

    @classmethod
    def from_3_to_10(cls, number: str):
        return cls.from_base_to_base(number, 3, 10)

    @classmethod
    def from_10_to_4(cls, number: int):
        return cls.from_base_to_base(number, 10, 4)

    @classmethod
    def from_4_to_10(cls, number: str):
        return cls.from_base_to_base(number, 4, 10)

    @classmethod
    def from_10_to_5(cls, number: int):
        return cls.from_base_to_base(number, 10, 5)

    @classmethod
    def from_5_to_10(cls, number: str):
        return cls.from_base_to_base(number, 5, 10)

    @classmethod
    def from_10_to_6(cls, number: int):
        return cls.from_base_to_base(number, 10, 6)

    @classmethod
    def from_6_to_10(cls, number: str):
        return cls.from_base_to_base(number, 6, 10)

    @classmethod
    def from_10_to_7(cls, number: int):
        return cls.from_base_to_base(number, 10, 7)

    @classmethod
    def from_7_to_10(cls, number: str):
        return cls.from_base_to_base(number, 7, 10)

    @classmethod
    def from_10_to_8(cls, number: int):
        return cls.from_base_to_base(number, 10, 8)

    @classmethod
    def from_8_to_10(cls, number: str):
        return cls.from_base_to_base(number, 8, 10)

    @classmethod
    def from_10_to_9(cls, number: int):
        return cls.from_base_to_base(number, 10, 9)

    @classmethod
    def from_9_to_10(cls, number: str):
        return cls.from_base_to_base(number, 9, 10)

    @classmethod
    def from_10_to_11(cls, number: int):
        return cls.from_base_to_base(number, 10, 11)

    @classmethod
    def from_11_to_10(cls, number: str):
        return cls.from_base_to_base(number, 11, 10)

    @classmethod
    def from_10_to_12(cls, number: int):
        return cls.from_base_to_base(number, 10, 12)

    @classmethod
    def from_12_to_10(cls, number: str):
        return cls.from_base_to_base(number, 12, 10)

    @classmethod
    def from_10_to_13(cls, number: int):
        return cls.from_base_to_base(number, 10, 13)

    @classmethod
    def from_13_to_10(cls, number: str):
        return cls.from_base_to_base(number, 13, 10)

    @classmethod
    def from_10_to_14(cls, number: int):
        return cls.from_base_to_base(number, 10, 14)

    @classmethod
    def from_14_to_10(cls, number: str):
        return cls.from_base_to_base(number, 14, 10)

    @classmethod
    def from_10_to_15(cls, number: int):
        return cls.from_base_to_base(number, 10, 15)

    @classmethod
    def from_15_to_10(cls, number: str):
        return cls.from_base_to_base(number, 15, 10)

    @classmethod
    def from_10_to_16(cls, number: int):
        return cls.from_base_to_base(number, 10, 16)

    @classmethod
    def from_16_to_10(cls, number: str):
        return cls.from_base_to_base(number, 16, 10)


class Numbers:
    @classmethod
    def difference(cls, a, b):
        return abs(a - b)

    @classmethod
    def average(cls, *abc):
        return sum(abc) / len(abc)


class ClockTimer:
    def __init__(self, name="Unnamed timer"):
        self._start = time.time()
        self._name = name

    def reset(self):
        self._start = time.time()

    def difference(self):
        return time.time() - self._start

    def __repr__(self):
        return f"[{self._name}]: +{self.difference()}s"

    def show(self):
        print(self.__repr__())


Timer = ClockTimer(name="Timer")
