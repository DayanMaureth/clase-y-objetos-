class TarjetaCredito:
    def __init__(self, titular: str):
        self.titular = titular

    def calcular_cashback(self, monto: float) -> float:
        return 0.0


class TarjetaGold(TarjetaCredito):
    def calcular_cashback(self, monto: float) -> float:
        return monto * 0.02


class TarjetaBlack(TarjetaCredito):
    def calcular_cashback(self, monto: float) -> float:
        return monto * 0.05


def mostrar_cashback(tarjeta: TarjetaCredito, monto: float):
    # Llamada polimórfica: no importa qué tipo de tarjeta sea
    print(f"{type(tarjeta).__name__} de {tarjeta.titular}: "
          f"compra ${monto:,.2f} -> cashback ${tarjeta.calcular_cashback(monto):,.2f}")


if __name__ == "__main__":
    tarjetas = [
        TarjetaCredito("Ana"),
        TarjetaGold("Carlos"),
        TarjetaBlack("Marta"),
    ]
    for t in tarjetas:
        mostrar_cashback(t, 1000.0)
