import graph_alg


def sort_population(population, start_v, finish_v):
  cum_sum = cum_sum_calc(population, start_v, finish_v)
  zipped_list = zip(cum_sum, population)
  sorted_list = sorted(zipped_list)
  population = [value[1] for value in sorted_list]
  return population


def cum_sum_calc_individual(individual, start_v, finish_v):
  cum_sum = 0
  current_v = start_v
  graph = graph_alg.Graph_alg().get_graph()
  for i in range(len(individual) - 1):
    if current_v == finish_v: break
    cum_sum += graph[current_v][individual[i + 1]]
    current_v = individual[i + 1]
  return cum_sum 


def cum_sum_calc(individuals, start_v, finish_v):
  cum_sum = []
  current_cum_sum = 0
  if len(individuals) > 1:
    for individual in individuals:
      current_cum_sum = cum_sum_calc_individual(individual, start_v, finish_v)
      cum_sum.append(current_cum_sum)
  return cum_sum