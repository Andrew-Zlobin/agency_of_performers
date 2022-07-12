from auxiliary_calculations import sort_population
import step_alg

step = step_alg.Alg_step_controler()
output_graph = step.graph

for start_v in range(step.size_graph):
  for finish_v in range(step.size_graph):
    # установка вершин
    if start_v != finish_v:
      step.set_v(start_v, finish_v)
      # создание начальной популяции
      step.step1_creation_initial_population()
      # начало итераций 
      for i in range(int(step.settings['max generations'])):
        # выбор родителей 
        step.step2_choice_parents()
        # вычисление вероятности мутации и кроссинговера особей
        step.step3_calculation_probability_mutation_and_crossover()
        # выбор пары 
        # кроссинговерб
        # оценка выживаемости особи
        # обновление популяции
        step.step4_crossover_and_population_renewal()
      population = step.get_population()
      new_list = sort_population(population, start_v, finish_v)
      new_list[0] = new_list[0][new_list[0].index(start_v):new_list[0].index(finish_v) + 1]
      output_graph[start_v][finish_v] = new_list[0]
      print(new_list[0])
    else:
      output_graph[start_v][finish_v] = [0]

for line in output_graph:
  print(line)

