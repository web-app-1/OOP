class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre.upper()
        self.salario = salario

class Programador(Empleado):
    def __init__(self, nombre, salario, lenguaje): # <-- El atributo lenguage es especifico para la clase programador
        super().__init__(nombre, salario) # <-- Llama al constructor de la clase padre(Empleado) para inicializar nombre y salario
        self.lenguaje = lenguaje

class Analista(Empleado):
    def __init__(self, nombre, salario, area): # <-- El atributo area es especifico para la clase programador
        super().__init__(nombre, salario) # <-- Llama al constructor de la clase padre(Empleado) para inicializar nombre y salario
        self.area = area


programador1 = Programador('Luis', 60000, 'Python')
analista1 = Analista('Pepo', 25000, 'Finanzas')

print(programador1.nombre)
print(analista1.nombre)