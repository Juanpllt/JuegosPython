class Ahorcado:

    contadorRondas = 0
    contadorMuertes = 0
    def __init__(self, palabra):
        self._palabra = palabra
        self._vidas = 5
        self._statusA = False
        self._letras = str
        self._palabraP = list(palabra)
        self.modPalabraP()
    def __str__(self) -> str:
        return f'Palabra: {self.palabra}\n Numero restante de vidas: {self.vidas} \n Ahorcado: {self.statusA}'

    @property
    def statusA(self):
        return self._statusA
    @statusA.setter
    def statusA(self, statusA):
        self._statusA = statusA
    
    @property
    def palabraP(self):
        return self._palabraP
    @palabraP.setter
    def palabraP(self, palabraP):
        self._palabraP = palabraP

    @property
    def palabra(self):
        return self._palabra
    @palabra.setter
    def palabra(self, palabra):
        self._palabra = palabra

    @property
    def letras(self):
        return self._letras
    @letras.setter
    def letras(self, letras):
        self._letras = letras

    @property
    def vidas(self):
        return self._vidas
    @vidas.setter
    def vidas(self, vida):
        self._vidas = vida
    def modPalabraP(self):
        for i in range(len(self.palabraP)):
            self.palabraP[i] = 'X'

    
    @classmethod
    def _contadorRondas(cls):
        cls.contadorRondas +=1
    @classmethod
    def _contadorMuertes(cls):
        cls.contadorMuertes +=1

    def quitarVida(self):
        self.vidas -=1
    def evaluarLetras(self):
        cambios = False
        for i in range(len(self.palabra)):
            if self.letras == self.palabra[i]:
                self.palabraP[i] = self.letras
                cambios = True
        if cambios == False:
            self.quitarVida()
            print("La letra era incorrecta")
        else:
            print(self.palabraP)



    
   
