import numpy as np


class Graph_alg:
  def __init__(self):
    #по умолчанию
    inf = 10
    self.graph =  np.array([[0, 3, 1, 3, inf, inf],
     [3, 0, 4, inf, inf, inf],
     [1, 4, 0, inf, 7, 5],
     [3, inf, inf, 0, inf, 2],
     [inf, inf, 7, inf, 0, 4],
     [inf, inf, 5, 2, 4, 0]])


  def get_graph(self):
    return self.graph
  

  def set_graph(self, new_graph):
    self.graph = new_graph
    print(self.graph)

  def save_data_graph(self, file_name):
    save_graph = np.array(self.graph)
    np.savetxt(file_name + '.txt', save_graph)


  def load_data_graph(self, file_name):
    load_graph = np.loadtxt(file_name + '.txt', dtype=int)
    return load_graph

  
  def true_graph(self):
    pass