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

#calcular_edad()

def numeros_impares():
    numero = int(input("ingrese el numero:"))

    for i in range(1, numero + 1, 1):
        print(i, end = ", \n ")
        time.sleep(1)
        if i == 60:
            break

#numeros_impares()

def reloj():
    tiempo = int(input("ingresa los segundos que deceas contar:"))

    for i in range(1,tiempo + 1, 1):
        print(i,"seg", end = " \n ")
        #time.sleep(1)
        if i == tiempo:
            print("\33[101m" "llegaste al timpo limite"+"\33[0m")
            break;
        if i == 60:
            break

#reloj()

def intereces_anuales():
    cantidad_Dinero = int(input("Ingresa la cantidad de dinero al año:"))
    inpuesto = float(input("ingresa el valor del interes:"))
    años = int(input("ingresas los años de invercion:"))
    for i in range(1, años + 1, 1):
        print("Año: ",i)
        print("Dinero al año: ", cantidad_Dinero)
        print("Interes: ", cantidad_Dinero * inpuesto / 100)
        print("Dinero total: ", cantidad_Dinero + (cantidad_Dinero * inpuesto / 100))
        print("\n")
        cantidad_Dinero = cantidad_Dinero + (cantidad_Dinero * inpuesto / 100)
        time.sleep(1)

intereces_anuales()

