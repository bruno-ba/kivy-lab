import kivy
import re
from kivy.app import App
from kivy.properties import NumericProperty, BooleanProperty
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
    down_factor_regex = re.compile(r'^(-)?([1-9])+0*$')  # aceita inteiros e com ou sem sinal negativo
    up_factor_regex = re.compile(r'\d+')  # aceita inteiros
    current_value = NumericProperty(0)  # valor atual do contador
    up_factor = NumericProperty(1)  # fator de subida
    down_factor = NumericProperty(-1)  # fator de descida
    up_lock = BooleanProperty(False)  # aciona o bloqueio do botão up
    down_lock = BooleanProperty(False)  # aciona o bloqueio do botão down

    def set_factor(self, value: str, direction: bool) -> None:  # configura valores para os fatores up e down

        if direction:
            self.up_lock = not self.up_lock
            up_mo = UpDown.up_factor_regex.search(value)
            self.up_factor = 0

            if up_mo:
                uf = int(up_mo.group())
                self.up_factor = 1 if uf <= 0 else uf

            else:
                self.up_factor = 1

        else:
            self.down_lock = not self.down_lock
            down_mo = UpDown.down_factor_regex.search(value)
            self.down_factor = 0

            if down_mo:
                df = int(down_mo.group())
                self.down_factor = df if df < 0 else df * -1

            else:
                self.down_factor = -1

    def increment_current_value(self, direction: bool) -> None:  # incrementa ou decrementa o valor corrente
        self.current_value += self.up_factor if direction else self.down_factor


code = """
<FactorButton@BoxLayout>:
    orientation: 'vertical'
    command_btn: None
    command_txt: None
    command_arg : None
    factor: None
    disabled_btn: True
    
    Button:
        text: str(root.factor)
        on_press: root.command_btn(root.command_arg)
        disabled: root.disabled_btn
        
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
                disabled_btn: root.down_lock
                
            FactorButton:
                command_btn: root.increment_current_value
                command_txt: root.set_factor
                command_arg: True
                factor: root.up_factor
                disabled_btn: root.up_lock
                
UpDown:
"""


class TestingApp(App):
    def build(self):
        return Builder.load_string(code)


if __name__ == '__main__':
    TestingApp().run()
