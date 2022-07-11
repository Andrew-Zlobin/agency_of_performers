import random


def transposition_adjacent_genes(individual):
  gen = random.randint(1, len(individual) - 2)
  individual[gen], individual[gen + 1] = individual[gen + 1], individual[gen]
  return individual


def gene_inversion(individual):
  gen = 0
  while ~individual[gen] in individual:
    gen = random.randint(0, len(individual) - 1)
  individual[gen] = ~individual[gen] 
  return individual


def transposition_any_genes(individual):
  gen1 = gen2 = 0
  while gen1 == gen2:
      gen1, gen2 = random.randint(1, len(individual) - 1), random.randint(1, len(individual) - 1)
  individual[gen1], individual[gen2] = individual[gen2], individual[gen1]
  return individual


def mutation_gauss(indv, muatation_rate = 2):
  for x in range(muatation_rate):
    indv[x] = round(indv[x] + random.gauss(0, 0.01))
  return indv


def possibility_mutation(individual, mutation_probability, method):
  chance = random.random()
  if chance > mutation_probability:
    return individual
  else:
    if method == 'Transposition adjacent genes':
      individual = transposition_adjacent_genes(individual)
    if method == 'Gene inversion':
      individual = gene_inversion(individual)
    if method == 'Transposition any genes':
      individual = transposition_any_genes(individual)
    return individual

