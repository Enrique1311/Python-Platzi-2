import csv

def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader) # transforma la info en un array
    data= []
    for row in reader:
      iterable = zip(header, row) # el zip une ambos array en un array de tuplas
      country_dict = {key: value for key, value in iterable} # itera el array de tuplas y lo transforma en dict
      data.append(country_dict)
    return data

if __name__ == '__main__':
  data = read_csv("./app/data.csv")
  print(data)
  print("*" * 50)
  print(data[0])
