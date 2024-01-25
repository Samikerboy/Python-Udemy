#name = [] = crea una lista para almacenar datos
friends = ["Kevin", "Karen", "Jim", "Bob", "John"]
lucky_numbers = [1, 12, 53, 129, 2]

# [2] = da el resultado de el numero que esta en la lista
print(friends[2])

# [n:] = agarra todos empezando por el numero que se puso
print(friends[1:])

friends[1] = "Mike"
print(friends)


#.extend() = agrega otra lista
friends.extend(lucky_numbers)

#.append() = agrega elementos a la lista
friends.append("Creed")

#.insert() = tiene dos parametros, uno para decir que quieres agregar y otro para especificar donde
friends.insert(1, "Kelly")

#.remove() = elimina el elemento de la lista seleccionado
friends.remove("Jim")

#.clear() = elimina todo lo que esta en una lista
friends.clear()

#elimina un elemento al azar de la lista
friends.pop()

#.index() te dira donde esta el elemento seleccionado
friends.index("Kevin")

#.count() dira cuantos elementos tienen el mismo nombre
friends.count("Mike")

#.sort() = solo funciona con tipos int y los ordena de mayor a menor
lucky_numbers.sort()

#.reverse() = solo funciona con tipos int y los ordena de menor a mayor
lucky_numbers.reverse()

#.copy() = copia una lista a otra.
friends2 = friends.copy()

print(friends)