# import utils
'''
import read_csv
import charts

def run():
  print("1- América del Sur")
  print("2- América del Norte")
  print("3- Oceanía")
  print("4- Europa")
  print("5- Asia")
  print("6- Africa")
  
  continentNumber = input('Escribe el núumero de continente quieres conocer los porcentajes de población: ')
  
  if continentNumber == "1":
    continent = "South America" 
    runGraph(continent)
  elif continentNumber == "2":
    continent = "North America"
    runGraph(continent)
  elif continentNumber == "3":
    continent = "Oceania"
    runGraph(continent)
  elif continentNumber == "4":
    continent = "Europe"
    runGraph(continent)
  elif continentNumber == "5":
    continent = "Asia"
    runGraph(continent)
  elif continentNumber == "6":
    continent = "Africa"
    runGraph(continent)
  else:
    print('¡Número incorrecto!')

def runGraph(continent):
  data = read_csv.read_csv('./app/data.csv')

  data = list(filter(lambda item: item['Continent'] == continent, data))

  countries = list(map(lambda x: x['Country'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  charts.generate_pie_chart(countries, percentages)



'''
'''
def run():
  data = read_csv.read_csv('./app/data.csv')
  country = input("Ingresa un país: ")
  
  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(labels, values)
'''
'''

if __name__ == "__main__": 
  run()
'''

a = {1,2}
b = {2,3}
print(a & b)