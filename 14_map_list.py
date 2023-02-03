numbers = [1, 2, 3, 4, 5]
numbers_2 = []

for i in numbers:
  numbers_2.append(i * 2)

print(numbers)
print(numbers_2)

numbers_3 = list(map(lambda i : i * 3, numbers)) # 

print(numbers_3)

numbers_4 = [1, 2, 3, 4]
numbers_5 = [5, 6, 7, 8]

result = list(map(lambda x, y : x + y, numbers_4, numbers_5)) # devuelve una lista con la suma los elementos de dos listas
print(result)