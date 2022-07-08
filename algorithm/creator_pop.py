import random
import itertools

inf = 100

graph = [[9, 3, 1, 3, inf, inf],
     [3, 0, 4, inf, inf, inf],
     [1, 4, 0, inf, 7, 5],
     [3, inf, inf, 0, inf, 2],
     [inf, inf, 7, inf, 0, 4],
     [inf, inf, 5, 2, 4, 0]]  

start_v = 0
population_size = 5
def population_creator(graph, start_v, population_size):
    random_v = [i for i in range(len(graph))]
    random_v.pop(start_v)
    com = itertools.permutations(random_v)
    number_of_individuals = 0
    population = []
    for val in com:
        if number_of_individuals == population_size:
          break
        
        individual = list(val)
        individual.insert(0, start_v)
        population.append(individual)
        number_of_individuals += 1
    return population 

print(population_creator(graph, start_v, population_size))