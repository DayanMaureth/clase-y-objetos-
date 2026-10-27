class Estudiante:
    NOTA_MIN = 0.0
    NOTA_MAX = 5.0

    def __init__(self, nombre: str):
        self.__nombre = nombre
        self.__notas = []

    # ---- Propiedades (solo lectura) ----
    @property
    def nombre(self) -> str:
        return self.__nombre

    @property
    def notas(self) -> list:
        # Se retorna una COPIA para que desde afuera no se pueda mutar la lista original
        return self.__notas.copy()

    # ---- Métodos ----
    def agregar_nota(self, nota: float):
        if not (self.NOTA_MIN <= nota <= self.NOTA_MAX):
            raise ValueError(
                f"Nota inválida ({nota}). Debe estar entre {self.NOTA_MIN} y {self.NOTA_MAX}."
            )
        self.__notas.append(nota)

    def calcular_promedio(self) -> float:
        if not self.__notas:
            return 0.0
        return sum(self.__notas) / len(self.__notas)


if __name__ == "__main__":
    est = Estudiante("Laura Pérez")
    est.agregar_nota(4.5)
    est.agregar_nota(3.8)
    est.agregar_nota(5.0)
    print(f"Estudiante: {est.nombre}")
    print(f"Notas: {est.notas}")
    print(f"Promedio: {est.calcular_promedio():.2f}")  # 4.43

    # Pruebas de validación
    for nota_mala in (-1, 5.5):
        try:
            est.agregar_nota(nota_mala)
        except ValueError as e:
            print("Error:", e)

    # La copia protege la lista original
    est.notas.append(1.0)
    print("Notas después de intentar modificar la copia:", est.notas)
