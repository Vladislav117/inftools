import os
import shutil
import time
import argparse
import zipfile


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


class Timers:
    main = Timer
    t1 = ClockTimer(name="Timer 1")
    t2 = ClockTimer(name="Timer 2")
    t3 = ClockTimer(name="Timer 3")
    t4 = ClockTimer(name="Timer 4")


class Input:
    @classmethod
    def value(cls, type=str, file=None):
        if file is None:
            value = input(">>> ")
            return type(value)
        else:
            f = open(file, encoding="utf-8")
            value = f.read()
            f.close()
            return type(value)

    @classmethod
    def values(cls, type=str, splitter=" ", file=None):
        if file is None:
            values = input(">>> ")
            values = values.split(splitter)
            return list(map(type, values))
        else:
            f = open(file, encoding="utf-8")
            values = f.read()
            values = values.split(splitter)
            f.close()
            return list(map(type, values))

    @classmethod
    def rows_of_values(cls, type=str, splitter=" ", file=None):
        if file is None:
            rows = list()
            row_index = 0
            while True:
                values = input(f"(Row {row_index}) >>> ")
                if values == "":
                    break
                values = values.split(splitter)
                rows.append(list(map(type, values)))
                row_index += 1
            return rows
        else:
            rows = list()
            f = open(file, encoding="utf-8")
            for line in f:
                values = line.split(splitter)
                rows.append(list(map(type, values)))
            f.close()
            return rows

    @classmethod
    def integer(cls, file=None):
        return Input.value(type=int, file=file)

    @classmethod
    def integers(cls, splitter=" ", file=None):
        return Input.values(type=int, splitter=splitter, file=file)

    @classmethod
    def rows_of_integers(cls, splitter=" ", file=None):
        return Input.rows_of_values(type=int, splitter=splitter, file=file)

    @classmethod
    def string(cls, file=None):
        return Input.value(type=str, file=file)

    @classmethod
    def strings(cls, splitter=" ", file=None):
        return Input.values(type=str, splitter=splitter, file=file)

    @classmethod
    def rows_of_strings(cls, splitter=" ", file=None):
        return Input.rows_of_values(type=str, splitter=splitter, file=file)

    @classmethod
    def float(cls, file=None):
        return Input.value(type=float, file=file)

    @classmethod
    def floats(cls, splitter=" ", file=None):
        return Input.values(type=float, splitter=splitter, file=file)

    @classmethod
    def rows_of_floats(cls, splitter=" ", file=None):
        return Input.rows_of_values(type=float, splitter=splitter, file=file)

    @classmethod
    def boolean(cls, file=None):
        return Input.value(type=bool, file=file)

    @classmethod
    def booleans(cls, splitter=" ", file=None):
        return Input.values(type=bool, splitter=splitter, file=file)

    @classmethod
    def rows_of_booleans(cls, splitter=" ", file=None):
        return Input.rows_of_values(type=bool, splitter=splitter, file=file)


if __name__ == '__main__':
    arguments_parser = argparse.ArgumentParser("inftools")
    arguments_parser.add_argument("-a", "--action", help="Action to do", default="none")
    arguments_parser.add_argument("-t", "--task", help="Task number(s) to work with", default="*")
    args = arguments_parser.parse_args()

    if args.action == "none":
        pass

    elif args.action in ("init", "prep", "initialize", "prepare", "install"):
        if os.path.exists(".inftools"):
            print()
            print("YOU CANNOT INITIALIZE INFTOOLS WHILE '.inftools' FILE EXISTS. REMOVE FILE BEFORE INITIALIZATION.")
            print("BE CAREFUL! INITIALIZATION WILL CLEAR YOUR SOLUTIONS AND ANSWERS!")
            print()

            exit(0)

        f = open(".inftools", "wt", encoding="utf-8")
        f.write("To initialize inftools again you should remove this file.")

        f = open("answers.txt", "wt", encoding="utf-8")
        f.write("\n".join([f"[] #{i}: " for i in range(1, 26)]) + "\n[] [] # 26: \n[] [] # 27: ")
        f.close()

        f = open("notes.txt", "wt", encoding="utf-8")
        f.close()

        if not os.path.exists("solutions"):
            os.mkdir("solutions")

        if not os.path.exists("backups"):
            os.mkdir("backups")

        task_numbers = [2, 5, 6, 7, 8, 11, 12, 14, 15, 16, 17, 19, 20, 21, 22, 23, 24, 25]

        for i in task_numbers:
            f = open(f"solutions/z{i}.py", "wt")
            f.write(f"#\n# Task {i}\n#\n")
            f.close()

    elif args.action in ("pattern",):
        pass  # Working with task number(s)

    elif args.action in ("clear", "uninstall"):
        if os.path.exists(".inftools"):
            print()
            print("YOU CANNOT CLEAR ALL FILES WHILE '.inftools' FILE EXISTS. REMOVE FILE BEFORE CLEARING.")
            print("BE CAREFUL! IT WILL DESTROY ALL GENERATED FILES WITH YOUR SOLUTIONS AND ANSWERS!")
            print()

            exit(0)

        if os.path.exists("solutions"):
            shutil.rmtree("solutions")
        os.remove("answers.txt")
        os.remove("notes.txt")

    elif args.action in ("calc", "result", "results", "check", "answers"):
        if os.path.exists("answers.txt"):
            f = open("answers.txt")
            text = f.read()
            f.close()

            good = text.count("[+]") + text.count("[v]")

            translation = {0: 0, 1: 7, 2: 14, 3: 20, 4: 27, 5: 34, 6: 40, 7: 43, 8: 46, 9: 48, 10: 51, 11: 54, 12: 56,
                           13: 59,
                           14: 62, 15: 64, 16: 67, 17: 70, 18: 72, 19: 75, 20: 78, 21: 80, 22: 83, 23: 85, 24: 88,
                           25: 90, 26: 93, 27: 95, 28: 98, 29: 100}

            print("-" * 32)
            print()
            print("Results: ")
            print()
            print(f"Primary score: {good}")
            print(f"Secondary score: {translation[good]}")
            print()
            print(f"=== TOTAL: {translation[good]}/100 ===")
            print()
            print("-" * 32)

    elif args.action in ("pack", "zip", "arch", "archive"):
        f = zipfile.ZipFile(f"archived-{time.strftime('%d.%m.%Y-%H.%M.%S')}.zip", "w")
        for address, dirs, files in os.walk('.\\'):
            for name in files:
                file = os.path.join(address, name)
                if not file.startswith(".\\.git") and not file.startswith(".\\.idea") and \
                    not file.startswith(".\\.gitignore") and not file.startswith(".\\README.md") and \
                        not file.endswith(".zip") and not file.startswith(".\\backups"):
                    f.write(file)
        f.close()

    elif args.action in ("backup",):
        f = zipfile.ZipFile(f"backups/backup-{time.strftime('%d.%m.%Y-%H.%M.%S')}.zip", "w")
        for address, dirs, files in os.walk('.\\'):
            for name in files:
                file = os.path.join(address, name)
                if not file.startswith(".\\.git") and not file.startswith(".\\.idea") and \
                        not file.startswith(".\\.gitignore") and not file.startswith(".\\README.md") and \
                        not file.endswith(".zip") and not file.startswith(".\\backups"):
                    f.write(file)
        f.close()




Timer.reset()
