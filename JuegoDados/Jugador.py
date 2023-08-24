import random

class Jugador: 
    def __init__(self) -> None:
        pass
    def __str__(self) -> str:
        pass

    @staticmethod
    def calcularRandom1():
        rand1 = random.randint(1,6)
        return rand1
    @staticmethod
    def calcularRandom2():
        rand2 = random.randint(1,6)
        return rand2
    @staticmethod
    def calcularRandom3():
        rand3 = random.randint(2,12)
        return rand3
    