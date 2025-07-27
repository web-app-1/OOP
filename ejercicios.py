'''
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



class Mascota:

    tipo_vida = 'Animal'

    def __init__(self, nombre, especie, energia):
        self.nombre = nombre
        self.especie = especie
        self.energia = energia

    def jugar(self, tiempo):
        tiempo_transcurrido = tiempo * 10
        self.energia = self.energia - tiempo_transcurrido
        print(f'Despues de Jugar la energia de {self.nombre} es: {self.energia}')

    def comer(self, comida):
        if comida == "croquetas":
            self.energia = self.energia + 20
        elif comida == "hueso":
            self.energia = self.energia + 10
        print(f'Despues de comer {comida}, la energia de {self.nombre} es: {self.energia}')

    def estado_animo(self):
        if self.energia >= 70:
            print(f'{self.nombre} está feliz!')
        elif self.energia >= 30:
            print(f'{self.nombre} está tranquilo!')
        else:
            print(f'{self.nombre} está cansado')


    def mostrar_estado(self):
        print(f'Soy {self.nombre} un {self.especie} y tengo {self.energia} de energia!')

            

mi_mascota = Mascota('Otto', 'Gato', 100)
mi_mascota.jugar(8)
#mi_mascota.comer('croquetas')
mi_mascota.mostrar_estado()
mi_mascota.estado_animo()        


class Producto:

    categoria_general = 'Bien de consumo'

    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def mostrar_info(self):
        print(f'Producto: {self.nombre}, Precio:{self.precio}, Stock:{self.stock} unidades.')

    
    def vender(self, cantidad):
        if self.stock >= cantidad:
            self.stock = self.stock - cantidad
        elif self.stock < cantidad:
            print(f'No hay suficiente stock disponible')

        print(f'Stock actual: {self.stock}')

    def reponer(self, cantidad):
        self.stock = self.stock + cantidad
        print(f'Se repusieron {cantidad} unidades, Stock actual: {self.stock}')


producto1 = Producto('Paila', 5.00, 34)
producto1.vender(34)
producto1.reponer(2)


class Plato:

    categoria_general = 'comida'

    def __init__(self, nombre, precio, disponible):
        self.nombre = nombre
        self.precio = precio
        self.disponible = disponible

    def mostrar_info(self):
        disponibilidad = "Sí" if self.disponible else "No"
        print(f'Plato: {self.nombre}, Precio: {self.precio}, Disponible: {disponibilidad}')

    def cambiar_disponibilidad(self, estado):
        if estado == True:
            self.disponible = True
        else:
            self.disponible = False

        print(f'Disponibilidad de {self.nombre}, actualizada a: {estado}')

    def ordenar(self):
        if self.disponible == True:
            print(f'Orden Recibida: {self.nombre}. Gracias por su pedido')
        else:
            print(f'(Lo sentimos, {self.nombre} no esta disponible en este momento)')

plato1 = Plato('patacones', 3.0, True)
plato1.mostrar_info()
plato1.ordenar()
plato1.cambiar_disponibilidad(False)
plato1.ordenar()



class Auto:

    tipo = 'Vehiculo'

    def __init__(self, marca, modelo, combustible):
        self.marca = marca
        self.modelo = modelo
        self.combustible = combustible

    def mostrar_info(self):
        print(f'Marca: {self.marca}, Modelo: {self.modelo}, Combustible: {self.combustible}')

    def conducir(self, distancia):
        litros_necesarios = distancia / 10

        if self.combustible < litros_necesarios:
            print(f'Combustible insuficiente para recorrer {distancia}')
        else:
            self.combustible = self.combustible - litros_necesarios
            print(f'Condujistes {distancia} km. Combustible actual {self.combustible}')


    def recargar(self, litros):
        self.combustible = self.combustible + litros
        print(f'Se recargaron {litros} litros. Combustible acutal: {self.combustible}')


auto1 = Auto("Toyota", "Corolla", 20)

auto1.mostrar_info()
auto1.conducir(50)
auto1.recargar(10)
auto1.conducir(200)



#Properties

class Producto:
    
    def __init__(self, nombre, precio, stock):
        self._nombre = nombre
        self._precio = precio
        self._stock = stock

    @property
    def nombre(self):
        return self._nombre
    
    @property
    def precio(self):
        return self._precio
    
    @property
    def stock(self):
        return self._stock
    
    def mostrar_info(self):
        print(f'Nombre: {self._nombre}, Precio: {self._precio}, Stock: {self._stock}')


    @precio.setter
    def precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self._precio = nuevo_precio
        else:
            print('El precio debe ser mayor que 0')

    @stock.setter
    def stock (self, nuevo_stock):
        if isinstance(nuevo_stock, int) and nuevo_stock >= 0:
            self._stock = nuevo_stock
        else:
            print('Ingrese una cantidad positiva')


p1 = Producto("Camiseta", 20.5, 10)
print(p1.precio)  
p1.precio = 25    
p1.precio = 5    
p1.mostrar_info()
    


class Empleado:

    def __init__(self, nombre, salario):
        self._nombre = nombre
        self._salario = salario

    @property
    def salario(self):
        return self._salario
    
    def mostrar_info(self):
        print(f'Empleado: {self._nombre}, Salario: {self._salario}')
    
    @salario.setter
    def salario(self, nuevo_salario):
        if nuevo_salario > 0:
            self._salario = nuevo_salario
        else:
            print('El salario debe ser mayor a 0')


empleado1 = Empleado("Luis", 1500)
empleado1.mostrar_info()            

empleado1.salario = -100            
empleado1.salario = 1800            
empleado1.mostrar_info()            



class CuentaBancaria:

    TIPOS_CUENTA = ('Ahorros', 'Corriente')

    def __init__(self, titular, saldo, tipo_cuenta):
        self._titular = titular
        self._saldo = saldo
        self._tipo_cuenta = tipo_cuenta

    @property
    def saldo(self):
        return self._saldo
    
    @property
    def tipo_cuenta(self):
        return self._tipo_cuenta
    
    @saldo.setter
    def saldo (self, nuevo_saldo):
        if isinstance(nuevo_saldo, int) and nuevo_saldo >= 0:
            self._saldo = nuevo_saldo
        else:
            print('Valor incorrecto')
        
    @tipo_cuenta.setter
    def tipo_cuenta(self, tipo):
        if tipo in CuentaBancaria.TIPOS_CUENTA:
            print(f'Su cuente es de {tipo}')
            self._tipo_cuenta = tipo 
        else:
            print('Tipo de cuenta no valida')
    
    def mostrar_info(self):
        print(f'Datos de la Cuenta -- Nombre: {self._titular}', {self.saldo}, {self.tipo_cuenta})


cuenta = CuentaBancaria("Luis", 2500, "Ahorros")
cuenta.mostrar_info()
cuenta.saldo = -200 
cuenta.tipo_cuenta = "VIP" 
cuenta.saldo = 2900 
cuenta.tipo_cuenta = "Corriente"
cuenta.mostrar_info()



#practica con @properties

class Cuenta:

    MONEDA_LEGAL = ('USD','EUR', 'PEN')

    def __init__(self, titular, saldo, moneda):
        self._titular = titular
        self._saldo = saldo
        self._moneda = moneda

    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self, nuevo_saldo):
        if nuevo_saldo < 0:
            print('El saldo no puede ser negativo')
        else:
            self._saldo = nuevo_saldo
            print(f'Nuevo saldo: {self._saldo}')

    @property
    def moneda(self):
        return self._moneda
    
    @moneda.setter
    def moneda(self, nueva_moneda):
        if nueva_moneda in Cuenta.MONEDA_LEGAL:
            self._moneda = nueva_moneda
        else:
            print('Moneda invalida')

    
    def mostrar_info(self):
        print(f'Detalle: Nombre: {self._titular}, Monto Actual:{self._saldo}, Tipo:{self._moneda}')


cuenta1 = Cuenta('Luis', 2123, 'USD')

cuenta1.mostrar_info()
cuenta1.saldo = 456436
cuenta1.saldo = -90



#Practica 1 con Aggregation

class Motor:
    
    def __init__(self, combustible, fuerza):
        self._combustible = combustible
        self._fuerza = fuerza

    @property
    def combustible(self):
        return self._combustible
    
    @property
    def fuerza(self):
        return self._fuerza
    
    def mostrar_info_motor(self):
        print(f'Detalles del motor: Tipo de Combustible:{self._combustible} | Fuerza Total: {self._fuerza}')
    

class Auto:
    def __init__(self, marca, modelo, motor):
        self._marca = marca
        self._modelo = modelo
        self._motor = motor

    @property
    def marca(self):
        return self._marca
    
    @property                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
    def modelo(self):
        return self._modelo
    
    
    def mostrar_info_auto(self):
        print(f'Marca: {self._marca} | Modelo: {self._modelo}')
        self._motor.mostrar_info_motor()
    
motor1 = Motor('Gasolina', 456)
auto1 = Auto('Ford', 'Mustang', motor1)

auto1.mostrar_info_auto()
        
'''

#Practica 2 con Aggregation

class Bateria:

    def __init__(self, capacidad, tipo):
        self._capacidad = capacidad
        self._tipo = tipo

    
    def mostrar_info_bateria(self):
        print(f'Detalles de la bateria: Capacidad: {self._capacidad} | Tipo: {self._tipo}')
    

class Celular:

    def __init__(self, marca, modelo, bateria):
        self._marca = marca
        self._modelo = modelo
        self._bateria = bateria

    def mostrar_info_celular(self):
        print(f'Detalles del Celular: Marca: {self._marca} | Modelo: {self._modelo}')
        self._bateria.mostrar_info_bateria()


bateria1 = Bateria('3000 mah', 'Li-Ion')
celular1 = Celular('Samosongo', 'UltraPEP88', bateria1)
celular1.mostrar_info_celular()    