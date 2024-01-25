total = 0

def moreT():
    #global hace que la variable que esta afuera de la funcion se conecte con la pones aqui y asi no crea una nueva
    global total
    total += 1
    return total

print(moreT())
print(moreT())
print(moreT())
