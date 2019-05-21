import random, math 

#Genera numeros aleatorios entre 1 y 5 
#usando la funcion de distribucion acumulada 
def genNumeroAleatorio():
  numeroAleatorio = random.random() #Genera un numero aleatorio uniforme entre [0, 1] 
  if(numeroAleatorio <= 0.3):
    return 1
  elif(numeroAleatorio <= 0.8):
    return 2
  elif(numeroAleatorio <= 0.9):
    return 3
  elif(numeroAleatorio <= 0.98):
    return 4
  elif(numeroAleatorio <= 1):
    return 5

# PUNTO A. 
#Generar 1000 numeros aleatorios apartir de la funcion de probabilidad descrita
def primerPuntoTaller():
  numerosAleatorios = []
  for i in range(0, 1000):
    numerosAleatorios.append(genNumeroAleatorio())
  print("Numeros aleatorios generados ", numerosAleatorios)

def segundoPuntoTaller():
  numerosAleatorios = []
  for i in range(0, 1000):
    numeroAleatorio = random.random() #Genera un numero aleatorio uniforme entre [0, 1]
    y =  -1*math.log(-1*math.log(numeroAleatorio))
    numerosAleatorios.append(y)
  print("Numeros aleatorios generados ", numerosAleatorios)

def tercerPuntoTaller():
  numerosAleatorios = []
  for i in range(0, 1000):
    aleatorioExpo =  genNumeroExpo() #Genera un numero aleatorio exponencial entre [0, 1]
    y =  -1*math.log(-1*math.log(aleatorioExpo))
    numerosAleatorios.append(y)
  print("Numeros aleatorios generados ", numerosAleatorios)

def genNumeroExpo():
  while(True):
    numeroAleatorio = random.random() #Genera un numero aleatorio uniforme entre [0, 1]
    aleatorioExpo = -1*math.log(1-numeroAleatorio)
    if(aleatorioExpo>= 0 and aleatorioExpo<= 1):
      return numeroAleatorio