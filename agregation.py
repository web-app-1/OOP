# Una clase usa otra clase como parte de su estructura, pero la clase usada puede existir por si sola

class Estudiante():

    def __init__(self, nombre):
        self.nombre = nombre


class Universidad():
    def __init__(self, nombre, estudiante):
        self.nombre = nombre
        self.estudiante = estudiante