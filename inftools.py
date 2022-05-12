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
