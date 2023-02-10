# print(0/0)
# print(result)

suma = lambda x, y:x + y
assert suma(2, 2) == 4 # verifica que sea correcto el resultado
# si no es correcto, devuelve un error

age = 10
if age < 18:
  raise Exception("No se permiten menores de edad")