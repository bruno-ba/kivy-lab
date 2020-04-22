class UpDownFactor:
    def __init__(self, up_factor=1, down_factor=-1):
        self._value_new, self._value_old, self._factor_up, self._factor_down = 0, 0, 1, -1
        self.factor_up = up_factor
        self.factor_down = down_factor

    @property
    def value_new(self):
        return self._value_new

    @value_new.setter
    def value_new(self, value):
        self._value_old = self._value_new
        self._value_new = value

    @property
    def value_old(self):
        return self._value_old

    @property
    def factor_up(self):
        return self._factor_up

    @factor_up.setter
    def factor_up(self, value):
        self._factor_up = value

    @property
    def factor_down(self):
        return self._factor_down

    @factor_down.setter
    def factor_down(self, value):
        self._factor_down = value
