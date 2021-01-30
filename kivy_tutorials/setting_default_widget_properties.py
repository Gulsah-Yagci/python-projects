from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

# Builder.load_file('myapp.kv')
Builder.load_string("""
<Button>
    
    font_size: 32
    background_normal: ''
    background_color: (0,0,1,1)
    
<TextInput>
    background_color: (150/255,150/255,150/255,1)

<Label>
    font_size: 32

<MyGridLayout>
    BoxLayout:
        orientation: 'vertical'
        size: root.width,root.height

        padding: 10
        spacing: 10
        
        Label:
            text: 'Name'
            
        TextInput:
            multiline: False
            
        Label:
            text: 'Game'
            color : (0,0,1,1)
        
        TextInput:
            multiline: False
            
        

        Button:
            text: 'Submit'

        Button:
            text: 'Clear'
            background_color: (1,0,0,1)


""")


class MyGridLayout(Widget):
    pass


class MyApp(App):
    def build(self):
        return MyGridLayout()


if __name__ == '__main__':
    MyApp().run()