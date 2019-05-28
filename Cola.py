from random import random

def tiempoEntreLlegadas():
  X = 2 + 3*random()
  tiempoLlegada = ((5*X*X) - 12)
  return tiempoLlegada

def tiempoServicio():
  r1 = random()
  print(r1)
  if(r1 <= 0.166666666666666667):
    return 1 + 2*random()
  elif (r1 <= 0.444444444444444):
    return 3 + 2*random()
  elif (r1 <= 0.777777777777778):
    return 5 + 2*random()
  else:
    return 7 + 2*random()

def simulacion():
  listaPersona = []
  for i in range(0, 50):
    tiempoPersona = [tiempoEntreLlegadas(), tiempoEntreSalida()]
    listaPersona.append(tiempoPersona)
  return listaPersona

def tiempoPromedioCliente():
  listaPersona = simulacion()

print(simulacion())
