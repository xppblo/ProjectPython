#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Bienvenido a la calculadora de propinas\n")

total = float(input("¿Cuál es el total de la cuenta?\n$"))
amigos = int(input("¿Cuántos amigos son?\n"))
porcentaje = int(input("¿Cuál es el porcentaje de propina?\n%"))
resultado = (total / amigos) * (porcentaje / 100 + 1)
print(f"Cada persona debera pagar: ${resultado: .2f}")