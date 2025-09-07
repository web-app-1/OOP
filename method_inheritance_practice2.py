class Empleado:
    def __init__(self, nombre, salario):
        self._nombre = nombre
        self._salario = salario

    @property
    def nombre(self):
        return self._nombre
    
    @property
    def salario(self):
        return self._salario
    

class Programador(Empleado):

    def __init__(self, nombre, salario, lenguaje):
        super().__init__(nombre, salario)
        self._lenguaje = lenguaje

       
    @property
    def lenguaje(self):
        return self._lenguaje
    
    def mostrar_info(self):
        return f'Datos del Empleado: Nombre: {self.nombre}, Salario: {self.salario}, Lenguaje: {self.lenguaje}'
    
class Disenador(Empleado):

    def __init__(self, nombre, salario, especialidad):
        super().__init__(nombre, salario)
        self._especialidad = especialidad

    @property
    def especialidad(self):
        return self._especialidad
    
    def mostrar_info(self):
        return f'Datos del Empleado: Nombre: {self.nombre}, Salario: {self.salario}, especialidad: {self.especialidad}'
    
 
programador1 = Programador('Pepo', 45000.00,'Python')
programador2 = Programador('Viche', 35000.00,'C')
disenador1 = Disenador('Mimi', 56000.00, 'Diseno de Interiores')

print(programador1.mostrar_info())
print(programador2.mostrar_info())

print(disenador1.nombre)
print(disenador1.mostrar_info())

