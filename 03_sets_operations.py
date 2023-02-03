set_a = {"Arg", "Bra", "Uru"}
set_b = {"Col", "Bra", "Ecu"}

set_c = set_a.union(set_b) # une dos sets
print(set_c)
print(set_a | set_b) # (set comprehension) otra forma de unir

set_d = set_a.intersection(set_b) # crea un conjunto con los elementos en común
print(set_d)
print(set_a & set_b) # (set comprehension) otra forma de hacerlo

set_dif = set_a.difference(set_b) # a partir de set_a crea un conjunto con los elementos que son distintos
print(set_dif)
print(set_a - set_b) # (set comprehension) otra forma de hacerlo

set_sym_dif = set_a.symmetric_difference(set_b) # crea un conjunto con los elementos que no se repiten de ambos
print(set_sym_dif)
print(set_a ^ set_b) # (set comprehension) otra forma de hacerlo