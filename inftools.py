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
