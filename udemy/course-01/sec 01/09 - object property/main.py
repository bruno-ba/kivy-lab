from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.recycleview import RecycleView


class AddLocationForm(BoxLayout):
    search_input = ObjectProperty()

    def get_location(self):
        print(f'your location {self.search_input.text}')


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
            on_press: root.get_location()

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
