import math

import kivy

kivy.require('1.0.5')


from kivy.config import Config
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '480')
#Config.set('graphics', 1)
#from kivy.core.window import Window
#Window.fullscreen = 'auto'

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
#from kivy.graphic
from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty
from kivy.graphics import Color, Ellipse, Line
from kivy.graphics import Rectangle, Color
from kivy.uix.widget import Widget



class Controller(GridLayout):
    pass

class CanvasWidget(Widget):
     
    def __init__(self, **kwargs):
 
        super(CanvasWidget, self).__init__(**kwargs)
 
        # Arranging Canvas
        with self.canvas:
 
            Color(.234, .456, .678, .8)  # set the colour
 
            # Setting the size and position of canvas
            self.rect = Rectangle(pos = self.center,
                                  size =(self.width / 2.,
                                        self.height / 2.))
 
            # Update the canvas as the screen size change
            self.bind(pos = self.update_rect,
                  size = self.update_rect)
 
    # update function which makes the canvas adjustable.
    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

class ControllerApp(App):
    matrix_size = 5
    adjacency_matrix = []
    def build(self):
        return Controller()


    def create_adjacency_matrix(self):
        self.root.ids.adjacency_matrix.clear_widgets()
        text = self.root.ids.input.text
        if text == '':
            return
        
        self.matrix_size = int(text)
        self.root.ids.adjacency_matrix.rows = self.matrix_size + 1
        self.root.ids.adjacency_matrix.cols = self.matrix_size + 1
        txt = Label(
                size_hint=[None, None],
                size=(50, 30),
                text = ''
            )
        self.root.ids.adjacency_matrix.add_widget(txt)
        for i in range(self.matrix_size):
            txt = Label(
                size_hint=[None, None],
                size=(50, 30),
                text = str(i + 1)
            )
            self.root.ids.adjacency_matrix.add_widget(txt)
        for i in range(self.matrix_size):
            txt = Label(
                size_hint=[None, None],
                size=(50, 30),
                text = str(i + 1)
            )
            self.root.ids.adjacency_matrix.add_widget(txt)
            for j in range(self.matrix_size):
                btn = TextInput(
                    size_hint=[None, None],
                    size=(50, 30),
                    multiline=False
                )
                self.root.ids.adjacency_matrix.add_widget(btn)


    def draw_graph(self):
        input_matrix = [i.text for i in self.root.ids.adjacency_matrix.children]
        self.adjacency_matrix = []
        for i in range(self.matrix_size):
            self.adjacency_matrix.append([])
            for j in range(self.matrix_size):
                x = input_matrix[-(self.matrix_size + 1) - i * (self.matrix_size + 1) - j - 2]
                self.adjacency_matrix[i].append(x)
                
        #print(self.adjacency_matrix)
        #print(self.root.ids.graph_vis.pos)
        #print(self.root.ids.graph_vis.size)
        
        #self.root.ids.graph_vis.clear_widgets()
        print(self.root.ids.graph_vis.children)
        #self.root.ids.graph_vis.add_widget(Canvas())
        with self.root.ids.graph_vis.canvas:
            #self.root.ids.graph_vis.canvas.clear()
            tops_count = self.matrix_size
            center_coords = [self.root.ids.graph_vis.pos[0] + self.root.ids.graph_vis.size[0] / 2,
                            self.root.ids.graph_vis.pos[1] + self.root.ids.graph_vis.size[1] / 2]
            graph_radius = 100
            alpha = 2 * math.pi / tops_count
            print(self.adjacency_matrix)
            for i in range(tops_count):
                d = 15.
                self.root.ids.graph_vis.canvas.add(Ellipse(pos=(center_coords[0] + graph_radius * math.cos(i * alpha) - d / 2, center_coords[1] + graph_radius * math.sin(i * alpha) - d / 2), size=(d, d)))
            for start_n, start in enumerate(self.adjacency_matrix):
                for target_n, target in enumerate(start):
                    print(start, target)
                    if target != 0:
                        print(start, target)
                        Line(points=[center_coords[0] + graph_radius * math.cos(start_n * alpha),
                                    center_coords[1] + graph_radius * math.sin(start_n * alpha),
                                    center_coords[0] + graph_radius * math.cos(target_n * alpha),
                                    center_coords[1] + graph_radius * math.sin(target_n * alpha)])
            #self.root.ids.graph_vis.canvas.draw()


if __name__ == '__main__':
    ControllerApp().run()