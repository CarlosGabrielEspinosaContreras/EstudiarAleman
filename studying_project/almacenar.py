import csv
import pandas as pd

class Almacenar:

    def __init__(self):
        self.path = "data_storage.csv"

    def iniciar_guardado(self, numero_lecciones):
        self.data_storage = open(self.path, "w")
    
    def un_dato(self, dato):
        self.data_storage.write("Leccion:" + str(dato))

    def una_lista(self, dato, saltar):
        for valor in dato:
            self.data_storage.write("," + valor)
        if saltar:
            self.data_storage.write("\n")

    def un_diccionario(self, diccionario, guardar_algo, que_cosa):
        if guardar_algo:
            self.data_storage.write("," + que_cosa)
        for key in diccionario:
            valor = diccionario[key]
            strin = "," + key + "," + valor
            self.data_storage.write(strin)

    def cerrar(self):
        self.data_storage.close()
