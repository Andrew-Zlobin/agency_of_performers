import matplotlib.pyplot as plt
import numpy as np
import graph_alg
import setting_alg
from creator_pop import population_creator
from fitness import fitness
from cx import mating
import decimal
import sel
#test хранение/установка/просмотр настроек и графа
#inf = 100
#new_graph1 = np.array([[9, 3, 1, 3, inf, inf],
#     [3, 0, 4, inf, inf, inf],
#     [1, 4, 0, inf, 7, 5],
#     [3, inf, inf, 0, inf, 2],
#     [inf, inf, 7, inf, 0, 4],
#     [inf, inf, 5, 2, 4, 0]])
#
#print(new_graph1)

#file_name = 'example_1'
#file_name2 = 'example_2'
#
#new_graph = graph_alg.Graph_alg()
#set_manager = setting_alg.Settings_alg()
#
#print(set_manager.get_all_settings_alg())
#print(set_manager.get_settings_alg('select_method'))
#set_manager.set_settings_alg('half_choice', 'select_method')
#print(set_manager.get_settings_alg('select_method'))
#
#
#set_manager.save_data_config(file_name)
#config = set_manager.load_data_config(file_name)
#print(config)
#set_manager.set_setting_alg_from_file(file_name)
#print(set_manager.get_all_settings_alg())
#
#
#print(new_graph.get_graph())
#new_graph.set_graph(new_graph1)
#print(new_graph.get_graph())
#
#new_graph.save_data_graph(file_name2)
#print(new_graph.load_data_graph(file_name2))

#algorithm
def float_range(start, stop, step):
  while start < stop:
    yield float(start)
    start += decimal.Decimal(step)
# создание начальной популяции
inf = 100
graph = [[0, 3, 1, 3, inf, inf],
     [3, 0, 4, inf, inf, inf],
     [1, 4, 0, inf, 7, 5],
     [3, inf, inf, 0, inf, 2],
     [inf, inf, 7, inf, 0, 4],
     [inf, inf, 5, 2, 4, 0]]  
population_size = 5

start_v = 0
finish_v = 5
population = population_creator(graph, start_v, population_size)

# вычисление пригодности каждой особи
population_fitness = {}
for individual in population:
  population_fitness[fitness(individual, graph, start_v)] = individual
population_fitness = sorted(population_fitness.items())
# вычисление вероятности мутации и кроссинговера
MUTATION_P_STEP = 1 / population_size 
MUTATION_P = list((float_range(0, 1, '0.1')))

CX_P_STEP = population_size // 10
CX_P = list((float_range(0, 1, '0.1')))
# выбор родителей
# выбор лучшей половины
parents_half = sel.half_choice(population)

parents1, parents2 = sel.fitness_proportionate_selection(parents_half)
parents = [parents1, parents2]
#кроссинговер родителей 
children = mating(parents, method='Two Pionts')
if fitness(children[0], graph, start_v) >= population_fitness[len(population_fitness) - 1][0]:
  population_fitness[len(population_fitness) - 1][0] = fitness(children[0], graph, start_v)
  population_fitness[len(population_fitness) - 1][1] = children[0]
population_fitness = sorted(population_fitness.items())
if fitness(children[1], graph, start_v) >= population_fitness[len(population_fitness) - 1][0]:
  population_fitness[len(population_fitness) - 1][0] = fitness(children[1], graph, start_v)
  population_fitness[len(population_fitness) - 1][0] = children[0]
