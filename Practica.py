import sympy,math
import numpy as np
from random import random

def tiempoEntreLlegadas():
    r1= random()
    x= -math.log(1-r1)/2
    return x
def tiempoEntreServicios():
    u1=random()
    u2=random()
    x1=math.sqrt(-2*math.log(u1))*math.cos(2*math.pi*u2) 
    x2=math.sqrt(-2*math.log(u1))*math.sin(2*math.pi*u2)
    xprima= 4+ math.sqrt(2.5)*x1
    return(xprima)
    

matriz= np.zeros((50,7))

for i in range(matriz.shape[0]):
    matriz[i][0]=round(int(i+1),0)
for i in range(matriz.shape[0]):
    matriz[i][1]=float(tiempoEntreLlegadas())
for i in range(matriz.shape[0]):
    matriz[i][2]=float(tiempoEntreServicios())

for i in range(matriz.shape[0]):
    print(matriz[i])
    print('\n')
