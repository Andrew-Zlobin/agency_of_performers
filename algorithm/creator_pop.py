import random


inf = 100

graph = [[9, 3, 1, 3, inf, inf],
     [3, 0, 4, inf, inf, inf],
     [1, 4, 0, inf, 7, 5],
     [3, inf, inf, 0, inf, 2],
     [inf, inf, 7, inf, 0, 4],
     [inf, inf, 5, 2, 4, 0]]  

max_ways = len(graph)**2
length_chrom = 6
pop = []
ver1 = 0
ver2 = 5

def pop_creat(ver1, ver2, length_chrom, graph):
  pop = []
  for _ in range(len(graph)):
    indv = [ver1]
    while len(indv) < length_chrom - 1:
      chance = ver1

      while chance == ver1 or chance == ver2 or chance in indv:
        chance = round(random.randint(0, length_chrom - 1))
      indv.append(chance)
    indv.append(ver2)
    pop.append(indv)
    print(indv)
  print(pop)
  return pop

print(pop_creat(ver1, ver2, length_chrom, graph))
