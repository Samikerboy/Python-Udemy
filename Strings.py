phrase = "Giraffe Academy"
print(phrase + " is cool")

# \n = comando para ponerle un espacio (enter) a un String
print("Giraffe\nAcademy")

# \" = imprime la quotation mark
print("Giraffe\"Academy")

#.lower() = convierte una frase o palabra en minusculas
#.upper() = convierte una frase o palabra en mayusculas
#isupper() o islower() = va a checar si esta en mayusculas o minusculas y dara un resultado booleano
print(phrase.lower().islower())


#len() = te dice cuantos caracteres tiene una frase o una variable
print(len(phrase))

#[] = imprime la letra seleccionada iniciando del 0 al ...
print(phrase[0])

#.index = dice donde esta una letra o un valor
#passing a parameter = el valor que le das a una funcion = parametro
print(phrase.index("a"))

#remplaza una palabra al momento de imprimir pero no cambia la variable
print(phrase.replace("Giraffe", "Elephant"))


