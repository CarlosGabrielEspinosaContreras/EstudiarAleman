class Leccion:

    contador_lecciones = 0

    def __init__(self, numero_leccion, diccionario_der = {"der":{}}, diccionario_die = {"die":{}}, diccionario_das = {"das":{}}):
        Leccion.contador_lecciones += 1
        self.__numero_leccion = numero_leccion
        self.diccionario_der = diccionario_der
        self.diccionario_die = diccionario_die
        self.diccionario_das = diccionario_das

    @property
    def introducir_nueva_palabra(self):
        nueva_palabra = input("Agregar palabra: ")
        self.guardar_palabra_en_diccionario(nueva_palabra)

    @property
    def introducir_nuevas_palabras(self):
        articulo = input("Articulo de la lista: ")
        lista_palabras_nuevas = input('Lista de palabras (separadas por coma, ejemplo: "apfel, tisch"): ')
        self.guardar_lista_en_diccionario(articulo, lista_palabras_nuevas)

    def guardar_palabra_en_diccionario(self, nueva_palabra):
        palabras = nueva_palabra.split(" ")
        if palabras[0].lower() == "der":
            if self.diccionario_der["der"] == "":
                self.diccionario_der["der"] = {palabras[1]:palabras[2]}
            else:
                self.diccionario_der["der"][palabras[1]] = palabras[2]
            print("Nueva lista de der: ", self.diccionario_der)

        if palabras[0].lower() == "die":
            if self.diccionario_die["die"] == "":
                self.diccionario_die["die"] = {palabras[1]:palabras[2]}
            else:
                self.diccionario_der["die"][palabras[1]] = palabras[2]
            print("Nueva lista de die: ", self.diccionario_die)

        if palabras[0].lower() == "das":
            if self.diccionario_das["das"] == "":
                self.diccionario_das["das"] = {palabras[1]:palabras[2]}
            else:
                self.diccionario_der["das"][palabras[1]] = palabras[2]
            print("Nueva lista de das: ", self.diccionario_das)

    def guardar_lista_en_diccionario(self, articulo, lista_palabras_nuevas):
        lista_palabras = lista_palabras_nuevas.split(", ")
        if articulo.lower() == "der":
            for palabra in lista_palabras:
                palabra = palabra.split(":")
                if self.diccionario_der["der"] == "":
                    self.diccionario_der["der"] = {palabra[0]:palabra[1]}
                else:
                    self.diccionario_der["der"][palabra[0]] = palabra[1]
            print(self.diccionario_der)

        if articulo.lower() == "die":
            for palabra in lista_palabras:
                palabra = palabra.split(":")
                if self.diccionario_die["die"] == "":
                    self.diccionario_die["die"] = {palabra[0]:palabra[1]}
                else:
                    self.diccionario_das["die"][palabra[0]] = palabra[1]
            print(self.diccionario_die)

        if articulo.lower() == "das":
            for palabra in lista_palabras:
                palabra = palabra.split(":")
                if self.diccionario_das["das"] == "":
                    self.diccionario_das["das"] = {palabra[0]:palabra[1]}
                else:
                    self.diccionario_das["das"][palabra[0]] = palabra[1]
            print(self.diccionario_das)
      
    @property
    def get_numero_leccion(self):
        return self.__numero_leccion

    @property
    def get_diccionario_der(self):
        return self.diccionario_der

    @property
    def get_diccionario_die(self):
        return self.diccionario_die

    @property
    def get_diccionario_das(self):
        return self.diccionario_das
