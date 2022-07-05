import random
import matplotlib.pyplot as plt
import numpy as np

def cxOnePoint(child1, child2):
    s = random.randint(2, len(child1)-3)
    child1[s:], child2[s:] = child2[s:], child1[s:]


def cxOnePointModif(child1, child2):
  s = 1
  child1[s:] = child2[s:]
  l = len(child1[s:]) - 1
  for loc in range(len(child2[:s])):
    if child2[l + loc] not in child1:
      child1[l + loc] = child2[l + loc]
  return child1

def mating(parents, method='Single Point'):
    if method == 'Single Point':
      cxOnePoint(parents[0], parents[1])

    if method == 'Single Point Mod':
      cxOnePointModif[parents[0], parents[1]]

    if method == 'Two Pionts':
        pivot_point_1 = random.randint(1, len(parents[0]) - 2)
        pivot_point_2 = random.randint(1, len(parents[0]) - 1)
        print(pivot_point_1, pivot_point_2)
        while pivot_point_2<pivot_point_1:
            pivot_point_2 = random.randint(1, len(parents[0]))
        offsprings = [parents[0][0:pivot_point_1]+
            parents[1][pivot_point_1:pivot_point_2]+
            [parents[0][pivot_point_2:]]]
        offsprings.append([parents[1][0:pivot_point_1]+
            parents[0][pivot_point_1:pivot_point_2]+
            [parents[1][pivot_point_2:]]])

    return offsprings

child1 = [1, 2, 5, 6]
child2 = [6, 5, 2, 1]
parents = [[1, 2, 5, 6], [6, 5, 2, 1]]
print(mating(parents, method='Single Point'))


