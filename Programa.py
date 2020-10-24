from ManejadorViajeros import ManejadorViajeros


def mostrarMemoria(mi_lista):

  for i in range(4):
    print('>> Dirección de memoria: {} '.format(hex(id(mi_lista)) ))
    print('>> Valor almacenado: ')
    print(    '{}'.format(mi_lista.getviajeroLista(i).MOSTRARDATOS()))
    print ("---------------------------------------------------------------------------------")

def zero(nro, manejadorViajero):
    print("\n\t                            FIN VIAJERO FRECUENTE ")
    print('###############################################################################')

def one(nro, manejadorViajero):
    print("\t\tConsultar Cantidad de Millas")
    millas=manejadorViajero.getviajeroLista(nro).CantidadTotalMillas()
    print("MILLAS Totales: ", millas)
    input('\nPara seleccionar otra opcion presione enter')

def two(nro, manejadorViajero): #####################################
    print("\t\tAcumular Millas")

    print("CANTIDAD DE MILLAS ACTUALES: ", manejadorViajero.getviajeroLista(nro).CantidadTotalMillas())
    aumentar = int(input("INGRESE MILLAS NUEVAS: "))
    manejadorViajero.acumularMillasL(nro, aumentar)
    print("MILLAS Totales ACTUALIZADAS: ", manejadorViajero.getCantidadTotalMillas(nro))
    input('\nPara seleccionar otra opcion presione enter')

def tree(nro, manejadorViajero):
    print("\t\tCanjear Millas")
    print("CANTIDAD DE MILLAS ACTUALES: ", manejadorViajero.getviajeroLista(nro).CantidadTotalMillas())
    canjear=int(input("¿CUANTAS MILLAS DESEA CANJEAR?: "))
    RESULTADO=manejadorViajero.canjearMillasL(nro, canjear)
    print("MILLAS CANJEADAS: ", RESULTADO)
    print("MILLAS DISPONIBLE: ", manejadorViajero.getviajeroLista(nro).CantidadTotalMillas(),"m")
    input('\nPara seleccionar otra opcion presione enter')




switcher = {
    0: zero,
    1: one,
    2: two,
    3: tree
}

def switch(argument, nro, manejadorViajero):
    func = switcher.get(argument, lambda x,y: print("Opción incorrecta"))
    func(nro, manejadorViajero)

if __name__ == '__main__':
    manejadorViajero= ManejadorViajeros()
    manejadorViajero.testViajeros()
    print('\n\n\t\t BIENVENIDO\n')
    nro=int(input("\t >>Ingrese su numero de pasajero frecuente (del 1 al 20): "))

    bandera = False # pongo la bandera en falso para forzar a que entre al bucle la primera vez
    while not bandera:
        print("")
        print('\t\t########################################')
        print("\t\t# 0) Salir                             #")
        print("\t\t# 1) Consultar Cantidad de Millas      #")
        print("\t\t# 2) Acumular Millas                   #")
        print("\t\t# 3) Canjear Millas                    #")
        print('\t\t########################################')
        opcion= int(input("\t >>Ingrese una opción: \n\t"))
        switch(opcion, nro, manejadorViajero)
        bandera = int(opcion)==0 # Si lee el 0 cambia la bandera a true y sale del menú



    ############################ PUNTO 3
    print('\n\n\t\t           ALMACENAMIENTO EN MEMORIA PARA 4 VIAJEROS')
    print('---------------------------------------------------------------------------------\n')
    mostrarMemoria(manejadorViajero)