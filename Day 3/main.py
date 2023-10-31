print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

camino = input("Encontraste una cueva a las orillas de una montaña, te  adentras en ella y te topas con que el camino se divide ¿Quieres ir a la izquierda o derecha?\n").lower()
if camino == "izquierda":
    print("Evitaste una caida mortal y continuas tu camino")
    camino2 = input("Te encuentras con un camino lleno de trampas, ¿Quieres pasar las trampas        'corriendo' o ir 'lentamente'?\n").lower()
    if camino2 == "lentamente":
        print("Pasas cuidadosamente a travez de las trampas y llegas a 3 puertas de diferrentes          colores")
        puerta = input("¿Cual elijes? ¿Amarillo, Azul o Rojo?\n").lower()
        if puerta == "amarillo" or puerta == "azul":
          print("Caes directo a las fauces de un dragón. Haz muerto")
        else:
          print("Encuentras el tesoro escondido y escapas por una salida secreta")
    else:
        print("Una trampa mortal te golpeo y mueres")
else:
    print("Caiste en una trampa, has perdido")