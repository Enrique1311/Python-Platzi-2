'''
# crea un dict a partir de un for
dict = {}
for i in range(1, 6):
  dict[i] = i
print(dict)

dict_2 = {i: i for i in range(1, 6)} # (dict comprehension) en una sóla línea
print(dict_2)

# crea un dict a partir de un for multiplicando el valor por 2
dict_3 = {}
for i in range(1, 6):
  dict_2[i] = i * 2
print(dict_2)

dict_4 = {i: i * 2 for i in range(1, 6)} # (dict comprehension) en una sóla línea
print(dict_4)
'''

# crea un dict a partir de una lista
import random
countries = ["Argentina", "Brasil", "Uruguay"]
population = {}
for country in countries:
  population[country] = random.randint(1, 100)

print(population)

population_2 = { country: random.randint(1, 100) for country in countries} # (dict comprehension)
print(population_2)

# crea un dict a partir de dos listas
names = ["Martu", "Santi", "Caro"]
ages = [14, 6, 42]

print(list(zip(names, ages))) # crea una lista con tuplas con la combinacion de dos listas

new_dict = {name: age for (name, age) in zip(names, ages)} # (dict comprehension)
print(new_dict)
