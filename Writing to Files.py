#Puedes leer archivos de otro lado y traerlos acá
# a = quieres agregar codigo en el codigo que tiene ese archivo
employee_file = open("employees.txt", "a")

#.write() = te deja escribir otras cosas en el archivo
print(employee_file.write("\nToby - Human Resources"))


employee_file.close()

