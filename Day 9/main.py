from replit import clear
from art import logo

print(logo)
print("Bienvenido a la apuesta secreta malditos malayas")

apostadores = {}

continuar = "si"

def nuevos_apostadores(nombre, apuesta):
  nuevo_apostador = {
    "nombre" : input("Ingresa tu nombre jugador: "),
    "apuesta" : int(input("Ingresa la cantidad a apostar: $"))
  }  
  apostadores[nuevo_apostador['nombre']] = nuevo_apostador['apuesta']

def apuesta_maxima(record_apuesta):
  max_apuesta = 0
  ganador = ""
  for apostadores in record_apuesta:
    cantidad_apuesta = record_apuesta[apostadores]
    if cantidad_apuesta > max_apuesta:
      max_apuesta = cantidad_apuesta
      ganador = apostadores
  print(f"El ganador de la apuesta es {ganador} y ha apostado ${max_apuesta}")
  

while continuar == "yes":
  nuevos_apostadores('nombre', 'apuesta')
  continuar = input("¿Quieres seguir agregando jugadores si o no?\n")
  if continuar == "no":
    continuar = "no"
    apuesta_maxima(apostadores)
  else:
    continuar = "si"
    clear()
#HINT: You can call clear() to clear the output in the console.