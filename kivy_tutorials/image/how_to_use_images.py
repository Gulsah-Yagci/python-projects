from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.image import Image

# Builder.load_file('myapp.kv')
Builder.load_string("""
<MyGridLayout>
    
    BoxLayout:
        orientation: 'vertical'
        size: root.width,root.height

        padding: 50
        spacing: 20

        Image:
            source: '2.jpg'
        
        
        Button:
            text: 'Submit'



""")


class MyGridLayout(Widget):
    pass


class MyApp(App):
    def build(self):
        Window.clearcolor = (1,1,1,1)
        return MyGridLayout()


if __name__ == '__main__':
    MyApp().run()