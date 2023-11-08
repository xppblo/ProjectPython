from replit import clear
from art import logo

def suma(n1, n2):
  return n1 + n2

def resta(n1, n2):
  return n1 - n2

def multiplicacion(n1, n2):
  return n1 * n2

def division(n1, n2):
  return n1 / n2

operations = {
  "+": suma,
  "-": resta,
  "*": multiplicacion,
  "/": division
}

def calculator():
  print(logo)

  num1 = float(input("¿Cuál es tu primer numero?: "))
  for symbol in operations:
    print(symbol)
  continuar = True
 
  while continuar:
    operacion_simbolo = input("Escoge tu operador: ")
    num2 = float(input("¿Cuál es tu siguiente numero?: "))
    funcion_calcular = operations[operacion_simbolo]
    respuesta = funcion_calcular(num1, num2)
    print(f"{num1} {operacion_simbolo} {num2} = {respuesta}")

    if input(f"Escribe 'y' para continuar calculando {respuesta}, o escribe 'n' para empezar un nuevo calculo: ") == 'y':
      num1 = respuesta
    else:
      continuar = False
      clear()
      calculator()

calculator()