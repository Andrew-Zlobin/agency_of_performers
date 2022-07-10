import math
import os
from kivy.uix.screenmanager import Screen

from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

from kivy.graphics import Color, Ellipse, Line
from kivy.graphics import Rectangle, Color
from kivy.clock import Clock

from kivy.uix.floatlayout import FloatLayout
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)


class SaveDialog(FloatLayout):
    save = ObjectProperty(None)
    text_input = ObjectProperty(None)
    cancel = ObjectProperty(None)
Factory.register('LoadDialog', cls=LoadDialog)
Factory.register('SaveDialog', cls=SaveDialog)

class ScreenMain(Screen):
    
    loadfile = ObjectProperty(None)
    savefile = ObjectProperty(None)
    text_input = ''
    def __init__(self, controller, **kwargs):
        self.controller = controller
        self.matrix_size = 10
        self.adjacency_matrix = [['0', '1', '0', '0', '1', '0', '1', '0', '0', '1'], #1
                                ['1', '0', '1', '0', '0', '0', '0', '0', '0', '0'],  #2
                                ['0', '1', '0', '1', '0', '0', '1', '0', '1', '0'],  #3
                                ['0', '0', '1', '0', '1', '0', '0', '0', '0', '0'],  #4
                                ['1', '0', '0', '1', '0', '1', '0', '0', '1', '0'],  #5
                                ['0', '0', '0', '0', '1', '0', '1', '0', '0', '0'],  #6
                                ['1', '0', '1', '0', '0', '1', '0', '1', '0', '0'],  #7
                                ['0', '0', '0', '0', '0', '0', '1', '0', '1', '0'],  #8
                                ['0', '0', '1', '0', '1', '0', '0', '1', '0', '1'],  #9
                                ['1', '0', '0', '0', '0', '0', '0', '0', '1', '0']]  #10

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
        self.save_matrix()

    def save_matrix(self):
        alg_matrix = []
        for i, i_value in enumerate(self.adjacency_matrix):
            alg_matrix.append([])
            for j, j_value in enumerate(i_value):
                if j_value == '':
                    alg_matrix[i].append(0.0)
                else:
                    alg_matrix[i].append(float(j_value))
        self.controller.set_graph(alg_matrix)
       

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

    def draw_tops(self, drawable_adjacency_matrix, tops_count, graph_radius, alpha, center_coords):
        with self.ids.graph_vis.canvas:
            for i in range(tops_count):
                d = 10.
                self.ids.graph_vis.canvas.add(Ellipse(pos=(center_coords[0] + graph_radius * math.cos(i * alpha) - d / 2, center_coords[1] + graph_radius * math.sin(i * alpha) - d / 2), size=(d, d)))

    def draw_edges(self, drawable_adjacency_matrix, tops_count, graph_radius, alpha, center_coords):
        with self.ids.graph_vis.canvas:
            for start_n, start in enumerate(drawable_adjacency_matrix):
                for target_n, target in enumerate(start):
                    if target != 0:
                        Line(points=[center_coords[0] + graph_radius * math.cos(start_n * alpha),
                                    center_coords[1] + graph_radius * math.sin(start_n * alpha),
                                    center_coords[0] + graph_radius * math.cos(target_n * alpha),
                                    center_coords[1] + graph_radius * math.sin(target_n * alpha)], width=1.5)

    def draw_graph(self, interval):
        
        drawable_adjacency_matrix = [['' for i in range(self.matrix_size)] for j in range(self.matrix_size)]
        for i in range(self.matrix_size):
            for j in range(self.matrix_size):
                if self.adjacency_matrix[i][j] == '':
                    drawable_adjacency_matrix[i][j] = 0
                else:
                    drawable_adjacency_matrix[i][j] = int(self.adjacency_matrix[i][j])

        
        center_coords = [self.ids.graph_vis.pos[0] + self.ids.graph_vis.size[0] / 2,
                        self.ids.graph_vis.pos[1] + self.ids.graph_vis.size[1] / 2]
        
        tops_count = self.matrix_size
        graph_radius = self.ids.graph_vis.size[1] / 4
        alpha = 2 * math.pi / tops_count
        with self.ids.graph_vis.canvas:
            Color(.0, .0, .0)
            Rectangle(pos=self.ids.graph_vis.pos, size=self.ids.graph_vis.size)
            Color(1.0, .0, .0)
        self.draw_edges(drawable_adjacency_matrix, tops_count, graph_radius, alpha, center_coords)
        self.draw_tops(drawable_adjacency_matrix, tops_count, graph_radius, alpha, center_coords)
        
        
    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def show_save(self):
        content = SaveDialog(save=self.save, cancel=self.dismiss_popup)
        self._popup = Popup(title="Save file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path, filename):
        with open(os.path.join(path, filename[0])) as stream:
            text_input = stream.read()
            self.adjacency_matrix = [[j[1:] if j[0] == ' ' else j for j in i.split(",")] for i in text_input.split("\n")]
            self.matrix_size = len(self.adjacency_matrix)
            self.ids.input.text = str(self.matrix_size)
            print(self.matrix_size)
            print(self.adjacency_matrix)
            self.create_adjacency_matrix()

        self.dismiss_popup()

    def save(self, path, filename):
        with open(os.path.join(path, filename), 'w') as stream:
            written_str = '\n'.join([', '.join(i) for i in self.adjacency_matrix])
            stream.write(written_str)

        self.dismiss_popup()