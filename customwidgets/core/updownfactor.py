from kivy.event import EventDispatcher
from kivy.properties import NumericProperty
from enum import Enum
import re


coerce_regex = re.compile(r'^(-)?\d+$')


class UpDownFactorCore(EventDispatcher):
    current_value = NumericProperty(0)
    before_value = NumericProperty(0)
    factor_pos = NumericProperty(1)
    factor_neg = NumericProperty(-1)
    factor_current = NumericProperty(0)

    def update_factor_pos(self, value):
        is_coerced,  self.factor_pos = UpDownFactorCore.coerce_by_signal(value=value, coerce_signal=1)
        return is_coerced, self.factor_pos

    def update_factor_neg(self, value):
        is_coerced, self.factor_neg = UpDownFactorCore.coerce_by_signal(value=value, coerce_signal=-1)
        return is_coerced, self.factor_neg

    def update_factor_current(self, value):
        is_coerced, self.factor_current = UpDownFactorCore.coerce_by_signal(value=value, coerce_signal=0)
        return is_coerced, self.factor_current

    def increase_current_value(self):
        self.before_value, self.current_value = self.current_value, self.current_value + self.factor_pos

    def decrease_current_value(self):
        self.before_value, self.current_value = self.current_value, self.current_value + self.factor_neg

    def set_current_value(self):
        self.before_value, self.current_value = 0, self.factor_current

    @staticmethod
    def coerce_by_signal(value, coerce_signal):

        def get_signal(num):
            if num == 0:
                return 0

            elif abs(num) == num:
                return 1

            elif abs(num) != num:
                return -1

            else:
                raise ValueError(f'\nerror <- num: {num}, not valid')

        coerced_value = coerce_signal
        is_coerced = True
        mo = coerce_regex.search(value)

        if mo:
            mog = int(mo.group())
            signal = get_signal(mog)

            if coerce_signal in [0, signal]:
                coerced_value = mog
                is_coerced = False

            else:
                coerced_value = mog * -1

        return is_coerced, coerced_value
