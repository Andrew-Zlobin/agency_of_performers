import math

from kivy.uix.screenmanager import Screen

from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

from kivy.graphics import Color, Ellipse, Line
from kivy.graphics import Rectangle, Color
from kivy.clock import Clock

class ScreenMain(Screen):
    
    def __init__(self, **kwargs):
        self.matrix_size = 5
        self.adjacency_matrix = [['0', '0', '1', '1', '0'],
                                ['0', '0', '0', '1', '1'],
                                ['1', '0', '0', '0', '1'],
                                ['1', '1', '0', '0', '0'],
                                ['0', '1', '1', '0', '0']]

        super(ScreenMain, self).__init__(**kwargs)

        Clock.schedule_interval(self.update_adjacency_matrix, .01)
        Clock.schedule_interval(self.draw_graph, .1)
        self.create_adjacency_matrix()

    def update_adjacency_matrix(self, interval):
        
        if self.ids.adjacency_matrix.children == []:
            return

        input_matrix = [i.text for i in self.ids.adjacency_matrix.children]
        self.adjacency_matrix = []
        for i in range(self.matrix_size):
            self.adjacency_matrix.append([])
            for j in range(self.matrix_size):
                x = input_matrix[-(self.matrix_size + 1) - i * (self.matrix_size + 1) - j - 2]
                #if x == '':
                #    x = '0'
                self.adjacency_matrix[i].append(x)
       

    def create_adjacency_matrix(self):
        #self.root.get
        
        self.ids.adjacency_matrix.clear_widgets()
        text = self.ids.input.text
        if text == '':
            #self.adjacency_matrix = []
            return
        for char in text:
            if char not in '1234567890':
                return
        
        new_matrix_size = int(text)
        new_adjacency_matrix = [['' for i in range(new_matrix_size)] for j in range(new_matrix_size)]
        for i, i_value in enumerate(self.adjacency_matrix):
            for j , j_value in enumerate(i_value):
                if i < new_matrix_size and j < new_matrix_size:
                    new_adjacency_matrix[i][j] = j_value
        self.adjacency_matrix = new_adjacency_matrix
        self.matrix_size = new_matrix_size
        self.ids.adjacency_matrix.rows = self.matrix_size + 1
        self.ids.adjacency_matrix.cols = self.matrix_size + 1
        txt = Label(
                size_hint=[None, None],
                size=(50, 30),
                text = ''
            )
        self.ids.adjacency_matrix.add_widget(txt)
        for i in range(self.matrix_size):
            txt = Label(
                size_hint=[None, None],
                size=(50, 30),
                text = str(i + 1)
            )
            self.ids.adjacency_matrix.add_widget(txt)
        for i in range(self.matrix_size):
            txt = Label(
                size_hint=[None, None],
                size=(50, 30),
                text = str(i + 1)
            )
            self.ids.adjacency_matrix.add_widget(txt)
            for j in range(self.matrix_size):
                btn = TextInput(
                    text=self.adjacency_matrix[i][j],
                    size_hint=[None, None],
                    size=(50, 30),
                    multiline=False
                )
                self.ids.adjacency_matrix.add_widget(btn)


    def draw_graph(self, interval):
        
        drawable_adjacency_matrix = [['' for i in range(self.matrix_size)] for j in range(self.matrix_size)]
        for i in range(self.matrix_size):
            for j in range(self.matrix_size):
                if self.adjacency_matrix[i][j] == '':
                    drawable_adjacency_matrix[i][j] = 0
                else:
                    drawable_adjacency_matrix[i][j] = int(self.adjacency_matrix[i][j])
        
        with self.ids.graph_vis.canvas:
            Color(.0, .0, .0)
            Rectangle(pos=self.ids.graph_vis.pos, size=self.ids.graph_vis.size)
            Color(1.0, .0, .0)
            tops_count = self.matrix_size
            center_coords = [self.ids.graph_vis.pos[0] + self.ids.graph_vis.size[0] / 2,
                            self.ids.graph_vis.pos[1] + self.ids.graph_vis.size[1] / 2]
            graph_radius = 100
            alpha = 2 * math.pi / tops_count
            for i in range(tops_count):
                d = 15.
                self.ids.graph_vis.canvas.add(Ellipse(pos=(center_coords[0] + graph_radius * math.cos(i * alpha) - d / 2, center_coords[1] + graph_radius * math.sin(i * alpha) - d / 2), size=(d, d)))
            for start_n, start in enumerate(drawable_adjacency_matrix):
                for target_n, target in enumerate(start):
                    if target != 0:
                        Line(points=[center_coords[0] + graph_radius * math.cos(start_n * alpha),
                                    center_coords[1] + graph_radius * math.sin(start_n * alpha),
                                    center_coords[0] + graph_radius * math.cos(target_n * alpha),
                                    center_coords[1] + graph_radius * math.sin(target_n * alpha)])