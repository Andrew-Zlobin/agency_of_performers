#from GA.setting_alg import Settings_alg

import threading
import time
class Controller:
    def __init__(self):
        self.settings = {}
        self.graph = []
        self.intermediate_result = []
        self.result = []



    def set_new_settings(self, new_settings):
        self.settings = new_settings

    def set_graph(self, new_graph):
        self.graph = new_graph

    def next_step_of_alg(self):
        pass

    def run_alg(self):
        self.result = self.graph
        return
    
    def get_result(self):
        print(self.result)
        return self.result

    def begin_alg(self):
        print('alg begins')

    def get_current_data(self):
        return [7, 89.6, 45.-56.34]

    def mainLoop(self):
        while True:
            time.sleep(3)
            print(self.settings)
            print(self.graph)

