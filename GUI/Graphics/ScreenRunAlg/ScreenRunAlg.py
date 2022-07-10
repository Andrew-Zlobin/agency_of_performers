import matplotlib as mpl
mpl.use('TkAgg', force=True)
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
import matplotlib.pyplot as plt
from kivy.garden.matplotlib import FigureCanvasKivyAgg
from kivy.clock import Clock
import numpy as np
class ScreenRunAlg(Screen):
    def __init__(self, controller, **kwargs):
        super(ScreenRunAlg, self).__init__(**kwargs)
        self.controller = controller
        Clock.schedule_interval(self.draw_graphic, 1.)
        signal = [7, 89.6, 45.-56.34]
  
        signal = np.array(signal)
          
        # this will plot the signal on graph
        plt.plot(signal)
          
        # setting x label
        plt.xlabel('Time(s)')
          
        # setting y label
        plt.ylabel('signal (norm)')
        plt.grid(True, color='lightgray')
          
        # adding plot to kivy boxlayout
        self.ids.mpl_graph.add_widget(FigureCanvasKivyAgg(plt.gcf()))

    def draw_graphic(self, interval):
        self.ids.mpl_graph.clear_widgets()
        signal = self.controller.get_current_data()
  
        signal = np.array(signal)
          
        # this will plot the signal on graph
        plt.plot(signal)
          
        # setting x label
        plt.xlabel('Time(s)')
          
        # setting y label
        plt.ylabel('signal (norm)')
        plt.grid(True, color='lightgray')
          
        # adding plot to kivy boxlayout
        self.ids.mpl_graph.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        result = self.controller.get_result()
        result = [[str(j) for j in i] for i in result]
        result = '\n'.join([', '.join(i) for i in result])
        self.ids.mpl_graph.add_widget(Label(text=result))
        print(result)
        

    def next_step(self):
        
        steps_count = 8
        i = steps_count - 1
        step_pointer = self.ids.steps.children[i].children[1].text
        print(self.ids.steps.children[i].children[0].text)
        print(step_pointer)
        while step_pointer != '*':
            i = i - 1
            if i < 0:
                i = steps_count - 1
            print(i)
            step_pointer = self.ids.steps.children[i].children[1].text
        self.ids.steps.children[i].children[1].text = ''
        self.ids.steps.children[i - 1].children[1].text = '*'
        print("next_step")