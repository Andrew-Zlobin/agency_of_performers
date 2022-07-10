import random
import matplotlib.pyplot as plt
import numpy as np


def cx_one_point(parents):
    child1 = parents[0]
    child2 = parents[1]  
    genes = random.randint(2, len(parents[0])-3)
    child1[genes:], child2[genes:] = child2[genes:], child1[genes:]
    return child1, child2

#маленький размер графа?
def cx_one_point_modif(parents):
  parent1 = parents[0]
  parent2 = parents[1]
  child1 = parents[0]
  child2 = parents[1]
  
  genes = random.randint(2, len(parent1)-3)

  child1[genes:] = parent1[genes:]
  child2[genes:] = parent2[genes:]

  for locus in range(genes + 1, len(parent2)):
    if parent2[locus] not in child1:
      child1.append(parent2[locus])
  locus = 0    
  while len(child1) != len(parent2):
    if parent1[locus] not in child1:
      child1.append(parent1[locus])    
    locus += 1

  for locus in range(genes + 1, len(parent1)):
    if parent1[locus] not in child2:
      child2.append(parent1[locus])
  locus = 0    
  while len(child2) != len(parent1):
    if parent2[locus] not in child2:
      child2.append(parent2[locus])    
    locus += 1   

  return child1, child2


def cx_two_point(parents):
  genes1 = random.randint(1, len(parents[0]) - 1)
  genes2 = random.randint(1, len(parents[0]) - 1)

  while genes1 > genes2 or genes1 == genes2:
    genes1 = random.randint(1, len(parents[0]) - 1)
    genes2 = random.randint(1, len(parents[0]) - 1)
  child1 = parents[0]
  child2 = parents[1]  
  child1[genes1:], child2[genes1:] = child2[genes1:], child1[genes1:]
  child1[genes2:], child2[genes2:] = child2[genes2:], child1[genes2:]
  return child1, child2


def choice_crossover_method(parents, method='Single Point Mod'):
  if method == 'Single Point':
    child1, child2 = cx_one_point(parents)
  if method == 'Single Point Mod':
    child1, child2 = cx_one_point_modif(parents)
  if method == 'Two Pionts':
    child1, child2 = cx_two_point(parents)

  return child1, child2

#child1 = [1, 2, 5, 6]
#child2 = [6, 5, 2, 1]
#parents = [[1, 2, 5, 6], [6, 5, 2, 1]]
#print(choice_crossover_method(parents, method='Two Pionts'))


