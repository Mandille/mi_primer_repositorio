import sys

def multiplicar (a,b):
    return a*b

if len(sys.argv) == 3:
    nombre=sys.argv[1]
    cantidad=int(sys.argv[2])
    multiplcado=multiplicar(cantidad,2)

    for i in range(multiplcado):
        print("Hola",nombre)

else:  
    print("Atención, espera 2 argumentos")


