
def suma_dos_valores(sumando1, sumando2,):
  global resultado
  resultado = sumando1 + sumando2
  return resultado 

#suma_dos_valores(9.5,5.9)
#print ("Primera suma:",resultado)
#suma_dos_valores(1,6)
#print ("Segunda suma:",resultado)

#def Calculadora_dos_valores(numero1, numero2, operador):
  
 # global resultado
  #if operador == 1:
   #resultado= numero1 + numero2 # si el operador es 1 es suma 
   #return resultado
  #elif operador == 2:
   # resultado= numero1 - numero2 # si el operador es 2 es resta 
    #return resultado
  #elif operador == 3:
   # resultado= numero1 * numero2 # si el operador es 3 es resta 
    #return resultado
  #elif operador == 4:
   # if numero2 != 0:
    #  resultado= numero1 / numero2 # si el operador es 4 es division
     # return resultado
   # else:
      #return "Error: División por cero"
  #else:
   # return "Error: Operador no válido"
  
#Calculadora_dos_valores(2,9,1)
#print ("Resultado de la suma:",resultado)
#Calculadora_dos_valores(2,9,2)
#print ("Resultado de la resta:",resultado)
#Calculadora_dos_valores(2,9,3)
#print("Resultado de la multiplicacion:",resultado)
#Calculadora_dos_valores(2,9,4)
#print("Resultado de la Divicion:",resultado)


def Teorema_pitagoras(a,b):
    global c
    c= (a**2+b**2)**0.5
    return c
#Teorema_pitagoras(4,5)
#print("Resultado de la hipotenusa es:",c)


def despeje_x():
  global x
  b=int(input("ingrese el valor de b="))
  c=int(input("ingrese el valor de c="))
  x=(c-b)/2
  print("El despejede x es:",x)
  return x
#despeje_x()

def funcion_and():
  global x
  a= bool(input("ingrese el valor de a:"))
  b= bool(input("ingrese el valor de b:"))
  c= bool(input("ingrese el valor de c:"))
  x= a and b and c
  print("El resultado del and es:",x)
  return x 

#funcion_and()

def pitagoras_funscion_sumar():
  global resul_pitagoras
  a = int(input("ingrese el valor de a:"))
  b = int(input("ingrese el valor de b:"))
  a2= a**2
  b2= b**2

  suma = suma_dos_valores(a2,b2)
  resul_pitagoras = suma**0.5
  print("el valor de pitagoras es:",resul_pitagoras)
  return resul_pitagoras

#pitagoras_funscion_sumar()
#def separador_contador():
 #  global resultado_contador
  # txt =str(input("ingrese la palabra:"))
   #letra = str(input("ingresela letra a contar:"))
   #resultado_contador = txt.count(letra)
   #print("esta es la cantidad de letas:",resultado_contador)

#letra = (txt)
#for letra in palabra:
 #   print(letra)
    

import random

def obtener_eleccion_computadora():
    opciones = ["piedra", "papel", "tijera"]
    return random.choice(opciones)

def determinar_ganador(jugador1, jugador2):
    if jugador1 == jugador2:
        return "Empate"
    elif (jugador1 == "piedra" and jugador2 == "tijera") or \
         (jugador1== "papel" and jugador2 == "piedra") or \
         (jugador1 == "tijera" and jugador2 == "papel"):
        return "Jugador1 gana"
    else:
        return "jugador2 gana"

def juego_piedra_papel_tijera():
    jugador1 = obtener_eleccion_computadora()  # El jugador también elige automáticamente
    jugador2 = obtener_eleccion_computadora()
    
    print(f"Jugador1 elige: {jugador1}")
    print(f"jugador2 elige: {jugador2}")
    
    resultado = determinar_ganador(jugador1, jugador2)
    print(f"Resultado: {resultado}")

# Ejecutar el juego
juego_piedra_papel_tijera()





   