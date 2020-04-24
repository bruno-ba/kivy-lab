import kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from customwidgets.uix.updownfactor import UpDownFactor

kivy.require('1.11.1')

Window.clearcolor = [0, 0, .2, 1]


root_kv = """
<root@BoxLayout>
    orientation: 'vertical'
    UpDownFactor:

root:
"""


class TestingApp(App):
    def build(self):
        return Builder.load_string(root_kv)


if __name__ == '__main__':
    TestingApp().run()
