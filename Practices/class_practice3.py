class Curso:
    def __init__(self, nombre, profesor, nivel):
        self._nombre = nombre
        self._profesor = profesor
        self._nivel = nivel

    @property
    def nombre(self):
        return self._nombre
    
    @property
    def profesor(self):
        return self._profesor
    
    @property
    def nivel(self):
        return self._nivel
    
    def info(self):
        return f'Nombre del Curso: {self._nombre}. Profesor: {self._profesor}. Nivel: {self._nivel}'
    

class Matematicas(Curso):
    def __init__(self, nombre, profesor, nivel, tema):
        super().__init__(nombre, profesor, nivel)
        self._tema = tema

    @property
    def tema(self):
        return self._tema
    
    def info(self):
        info_base = super().info()
        return f'{info_base}. Tema: {self._tema}'
    
class Historia(Curso):
    def __init__(self, nombre, profesor, nivel, epoca):
        super().__init__(nombre, profesor, nivel)
        self._epoca = epoca

    @property
    def epoca(self):
        return self._epoca
    
    def info(self):
        info_base = super().info()
        return f'{info_base}. Epoca: {self._epoca}'


curso1 = Matematicas('Matematicas I', 'Apollo Jimbo', 'Principiante', 'Los Numeros Reales')
curso2 = Historia('Historia III', 'Leonel Z', 'Intermedio', 'Historia del Mundo')

print(curso1.info())
print(curso2.info())