import random
import fitness
import matplotlib.pyplot as plt
import numpy as np

inf = 100
graph = [[0, 3, 1, 3, inf, inf],
     [3, 0, 4, inf, inf, inf],
     [1, 4, 0, inf, 7, 5],
     [3, inf, inf, 0, inf, 2],
     [inf, inf, 7, inf, 0, 4],
     [inf, inf, 5, 2, 4, 0]]  


def cum_sum_calc_individual(individual, start_v, finish_v):
  cum_sum = 0
  #individual = individual[start_v:finish_v]
  current_v = start_v
  for i in range(len(individual) - 1):
    if current_v == finish_v: break
    cum_sum += graph[current_v][individual[i + 1]]
    current_v = individual[i + 1]

  #individual = np.array(individual)
  #cum_sum.append(individual.cumsum()[len(individual) - 1])
  return cum_sum 

def cum_sum_calc(individuals, start_v, finish_v):
  cum_sum = []
  current_cum_sum = 0
  if len(individuals) > 1:
    for individual in individuals:
    #  individual = individual[start_v:finish_v]
#
    #  individual = np.array(individual)
    #  cum_sum.append(individual.cumsum()[len(individual) - 1])
      current_cum_sum = cum_sum_calc_individual(individual, start_v, finish_v)
      cum_sum.append(current_cum_sum)
  return cum_sum

# маленькая популяция ?
# турнирный отбор
def tournament_selection(population, percentage_parents, start_v, finish_v):
    p_len = len(population)
    parents = []
    for _ in range(int(round(len(population) * percentage_parents, 0))):
        i1 = i2 = i3 = 0
        #while i1 == i2 or i1 == i3 or i2 == i3 or population[i1] in parents or population[i2] in parents or population[i3] in parents:
        while i1 == i2 or i1 == i3 or i2 == i3:
            i1, i2, i3 = random.randint(0, p_len-1), random.randint(0, p_len-1), random.randint(0, p_len-1)
        individuals = [population[i1], population[i2], population[i3]]
        cum_sum = cum_sum_calc(individuals, start_v, finish_v)
        zipped_list = zip(cum_sum, individuals)
        sorted_list = sorted(zipped_list)
        parents.append(sorted_list[0][1])

    return parents

# отбор по правилу рулетки (пропорциональная приспособленность)
def roulette_selection(population, percentage_parents):
  cum_sum = cum_sum_calc(population, start_v, finish_v)
  parents = []
  p_len = int(len(population) * percentage_parents)
  #var1
  while len(parents) < p_len:
    selected_individual = population[cum_sum.index(random.choice(cum_sum))] 
    if selected_individual not in parents:
      parents.append(selected_individual)
  #var2
  #chance = random.randint(min(cum_sum), max(cum_sum)) 
  #cum_sum_population = {}
  #for i in range(len(cum_sum)):
  #  cum_sum_population[cum_sum[i]] = population[i]
  #cum_sum_population[chance] = []
  #cum_sum_population = sorted(cum_sum_population.items(), reverse=True)
  #cum_index = 0
  #for i in range(len(cum_sum_population)):
  #  if cum_sum_population[i][0] == chance:
  #    cum_index = i
  #    break
  #selected_individual = cum_sum_population[cum_index - 1][1]
  return parents

# стохастическая универсальная выборка
def stochastic_universal_sampling(population):
  pass

# выбор наиболее подходящей половины
def half_choice(population, percentage_parents, start_v, finish_v):
  cum_sum = cum_sum_calc(population, start_v, finish_v)
  zipped_list = zip(cum_sum, population)
  sorted_list = sorted(zipped_list)
  population_size = int(len(population) * percentage_parents)
  new_list = [value[1] for value in sorted_list]
  return new_list[population_size:]


def selection_parents(population, percentage_parents, method, start_v, finish_v):

  if method == 'Tournament selection':
    parents = tournament_selection(population, percentage_parents, start_v, finish_v)
  if method == 'Better half choice':
    parents = half_choice(population, percentage_parents, start_v, finish_v)
  if method == 'Roulette selection':
    parents = roulette_selection(population, percentage_parents)
  return parents
individual = [0, 1, 2, 3, 5, 4]
individual2 = [0, 1, 2, 4, 3, 5]
pop = [individual, individual2]
start_v = 0
finish_v = 3
graph = [[0, 3, 1, 3, inf, inf],
     [3, 0, 4, inf, inf, inf],
     [1, 4, 0, inf, 7, 5],
     [3, inf, inf, 0, inf, 2],
     [inf, inf, 7, inf, 0, 4],
     [inf, inf, 5, 2, 4, 0]]  
print(cum_sum_calc(pop, start_v, finish_v))