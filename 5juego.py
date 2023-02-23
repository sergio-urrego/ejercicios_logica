from os import system
notas=[]
alumnos=[]
def menu1():
    print("________________________________________________________________________________________________")
    print("--------------------------------------BIENVENIDO------------------------------------------------")
    print("________________________________________________________________________________________________")
    print("1.insertar estudiate y su nota ")
    return(menu1)
menu1()

cant=int(input("digite cuantos alumnos vas a ingresar a la lista\n"))
for f in range (cant):
    nombre=str(input(f"dijita el numbre del {[f+1]} alumno\n"))
    print("----------------------------------------------------------------------------------------------------")
    alumnos.append(nombre)
l=len(alumnos)
can=int(input("ingresa el numero de notas que debe tener cada estudiante\n"))
for fi in range (l):
    lista=[]
    for c in range (can):
        nota=float(input(f"ingresa la nota {c+1} de \n"))
        lista.append(nota)
    notas.append(lista)


print(alumnos)
print(notas)
def manu2():
    print("________________________________________________________________________________________________")
    print("--------------------------------------BIENVENIDO------------------------------------------------")
    print("________________________________________________________________________________________________") 
    print("1.mostrar la lista de estudiantes con sus calificaciones")
    print("2.calcular la media de las calificaciones")
    print("3.calcular el numero de aprobados")
    print("4.mostar los estudiantes con mejor calificacion")
    print("5.mostrar los estudiantes con calificacion superior a la media")
    print("6.mostrar la lista de estudiantes con sus calificaciones")
    print("7.consultar la calificaciones de un estudiante")
    return(manu2)
manu2()

opcion=int(input("elija una de las opciones anteriores\n"))
if opcion==1:
    notitas=[]
    for c in  range(len(notas)): 
        definitiva=notas[c]
        notitas.append(definitiva)
        nombre=alumnos[notitas.index(definitiva)]
        print(f"{nombre} tiene las sigientes notas {definitiva}")
        #print(f"{alumnos[f]} tiene {notitas}")

elif opcion==2:
    notitas=[]
    for c in  range(len(notas)): 
        definitiva=notas[c]
        notitas.append(definitiva)
        nombre=alumnos[notitas.index(definitiva)]
        su=sum(definitiva)
        media=su/can
        print(f"{nombre} tiene las sigientes notas {definitiva} y la media de sus calificaciones es de {media}" )
elif opcion ==3:
    promedio=float(input("digite el promedio minimo de la escula\n"))
    aprobados=0
    


