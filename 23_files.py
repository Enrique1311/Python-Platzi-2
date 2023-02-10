file = open("./text.txt")
# print(file.read())
# print(file.readline()) # lee línea por línea
# print(file.readline())
# print(file.readline())

for line in file: # también lee línea por línea
  print(line)

file.close() # cierra el archivo para liberar memoria

with open("./text.txt") as file: # Abre y cierra el archivo a leer
  for line in file: 
    print(line)