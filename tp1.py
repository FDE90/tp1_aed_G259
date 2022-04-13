import random

puntaje_usuario = 0



print("Bienvenido al black jack")
carta_1 = int(input("ingrase carta 1: "))
#CARTA 1 USUARIO
if carta_1 ==1:
    carta_1 = 11
    puntaje_usuario+=carta_1
else:
    if carta_1 == 11 or carta_1 == 12 or carta_1 == 13:
        carta_1 = 10
        puntaje_usuario+=carta_1
    else:
        puntaje_usuario+=carta_1
#CARTA 2 USUARIO
carta_2 = int(input("ingrase carta 2: "))
if carta_2 == 11 or carta_2 == 12 or carta_2 == 13:
    carta_2 = 10
    puntaje_usuario += carta_2
else:
    puntaje_usuario += carta_2
#CARTA 3 USUARIO
if puntaje_usuario<21:
    carta_3 = int(input("ingrase carta 3: "))
    puntaje_usuario += carta_3
print(puntaje_usuario)
    
        




