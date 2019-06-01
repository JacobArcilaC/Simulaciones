from random import random
from time import sleep
from collections import Counter
from copy import copy
import matplotlib.pyplot as plt

def tiempoEntreLlegadas():
  x = 2 + 3 * random()
  return (5*((x)**2) - 12)/113

def obtenerProbabilidad(lista):
  totalElementos = 0
  for i in lista:
    totalElementos += i[0]
  return [round(elemento[0]/totalElementos,2) for elemento in lista ]

def obtenerAcumulada(lista):
  probabilidadades = obtenerProbabilidad(lista)
  acumulada = [0]
  acumulado = 0
  for probabilidad in probabilidadades:
    acumulado += probabilidad 
    acumulado = round(acumulado,2)
    acumulada.append(acumulado)
  return acumulada

def obtenerIntervalo(lista, numero):
  for i in range(1, len(lista)):
    if (lista[i-1] <= numero < lista[i]):
      return i-1

def duracionServicio(acumulada,lista):
  r1 = random()
  r2 = random()
  intervalo = obtenerIntervalo(acumulada, r1)
  limiteInferior, limiteSuperior = lista[intervalo][1]
  return limiteInferior + (limiteSuperior - limiteInferior)*r2

def obtenerTiempoEntreLlegadas(lista):
  resultado = [0]
  for i in lista:
    resultado.append(i + resultado[len(resultado)])

def simulacion(tLlegadas, tServicios):
    tiempoDeAtencion = []
    tiemposSalida = []
    numeroPersonas = [0]
    tSimulacion = [0]

    tSimulacion.append(tLlegadas[0])
    tiempoDeAtencion.append(tSimulacion[-1])
    numeroPersonas.append(1)
    tiemposSalida.append(tLlegadas.pop(0) + tServicios.pop(0))
    while tLlegadas or tServicios:
      if(tLlegadas):
          if(numeroPersonas[-1] > 0 and tLlegadas[0] > tiemposSalida[-1]):
              numeroPersonas.append(numeroPersonas[-1] - 1)
              if(numeroPersonas[-1] == 0):
                  tSimulacion.append(tiemposSalida[-1])
              else: 
                  tSimulacion.append(tiemposSalida[-1])
                  tiemposSalida.append(tSimulacion[-1] + tServicios.pop(0))
                  tiempoDeAtencion.append(tSimulacion[-1])
          else:
              tSimulacion.append(tLlegadas.pop(0))
              if(numeroPersonas[-1] == 0):
                  tiemposSalida.append(tSimulacion[-1] + tServicios.pop(0))
                  tiempoDeAtencion.append(tSimulacion[-1])
              numeroPersonas.append(numeroPersonas[-1] + 1)

      else:
          numeroPersonas.append(numeroPersonas[-1] - 1)
          if(numeroPersonas[-1] == 0):
              tSimulacion.append(tiemposSalida[-1])

          else: 
              tSimulacion.append(tiemposSalida[-1])
              tiemposSalida.append(tSimulacion[-1] + tServicios.pop(0))
              tiempoDeAtencion.append(tSimulacion[-1])

    return (tSimulacion,  numeroPersonas, tiemposSalida, tiempoDeAtencion)

#obtener datos de la simulacion de la cola
tiemposDeLlegada = []
for i in range(50):
    tiemposDeLlegada.append(tiempoEntreLlegadas())

tiemposDeServicios = []
for i in range(50):
    tiemposDeServicios.append(duracionServicio(acumulada,lista))
tiemposDeLlegada.sort()
resultados = simulacion(copy(tiemposDeLlegada),copy(tiemposDeServicios))
tiempoEnElSistema = []
for i in range(len(resultados[2])):
    tiempoEnElSistema.append(resultados[2][i] - tiemposDeLlegada[i])
media = sum(tiempoEnElSistema)/len(tiempoEnElSistema)

print("El promedio de tiempo en el sistema es de: ", media)

desviacionEstandar = 0
for i in tiempoEnElSistema:
      desviacionEstandar += (i - media)**2
desviacionEstandar = desviacionEstandar/(len(tiempoEnElSistema) - 1)
desviacionEstandar = desviacionEstandar**(1/2)

#Intervalo de confianza apartir de los 50 datos con alfa = 0.1 y 49 grados de libertad sera 1.6766
intervaloDeConfianza = ((1.6766)*desviacionEstandar)/((len(tiempoEnElSistema))**(1/2))
limiteSuperior = media + intervaloDeConfianza
limiteInferior = media - intervaloDeConfianza

print("Limites son: ", " Inferior: ",limiteInferior," Superior: " ,limiteSuperior,)

#Mostrar Histograma Tiempo Promedio de Espera de los clientes
tiempoDeEspera = [resultados[3][i] - tiemposDeLlegada[i] for i in range(len(resultados[3])) ]
plt.title('Tiempos De Espera')
plt.hist(tiempoDeEspera,alpha=1, edgecolor = 'black',  linewidth=1)
plt.ylabel('Número de Personas')
plt.xlabel('Tiempo de espera[min]')
plt.grid(True)
plt.show()
plt.clf()
