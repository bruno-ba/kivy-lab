import kivy
from kivy.app import App
from kivy.properties import NumericProperty
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.core.window import Window

kivy.require('1.11.1')

Window.clearcolor = [0, 0, .2, 1]


class UpDown(Widget):
    """
    simples contador que adiciona um fator para incremento e outro fator para decremento, podendo ser alterado pelas
    caixas de texto
    """
    current_value = NumericProperty(0)  # valor atual do contador
    up_factor = NumericProperty(1)  # fator de subida
    down_factor = NumericProperty(-1)  # fator de descida

    def set_factor(self, value: str, direction: bool) -> None:  # configura valores para os fatores

        def safe_cast(val, to_type, default=None):
            try:
                return to_type(val)

            except (ValueError, TypeError):
                return default

        factor = safe_cast(value, int, 0)

        if factor == 0:
            if direction:
                self.up_factor = 0
                self.up_factor = 1

            else:
                self.down_factor = 0
                self.down_factor = -1

        else:
            factor = abs(factor)

            if direction:
                self.up_factor = 0
                self.up_factor = factor

            else:
                self.down_factor = 0
                self.down_factor = factor * -1

    def increment_current_value(self, direction: bool) -> None:  # incrementa ou decrementa o valor corrente
        self.current_value += self.up_factor if direction else self.down_factor


code = """
<FactorButton@BoxLayout>:
    orientation: 'vertical'
    command_btn: None
    command_txt: None
    command_arg : None
    factor: None
    Button:
        text: str(root.factor)
        on_press: root.command_btn(root.command_arg)
    TextInput:
        size_hint_y: .5
        text: str(root.factor)
        input_filter: 'int'
        multiline: False
        on_text_validate: root.command_txt(self.text, root.command_arg)
        on_focus: root.command_txt(self.text, root.command_arg)

<UpDown@Widget>:
    BoxLayout:
        orientation:'vertical'
        size_hint: (None, None)
        size:(root.width, root.height)
           
        Label:
            size_hint_y: .2
            text: str(root.current_value)
            
        BoxLayout:
            orientation: 'horizontal'
                
            FactorButton:
                command_btn: root.increment_current_value
                command_txt: root.set_factor
                command_arg: False
                factor: root.down_factor
                
            FactorButton:
                command_btn: root.increment_current_value
                command_txt: root.set_factor
                command_arg: True
                factor: root.up_factor
                
UpDown:
"""


class TestingApp(App):
    def build(self):
        return Builder.load_string(code)


if __name__ == '__main__':
    TestingApp().run()
