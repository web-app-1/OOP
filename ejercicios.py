class Animal:

    tipo_reino = "Animalia"

    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

    def presentarse(self):
        print(f'Hola soy {self.nombre}, soy un {self.especie} y tengo {self.edad} anos.')


animal1 = Animal("Pepo", "Felino", 2)

animal1.presentarse()


class Persona:

    tipo_ser = "Humano"

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar_a(self, otrapersona):
        print(f'Hola {otrapersona}, soy {self.nombre} y tengo {self.edad}')

yo = Persona('Luis', 39)
yo.saludar_a('Pepo')


class Vehiculo:

    tipo = "Transporte"

    def __init__(self, marca, color, velocidad):
        self.marca = marca
        self.color = color
        self.velocidad = velocidad

    def acelerar(self, incremento):
        self.velocidad = self.velocidad + incremento
        print(f'La velocidad actual del {self.marca} es {self.velocidad} km/h')


mi_vehiculo = Vehiculo("Ford", "Negro", 80)
mi_vehiculo.acelerar(20)