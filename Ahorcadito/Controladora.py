from Ahorcado import Ahorcado

class Controladora:
    ahorcado = Ahorcado()
    def __init__(self,rondas=1, palabra=str):
        self._rondas = rondas
        self._palabra = palabra
        self.setRondasConE()
    def __str__(self):
        pass
    @property
    def rondas(self):
        return self._rondas
    @rondas.setter
    def rondas(self, rondas):
        self._rondas = rondas
    def crearRondas(self):
        self.ahorcado.evaluarLetras()
    def setRondasConE(self):
        self.rondas = int(input("Ingrese el numero de rondas: "))
        for i in range(self.rondas):
            self.cambiarPalabra()
            self.crearRondas()
            print(self.ahorcado)        
    def cambiarPalabra(self):
        self.ahorcado.palabra = input("Ingrese la palabra: ").upper()
