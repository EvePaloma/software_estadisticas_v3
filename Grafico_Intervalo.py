import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate

#Aca ingresa el multiplicador de x al cuadrado
valA = 1
#Aca ingresa el valor del multiplicador de x
valB = 2
#Aca ingresa el valor del multplicador del num
valC = 3
#Aca ingresa el valor de x en la función
valx = 0

def funcion_cuad(a, b, c, x):
    #Función integral, ingresan los datos que de el usuario, el usuario ingresa los multiplicadores de x, x y el num
    y = a * (x**2) + b * x + c
    return (y)

#El usuario ingresa el valor menor del rango
limiteInferior = 0
#El usuario ingresa el valor mayor del rango
limiteSuperior = 0
#El usuario ingresa la cantidad de particiones que va a tener el rango
cantidad_intervalos = 8

#Función que calcula los rectangulos de abajo de la función
#Se ingresa la función, el limite menor, el límite mayor, y la cantidad de intervalitos
def RiemannInf(f, Li, Ls, n):
    #x va a tomar el número que tiene cada intervalo. Linspace divide el rango en n intervalos con el mismo tamaño
    x = np.linspace(Li, Ls, n)
    #variable donde se van a sumar las areas de los rectangulos
    area_total = 0
    #Una lista donde se almacenan cada area de cada rectángulo
    areas_rectangulos = []
    #variable donde se almacena el valor de la izquierda del subintervalo
    valor_izquierdo = 0
    #variable donde se almacena el valor de la derecha del subintervalo
    valor_derecho = 0
    #Coordenadas en 'x' de las esquinas de cada barra del grafico de barras
    coor_x = []
    #Coordenadas en 'y' de las esquinas de cada barra del grafico de barras                             
    coor_y = []                             

#Ver si toma las variables que deberia
#Cambiar los valores dentro del f de x, de donde salen?
    for i in range (1, n):
        #Suma de Riemman
        #busca el valor de la izquierda del subintervalo
        valor_izquierdo = (f(valA, valB, valC, x[i-1]))
        #busca el valor a la derecha del subintervalo
        valor_derecho = (f(valA, valB, valC, x[i]))
        #compara el tamaño de la izquierda con el de la derecha y elige el menor
        menor = min([f(valA, valB, valC, x[i-1]), f(valA, valB, valC, x[i])])
        #Calcula el ancho del rectángulo
        ancho = x[i] - x[i-1]
        #Agrega el area de los rectangulos a la lista de los angulos de los rectángulos
        areas_rectangulos.append(menor*ancho)
        #Suma al total el tamaño del area del rectángulo i
        area_total += menor*ancho

        #Datos Grafico de Barras:
        #1) Esquina inferior izquierda
        coor_x.append(x[i-1])
        coor_y.append(0)
        #2) Esquina superior izquierda
        coor_x.append(x[i-1])
        coor_y.append(menor)
        #3) Esquina superior derecha
        coor_x.append(x[i])
        coor_y.append(menor)
        #4) Esquina inferior derecha
        coor_x.append(x[i])    
        coor_y.append(0)

    return(area_total, coor_x, coor_y)

#Función que calcula los rectangulos de arriba de la función
#Se ingresa la función, el limite menor, el límite mayor, y la cantidad de intervalitos
def RiemannSup(f, Li, Ls, n):
    #x va a tomar el número que tiene cada intervalo. Linspace divide el rango en n intervalos con el mismo tamaño
    x = np.linspace(Li, Ls, n)
    #variable donde se van a sumar las areas de los rectangulos
    area_total = 0
    #Una lista donde se almacenan cada area de cada rectángulo
    areas_rectangulos = []
    #variable donde se almacena el valor de la izquierda del subintervalo
    valor_izquierdo = 0
    #variable donde se almacena el valor de la derecha del subintervalo
    valor_derecho = 0
    #Coordenadas en 'x' de las esquinas de cada barra del grafico de barras
    coor_x = []
    #Coordenadas en 'y' de las esquinas de cada barra del grafico de barras                             
    coor_y = []                             

    for i in range (1, n):
        #Suma de Riemman
        #busca el valor de la izquierda del subintervalo
        valor_izquierdo = (f(valA, valB, valC, x[i-1]))
        #busca el valor a la derecha del subintervalo
        valor_derecho= (f(valA, valB, valC, x[i]))
        #compara el tamaño de la izquierda con el de la derecha y elige el menor
        menor = max([f(valA, valB, valC, x[i-1]), f(valA, valB, valC, x[i])])
        #Calcula el ancho del rectángulo
        ancho = x[i] - x[i-1]
        #Agrega el area de los rectangulos a la lista de los angulos de los rectángulos
        areas_rectangulos.append(menor*ancho)
        #Suma al total el tamaño del area del rectángulo i
        area_total += menor*ancho

        #Datos Grafico de Barras:
        #1) Esquina inferior izquierda
        coor_x.append(x[i-1])
        coor_y.append(0)
        #2) Esquina superior izquierda
        coor_x.append(x[i-1])
        coor_y.append(menor)
        #3) Esquina superior derecha
        coor_x.append(x[i])
        coor_y.append(menor)
        #4) Esquina inferior derecha
        coor_x.append(x[i])    
        coor_y.append(0)

    return(area_total, coor_x, coor_y)


#Gráfico inferior
n_intervalos = 8
Area_inferior, xbar, ybar = RiemannInf(funcion_cuad, limiteInferior, limiteSuperior, n_intervalos)
#Porcentaje de error
#e1 = ((Aexacta - Area_inferior)/Aexacta)*100

x = np.linspace(limiteInferior, limiteSuperior, 20)

print("Grafica de la funcion")
plt.plot(x, funcion_cuad(valA, valB, valC, x), 'k', label=("f(x)"))
plt.plot(xbar, ybar, 'b:', label=("Suma de Riemann Inferior"))
plt.xlabel("x")            #Etiqueta de eje
plt.ylabel("f(x)")            #Etiqueta de eje
plt.title("Grafica de f(x)") #Titulo del grafico
plt.legend()                    #Leyendas
plt.show()                      #Mostrar grafico

print(Area_inferior)

#Gráfico superior
n_intervalos = 8
Area_superior, xbar, ybar = RiemannSup(funcion_cuad, limiteInferior, limiteSuperior, n_intervalos)
#Porcentaje de error
#e2 = ((Aexacta - Area_inferior)/Aexacta)*100

x = np.linspace(limiteInferior, limiteSuperior, 20)

print("Grafica de la funcion")
plt.plot(x, funcion_cuad(valA, valB, valC, x), 'k', label=("f(x)"))
plt.plot(xbar, ybar, 'b:', label=("Suma de Riemann Superior"))
plt.xlabel("x")            #Etiqueta de eje
plt.ylabel("f(x)")            #Etiqueta de eje
plt.title("Grafica de f(x)") #Titulo del grafico
plt.legend()                    #Leyendas
plt.show()                      #Mostrar grafico

tabla = [['Inferior', n_intervalos, Area_superior], 
         ['Superior', n_intervalos, Area_inferior]
         ]

print(tabulate(tabla, headers = ["Particion", "Suma", "Error (%)"]))