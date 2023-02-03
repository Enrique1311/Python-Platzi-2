price = 100 # global: no se puede usar dentro de una función


def increment():
  price = 200 # dentro de la función
  price = price + 10
  print(price)
  return price

print(price)
price_2 = increment()
print(price_2)