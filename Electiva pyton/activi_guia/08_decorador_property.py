class Empleado:
    def __init__(self, nombre: str, salario: float):
        self.nombre = nombre
        self._salario = salario

    @property
    def salario(self) -> float:  # Getter de propiedad
        return self._salario

    @salario.setter
    def salario(self, nuevo_salario: float):  # Setter con validación
        if nuevo_salario >= 1300.0:
            self._salario = nuevo_salario
        else:
            raise ValueError("El salario no puede ser inferior al mínimo legal.")


emp = Empleado("Carlos Gómez", 2000.0)
emp.salario = 2500.0  # Asignación limpia usando el setter
print(emp.salario)    # Lectura usando getter: 2500.0
