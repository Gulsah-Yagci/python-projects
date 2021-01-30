"""

font_size=30,
                             size_hint_y = None,
                             height = 50,
                             size_hint_x = None,
                             width = 20

"""




import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGridLayout(GridLayout):
    # Initialize infinite keywords
    def __init__(self,**kwargs):
        # Call grid layout constructor
        super(MyGridLayout,self).__init__(**kwargs)

        # Set columns
        self.cols = 1
        self.row_force_default =True
        self.row_default_height = 120
        self.col_force_default = True
        self.col_default_width = 100

        # create a second gridlayout
        self.top_grid = GridLayout(row_force_default = True,
                                   row_default_height = 40,
                                   col_force_default=True,
                                   col_default_width=100,)
        self.top_grid.cols =2

        # Add widgets
        self.top_grid.add_widget(Label(text='Name: '))
        # Add Input Box
        self.name = TextInput(multiline=False)
        self.top_grid.add_widget(self.name)

        self.top_grid.add_widget(Label(text='Favorite Game: '))
        # Add Input Box
        self.game = TextInput(multiline=False)
        self.top_grid.add_widget(self.game)

        self.top_grid.add_widget(Label(text='Favorite Color: '))
        # Add Input Box
        self.color = TextInput(multiline=False)
        self.top_grid.add_widget(self.color)

        # add the new top_grid to our app
        self.add_widget(self.top_grid)

        # Create a Submit Button

        self.submit = Button(text = 'Submit')
        # Bind the button
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)

    def press(self,instance):
        name = self.name.text
        game = self.game.text
        color = self.color.text

        print(f'Hello {name}, you like {game}, and your favorite color is {color}')
        # print it to the screen
        self.add_widget(Label(text='Hello {name}, you like {game}, and your favorite color is {color}'))

        #clear the input boxes

        self.name.text = ''
        self.game.text = ''
        self.color.text = ''


class MyApp(App):
    def build(self):
        return MyGridLayout()


if __name__ == '__main__':
    MyApp().run()