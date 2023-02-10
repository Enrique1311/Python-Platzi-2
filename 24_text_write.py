# # Agregar texto a un archivo
# with open("./text.txt", "r+") as file: # +r es para que permita la lectura y escritura
#   for line in file: 
#     print(line)
#   file.write("nuevo texto en éste archivo\n") # \n es para hacer un salto de línea
#   file.write("otra linea\n")
#   file.write("otra linea\n") 

with open("./text.txt", "w+") as file: # +r es para que permita la lectura y sobreescritura
  for line in file: 
    print(line)
  file.write("nuevo texto en éste archivo\n") # \n es para hacer un salto de línea
  file.write("otra linea\n")
  file.write("otra linea\n") 

