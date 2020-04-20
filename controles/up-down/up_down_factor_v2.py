import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty, StringProperty
from kivy.event import EventDispatcher
from kivy.lang import Builder
from kivy.core.window import Window
import re

kivy.require('1.11.1')


class UpDownFactor(EventDispatcher):
    down_factor_regex = re.compile(r'^(-)?\d+$')  # aceita inteiros e com ou sem sinal negativo
    up_factor_regex = re.compile(r'\d+')  # aceita inteiros
    up_factor = NumericProperty(1)  # 1 if value == 0 else value
    down_factor = NumericProperty(-1)  # -1 if value == 0 else ((value * -1) if 0 < value else value)
    current_value = NumericProperty(0)

    def up_current_value(self):
        self.current_value += self.up_factor

    def down_current_value(self):
        self.current_value += self.down_factor

    @staticmethod
    def up_factor_coerce(value: int) -> int:
        if 0 < value:
            return value
        else:
            return 1

    @staticmethod
    def down_factor_coerce(value: int) -> int:
        if value < 0:
            return value
        else:
            if 0 < value:
                return value * -1
            else:
                return -1

    @staticmethod
    def up_factor_convert(value: str) -> int:
        fac_mo = UpDownFactor.up_factor_regex.search(value)
        if fac_mo:
            return UpDownFactor.up_factor_coerce(int(fac_mo.group()))
        else:
            return 1

    @staticmethod
    def down_factor_convert(value: str) -> int:
        fac_mo = UpDownFactor.down_factor_regex.search(value)
        if fac_mo:
            return UpDownFactor.down_factor_coerce(int(fac_mo.group()))
        else:
            return -1


class FactorComp(BoxLayout):
    factor = StringProperty('0')
    focus_command = None
    press_command = None

    def on_press_callback(self):
        if self.press_command:
            self.press_command()
            print('has_command')
        else:
            print('not_has_command')

    def on_focus_callback(self, arg):
        value = arg
        if value:
            print('focus')
        else:
            print('lost focus')
            if self.focus_command:
                self.focus_command()


class UpDownFactorControl(BoxLayout):
    current_value = StringProperty('0')

    def __init__(self, **kwargs):
        super(UpDownFactorControl, self).__init__(**kwargs)
        self.ud_fc = UpDownFactor()
        self.ud_fc.bind(current_value=self.current_value_callback)

    def current_value_callback(self, element, value):
        self.current_value = str(value)

    def up_factor_command(self):
        self.ud_fc.up_current_value()
        print(f'up_command')

    def down_factor_command(self):
        self.ud_fc.down_current_value()
        print(f'down_command')


code = """
<FactorComp>:
    orientation: 'vertical'

    Button:
        id: btn_factor
        text: root.factor
        disabled: txt_factor.focus
        on_press: root.on_press_callback()
    
    TextInput:
        id: txt_factor
        size_hint_y: .5
        text: root.factor
        input_filter: 'int'
        multiline: False
        on_focus: root.on_focus_callback(args[1])
        

<UpDownFactorControl>:
    orientation: 'vertical'
    
    Label:
        text: root.current_value
    
    BoxLayout:
        orientation: 'horizontal'
        
        FactorComp:
            press_command: root.down_factor_command
    
        FactorComp:
            press_command: root.up_factor_command
            
UpDownFactorControl:
"""


class TestingApp(App):
    def build(self):
        return Builder.load_string(code)


if __name__ == '__main__':
    Window.clearcolor = [0, 0, .2, 1]
    TestingApp().run()
