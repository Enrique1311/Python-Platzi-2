import module_1

data = [
  {
    "Country": "Argentina",
    "Population": 45000000
  },
      {
    "Country": "Brasil",
    "Population": 210000000
  }
]

# se coloca dentro de una función para que no se ejecute automáticamente
# para ejecutarlo hay que llamar a la función
def run():
  keys, values = module_1.get_population()
  print(keys, values)

  print(module_1.a)

  country = input("Ingresa un país: ")

  result = module_1.population_by_country(data, country)
  print(result)

if __name__ == "__main__": # es para que permita ejecutar desde la terminal éste archivo
  run()

