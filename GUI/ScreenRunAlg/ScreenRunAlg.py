from kivy.uix.screenmanager import Screen
import matplotlib.pyplot as plt
#from kivy.garden.matplotlib import FigureCanvasKivyAgg

class ScreenRunAlg(Screen):
    def __init__(self, **kwargs):
        super(ScreenRunAlg, self).__init__(**kwargs)
#        signal = [7, 89.6, 45.-56.34]
#  
#        signal = np.array(signal)
#          
#        # this will plot the signal on graph
#        plt.plot(signal)
#          
#        # setting x label
#        plt.xlabel('Time(s)')
#          
#        # setting y label
#        plt.ylabel('signal (norm)')
#        plt.grid(True, color='lightgray')
#          
#        # adding plot to kivy boxlayout
#        self.str.layout.add_widget(FigureCanvasKivyAgg(plt.gcf()))

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