from kivy.event import EventDispatcher
from kivy.properties import StringProperty
from controls.models.updownfactor import UpDownFactor as UpDownModel
import re

model = UpDownModel(10, -10)
re_up = re.compile(r'\d+')
re_down = re.compile(r'^(-)?\d+$')


class UpDownFactor(EventDispatcher):
    value_new = StringProperty('0')
    value_old = StringProperty('0')
    factor_up = StringProperty('10')
    factor_down = StringProperty('-10')

    def cmd_press_new(self, *cmd_args):
        self._coerce_new(cmd_args[0])
        self._update_values()

    def cmd_press_up(self, *cmd_args):
        self._coerce_up(cmd_args[0])
        model.value_new += model.factor_up
        self._update_values()

    def cmd_press_down(self, *cmd_args):
        self._coerce_down(cmd_args[0])
        model.value_new += model.factor_down
        self._update_values()

    def cmd_focus_up(self, *cmd_args):
        self._coerce_up(cmd_args[0])

    def cmd_focus_down(self, *cmd_args):
        self._coerce_down(cmd_args[0])

    def _update_values(self):
        self.value_old, self.value_new = str(model.value_old), str(model.value_new)

    def _coerce_up(self, value):
        coerce = 1
        mo = re_up.search(value)
        if mo:
            var = int(mo.group())
            if var == 0:
                pass

            elif var < 0:
                coerce = var * -1

            else:
                coerce = var

        model.factor_up = coerce
        self.factor_up = '...'
        self.factor_up = str(model.factor_up)

    def _coerce_down(self, value):
        coerce = -1
        mo = re_down.search(value)
        if mo:
            var = int(mo.group())
            if var == 0:
                pass

            elif 0 < var:
                coerce = var * -1

            else:
                coerce = var

        model.factor_down = coerce
        self.factor_down = '...'
        self.factor_down = str(model.factor_down)

    def _coerce_new(self, value):
        coerce = 0
        mo = re_down.search(value)
        if mo:
            var = int(mo.group())
            coerce = var

        model.value_new = coerce
        self.value_new = '...'
        self.value_new = str(model.value_new)