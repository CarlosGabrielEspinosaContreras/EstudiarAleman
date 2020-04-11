import almacenar
import leccion
import csv

def call_funcion(funcion):
    funcion_number = int(funcion)
    if funcion_number == 1:
        leccion = int(input("Numero de leccion: "))
        se_crea = True
        rango_arreglo_lecciones = range(0, len(arreglo_lecciones))
        for indice in rango_arreglo_lecciones:
            if arreglo_lecciones[indice].get_numero_leccion == leccion:
                print("Ya se ha creado esa leccion")
                se_crea = False
                break
            else: se_crea = True
        if se_crea: crear_leccion(leccion)
        reiniciar()
    elif funcion_number == 2:
        leccion = int(input("Numero de leccion: "))
        rango_arreglo_lecciones = range(0, len(arreglo_lecciones))
        pri = False
        for indice in rango_arreglo_lecciones:
            if arreglo_lecciones[indice].get_numero_leccion == leccion:
                arreglo_lecciones[indice].introducir_nueva_palabra
                pri = False
                break
            else: pri = True
        if pri:print("No se ha creado esa leccion")
        reiniciar()
    elif funcion_number == 3:
        leccion = int(input("Numero de leccion: "))
        rango_arreglo_lecciones = range(0, len(arreglo_lecciones))
        pri = False
        for indice in rango_arreglo_lecciones:
            if arreglo_lecciones[indice].get_numero_leccion == leccion:
                arreglo_lecciones[indice].introducir_nuevas_palabras
                pri = False
                break
            else: pri = True
        if pri: print("No se ha creado esa leccion")
        reiniciar()
    elif funcion_number == 4:
        guardar_datos()

def crear_leccion(numero_leccion,):
    arreglo_lecciones.append(leccion.Leccion(numero_leccion))

def imprimir_lista(lista):
    for valores in lista:
        print(valores)

def reiniciar():
    imprimir_lista(opciones)
    funcion = input()
    call_funcion(funcion)

def guardar_datos():
    guardar.iniciar_guardado(str(len(arreglo_lecciones)))
    rango_arreglo_lecciones = range (0, len(arreglo_lecciones))
    for i in rango_arreglo_lecciones:
        guardar.un_dato(arreglo_lecciones[i].get_numero_leccion)
        guardar.un_diccionario(arreglo_lecciones[i].get_diccionario_der["der"], True, "der")
        guardar.un_diccionario(arreglo_lecciones[i].get_diccionario_die["die"], True, "die")
        guardar.un_diccionario(arreglo_lecciones[i].get_diccionario_das["das"], True, "das")
    guardar.cerrar()

def cargar_lecciones():
    data_storage = open("data_storage.csv", "r")
    reader = csv.reader(data_storage)
    diccionario_lecciones = {}

    for row in reader:

        numero_leccion = 0
        diccionario_der = {"der": {}}
        diccionario_die = {"die": {}}
        diccionario_das = {"das": {}}

        die_loc = 0
        for die_loc, valor in enumerate(row):
            if valor == "die":
                break

        das_loc = 0
        for das_loc, valor in enumerate(row):
            if valor == "das":
                break

        diccionario_lecciones [row[0]] = {row[1]:{},row[die_loc]:{},row[das_loc]:{}}
        rango_der_die = range(2, die_loc, 2)
        rango_die_das = range(die_loc +1, das_loc, 2)
        rango_das_end = range(das_loc +1, len(row), 2)

        numero_leccion = int(row[0].lstrip("Leccion:"))

        for indice in rango_der_die:
            if diccionario_der["der"] == "":
                diccionario_der["der"] = {row[indice]:row[indice+1]}
            else:
                diccionario_der["der"][row[indice]] = row[indice+1]
            
        for indice in rango_die_das:
            if diccionario_die["die"] == "":
                diccionario_die["die"] = {row[indice]:row[indice+1]}
            else:
                diccionario_die["die"][row[indice]] = row[indice+1]

        for indice in rango_das_end:
            if diccionario_das["das"] == "":
                diccionario_das["das"] = {row[indice]:row[indice+1]}
            else:
                diccionario_das["das"][row[indice]] = row[indice+1]
        arreglo_lecciones.append(leccion.Leccion(numero_leccion, diccionario_der, diccionario_die, diccionario_das))
    

arreglo_lecciones = []
cargar_lecciones()
guardar = almacenar.Almacenar()
opciones = ["1:Crear una nueva leccion", "2:Agregar una nueva palabra", "3:Introducir lista de palabras", "4:Guardar datos"]

imprimir_lista(opciones)
funcion = input()
call_funcion(funcion)