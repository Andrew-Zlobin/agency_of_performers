import step_alg
from auxiliary_calculations import sort_population

def move():
  print("step: ")
  step = input()
  if step == 'next_step':
    return "step"
  if step == 'end':
    return "end"
  else:
    return "end"

def run_step():
  current_step = [0]*6
  step = step_alg.Alg_step_controler()
  output_graph = step.graph
  flag = "step"
  for start_v in range(step.size_graph):
    for finish_v in range(step.size_graph):
      if flag == "step":
        flag = move()
      if current_step[0] == 0:  # установка вершин
        if start_v != finish_v:
          step.set_v(start_v, finish_v)
          current_step[0] = 1
          current_step[1] = 0
        else:
          output_graph[start_v][finish_v] = [0]
          continue
      if flag == "step":
        flag = move()
      if current_step[1] == 0: # создание начальной популяции
        step.step1_creation_initial_population()
        current_step[1] = 1
        current_step[2] = 0
      if flag == "step":
        flag = move()
      if current_step[2] == 0: # начало итераций 
        for i in range(int(step.settings['max generations'])):
          if flag == "step":
            flag = move()
          if current_step[3] == 0: # выбор родителей 
            step.step2_choice_parents()
            current_step[3] = 1
          if flag == "step":
            flag = move()
          if current_step[4] == 0: # вычисление вероятности мутации и кроссинговера особей
            step.step3_calculation_probability_mutation_and_crossover()
            current_step[4] = 1
          if flag == "step":
            flag = move()
          if current_step[5] == 0:
          # выбор пары 
          # кроссинговерб
          # оценка выживаемости особи
          # обновление популяции
            step.step4_crossover_and_population_renewal()
            current_step[5] = 1
            current_step[3] = 0
            current_step[4] = 0

        population = step.get_population()
        new_list = sort_population(population, start_v, finish_v)
        new_list[0] = new_list[0][new_list[0].index(start_v):new_list[0].index(finish_v) + 1]
        output_graph[start_v][finish_v] = new_list[0]
        print(new_list[0])
        current_step[2] = 0

      current_step[0] = 0
      current_step[1] = 0

  return output_graph

def main():
  step = step_alg.Alg_step_controler()
  output_graph = step.graph
  if len(output_graph) == 1:
    return [0]
  elif len(output_graph) == 2:
    return output_graph
  else:
    output_graph = run_step()
    
  for line in output_graph:
    print(line)


main()
