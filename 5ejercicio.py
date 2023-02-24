from os import system

notas=[]
alumnos=[]
aprobados=0
reprobados=0

def menu1():
    print("________________________________________________________________________________________________")
    print("--------------------------------------BIENVENIDO------------------------------------------------")
    print("________________________________________________________________________________________________")
    return(menu1)
menu1()
system("cls")

nalumnos=int(input("digite cuantos alumnos vas a ingresar a la lista\n"))

cantn=int(input("ingresa el numero de notas que debe tener cada estudiante\n"))

for f in range (nalumnos):
    nombre=str(input(f"dijita el numbre del {[f+1]} alumno\n"))
    alumnos.append(nombre)
    lista=[]
    for c in range (cantn):
        nota=float(input(f"ingresa la nota {c+1} de {alumnos[f]} \n"))
        print("----------------------------------------------------------------------------------------------------")
        lista.append(nota)
    notas.append(lista)
inicio=0
while inicio==0:

    def menup():
        print("________________________________________________________________________________________________")
        print("--------------------------------------BIENVENIDO------------------------------------------------")
        print("________________________________________________________________________________________________") 
        print("1.mostrar la lista de estudiantes con sus calificaciones")
        print("2.calcular la media de las calificaciones")
        print("3.calcular el numero de aprobados")
        print("4.mostar los estudiantes con mejor calificacion")
        print("5.mostrar los estudiantes con calificacion superior a la media")
        print("6.consultar la calificaciones de un estudiante")
        return(menup)
    menup()

    opcion=int(input("elija una de las opciones anteriores\n"))
    if opcion == 1:
        notitas=[]
        for c in  range(len(notas)): 
            definitiva=notas[c]
            notitas.append(definitiva)
            nombre=alumnos[notitas.index(definitiva)]
            print(f"{nombre} tiene las sigientes notas {definitiva}")
            input("presione enter para continuar")
            salir=0

    elif opcion==2:
        notitas=[]
        for c in  range(len(notas)): 
            definitiva=notas[c]
            notitas.append(definitiva)
            nombre=alumnos[notitas.index(definitiva)]
            su=sum(definitiva)
            media=su/cantn
            print(f"{nombre} tiene las sigientes notas {definitiva} y la media de sus calificaciones es de {media}" )
            input("presione enter para continuar")
            salir=0

    if opcion==3:
        promedio=float(input("ingrese el promedio minimo para que el estudiante apruebe dependiendo el rango de calificacion\n"))
        notitas=[]
        for c in  range(len(notas)):
            definitiva=notas[c]
            notitas.append(definitiva)
            nombre=alumnos[notitas.index(definitiva)]
            su=sum(definitiva)
            media=su/cantn
            if media>= promedio:
                aprobados=aprobados+1
                print(f"el alumn@ {nombre} aprobado con un promedio de {media}")
            if media < promedio:
                repro=repro+1
                print(f"el alumn@ {nombre} reprobo con un promedio de {media}")
        print(f"el numero de aprobados es de {aprobados}")
        print(f"el numero de reprobados es de {reprobados}")
        input("presione enter para continuar")
        salir=0

    if opcion==4:
        superior=float(input("ingrese el promedio adecuado para que el estudiante sea sobresaliente dependiendo el rango de calificacion\n"))
        notitas=[]
        for c in  range(len(notas)):
            definitiva=notas[c]
            notitas.append(definitiva)
            nombre=alumnos[notitas.index(definitiva)]
            su=sum(definitiva)
            media=su/cantn
            if media>= superior:
                aprobados=aprobados+1
                print(f"el alumn@ {nombre}  tiene una notafinal sobresaliente un promedio de {media:.1f}")
                input("presione enter para continuar")
                salir=0

    if opcion==6:
        nombreb=str(input("ingresa el nombre del estudiante que deseas buscar\n"))
        notitas=[]
        for c in  range(len(notas)):
            definitiva=notas[c]
            notitas.append(definitiva)
            nombre=alumnos[notitas.index(definitiva)]
            if nombreb==nombre:
                print(f"las notas del alumn@ {nombre} son {definitiva}")
                input("presione enter para continuar")
                salir=0

