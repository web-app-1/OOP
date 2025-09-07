#Ejercicio 1

class Vehiculo:
    def __init__(self, tipo, marca, modelo):
        self._tipo = tipo
        self._marca = marca
        self._modelo = modelo

    @property
    def tipo(self):
        return self._tipo
    
    @property
    def marca(self):
        return self._marca
    
    @property
    def modelo(self):
        return self._modelo
    
    def mostrar_info(self):
        clase = self.__class__.__name__
        return f'Detalles: {clase}| Tipo:{self._tipo}, Marca:{self._marca}. Modelo:{self._modelo}'
    
class Auto(Vehiculo):
    def __init__(self, tipo, marca, modelo, puertas):
        super().__init__(tipo, marca, modelo)
        self._puertas = puertas

    def mostrar_info(self):
        info_base = super().mostrar_info()
        return f'{info_base}. # Puertas: {self._puertas}'

class Moto(Vehiculo):
    def __init__(self, tipo, marca, modelo, cilindrada):
        super().__init__(tipo, marca, modelo)
        self._cilindrada = cilindrada

    def mostrar_info(self):
        info_base = super().mostrar_info()
        return f'{info_base}. Cilindrada:{self._cilindrada}'

auto1 = Auto('SUV', 'Totoya', 'RAV4', 5)
auto2 = Auto('4x4', 'Ford', 'F350', 6)

moto1 = Moto('Racing','Yahama', 'YH-XV', 6)
moto2 = Moto('All_Terrain', 'Honda', 'HON-23', 4)


print(auto1.mostrar_info())
print(auto2.mostrar_info())

print(moto1.mostrar_info())
print(moto2.mostrar_info())
