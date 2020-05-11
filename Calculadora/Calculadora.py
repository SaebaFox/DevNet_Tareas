import math
import os
import time
valor1, valor2 = 0,0

def suma (sumando1, sumando2):
   return sumando1 + sumando2

def resta (minuendo, sustraendo):
   return minuendo - sustraendo

def multi (factor1, factor2):
   return factor1 * factor2

def divi (dividendo, divisor):
   if divisor == 0:
      print("no se puede realizar division por 0")
      return dividendo
   else:
      return dividendo / divisor

def divent (dividendo, divisor):
   return dividendo // divisor

def expo (base, exponente):
   return base ** exponente

def raiz(radicando):
   return math.sqrt(radicando)

def operacion():
   print("**********************")
   print("Introduce la operacion")
   print("+ suma ")
   print("- resta")
   print("* multiplicacion")
   print("/ division")
   print("** exponente")
   print("sqrt raiz cuadrada")
   print("**********************")
   return input("")

def calcular(valor1,operacion,valor2=""):
   if (operacion == "+" or operacion == "suma"):
      return suma(valor1,valor2)

   elif(operacion == "-" or operacion == "resta"):
      return resta(valor1,valor2)

   elif(operacion == "*" or operacion == "multiplicacion"):
      return multi(valor1,valor2)

   elif(operacion == "/" or operacion == "division"):
      return divi(valor1,valor2)

   elif(operacion == "**" or operacion == "exponente"):
      return expo(valor1,valor2)

   elif(operacion == "sqrt" or operacion == "raiz"):
      return raiz(valor1)

   elif(operacion == "-" or operacion == "cuadrado"):
      return raiz(valor1,2)
   else:
      print("operacion no soportada")



def mostrarResultado(resul,valor1,operacion,valor2 ="",):
   print(valor1,operacion,valor2,"=",resul)
   input()

def valor():
   valorintroducido = input("Introduce un valor \n")
   try:
      return int(valorintroducido)
   except:
      print("no es un numero")
      return valor();

def calcular_menu():
   while True :
      os.system("clear")
      valor1 = valor()
      os.system("clear")
      operacio = operacion()
      if (operacio == "sqrt" or operacio == "raiz"):
         mostrarResultado(calcular(valor1,operacio),valor1,str(operacio))
      else:
         os.system("clear")
         valor2 = valor()
         os.system("clear")
         mostrarResultado(calcular(valor1,operacio,valor2),valor1,str(operacio),valor2)


print(multi(valor1,valor2))
calcular_menu()