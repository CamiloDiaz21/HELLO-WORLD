import time
def ejercico1():
    palabra = str(input("Por favor ingresar palabra:"))
    Cantidad = int(input("por favor ingresar la cantidad de veces:"))
    for i in range(Cantidad):
        print("valor de la variable: ", i + 1)
        print(palabra)
        time.sleep(2)
#ejercico1()

def cantidad_años():
    Edad = int(input("ingrese la cantidad de años que tienes:"))
    for i in range(Edad):
        print("valor de la edad: ", i + 1)
        time.sleep(1)

#cantidad_años()

def calcular_edad():
    año = int(input("ingresar el año actual: "))
    añon = int(input("ingresar el año de nacimiento:"))
    edad = año- añon
    for i in range(edad + 1):
        print("Año: ",añon + i +1)
        print(i+1)
        time.sleep(1)
    return edad

calcular_edad()