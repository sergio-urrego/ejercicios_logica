from random import randint
from os import system
etapas=[[0,0,0,0,0],
        [0,0,0,0,0], 
        [0,0,0,0,0],
        [0,0,0,0,0]]
ciclistas=["sharick","yuri","hugo","allan","sara"]
for f in range (len(etapas)):
        for c in range (5):
                etapas [f][c]= randint(180,360)*(60)        

salir=0
while salir==0: 
        system("cls")
        def menu():
                print("________________________________________________________________________________________________")
                print("--------------------------------------BIENVENIDO------------------------------------------------")
                print("________________________________________________________________________________________________")
                print("elija una opción")
                print("1.ganador por etapa")
                print("2.ganador de la vuelta")
                print("3.ganador por  cada etapasa")
                return(menu)
        menu()
        #print(etapas)

        opcion=int(input("elija una de las opciones anteriores\n"))

        if opcion == 1:
                etapa=int(input("elija una de las 5 etapas\n"))
                c=etapa-1
                ganador=[]
                for f in range (len(etapas)):
                        ganador.append(etapas[f][c])
                minimo=min(ganador)
                definitivo=ciclistas[ganador.index(minimo)]
                print("--------------------------------------------------------------------------------------------------")
                print(f"el ganardor de la etapa {etapa} es {definitivo} con un tiempo {minimo} segundos")
                input("presione enter para continuar")
                salir=0
        elif opcion==2:
                total=[]
                lista=[]
                for f in range (len(etapas)):
                        for c in range (5):
                                lista.append(etapas[f][c])
                vuelta=total.append(sum(lista))
                tiem=min(total)
                ganadorv=ciclistas[total.index(tiem)]
                print("--------------------------------------------------------------------------------------------------")
                print(f"el ganador es {ganadorv} con un tiempo de {tiem} segundos ")
                input("presione enter para continuar")
                salir=0
        elif opcion==3:
                for c in range (5):
                        t=[]
                        for f in range(len(etapas)):
                                t.append(etapas[f][c])
                        tiempos=min(t)
                        nombre=ciclistas[t.index(tiempos)]
                        print("--------------------------------------------------------------------------------------------------")
                        print(f"el ganador de la etapa {c+1} es {nombre} con un tiempo de {tiempos} segundos")
                        input("presione enter para continuar")
                        salir=0


