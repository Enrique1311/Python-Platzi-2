def find_volumen(length=2, width=1, depth=1): # valores de los parámetros por defecto
  return length * width * depth, width, "Hola" # si ponemos varios elementos, retorna una tupla 

# asignación de los resultados a distintas variables
volumen, width, text = find_volumen(width=20) # se puedrían colocar sólo los argumentos que queremos

print(volumen)
print(width)
print(text)