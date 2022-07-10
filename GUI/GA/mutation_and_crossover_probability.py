import decimal
import numpy as np

def float_range(start, stop, step):
  while start < stop:
    yield float(start)
    start += decimal.Decimal(step)


def calculate_mutation_probability_array(upper_limit_mutation, lower_bound_mutation, population_size):
  mutation_range = upper_limit_mutation - lower_bound_mutation
  mutation_step = round(mutation_range / population_size, 4)
  #upper_limit_mutation = mutation_step * population_size
  mutation_p = [i for i in np.arange(lower_bound_mutation, upper_limit_mutation, mutation_step)]
  return mutation_p


def calculate_crossover_probability_array(upper_limit_crossover, lower_bound_crossover, population_size):
  crossover_range = upper_limit_crossover - lower_bound_crossover
  crossover_step = round(crossover_range / population_size, 4)
  #upper_limit_mutation = mutation_step * population_size
  crossover_p = [i for i in np.arange(lower_bound_crossover, upper_limit_crossover, crossover_step)]
  crossover_p.sort(reverse=True)
  return crossover_p


def calculate_mutation_probability_individual(mutation_probability_array, individual, population):
  unit_num = 0
  for unit_num in range(len(population)):
    if population[unit_num] == individual:
      break
  return mutation_probability_array[unit_num]


def calculate_crossover_probability_individual(crossover_probability_array, individual, population):
  unit_num = 0
  for unit_num in range(len(population)):
    if population[unit_num] == individual:
      break
  return crossover_probability_array[unit_num]