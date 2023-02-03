items = [
  {
    "product": "camisa",
    "price": 8000,
  },
  {
    "product": "pantalones",
    "price": 10000
  },
  {
    "product": "remera",
    "price": 6000
  }
]

prices = list(map(lambda item: item["price"], items))
print(prices)

def add_taxes(item):
  new_item = item.copy() # crea una copia de la lista con los nuevos atributos y no modifica el original
  new_item["taxes"] = new_item["price"] * .21
  return new_item

new_items = list(map(add_taxes, items)) # agrega un atributo al dict
print(new_items)
print(items)