import random
import matplotlib.pyplot as plt
 
# p_len - размер популяции
# population - популяция
import fitness
import random
import matplotlib.pyplot as plt
import numpy as np
#test
population = [[10, 1, 9, 9],
               [8, 8, 5, 7],
               [10, 5, 6, 6],
               [8, 5, 7, 4],
               [4, 4, 6, 3],
               [2, 5, 5, 4],
               [8, 0, 6, 0],
               [4, 3, 2, 1]]


# турнирный отбор
def selTournament(population, p_len):
    offspring = []
    for n in range(p_len):
        i1 = i2 = i3 = 0
        while i1 == i2 or i1 == i3 or i2 == i3:
            i1, i2, i3 = random.randint(0, p_len-1), random.randint(0, p_len-1), random.randint(0, p_len-1)

        offspring.append(min([population[i1], population[i2], population[i3]]))

    return offspring


def cum_sum_calc(population):
  cum_sum = []
  for individual in population:
    individual = np.array(individual)
    cum_sum.append(individual.cumsum()[len(individual) - 1])
  
  return cum_sum


# отбор по правилу рулетки (пропорциональная приспособленность)
def fitness_proportionate_selection(population):
  cum_sum = cum_sum_calc(population)
  #var1
  selected_individual1 = population[cum_sum.index(random.choice(cum_sum))] 

  #var2
  chance = random.randint(min(cum_sum), max(cum_sum)) 
  cum_sum_population = {}
  for i in range(len(cum_sum)):
    cum_sum_population[cum_sum[i]] = population[i]
  cum_sum_population[chance] = []
  cum_sum_population = sorted(cum_sum_population.items(), reverse=True)
  cum_index = 0
  for i in range(len(cum_sum_population)):
    if cum_sum_population[i][0] == chance:
      cum_index = i
      break

  selected_individual = cum_sum_population[cum_index - 1][1]
  return selected_individual, selected_individual1

# стохастическая универсальная выборка
def stochastic_universal_sampling(population):
  pass

# выбор наиболее подходящей половины
def half_choice(population):
  cum_sum = cum_sum_calc(population)
  cum_sum_population = {}
  for i in range(len(cum_sum)):
    cum_sum_population[cum_sum[i]] = population[i]
  cum_sum_population = sorted(cum_sum_population.items())
  new_population = []
  for index_sum in range(len(cum_sum_population) // 2):
    sum = cum_sum_population[index_sum]
    new_population.append(sum[1])
  return new_population

p_len = 8
print(selTournament(population, p_len))
print(half_choice(population))
print(fitness_proportionate_selection(population))