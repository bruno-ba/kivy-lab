from kivy.app import App
from kivy.lang import Builder
from kivy.network.urlrequest import UrlRequest
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.recycleview import RecycleView
"""
https://samples.openweathermap.org/data/2.5/weather?q=London,uk&appid=
"""

import requests


class AddLocationForm(BoxLayout):
    search_input = ObjectProperty()

    def search_location(self):
        req = requests.get('http://api.openweathermap.org/data/2.5/forecast/daily?id=524901&appid=c68fb2b42d84462c55e23e13714ef21f&lang={pt}')

        print(req.text)


root_kv = """
<AddLocationForm>:
    orientation: 'vertical'
    search_input:search_box

    BoxLayout:
        size_hint_y: None
        height:'40dp'


        TextInput:
            id: search_box
            size_hint_x: .5


        Button:
            size_hint_x: .25
            text: 'Search'
            on_press: root.search_location()

        Button:
            size_hint_x: .25
            text: 'Current Location'

    RecycleView:
        id: search_results_list

        data:[]

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
