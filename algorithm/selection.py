import random
import fitness
import matplotlib.pyplot as plt
import numpy as np

def cum_sum_calc_individual(individual):
  cum_sum = []
  individual = np.array(individual)
  cum_sum.append(individual.cumsum()[len(individual) - 1])
  return cum_sum 

def cum_sum_calc(individuals):
  cum_sum = []
  if len(individuals) > 1:
    for individual in individuals:
      individual = np.array(individual)
      cum_sum.append(individual.cumsum()[len(individual) - 1])
  return cum_sum

# маленькая популяция ?
# турнирный отбор
def tournament_selection(population, percentage_parents):
    p_len = len(population)
    parents = []
    for _ in range(int(round(len(population) * percentage_parents, 0))):
        i1 = i2 = i3 = 0
        while i1 == i2 or i1 == i3 or i2 == i3 or population[i1] in parents or population[i2] in parents or population[i3] in parents:
            i1, i2, i3 = random.randint(0, p_len-1), random.randint(0, p_len-1), random.randint(0, p_len-1)
        individuals = [population[i1], population[i2], population[i3]]
        cum_sum = cum_sum_calc(individuals)
        zipped_list = zip(cum_sum, individuals)
        sorted_list = sorted(zipped_list)
        parents.append(sorted_list[0][1])

    return parents

# отбор по правилу рулетки (пропорциональная приспособленность)
def roulette_selection(population, percentage_parents):
  cum_sum = cum_sum_calc(population)
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
def half_choice(population, percentage_parents):
  cum_sum = cum_sum_calc(population)
  zipped_list = zip(cum_sum, population)
  sorted_list = sorted(zipped_list)
  population_size = len(population) * percentage_parents
  new_list = [value[1] for value in sorted_list]
  return new_list[population_size:]


def selection_parents(population, percentage_parents, method = 'Tournament selection'):

  if method == 'Tournament selection':
    parents = tournament_selection(population, percentage_parents)
  if method == 'Better half choice':
    parents = half_choice(population, percentage_parents)
  if method == 'Roulette selection':
    parents = roulette_selection(population, percentage_parents)
  return parents