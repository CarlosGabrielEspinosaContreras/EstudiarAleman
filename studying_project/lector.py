import csv

data_storage = open("data_storage.csv", "r")

reader = csv.reader(data_storage)

lecciones = {}
def cargar_lecciones():
    for row in reader:
        die_loc = 0
        for die_loc, valor in enumerate(row):
            if valor == "die":
                break
        das_loc = 0
        for das_loc, valor in enumerate(row):
            if valor == "das":
                break
        lecciones [row[0]] = {row[1]:{},row[die_loc]:{},row[das_loc]:{}}
        rango_der_die = range(2, die_loc, 2)
        rango_die_das = range(die_loc +1, das_loc, 2)
        rango_das_end = range(das_loc +1, len(row), 2)
        for indice in rango_der_die:
            if lecciones[row[0]][row[1]] == "":
                lecciones[row[0]][row[1]] = {row[indice]:row[indice+1]}
            else:
                lecciones[row[0]][row[1]][row[indice]] = row[indice+1]
        for indice in rango_die_das:
            if lecciones[row[0]][row[die_loc]] == "":
                lecciones[row[0]][row[die_loc]] = {row[indice]:row[indice+1]}
            else:
                lecciones[row[0]][row[die_loc]][row[indice]] = row[indice+1]
            for indice in rango_das_end:
                if lecciones[row[0]][row[das_loc]] == "":
                    lecciones[row[0]][row[das_loc]] = {row[indice]:row[indice+1]}
                else:
                    lecciones[row[0]][row[das_loc]][row[indice]] = row[indice+1]
