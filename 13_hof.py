# Higher Order Functions
def increment(x): #versión normal
  return x + 1

increment_2 = lambda x: x + 1 # versión lambda

def high_order_function(x, func): # versión normal
  return x + func(x)

high_order_function_2 = lambda x, func: x + func(x) # version lambda

result = high_order_function(2, increment)
print(result)

result = high_order_function_2(3, increment_2)
print(result)

result = high_order_function_2(4, lambda x : x + 8)
print(result)