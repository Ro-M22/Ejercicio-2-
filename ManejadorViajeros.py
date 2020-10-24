from ViajeroFrecuente import ViajeroFrecuente
import csv
class ManejadorViajeros:
    #__listaViajeros=[]
    def __init__(self):
        self.__listaViajeros=[]

    def agregarViajero(self, unViajero):
        self.__listaViajeros.append(unViajero)
    def getviajeroLista(self, unViajero):
        return self.__listaViajeros[unViajero]
    def LISTAVIAJERO(self):
        return self.__listaViajeros

    def acumularMillasL(self, unViajero, millasNuevas):
        return self.__listaViajeros[unViajero].acumularMillas(millasNuevas)

    def canjearMillasL(self, unViajero, canje):
        return self.__listaViajeros[unViajero].canjearMillas(canje)

    def getCantidadTotalMillas(self, unViajero):
        return self.__listaViajeros[unViajero].CantidadTotalMillas()

    def __str__(self):
        s= ""
        for viajero in self.__listaViajeros:
            s+= str(viajero)+ "\n"
            return s

    def testViajeros(self):
        archivo= open("Viajeros.csv")
        reader= csv.reader(archivo, delimiter=",")
        for fila in reader:
            nro= int(fila[0])
            dni= fila[1]
            nombre= fila[2]
            apellido= fila[3]
            millas= int(fila[4])
            unViajero=ViajeroFrecuente(nro, dni, nombre, apellido, millas)
            self.agregarViajero(unViajero)














