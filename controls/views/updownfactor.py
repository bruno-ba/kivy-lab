from kivy.lang import Builder
from kivy.core.window import Window

imports_kv = """
#: import UpDownVM controls.viewmodels.updownfactor.UpDownFactor
#: set vm UpDownVM()
"""

factor_control_kv = """
<FactorControl@BoxLayout>:
    orientation: 'vertical'
    factor: ''
    lbl_info: 'lbl'
    cmd_press: None
    cmd_focus: None
    Button:
        id: btn_factor
        text: root.factor
        disabled: txt_factor.focus
        on_press: if root.cmd_press: root.cmd_press(txt_factor.text)
    TextInput:
        id: txt_factor
        size_hint_y: .2
        text: root.factor
        input_filter: 'int'
        multiline: False
        on_focus: if root.cmd_focus and not self.focus: root.cmd_focus(self.text)
    Label: 
        text: root.lbl_info
        size_hint_y: .1
"""

up_down_factor_control_kv = """
<UpDownFactorControl@BoxLayout>:
    orientation: 'vertical'
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: vm.value_new
            font_size: 25,'sp'
        Label:
            font_size: 15,'sp'
            text: vm.value_old
    BoxLayout:
        orientation: 'horizontal'
        FactorControl:
            factor: vm.factor_down
            cmd_press: vm.cmd_press_down
            cmd_focus: vm.cmd_focus_down
            lbl_info: 'down'
            
        FactorControl:
            size_hint_x: .3
            factor: ''
            cmd_press: vm.cmd_press_new
            # cmd_focus: vm.cmd_focus_down
            lbl_info: 'set'
            
        FactorControl:
            factor: vm.factor_up
            cmd_press: vm.cmd_press_up
            cmd_focus: vm.cmd_focus_up
            lbl_info: 'up'
"""

init_kv = """
UpDownFactorControl:
"""

code_kv = \
    imports_kv \
    + factor_control_kv \
    + up_down_factor_control_kv \
    + init_kv

if __name__ == '__main__':
    import kivy
    from kivy.app import App

    kivy.require('1.11.1')
    Window.clearcolor = [0, 0, .2, 1]


    class TestingApp(App):

        def build(self):
            return Builder.load_string(code_kv)


    TestingApp().run()
