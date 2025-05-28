numero_secreto=random.randint(1,100)
noAdivinado=True

def rangoCorrecto(num):
    minimo=1
    maximo=100
    return minimoi>num>maximo
while noAdivinado:
    numeroIngresado= int (input("adivina el numero (entre 1 y 100):" ))
    if rangoCorrecto(numeroIngresado):
        print("por")

 MIERCOLES 28 DE MAYO 

    def nombreDeFuncion(parametros, argumentos):
        print("esto es una funcion")
nombreDeFuncion("parametros",
                "esto es unn argumento")
def ingresarNumero(mensaje):
    entrada = input(mensaje)
    esEntero = int(entrada)
    return esEntero