# definir una función
def my_print():
  print("This is my print function")
  print("This is my print function (2)") 
my_print()

def my_print_2(text): # con parámetro
  print(text * 2) 

my_print_2("Hello")
my_print_2("World")

def suma(a, b):
  print(f"La suma de {a} + {b} = {a + b}")
  my_print_2(a + b) # llamada de una funcion dentro de otra funcuón

suma(20,30)

