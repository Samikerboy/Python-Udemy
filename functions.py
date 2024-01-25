#def = para crear una funcion
#def ---():
#(parametro) = dice que si quieres un parametro o algo que pida para que se ejecute el comando entonces aqui estamos pidiendo que cuando ejetues el comando que pida un nombre para que lo pueda inprimir con el nombre
def say_hi(name):
    print("Hello " + name)

say_hi(input("whats your name?"))

#al crear el parametro name y ponerle el igual a darth vader le estas dando un valor predeterminado para cuando llames a la funcion y no pongas valores que te ponga ese de default.
def say_hello(name="Darth Vader"):
    print(f"helllllooooooo {name}")

def test(a):

    #Eso sirve para ponerle informacion a una funcion y cuando la quieras usar te diga
    '''
    Info: This functions tests and prints the parameter you give
    '''
    print(a)

test("Hola")

#te imprime para que sirve la funcion justo lo que sta arriba de Info:
help(test)
print(test.__doc__)


#Al poner la * a args hace todos los argumentos en una como si una lista tuviera muchos pero solo es una lista ahi acepta todos los datos de la lsita.
def super_func(*args):
    return sum(args)

super_func(1,2,3,4,5,6)
