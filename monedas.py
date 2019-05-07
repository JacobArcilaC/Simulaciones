import random

def simularJuego():
    cantidadCaras = 0
    cantidadSellos = 0
    utilidad = 0
    while(abs(cantidadCaras - cantidadSellos) != 3):
        probabilidad = float(random.random())
        if(probabilidad < 0.5):
            cantidadCaras += 1.0
        else:
            cantidadSellos += 1.0
        utilidad -= 1.0
    utilidad += 8.0
    totalLanz = cantidadCaras + cantidadSellos
    return [utilidad, totalLanz]

def ejecutarSimulaciones(maxIter):
    listaUtilidades = []
    listaNroLanzamientos = []
    for i in range(0, maxIter):
        listaUtilidades.append(simularJuego()[0])
        listaNroLanzamientos.append(simularJuego()[1])
    calcularEstadistica(listaUtilidades, listaNroLanzamientos)
    
def calcularEstadistica(listaUtilidades, listaNroLanzamientos):
    utilidadProm = sum(listaUtilidades)/len(listaUtilidades)
    lanzamientosProm  = sum(listaNroLanzamientos)/len(listaNroLanzamientos)
    probabilidadGanar = probGanar(listaUtilidades)
    print({"Utilidad Promedio Obtenida": utilidadProm, 
            "Numero de Lanzamientos Realizados en Promedio": lanzamientosProm, 
            "Probabilidad de obtener una ganancia >= 0": probabilidadGanar,
            "Probabilidad de obtener una ganancia < 0": 1 - probabilidadGanar})

def probGanar(listaUtilidades):
    numeroUtilidadesPos = 0
    for i in range(0, len(listaUtilidades)):
        if(listaUtilidades[i] >= 0):
            numeroUtilidadesPos += 1
    probGanar = float(numeroUtilidadesPos)/len(listaUtilidades)
    return probGanar

cantidadJuegos = int(input("Ingrese el numero de iteraciones a ejecutar"))
ejecutarSimulaciones(cantidadJuegos)
    
