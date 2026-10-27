class Vehiculo:
    def __init__(self, marca: str, modelo: str):
        self._marca = marca
        self._modelo = modelo

    def obtener_info(self) -> str:
        return f"Vehículo: {self._marca} {self._modelo}"


class AutoElectrico(Vehiculo):
    def __init__(self, marca: str, modelo: str, bateria_kwh: float):
        super().__init__(marca, modelo)
        self.__bateria = bateria_kwh
        self.__carga_actual = 20.0  # Porcentaje inicial

    def cargar_bateria(self, porcentaje: float):
        if 0 <= porcentaje <= (100 - self.__carga_actual):
            self.__carga_actual += porcentaje
            print(f"Carga exitosa. Batería al {self.__carga_actual}%")
        else:
            print("Error: Excede el límite de carga (100%).")


tesla = AutoElectrico("Tesla", "Model 3", 75.0)
print(tesla.obtener_info())
tesla.cargar_bateria(50.0)   # Carga exitosa. Batería al 70.0%
tesla.cargar_bateria(50.0)   # Error: Excede el límite de carga (100%).
