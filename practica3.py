import random, math 

#Genera numeros aleatorios entre 1 y 5 
#usando la funcion de distribucion acumulada 
def genRandomNumber():
  randomNumber = random.random() #Genera un numero aleatorio uniforme entre [0, 1] 
  if(randomNumber <= 0.3):
    return 1
  elif(randomNumber <= 0.8):
    return 2
  elif(randomNumber <= 0.9):
    return 3
  elif(randomNumber <= 0.98):
    return 4
  elif(randomNumber <= 1):
    return 5

# PUNTO A. 
#Generar 1000 numeros aleatorios apartir de la funcion de probabilidad descrita
def primerPuntoTaller():
  randomNumbers = []
  for i in range(0, 1000):
    randomNumbers.append(genRandomNumber())
  print("Numeros aleatorios generados ", randomNumbers)

def segundoPuntoTaller():
  randomNumbers = []
  for i in range(0, 1000):
    randomNumber = random.random() #Genera un numero aleatorio uniforme entre [0, 1]
    y =  -1*math.log(-1*math.log(randomNumber))
    randomNumbers.append(y)
  print("Numeros aleatorios generados ", randomNumbers)

def tercetPuntoTaller():