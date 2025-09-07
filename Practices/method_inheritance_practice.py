# Clase base Animal: todos los animales tienen nombre y edad
class Animal:
    # Constructor de Animal: recibe nombre y edad
    def __init__(self, nombre, edad):
        self._nombre = nombre   # ← Guarda el nombre como atributo protegido
        self._edad = edad      # ← Guarda la edad como atributo protegido

# Subclase Perro que hereda de Animal
class Perro(Animal):
    # Constructor de Perro: recibe nombre, edad y raza
    def __init__(self, nombre, edad, raza): 
        # Los parámetros (nombre, edad) se repiten aquí porque:
        # 1. Necesitas recibirlos al crear el objeto
        # 2. Debes pasarlos al constructor de la clase padre
        
        super().__init__(nombre, edad)  # ← Llama al constructor del padre (Animal)
                                        #    para que inicialice nombre y edad
        
        self._raza = raza               # ← Guarda la raza como atributo propio de Perro


    @property
    def edad(self):
        return self._edad
    
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def raza(self):
        return self._raza

    def ladrar(self):
        print('Guau!')

class Gato(Animal):
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad)
        self._color = color

    @property
    def nombre(self):
        return self._nombre
    
    @property
    def edad(self):
        return self._edad
    
    @property
    def color(self):
        return self._color


    def maullar(self):
        print('Miau')

perro1 = Perro('Rocky', 3, 'Pastor Aleman')
print(perro1.edad)
print(perro1.nombre)
print(perro1.raza)
perro1.ladrar()

gato1 = Gato('Pepo', 13,'Blanco y Naranja')
print(gato1.nombre)
print(gato1.color)
print(gato1.edad)
gato1.maullar()