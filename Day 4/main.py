rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random

user = int(input("Introduce el numero segun tu elección Piedra es 0, Papel es 1 y Tijeras es 2 \n\nElige con cuidado!!\n"))

if user == 0:
  print("Tu elección es la Roca")
  print(rock)
elif user == 1:
  print("Tu elección es el Papel")
  print(paper)
elif user == 2:
  print("Tu elección es la Tijera")
  print(scissors)
else:
  print("Solo puedes escojer una opción que te di")

computer = random.randint(0, 2)


if computer == 0:
  print("La computadora eligio la Roca")
  print(rock)
elif computer == 1:
  print("La computadora eligio el Papel")
  print(paper)
elif computer == 2:
  print("La computadora eligio las Tijera")
  print(scissors)
else:
  print("Solo puedes escojer una opción que te di")

if computer == 0 and user == 1:
  print("Papel vence a la roca, Ganaste")
elif computer == 0 and user == 2:
  print("Roca vence a las Tijeras, Perdiste")
elif computer == 1 and user == 0:
  print("Papel vence a la roca, Perdiste")
elif computer == 1 and user == 2:
  print("Tijeras vence al Papel, Ganaste")
elif computer == 2 and user == 0:
  print("Roca vence a las Tijeras, Ganaste")
elif computer == 2 and user == 1:
  print("Tijeras vence al Papel, Perdiste")
else:
  print("Ambos elijieron la misma opción, es un Empate")