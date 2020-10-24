class ViajeroFrecuente:
    __nroViajero= 0
    __DNI=""
    __NombreViajero= ""
    __ApellidoViajero= ""
    __MillasAcum= 0

    def __init__(self, nrov=0, dni="000000000", nombre="-", apellido="-", millas=0):
        self.__nroViajero=nrov
        self.__DNI=dni
        self.__NombreViajero=nombre
        self.__ApellidoViajero=apellido
        self.__MillasAcum=millas

    def getNRO(self):
        return self.__nroViajero

    def getDNI(self):
        return self.__DNI

    def getNom(self):
        return self.__NombreViajero

    def getApellido(self):
        return self.__ApellidoViajero

    def MOSTRARDATOS(self):
        return print("DATOS:\n", self.__nroViajero, self.__DNI, self.__NombreViajero, self.__ApellidoViajero, self.__MillasAcum)

    def CantidadTotalMillas(self):
        return self.__MillasAcum

    def acumularMillas(self, millasNuevas1):
        actualizadas = self.__MillasAcum + millasNuevas1
        self.__MillasAcum=actualizadas
        return actualizadas

    def canjearMillas(self, canje):
        if canje<=self.__MillasAcum:
            acum=self.__MillasAcum
            acum -= canje
            self.__MillasAcum=acum
            #print("MILLAS CANJEADAS: ",canje)
            return canje
        else:
            return print("***ERROR EN LA OPERACIÓN***")

##################################################PRUEBA DE LA CLASE##############
#a=ViajeroFrecuente(2, "3900900", "JERMIAS", )
#a.MOSTRARDATOS()
#acumular= int(input("INGRESE MILLAS NUEVAS: "))
#a.acumularMillas(acumular)
#sumarmasmillas=int(input())
#a.acumularMillas(sumarmasmillas)
#print("MILLAS TOTAL: ", a.CantidadTotalMillas())
#canjearr=int(input("CANJEAR MILLAS: "))
#a.canjearMillas(canjearr)
#print("AHORA TIENE: ",canjearr, "Millas para usar")
#print("SUS MILLAS ACUMULADAS SON: ", a.CantidadTotalMillas())
#################################################################################

