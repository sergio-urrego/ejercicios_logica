from random import randint
from os import system
contador1=0
contador2=0
dado1=0
dado2=0
acumulado=0
repetir=""
system("cls")
inicio=0
while inicio==0:
    system("cls")
    jugador1=str(input("digite el nombre del primer jugador "))
    jugador2=str(input("digite el nombre del segundo jugador "))
    print("-----------------------------------------------------------------------------------------------")
    while jugador1==jugador2:
        print('lo sentimos no puedo haber dos jugadores con el mismo nombre')
        jugador1=str(input("vuelva a digitar el nombre del primer jugador "))
        jugador2=str(input("vuelva a digitar el nombre del segundo jugador "))
        print("-----------------------------------------------------------------------------------------------")
    puntos=int(input("digite a cuantos puntos desean jugar  que sea mayor a 50\n- "))
    while puntos < 50:
        puntos=int(input("digite a cuantos puntos desean jugar pero esta vez que sea mayor a 50\n- "))

    if contador1==0 and contador2==0:
        while contador1<puntos and contador2<puntos:
            print(contador1)
            print(contador2)
            tirador1=str(input(f'{jugador1} digite "si" para tirar el dado '))
            dado1=randint(1,6)
            if tirador1 =="si":
                print(f'el numero es {dado1}')
            tirador2=str(input(f'{jugador2} digite "si" para tirar el dado '))
            dado2=randint(1,6)
            if tirador1 =="si":
                print(f'el numero es {dado2}')
            if dado2< dado1:
                print(f'como {jugador1} saco mayor puntaje se gana tambien la cantidad de {jugador2}')
                while acumulado>0:
                    contador1=contador1+acumulado
                    acumulado=0
                contador1=contador1+dado1+dado2
                print("-----------------------------------------------------------------------------------------------")
            if dado1< dado2:
                print(f'como {jugador2} saco mayor puntaje se gana tambien la cantidad de {jugador1}')
                while acumulado>0:
                    contador2=contador2+acumulado
                    acumulado=0
                contador2=contador2+dado1+dado2
                print("-----------------------------------------------------------------------------------------------")
            if dado1==dado2:
                print('como estan empatados el sigiente que saque puntaje mayor se lleva la suma del puntaje anterior ')
                acumulado=dado1+dado2
                print("-----------------------------------------------------------------------------------------------")
            if contador1>=puntos:
                print(f'el ganador es {jugador1} con {contador1} puntos a {contador2} puntos ')
                repetir=str(input("desea volver a jugar?\nsi/no?- "))
            elif contador2>=puntos:
                print(f'el ganador es {jugador2} con {contador2} puntos a {contador1} puntos ')
                repetir=str(input("desea volver a jugar?\nsi/no?- "))
            if repetir=="no":
                print("gracias por aver jugado ")
                inicio=1



        


