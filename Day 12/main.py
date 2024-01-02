#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
import random

print(logo)

numero = random.randint(1, 100)

print(numero)

vidas = 0
print("Bienvenido al juego de la adivinanza")
text = input("Escribe la dificultad del desafio, facil o dificil\n")

if text == "facil":
    vidas = 10
else:
    vidas = 5

print(f"Tienes {vidas} vidas para completar el desafio, buena suerte")

while vidas > 0:
    adivina = int(input("Escribe un numero del 1 al 100:\n"))
    if numero > adivina:
        vidas -= 1
        print(
            f"Haz perdido una vida te quedan {vidas}, es un numero muy bajo sigue intentando"
        )
    elif numero < adivina:
        vidas -= 1
        print(
            f"Haz perdido una vida te quedan {vidas}, es un numero muy alto sigue intentando"
        )
    else:
        vidas = -1
        print(f"Felicidades haz ganado, el numero correcto era {numero}")
if vidas == 0:
    print("Haz perdido no te quedan vidas")