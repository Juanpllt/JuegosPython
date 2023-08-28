class Ahorcado:

    contadorRondas = 0
    contadorMuertes = 0
    def __init__(self, palabra="Casa",letras=str):
        self._palabra = palabra
        self._vidas = 5
        self._letras = letras
        self._palabraP = list
        self.statusA = False
        
    def __str__(self) -> str:
        return f'\nPalabra: {self.palabra}\nNumero restante de vidas: {self.vidas}\nEstado vital: {self.statusA} Muertes: {self.contadorMuertes} Ronda: {self.contadorRondas}'

    @property
    def statusA(self):
        status = self._statusA
        if status is False:
            return "Vivo"
        else:
            return "Muerto"
    @statusA.setter
    def statusA(self, statusA):
        self._statusA = statusA
    
    @property
    def palabraP(self):
        return self._palabraP
    @palabraP.setter
    def palabraP(self, palabraP):
        self._palabraP = palabraP
        self.modPalabraP()

    @property
    def palabra(self):
        return self._palabra
    @palabra.setter
    def palabra(self, palabra):
        self._palabra = palabra
        self.palabraP = list(palabra)

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
        while (self.vidas > 0) and list(self.palabra)!=self.palabraP:
            self.letras = input("Ingrese letra/s:").upper()
            if self.vidas >0:
                cambios = False
                for x in range(len(self.letras)):
                    for i in range(len(self.palabra)):
                        if self.letras[x] == self.palabra[i]:
                            self.palabraP[i] = self.letras[x]
                            cambios = True
                    if cambios == False:
                        self.quitarVida()
                        print(f"La letra {self.letras} era incorrecta")
                    else:
                        print(self.palabraP)
        if self.vidas <=0:
            self._contadorMuertes()
            self.statusA = True
        self._contadorRondas()   
                
        
    

    
   
