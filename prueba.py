import numpy as np

valA = 1
#Aca ingresa el valor del multiplicador de x
valB = -2
#Aca ingresa el valor del multplicador del num
valC = 3

def funcion_cuad(a, b, c, x):
    #Función integral, ingresan los datos que de el usuario, el usuario ingresa los multiplicadores de x, x y el num
    y = a * (x**2) + b * x + c
    return (y)

#El usuario ingresa el valor menor del rango
limiteInferior = 2
#El usuario ingresa el valor mayor del rango
limiteSuperior = 5
#El usuario ingresa la cantidad de particiones que va a tener el rango
cantidad_intervalos = 3

x = np.linspace(limiteInferior, limiteSuperior, cantidad_intervalos+1)
print(x)
#variable donde se van a sumar las areas de los rectangulos
area_total = 0
#Coordenadas en 'x' de las esquinas de cada barra del grafico de barras
coor_x = []
#Coordenadas en 'y' de las esquinas de cada barra del grafico de barras                             
coor_y = []                             

diccionario_inferior = {}

for i in range (1, cantidad_intervalos+1):
    #Suma de Rieman
    #compara el tamaño de la izquierda con el de la derecha y elige el menor
    menor = min(funcion_cuad(valA, valB, valC, x[i-1]), funcion_cuad(valA, valB, valC, x[i]))
    print(menor)
    #Calcula el ancho del rectángulo
    ancho = x[i] - x[i-1]
    #Suma al total el tamaño del area del rectángulo i
    area_total += menor*ancho

    diccionario_inferior["infI" + str(i)] = (x[i-1],0)
    diccionario_inferior["supI" + str(i)] = (x[i-1],menor)
    diccionario_inferior["supD" + str(i)] = (x[i],menor)
    diccionario_inferior["infD" + str(i)] = (x[i],0)
    
print(area_total)

print(diccionario_inferior)