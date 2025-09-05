class Polygon:
    # Constructor de Polygon, define los atributos básicos de cualquier polígono
    def __init__(self, num_sides, color):
        self.num_sides = num_sides   # Guarda cuántos lados tiene la figura (atributo común)
        self.color = color           # Guarda el color de la figura (atributo común)

'''¿Por qué?
Queremos que cualquier figura geométrica tenga al menos número de lados y color,
para no tener que escribir esto en cada figura nueva.'''


class Triangle(Polygon):
    NUM_SIDES = 3  # Constante: todos los triángulos tienen 3 lados

    # Constructor específico para Triangle
    def __init__(self, base, height, color):
        # Llama al constructor de Polygon para inicializar los atributos comunes:
        # self.num_sides (le pasamos 3) y self.color (el color que recibimos)
        Polygon.__init__(self, Triangle.NUM_SIDES, color)

        # Ahora agregamos los atributos propios de Triangle
        self.base = base         # Base del triángulo (atributo propio)
        self.height = height     # Altura del triángulo (atributo propio)
        
'''¿Por qué?
Así te aseguras que cada triángulo tenga los atributos comunes
y además los que necesita él solamente (base y altura).'''        

class Square(Polygon):
    NUM_SIDES = 4  # Constante: todos los cuadrados tienen 4 lados

    # Constructor específico para Square
    def __init__(self, base, height, color):
        # Llama al constructor de Polygon para inicializar los atributos comunes:
        # self.num_sides (le pasamos 4) y self.color (el color que recibimos)
        Polygon.__init__(self, Square.NUM_SIDES, color)

        # Ahora agregamos los atributos propios de Square
        self.base = base         # Base del cuadrado (atributo propio)
        self.height = height     # Altura del cuadrado (atributo propio)


# Crear un triángulo
t = Triangle(10, 8, "azul")
# - Se guardan: num_sides=3 (de Polygon), color="azul" (de Polygon), base=10 (Triangle), height=8 (Triangle)

# Crear un cuadrado
s = Square(6, 6, "verde")
# - Se guardan: num_sides=4 (de Polygon), color="verde" (de Polygon), base=6 (Square), height=6 (Square)

# Acceder a los atributos heredados y propios
print(t.num_sides)   # 3      ← heredado de Polygon
print(t.color)       # azul   ← heredado de Polygon
print(t.base)        # 10     ← propio de Triangle
print(t.height)      # 8      ← propio de Triangle

print(s.num_sides)   # 4      ← heredado de Polygon
print(s.color)       # verde  ← heredado de Polygon
print(s.base)        # 6      ← propio de Square
print(s.height)      # 6      ← propio de Square
