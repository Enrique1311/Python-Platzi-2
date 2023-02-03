def increment(x): # función normal
  return x + 1

increment_2 = lambda x : x + 1

result = increment(10)
print(result)

result = increment_2(20)
print(result)


full_name = lambda name, last_name: f"El nombre completo es {name.title()} {last_name.title()}" # lanbda function
text = full_name("enrique", "Spinelli")
print(text)
