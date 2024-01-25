#Puedes leer archivos de otro lado y traerlos acá
# r = solo quieres leer el codigo que tiene ese archivo
# w = quieres editar el codigo el codigo que tiene ese archivo
# a = quieres agregar codigo en el codigo que tiene ese archivo
# r+ = quieres editar y leer el codigo el codigo que tiene ese archivo
employee_file = open("employees.txt", "r")

#.readable() = marca si un archivo es leible
print(employee_file.readable())

#.read() = va a leer e imprimir el archivo
print(employee_file.read())

#.readline() = va a leer e imprimir la primera linea del archivo
print(employee_file.readline())


for employee in employee_file.readlines():
    print(employee)

employee_file.close()


