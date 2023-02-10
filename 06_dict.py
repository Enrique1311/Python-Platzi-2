import random
countries = ["Argentina", "Brasil", "Uruguay"]

population = { country: random.randint(1, 100) for country in countries} #
print(population)

# crea un dict a partir de otro dict con condiciones
result = {country: population for (country, population) in population.items() if population > 20} # (dict comprehension)
print(result)

# crea un dict a partir de un string con las vocales que están en el string con los valores en Mayúscula
text = "Mi nombre es Enrique"
dict = {c: c.upper() for c in text if c in "aeiou"}
print(dict)


