from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleview import RecycleView


class AddLocationForm(BoxLayout):

    def get_location(self):
        print(f'your location')


root_kv = """
<AddLocationForm>:
    orientation: 'vertical'

    BoxLayout:
        size_hint_y: None
        height:'40dp'

        TextInput:
            size_hint_x: .5

        Button:
            size_hint_x: .25
            text: 'Search'
            on_press: root.get_location()

        Button:
            size_hint_x: .25
            text: 'Current Location'

    RecycleView:
        data:[{'text': 'Palo Alto'}, {'text': 'Mx'}, {'text': 'Palo'}, {'text': 'US'}]

        viewclass: 'Label'


        RecycleBoxLayout:
            default_size: None, dp(20)
            default_size_hint: 1 , None
            size_hint_y: None
            height: self.minimum_height
            orientation: 'vertical'

AddLocationForm:
"""


class WeatherApp(App):
    def build(self):
        return Builder.load_string(root_kv)


if __name__ == '__main__':
    app = WeatherApp()
    app.run()
