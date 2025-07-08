'''Clases:

Una clase es como un molde que define cómo serán los objetos creados a partir de ella.

''' 

class House:
    def __init__(self, price): # -> 1
        self.price = price # -> 2, 3

# 1: El método __init__ es el método constructor. Se ejecuta automáticamente cuando creas una instancia (objeto) de la clase. Su función es inicializar los atributos del objeto.
# 2: self hace referencia a la instancia actual que se esta creando.
# 3: price: es el parametro externo que debes pasar al crear una instancia

house1 = House(77000)
house2 = House(120000)

print(house1.price)
print(house2.price)


class BackPack:
    def __init__(self, color, size):
        self.items = []
        self.color = color
        self.size = size