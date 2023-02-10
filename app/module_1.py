def get_population():
  keys = ["Arg", "Bra"]
  values = [45000000, 210000000]
  return keys, values

a = "Hola"

def population_by_country(data, country):
  result = list(filter(lambda item: item["Country"] == country, data))
  return result