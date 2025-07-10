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


class CuentaBancaria:

    banco = "Banco Central"

    def __init__(self,titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad):
        self.saldo = self.saldo + cantidad
        print(f'Se depositaron {cantidad}. Saldo actual: {self.saldo}')

    def retirar(self, cantidad):
        if cantidad > self.saldo:
            print('Fondos insuficientes')
        else:
            self.saldo = self.saldo - cantidad
            print(f'se retiraron {cantidad}. Sado actual: {self.saldo}')
            
    def mostrar_saldo(self):
        print(f'El saldo de {self.titular} es {self.saldo}')

    
cuenta1 = CuentaBancaria("Luis", 100)

cuenta1.depositar(5)
cuenta1.retirar(100)
cuenta1.mostrar_saldo()
    