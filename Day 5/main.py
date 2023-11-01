#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#contrasena = ""

#for n in range(1, nr_letters +1):
#  contrasena += random.choice(letters)
  
#for n in range(1, nr_numbers +1):
#  contrasena += random.choice(numbers)
  
#for n in range(1, nr_symbols +1):
#  contrasena += random.choice(symbols)

#print(f"This is your password : {contrasena}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

contrasena = []

for n in range(1, nr_letters +1):
  contrasena.append(random.choice(letters))

for n in range(1, nr_numbers +1):
  contrasena += random.choice(numbers)

for n in range(1, nr_symbols +1):
  contrasena += random.choice(symbols)

random.shuffle(contrasena)

password = ""

for char in contrasena:
  password += char

print(f"This is your random password : {password}")