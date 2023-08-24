from collections import Counter
from Jugador import Jugador
import time

class Ronda:
    jugador = Jugador()
    jugador2 = Jugador()
    
    statusJugador = True

    def __init__(this):
        this._listaRandoms = None
        this._listaSumas = None
        this._listaCasa = None
        this._statusJugador = None
        this._masComun = None
        this.resultado()
        this.evaluarDados()
    def __str__(this):
        return f'{this.listaRandoms} {this.listaSumas} {this.listaCasa} {this.statusJugador} {this.masComun}'
    @property
    def listaRandoms(this):
        return this._listaRandoms
    @property
    def listaSumas(this):
        return this._listaSumas
    @property
    def listaCasa(this):
        return this._listaCasa
    @property
    def statusJugador(this):
        return this._statusJugador
    @property
    def masComun(this):
        return this._masComun
    
    def mostrarTurno(this):
        print("La Ronda ha comenzado")
        turno = 0
        suma = 0
        for i in range(0,len(this.listaRandoms),2):
            turno +=1
            time.sleep(1)
            print("Turno",turno)
            time.sleep(0.5)
            print("Tirando Dados")
            this.esperaDados()
            print(f'Primer Dado: {this.listaRandoms[i]} Segundo Dado: {this.listaRandoms[i+1]} Suma de los Dados: {this.listaSumas[suma]} \nSuma de los dados de la casa: {this.listaCasa[suma]}')
            suma +=1
        if this.statusJugador ==True:
            time.sleep(0.5)
            print("Ganador")
        else:
            print("Perdedor, la casa gana")
    @staticmethod
    def esperaDados():
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        
    def evaluarDados(this):
        masComun = Counter(this.listaRandoms).most_common()
        this._masComun = masComun[0][0]
    def resultado(this):
        listaSumas = []
        listaRandoms = []
        listaCasa = []
        status = False
        
        
        while status == False:    
            rand1 = this.jugador.calcularRandom1()
            rand2 = this.jugador.calcularRandom2()

            listaRandoms.append(rand1)
            listaRandoms.append(rand2)

            sumaRands = rand1 + rand2

            listaSumas.append(sumaRands)

            rand3 = this.jugador2.calcularRandom3()
            listaCasa.append(rand3)
            
            if (sumaRands == 7) or (sumaRands == 2):
                status = True
                statusJugador = True

                
            elif (sumaRands == 12) or (rand3 ==7):
                status = True
                statusJugador = False
            else: 
                pass
        this._listaRandoms = listaRandoms
        this._listaSumas = listaSumas
        this._listaCasa = listaCasa
        this._statusJugador = statusJugador
        
        