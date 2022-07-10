import itertools


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
