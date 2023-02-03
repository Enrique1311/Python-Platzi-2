set_countries = {"Arg", "Bra", "Uru"}

size = len(set_countries)
print (size)

print("Arg" in set_countries) # True

set_countries.add("Par") # agrega un elemento
print(set_countries)

set_countries.update({"Chi", "Col", "Per"}) # agrega varios elementos
print(set_countries)

set_countries.remove("Chi") # elimina
