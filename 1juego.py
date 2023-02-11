from random import randint
from os import system

intentos=0

inicio = 0
while inicio == 0 :
    numero=randint(0,100)
    system("cls")
    print("----------------------------------------------------------------------------------------------")
    print("---------------------------------Bienvenido-------------------------------------------------- ")
    print("----------------------------------------------------------------------------------------------")
    nombre=str(input("------------------------------escribe tu nombre----------------------------------------------------- \n"))
    opcion1=str(input(f"{nombre} desea jugar a adivinar el numero de 1 a 100?\nsi/no? "))
    while opcion1 !="no" and opcion1 != "si":
        opcion1=str(input("operacion erronea digita\nsi/no? "))
    if opcion1=="si":
        print(numero)
        while intentos==0:
            usuario=int(input(f"digite un entero de 1 a 100\n' "))
            print("---------------------------------------------------------------------------------")
            intentos=intentos+1
            while usuario < numero:
                print("el numero es mayor al digitado ") 
                usuario=int(input(f"vuelve a intentarlo llevas {intentos} intentos\n "))
                print("---------------------------------------------------------------------------------")
                intentos=intentos+1
            while usuario>numero:
                print("el numero es menor al digitado") 
                usuario=int(input(f"vuelve a intentarlo llevas {intentos} intentos\n "))
                print("---------------------------------------------------------------------------------")
                intentos=intentos+1
            if usuario == numero :
                intentos=intentos+1  
                print(f"bien, adivinaste el numero que era {numero} en {intentos} intentos")
                print("---------------------------------------------------------------------------------")
                opcion1=str(input("desea volver a intentarlo?\nsi/no? "))
            if opcion1 == "no":
               inicio = 1
    elif opcion1 =="no" :
        print ("Salida Exitosa...Lo esperamos pronto....")
        inicio=1