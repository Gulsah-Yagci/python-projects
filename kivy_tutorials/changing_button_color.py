from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

#Builder.load_file('myapp.kv')
Builder.load_string("""
<MyGridLayout>

    name:name
    game:game
    color:color

    GridLayout:
        cols:1
        size: root.width, root.height
        GridLayout:
            cols:2

            Label:
                text: 'Name'
            TextInput:
                id:name
                multiline:False
                background_color: (1,0,1,0.5)

            Label:
                text: 'Game'
            TextInput:
                id:game
                multiline:False

            Label:
                text: 'Color'
            TextInput:
                id:color
                multiline:False

        Button:
            text: 'Submit'
            font_size: 30
            on_press: root.press()
            #RGB _ A
            background_normal: ''
            background_color: (1,0,1,0.5)
""")
class MyGridLayout(Widget):


    def press(self):
        name = self.name.text
        game = self.game.text
        color = self.color.text

        print(f'Hello {name}, you like {game}, and your favorite color is {color}')
        # print it to the screen
        #self.add_widget(Label(text='Hello {name}, you like {game}, and your favorite color is {color}'))

        # clear the input boxes

        self.name.text = ''
        self.game.text = ''
        self.color.text = ''




class MyApp(App):
    def build(self):
        return MyGridLayout()


if __name__ == '__main__':
    MyApp().run()