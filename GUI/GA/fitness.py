from selection import cum_sum_calc
from selection import cum_sum_calc_individual
from mutation import possibility_mutation

def fitness(individual, graph, finish_v):
  route_length = 0
  for index_current_v in range(1, len(individual)):
    route_length += graph[individual[index_current_v - 1]][individual[index_current_v]]
    if individual[index_current_v] == finish_v:
      break
  return route_length


def fitness_individual_in_population(population, individual, mutation_probability, method):
  cum_sum = cum_sum_calc(population)
  zipped_list = zip(cum_sum, population)
  sorted_list = sorted(zipped_list)
  population = [value[1] for value in sorted_list]
  if cum_sum_calc_individual(possibility_mutation(individual, mutation_probability, method)) < cum_sum_calc_individual(population[len(population) - 1]):
    population[len(population) - 1] = individual
  return population