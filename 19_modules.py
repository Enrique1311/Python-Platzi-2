# módulo para saber el path
import sys
print(sys.path)

# módulo de expresiones regulares
import re 
text = "Mi númer de tel es 15678912345 y el código de mi país es 54"
result = re.findall("[0-9]+", text) # expresión regular para buscar números
print(result)

# módulo para fecha y hora 
import time  
timestamp = time.time()
print(timestamp)

localTime = time.localtime()
result = time.asctime(localTime)
print(result)

# módulos para colecciones
import collections
numbers = [1,1,2,3,3,3,4,5,5,5,5]
counter = collections.Counter(numbers) # retorna un dict con la frecuencia de cada número
print(counter)
