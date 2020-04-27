from kivy.app import App
from kivy.lang import Builder
from kivy.uix.recycleview import RecycleView


root_kv = """
<AddLocationForm@BoxLayout>:
    orientation: 'vertical'
    
    BoxLayout:
        size_hint_y: None
        height:'40dp'
        
        TextInput:
            size_hint_x: .5
           
        Button:
            size_hint_x: .25
            text: 'Search'
        
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
