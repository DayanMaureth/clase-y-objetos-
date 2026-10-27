class DispositivoConectado:
    def conectar(self):
        print("Estableciendo conexión a la red...")


class CamaraSeguridad:
    def grabar(self):
        print("Grabando video HD...")


class CamaraIP(DispositivoConectado, CamaraSeguridad):  # Herencia múltiple
    pass


cam = CamaraIP()
cam.conectar()
cam.grabar()

# Inspección del MRO
print(CamaraIP.mro())
# [<class '__main__.CamaraIP'>, <class '__main__.DispositivoConectado'>,
#  <class '__main__.CamaraSeguridad'>, <class 'object'>]
