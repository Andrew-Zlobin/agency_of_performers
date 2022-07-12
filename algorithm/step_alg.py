import graph_alg
import setting_alg
from auxiliary_calculations import sort_population
from selection import selection_parents
import random
import setting_alg
from mutation_and_crossover_probability import calculate_mutation_probability_array
from mutation_and_crossover_probability import calculate_crossover_probability_array
from fitness import fitness_individual_in_population
from crossover import choice_crossover_method
from mutation_and_crossover_probability import calculate_crossover_probability_individual 
from mutation_and_crossover_probability import calculate_mutation_probability_individual
from creator_pop import population_creator
import logging

class Alg_step_controler():
  def __init__(self):
    graph = graph_alg.Graph_alg()
    self.graph = graph.get_graph()
    self.size_graph = len(self.graph)
    logging.basicConfig(filename="sample.log", level=logging.INFO)
    settings = setting_alg.Settings_alg()
    self.settings = settings.get_all_settings_alg()
    # настройки популяции
    self.population_size = int(self.settings['population_size'])
    self.population = []
    # настройки итерации
    self.parents = []
    self.size_parents_population = 0
    self.mutation_probability_array = [] 
    self.crossover_probability_array = []
    self.start_v = 0
    self.finish_v = 0
    self.pair = []

  def set_v(self, start_v, finish_v):
    self.start_v = start_v
    self.finish_v = finish_v
    mes = f"Current graph vertices : {start_v}, {finish_v}" 
    logging.info(mes)

  def get_population(self):
    return self.population  

  def get_best_individual(self):
      individuals = self.population  
      individuals = sort_population(individuals, self.start_v, self.finish_v)
      individuals[0] = individuals[0][individuals[0].index(self.start_v):individuals[0].index(self.finish_v) + 1]
      mes = f"Best individual : {individuals[0]}" 
      logging.info(mes)
      return individuals[0]

  def step1_creation_initial_population(self):
    population = population_creator(self.graph, self.start_v, self.population_size)
    self.population = population
    mes = f"Initial population : {population}" 
    logging.info(mes)
    return population


  def step2_choice_parents(self):
    self.population = sort_population(self.population, self.start_v, self.finish_v)
    self.parents = selection_parents(self.population, float(self.settings['percentage parents']), self.settings['select_method'], self.start_v, self.finish_v)
    self.size_parents_population = len(self.parents)
    self.parents = sort_population(self.parents, self.start_v, self.finish_v)
    mes = f"Choice parents : {self.parents}" 
    logging.info(mes)    
    return self.parents


  def step3_calculation_probability_mutation_and_crossover(self):
    self.mutation_probability_array = calculate_mutation_probability_array(float(self.settings['upper_limit_mutation']), float(self.settings['lower_bound_mutation']), self.size_parents_population)
    self.crossover_probability_array = calculate_crossover_probability_array(float(self.settings['upper_limit_crossover']), float(self.settings['lower_bound_crossover']), self.size_parents_population)
    mes = f" Calculation probability mutation and crossover : {self.mutation_probability_array}, { self.crossover_probability_array}" 
    logging.info(mes)
    return self.mutation_probability_array, self.crossover_probability_array


  def population_renewal(self):
    child1, child2 = choice_crossover_method(self.pair, self.settings['cx_method'])
    mes = f"Chidl1, child2 : {child1}, {child2}" 
    logging.info(mes)
    chance_mutation_child1 = calculate_mutation_probability_individual(self.mutation_probability_array, self.pair[0], self.parents)
    mes = f"Chance mutation child1 : {chance_mutation_child1}" 
    logging.info(mes)
    self.population = fitness_individual_in_population(self.population, child1, chance_mutation_child1, self.settings['mut_method'], self.start_v, self.finish_v)
    chance_mutation_child2 = calculate_mutation_probability_individual(self.mutation_probability_array, self.pair[0], self.parents)
    mes = f"chance mutation child2 : {chance_mutation_child2}" 
    logging.info(mes)
    self.population = fitness_individual_in_population(self.population, child2, chance_mutation_child2, self.settings['mut_method'], self.start_v, self.finish_v)
    return self.population


  def choice_pair(self):
    i1 = i2 = 0
    self.pair = []
    while i1 == i2:
        i1, i2 = random.randint(0, self.size_parents_population - 1), random.randint(0, self.size_parents_population - 1)
    parent1 = self.parents[i1]
    parent2 = self.parents[i2]
    self.pair.append(parent1)
    self.pair.append(parent2)
    mes = f"Choice pair: {parent1}, {parent2}" 
    logging.info(mes)
    return self.pair


  def step4_crossover_and_population_renewal(self):
    for _ in range(self.size_parents_population):
      self.pair = self.choice_pair()
      chance_crossover = calculate_crossover_probability_individual(self.crossover_probability_array, self.pair[0], self.parents)
      mes = f"Chance crossover: {chance_crossover}" 
      logging.info(mes)
      chance = random.random()
      if chance_crossover < chance:
        self.population =  self.population_renewal()
      else:
        continue
    return self.population