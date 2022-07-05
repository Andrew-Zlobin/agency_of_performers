import random
import matplotlib.pyplot as plt
 
P_MUTATION = 0.1        # вероятность мутации индивидуума
#test
population = [[10, 1, 9, 9],
               [8, 8, 5, 7],
               [10, 5, 6, 6],
               [8, 5, 7, 4],
               [4, 4, 6, 3],
               [2, 5, 5, 4],
               [8, 0, 6, 0],
               [4, 3, 2, 1]]


def mutation_neighb_trans(indv):
  gen = random.randint(0, len(indv)-2)
  double_gen = indv + indv
  indv[gen] = double_gen[gen + 1]
  indv[gen + 1] = double_gen[gen]
  return indv


def mutation_trans(indv):
  i1 = i2 = 0
  while i1 == i2:
      i1, i2 = random.randint(0, len(indv)-1), random.randint(0, len(indv)-1)
  indv[i1], indv[i2] = indv[i2], indv[i1]
  return indv

def mutation_gauss(indv, muatation_rate = 2):
  for x in range(muatation_rate):
    indv[x] = round(indv[x] + random.gauss(0, 0.01))
  return indv

def mut_gen(population, P_MUTATION):
  new_population = []
  for indv in population:
    chance = random.random()
    if chance > P_MUTATION:
      new_indv = mutation_trans(indv) 
      new_population.append(new_indv)
    else:
      new_population.append(indv)
  return new_population

print(mut_gen(population, P_MUTATION))
