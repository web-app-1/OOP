#Ejercicio 2

class Fruta:
    def __init__(self, nombre, color, acidez):
        self._nombre = nombre
        self._color = color
        self._acidez = acidez

    @property
    def nombre(self):
        return self._nombre
    
    @property
    def color(self):
        return self._color
    
    def descripcion(self):
        return f'Detalle de la fruta:Nombre: {self._nombre}. Color:{self._color}. Acidez {self._acidez}'
    

class Baya(Fruta):
    def __init__(self, nombre, color, acidez, es_comestible):
        super().__init__(nombre, color, acidez)
        self._es_comestible = es_comestible

    @property
    def es_comestible(self):
        return self._es_comestible
    
    def descripcion(self):
        info_base = super().descripcion()
        return f'{info_base}. Es comestible: {self._es_comestible}'
    
class Banana(Fruta):
    def __init__(self, nombre, color, acidez, precio):
        super().__init__(nombre, color, acidez)
        self._precio = precio
    
    @property
    def precio(self):
        return self._precio
    
    def descripcion(self):
        info_base = super().descripcion()
        return f'{info_base}. Precio: {self._precio}'
    
fruta1 = Baya('Cereza','rojo', 2.4, True)
fruta2 = Baya('Uva', 'morado', 3.4, True)
fruta3 = Baya('Nocomer', 'negro', 100.00, False)

fruta4 = Banana('Banana Verde', 'Verde', 45.00, 1.40)
fruta5 = Banana('Banana','amarillo', 2.43, 0.25)

print(fruta1.descripcion())
print(fruta4.descripcion())