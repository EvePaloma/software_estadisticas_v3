import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate

#RECORDAR QUE PUEDEN ENTRAR VALORES NEGATIVOS
#Aca ingresa el multiplicador de x al cuadrado
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

#Función que calcula los rectangulos de abajo de la función
#Se ingresa la función, el limite menor, el límite mayor, y la cantidad de intervalitos
def Riemann_inferior(Li, Ls, n):
    #x va a tomar el número que tiene cada intervalo. Linspace divide el rango en n intervalos con el mismo tamaño
    x = np.linspace(Li, Ls, n)
    #variable donde se van a sumar las areas de los rectangulos
    area_total = 0
    #Coordenadas en 'x' de las esquinas de cada barra del grafico de barras
    coor_x = []
    #Coordenadas en 'y' de las esquinas de cada barra del grafico de barras                             
    coor_y = []                             

    diccionario_inferior = {}

    for i in range (1, n):
        #Suma de Rieman
        #compara el tamaño de la izquierda con el de la derecha y elige el menor
        menor = min(funcion_cuad(valA, valB, valC, x[i-1]), funcion_cuad(valA, valB, valC, x[i]))
        #Calcula el ancho del rectángulo
        ancho = x[i] - x[i-1]
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

        diccionario_inferior["infI" + str(i)] = (x[i-1],0)
        diccionario_inferior["supI" + str(i)] = (x[i-1],menor)
        diccionario_inferior["supD" + str(i)] = (x[i],menor)
        diccionario_inferior["infD" + str(i)] = (x[i],0)

    return(area_total, coor_x, coor_y, diccionario_inferior)

print(Riemann_inferior(limiteInferior, limiteSuperior, cantidad_intervalos))


#Función que calcula los rectangulos de arriba de la función
#Se ingresa la función, el limite menor, el límite mayor, y la cantidad de intervalitos
def Riemann_superior(Li, Ls, n):
    #x va a tomar el número que tiene cada intervalo. Linspace divide el rango en n intervalos con el mismo tamaño
    x = np.linspace(Li, Ls, n)
    #variable donde se van a sumar las areas de los rectangulos
    area_total = 0
    #Coordenadas en 'x' de las esquinas de cada barra del grafico de barras
    coor_x = []
    #Coordenadas en 'y' de las esquinas de cada barra del grafico de barras                             
    coor_y = []                             
    
    for i in range (1, n):
        #Suma de Rieman
        #compara el tamaño de la izquierda con el de la derecha y elige el menor
        mayor = max(funcion_cuad(valA, valB, valC, x[i-1]), funcion_cuad(valA, valB, valC, x[i]))
        #Calcula el ancho del rectángulo
        ancho = x[i] - x[i-1]
        #Suma al total el tamaño del area del rectángulo i
        area_total += mayor*ancho

        #Datos Grafico de Barras:
        #1) Esquina inferior izquierda
        coor_x.append(x[i-1])
        coor_y.append(0)
        #2) Esquina superior izquierda
        coor_x.append(x[i-1])
        coor_y.append(mayor)
        #3) Esquina superior derecha
        coor_x.append(x[i])
        coor_y.append(mayor)
        #4) Esquina inferior derecha
        coor_x.append(x[i])    
        coor_y.append(0)

    return(area_total, coor_x, coor_y)

print(Riemann_superior(limiteInferior, limiteSuperior, cantidad_intervalos))

#Calculamos la integral indefinida(antiderivada) de la función cuadrática
def integral_indefinida(x, a, b, c):
    return (a / 3) * (x ** 3) + (b / 2) * (x ** 2) + c * x


#Calculamos el área exacta usando la integral definida
def area_exacta(Li, Ls, a, b, c):
    #Calculamos la integral indefinida en los límites superior e inferior
    integral_superior = integral_indefinida(Ls, a, b, c)
    integral_inferior = integral_indefinida(Li, a, b, c)
    
    #Área exacta es la diferencia entre los limites
    area = integral_superior - integral_inferior
    return area


#Comparamos las áreas sin usar valor absoluto
'''def calcular_error(area_exacta, area_aprox):
    if area_exacta > area_aprox:
        error = area_exacta - area_aprox
    else:
        error = area_aprox - area_exacta
    return error'''


#Gráfico inferior
n_intervalos = 4
Area_inferior, xbar, ybar, diccionario_inferior = Riemann_inferior( limiteInferior, limiteSuperior, n_intervalos)
Area_exacta = area_exacta(limiteInferior, limiteSuperior, valA, valB, valC)
#Porcentaje de error
error1 = ((Area_exacta - Area_inferior)/Area_exacta)*100

x = np.linspace(limiteInferior, limiteSuperior, 20)  #Número de puntos que usamos para graficar la curva

print("Grafica de la funcion")
plt.plot(x, funcion_cuad(valA, valB, valC, x), 'k', label=("f(x)"))      #Se grafican los valores de x y la función
plt.plot(xbar, ybar, 'b:', label=("Suma de Riemann Inferior"))           #Se grafican las barras
plt.xlabel("x")            #Etiqueta de eje
plt.ylabel("f(x)")            #Etiqueta de eje
plt.title("Grafica de f(x)") #Titulo del grafico
plt.legend()                    #Leyendas
plt.show()                      #Mostrar grafico

print(Area_inferior)

valor_area_exacta = area_exacta(limiteInferior, limiteSuperior, valA,valB,valC)
#error_inf = calcular_error(valor_area_exacta,Area_inferior)

#Gráfico superior
n_intervalos = 4
Area_superior, xbar, ybar = Riemann_superior(limiteInferior, limiteSuperior, n_intervalos)
Area_exacta = area_exacta(limiteInferior, limiteSuperior, valA, valB, valC)
#Porcentaje de error
error2 = ((Area_exacta - Area_superior)/Area_exacta)*100

x = np.linspace(limiteInferior, limiteSuperior, 20)

print("Grafica de la funcion")
plt.plot(x, funcion_cuad(valA, valB, valC, x), 'k', label=("f(x)"))
plt.plot(xbar, ybar, 'b:', label=("Suma de Riemann Superior"))
plt.xlabel("x")            #Etiqueta de eje
plt.ylabel("f(x)")            #Etiqueta de eje
plt.title("Grafica de f(x)") #Titulo del grafico
plt.legend()                    #Leyendas
plt.show()                      #Mostrar grafico

print(Area_superior)

valor_area_exacta = area_exacta(limiteInferior,limiteSuperior,valA,valB,valC)
#error_sup = calcular_error(valor_area_exacta,Area_superior)

tabla = [['Inferior', n_intervalos, Area_inferior,error1], 
         ['Superior', n_intervalos, Area_superior,error2],
         ['Exacta', '', valor_area_exacta, '']
         ]

print(tabulate(tabla, headers = [""," Particion",  "Suma" , "Error (%)"])) 
