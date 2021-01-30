from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_file('myapp.kv')

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