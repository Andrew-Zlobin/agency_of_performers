import matplotlib.pyplot as plt
import numpy as np
import graph_alg
import setting_alg


#test хранение/установка/просмотр настроек и графа
inf = 100
new_graph1 = np.array([[9, 3, 1, 3, inf, inf],
     [3, 0, 4, inf, inf, inf],
     [1, 4, 0, inf, 7, 5],
     [3, inf, inf, 0, inf, 2],
     [inf, inf, 7, inf, 0, 4],
     [inf, inf, 5, 2, 4, 0]])

print(new_graph1)

file_name = 'example_1'
file_name2 = 'example_2'

new_graph = graph_alg.Graph_alg()
set_manager = setting_alg.Settings_alg()

print(set_manager.get_all_settings_alg())
print(set_manager.get_settings_alg('select_method'))
set_manager.set_settings_alg('half_choice', 'select_method')
print(set_manager.get_settings_alg('select_method'))


set_manager.save_data_config(file_name)
config = set_manager.load_data_config(file_name)
print(config)
set_manager.set_setting_alg_from_file(file_name)
print(set_manager.get_all_settings_alg())


print(new_graph.get_graph())
new_graph.set_graph(new_graph1)
print(new_graph.get_graph())

new_graph.save_data_graph(file_name2)
print(new_graph.load_data_graph(file_name2))
