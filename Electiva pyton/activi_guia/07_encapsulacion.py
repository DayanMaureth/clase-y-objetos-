class CuentaBancaria:
    def __init__(self, titular: str, saldo_inicial: float):
        self.titular = titular
        self.__saldo = saldo_inicial  # Atributo privado (name mangling)

    def depositar(self, monto: float):
        if monto > 0:
            self.__saldo += monto
        else:
            print("Error: Monto inválido.")

    def obtener_saldo(self) -> float:  # Getter controlado
        return self.__saldo


cuenta = CuentaBancaria("Ing. Hernández", 5000.0)
cuenta.depositar(1500.0)
print(cuenta.obtener_saldo())  # Imprime: 6500.0
# print(cuenta.__saldo)  -> Eleva AttributeError
