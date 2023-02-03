'''
# crea una lista con un ciclo for
numbers = []
for element in range(1, 11):
  numbers.append(element)

print(numbers)

numbers_2 = [element for element in range(1, 11)] # (set comprehension) en una sóla línea de código
print(numbers_2)

# crea una lista multiplicando cada elemento por 3
numbers_mult = []
for element in range(1, 11):
  numbers_mult.append(element * 3)

print(numbers_mult)

numbers_mult_2 = [element * 2 for element in range(1, 11)] # (set comprehension) en una sóla línea
print(numbers_mult_2)
''' 
# crea una lista con los elementos pares mult por dos
numbers = []
for i in range(1, 11):
  if i % 2 == 0:
    numbers.append(i * 2)

print(numbers)

numbers_2 = [i * 2 for i in range(1, 11) if i % 2 == 0] # (list comprehension) en una sóla línea
print(numbers_2)
