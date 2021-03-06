import graph_alg
import setting_alg
import random
from creator_pop import population_creator
from mutation import possibility_mutation
from fitness import fitness
from fitness import fitness_individual_in_population
from crossover import choice_crossover_method
from selection import selection_parents
from selection import cum_sum_calc
from mutation_and_crossover_probability import calculate_mutation_probability_array
from mutation_and_crossover_probability import calculate_crossover_probability_array
from mutation_and_crossover_probability import calculate_crossover_probability_individual 
from mutation_and_crossover_probability import calculate_mutation_probability_individual
#algorithm
new_graph = graph_alg.Graph_alg()
settings = setting_alg.Settings_alg()
inf = 100
graph = [[0, 3, 1, 3, inf, inf],
     [3, 0, 4, inf, inf, inf],
     [1, 4, 0, inf, 7, 5],
     [3, inf, inf, 0, inf, 2],
     [inf, inf, 7, inf, 0, 4],
     [inf, inf, 5, 2, 4, 0]]  
new_graph.set_graph(graph)
settings = settings.get_all_settings_alg()
population_size = int(settings['POPULATION_SIZE'])
percentage_parents = float(settings['percentage parents'])
# создание начальной популяции
start_v = 0
finish_v = 5
population = population_creator(graph, start_v, population_size)
for i in range(int(settings['MAX_GENERATIONS'])):
  cum_sum = cum_sum_calc(population)
  zipped_list = zip(cum_sum, population)
  sorted_list = sorted(zipped_list)
  population = [value[1] for value in sorted_list]
  # цикл
  # выбор родителей 
  parents = selection_parents(population, percentage_parents, method = 'Tournament selection')
  size_new_population = len(parents)
  cum_sum = cum_sum_calc(parents)
  zipped_list = zip(cum_sum, parents)
  sorted_list = sorted(zipped_list)
  parents = [value[1] for value in sorted_list]
  # вычисление вероятности мутации и кроссинговера особей
  mutation_probability_array = calculate_mutation_probability_array(float(settings['upper_limit_mutation']), float(settings['lower_bound_mutation']), size_new_population)
  crossover_probability_array = calculate_crossover_probability_array(float(settings['upper_limit_crossover']), float(settings['lower_bound_crossover']), size_new_population)
  # выбор пары
  for _ in range(size_new_population):
    i1 = i2 = 0
    pair = []
    while i1 == i2:
        i1, i2 = random.randint(0, size_new_population - 1), random.randint(0, size_new_population - 1)
    parent1 = parents[i1]
    parent2 = parents[i2]
    pair.append(parent1)
    pair.append(parent2)
    chance_crossover = calculate_crossover_probability_individual(crossover_probability_array, parent1, parents)
    chance = random.random()
    if chance_crossover < chance:
      child1, child2 = choice_crossover_method(pair, settings['cx_method'])
      chance_mutation_child1 = calculate_mutation_probability_individual(mutation_probability_array, parent1, parents)
      #chance = random.randint()
      #if chance_mutation_child1 < chance:
        #child1 = possibility_mutation(child1, chance_mutation_child1, settings['mut_method'])
      population = fitness_individual_in_population(population, child1, chance_mutation_child1, settings['mut_method'])
      #chance_mutation_child1 = calculate_mutation_probability_individual(crossover_probability_array, parent1, population)
      chance_mutation_child2 = calculate_mutation_probability_individual(mutation_probability_array, parent2, parents)
      population = fitness_individual_in_population(population, child2, chance_mutation_child2, settings['mut_method'])
    else:
      continue
  print(population)
# оценка выживаемости особи
# добавление в популяцию 
