import random

puntaje_usuario = 0
carta1_carta2_no_suman21 = False


print("Bienvenido al black jack")
carta_1 = int(input("ingrase carta 1: "))
#CARTA 1 USUARIO
if carta_1 == 1:
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
# CAMBIO DE VALORES A CARTA_2 
if carta_2 == 11 or carta_2 == 12 or carta_2 == 13:
    carta_2 = 10
else:
    if carta_1 < 10 and carta_2 == 1:
        carta_2 = 11
        puntaje_usuario += carta_2

# CASO BACK JACK CON 2 CARTAS
if (carta_2*11 + carta_1 == 21) or (carta_1+carta_2==21):
    puntaje_usuario = 21
    print("su puntaje es: ",puntaje_usuario,"BACK JACK")
else:
    if carta_1 + carta_2 < 21:
        carta_3 = int(input("ingrase carta 3: "))
    else:
        if carta_3 == 11 or carta_3 == 12 or carta_3 == 13:
            carta_3 = 10
            puntaje_usuario += carta_3
            print("su puntaje es: ",puntaje_usuario)
            
#     else:
#         if carta_2 == 1:
#             carta_2 = 1
#             puntaje_usuario+=carta_2
#CARTA 3 USUARIO
# if puntaje_usuario<21:
#     carta_3 = int(input("ingrase carta 3: "))
#     carta1_carta2_no_suman21 = True
# else:
#     print("su puntaje es: ", puntaje_usuario, "ha perdido")

# if carta_3 == 11 or carta_3 == 12 or carta_3 == 13:
#     puntaje_usuario+=carta_3
#     print("su puntaje es: ", puntaje_usuario, "ha perdido")
# else:
#     if carta_3 == 1:
#         carta_3 = 1
#         puntaje_usuario+=carta_3
#         print("su puntaje es: ", puntaje_usuario)
#     else:
#         puntaje_usuario+=carta_3
#         print("su puntaje es: ", puntaje_usuario)

        




