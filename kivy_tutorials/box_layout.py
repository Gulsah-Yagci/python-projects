from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

#Builder.load_file('myapp.kv')
Builder.load_string("""
<MyGridLayout>
    BoxLayout:
        orientation: 'horizontal' # vertical
        size: root.width,root.height
        
        padding: 50
        spacing: 20
        
        
        Button:
            text: 'hello world'
        
        Button:
            text: 'goodbye world'
        
        Button:
            text: 'I am hungry'
            pos_hint: {'center_y': 0.5} # center_x --- if vertical
            size_hint: (0.5,0.5)
            width: 100
            height: 50 
    
""")
class MyGridLayout(Widget):


    pass




class MyApp(App):
    def build(self):
        return MyGridLayout()


if __name__ == '__main__':
    MyApp().run()