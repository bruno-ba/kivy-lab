from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.properties import StringProperty
from kivy.lang import Builder
from customwidgets.core.updownfactor import UpDownFactorCore


class ValueFactor(BoxLayout):
    text = StringProperty('text')
    info = StringProperty('info')

    def __init__(self, **kwargs):
        super(ValueFactor, self).__init__(**kwargs)
        self.press_cmd = None
        self.focus_cmd = None

    def press_callback(self):
        if self.press_cmd:
            self.press_cmd()

    def focus_callback(self, txt, focus):
        if self.focus_cmd and not focus:
            is_coerced, coerced_value = self.focus_cmd(value=txt)
            print(f'is_coerced:{is_coerced} | coerced_value:{coerced_value}')
            if is_coerced:
                self.text = '...'

            self.text = str(coerced_value)


class UpDownFactor(BoxLayout, UpDownFactorCore):
    pass


value_factor_kv = """
<ValueFactor>:
    orientation: 'vertical'
    Button: 
        text: txt_factor.text
        disabled: txt_factor.focus
        on_press: root.press_callback()

    TextInput:
        id: txt_factor
        size_hint_y: .2
        text: root.text
        input_filter: 'int'
        multiline: False
        on_focus: root.focus_callback(txt_factor.text, self.focus)
    
    Label: 
        text: root.info
        size_hint_y: 0.1
"""

up_down_factor_kv = """
<UpDownFactor>:
    orientation: 'vertical'
    
    BoxLayout:
        orientation: 'vertical'
        
        Label:
            text: str(root.current_value)
            font_size: 25,'sp'
    
        Label:
            visibility: False
            text: str(root.before_value)
            font_size: 15,'sp'
    
        BoxLayout:
            orientation: 'horizontal'
    
            ValueFactor:
                text: str(root.factor_neg)
                info: 'down'
                press_cmd: root.decrease_current_value
                focus_cmd: root.update_factor_neg
    
    
            ValueFactor:
                visibility: False
                text: '0'
                size_hint_x: .3
                info: 'set'
                press_cmd: root.set_current_value
                focus_cmd: root.update_factor_current
    
    
            ValueFactor:
                text: str(root.factor_pos)
                info: 'up'
                press_cmd: root.increase_current_value
                focus_cmd: root.update_factor_pos
"""

code_kv = value_factor_kv + up_down_factor_kv


Builder.load_string(code_kv)
