import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate
from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.pyplot import text
from matplotlib import style

class INTERVALOS(Frame):
    def __init__(self, master = None):
        super().__init__(master, width = 1100, height = 650, bg = "DeepSkyBlue4")
        self.master = master
        self.pack_propagate(False) 
        self.pack(expand=True)
        self.menu()

    def validar(self, entrada):
        if entrada == "" or entrada == "-" or entrada == ".":  
            return True
        try:
            float(entrada)
            return True
        except ValueError:
            return False
    
    def funcion_cuad(self, x):
        a = float(self.valA.get())
        b = float(self.valB.get())
        c = float(self.valC.get())
        #Función integral, ingresan los datos que de el usuario, el usuario ingresa los multiplicadores de x, x y el num
        y = a * (x**2) + b * x + c
        return (y)

    #Calculamos la integral indefinida(antiderivada) de la función cuadrática
    def integral_indefinida(self, x):
        a = float(self.valA.get())
        b = float(self.valB.get())
        c = float(self.valC.get())
        #Función integral, ingresan 
        return (a / 3) * (x ** 3) + (b / 2) * (x ** 2) + c * x

    #Calculamos el área exacta usando la integral definida
    def area_exacta(self, Li, Ls):
        #Calculamos la integral indefinida en los límites superior e inferior
        integral_superior = self.integral_indefinida(Ls)
        integral_inferior = self.integral_indefinida(Li)
        
        #Área exacta es la diferencia entre los limites
        area = integral_superior - integral_inferior
        return area

    #Función que calcula los rectangulos de abajo de la función
    #Se ingresa la función, el limite menor, el límite mayor, y la cantidad de intervalitos
    #Se le suma 1 a n, ya que al dividir los intervalos, son las lineas las que cuentan y no los espacios
    def Riemann_inferior(self, Li, Ls, n):
        #x va a tomar el número que tiene cada intervalo. Linspace divide el rango en n intervalos con el mismo tamaño
        x = np.linspace(Li, Ls, n+1)
        #variable donde se van a sumar las areas de los rectangulos
        area_total = 0
        #Coordenadas en 'x' de las esquinas de cada barra del grafico de barras
        coor_x = []
        #Coordenadas en 'y' de las esquinas de cada barra del grafico de barras                             
        coor_y = []                             

        diccionario_inferior = {}

        for i in range (1, n+1):
            #Suma de Rieman
            #compara el tamaño de la izquierda con el de la derecha y elige el menor
            menor = min(self.funcion_cuad(x[i-1]), self.funcion_cuad(x[i]))
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

        return(area_total, coor_x, coor_y)

    #Función que calcula los rectangulos de arriba de la función
    #Se ingresa la función, el limite menor, el límite mayor, y la cantidad de intervalitos
    def Riemann_superior(self, Li, Ls, n):
        #x va a tomar el número que tiene cada intervalo. Linspace divide el rango en n intervalos con el mismo tamaño
        x = np.linspace(Li, Ls, n+1)
        #variable donde se van a sumar las areas de los rectangulos
        area_total = 0
        #Coordenadas en 'x' de las esquinas de cada barra del grafico de barras
        coor_x = []
        #Coordenadas en 'y' de las esquinas de cada barra del grafico de barras                             
        coor_y = []                             
        
        for i in range (1, n+1):
            #Suma de Rieman
            #compara el tamaño de la izquierda con el de la derecha y elige el menor
            mayor = max(self.funcion_cuad(x[i-1]), self.funcion_cuad(x[i]))
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

    def graficar(self):
        #Gráfico inferior
        n_intervalos = int(self.intervalos.get())
        limI = float(self.lim_inferior.get())
        limS = float(self.lim_superior.get())

        area_inferior, xbarI, ybarI = self.Riemann_inferior(limI, limS, n_intervalos)
        area_superior, xbarS, ybarS = self.Riemann_superior(limI, limS, n_intervalos)

        area_exacta = self.area_exacta(limI, limS)

        #Porcentaje de error
        error1 = ((area_exacta - area_inferior)/area_exacta)*100
        x = np.linspace(limI - 2, limS + 2, 25)  #Número de puntos que usamos para graficar la curva

        #grafico inferior
        figI, axI = plt.subplots(figsize=(4.5, 3.5))
        axI.plot(x, self.funcion_cuad(x), 'k', label="f(x)")
        axI.plot(xbarI, ybarI, 'r:', label="Suma de Riemann Inferior")
        axI.set_xlabel("x")
        axI.set_ylabel("f(x)")
        axI.set_title("Grafica de f(x)")
        axI.legend()

        # borra lo del canvas
        for widget in self.canva_I.winfo_children():
            widget.destroy()

        # pone la figura en el canvas
        cnvI = FigureCanvasTkAgg(figI, master=self.canva_I)
        cnvI.draw()
        cnvI.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)

        #Grafico superior
        figS, axS = plt.subplots(figsize=(4.5, 3.5)) 
        axS.plot(x, self.funcion_cuad(x), 'k', label="f(x)")
        axS.plot(xbarS, ybarS, 'b:', label="Suma de Riemann Superior")
        axS.set_xlabel("x")
        axS.set_ylabel("f(x)")
        axS.set_title("Grafica de f(x)")
        axS.legend()

        # borra lo del canvas
        for widget in self.canva_S.winfo_children():
            widget.destroy()

        # pone la figura en el canvas
        cnvS = FigureCanvasTkAgg(figS, master=self.canva_S)
        cnvS.draw()
        cnvS.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)

    def menu(self):
        validacion = self.register(self.validar)
        color = "PaleTurquoise3"
        borde = LabelFrame(self, text= "Cálculo del área en intervalos", width= 1100, height= 600, bg= color)
        borde.pack_propagate(False)
        borde.pack(expand=True, padx= 15, pady=15)
        
        cont_total = Frame(borde, bg= color)
        cont_total.pack()
        contenedor_funcion = Frame(cont_total, bg= color, width=600)
        contenedor_funcion.grid(row=0, column=1, columnspan= 3, padx= 15)
        contenedor_lim = Frame(cont_total, bg= color, width= 600)
        contenedor_lim.grid(row=1, column=1, columnspan=3, pady= 8, sticky= W)
        contenedor_btn = Frame(cont_total, bg= color, width= 200, height= 100)
        contenedor_btn.grid(row=0, column= 4, rowspan=2)

        contenedor = Frame(borde)
        contenedor.pack(pady= 10, padx= 20)
        self.contenedor_i = Frame(contenedor, width= 500, height= 400, bg="khaki1")
        self.contenedor_i.grid(row=0, column=0, padx= 8, pady= 10)
        self.contenedor_s = Frame(contenedor, width= 500, height= 400, bg="khaki2")
        self.contenedor_s.grid(row= 0, column=1, padx= 8, pady= 10)
        
        #Ingreso de valores de la función
        self.valA = StringVar()
        self.valB = StringVar()
        self.valC = StringVar()

        self.A = Entry(contenedor_funcion, validate="key", validatecommand=(validacion, '%P'))
        self.A.config(textvariable= self.valA, font=("Verdana", 13), justify=CENTER, width= 5)
        self.A.grid(row= 1, column=1, pady=10)
        Label(contenedor_funcion, text="  *  x^2  +  ", font=("Verdana", 14), justify=CENTER, bg= color).grid(row=1, column=2, pady=10)
        self.B = Entry(contenedor_funcion, validate="key", validatecommand=(validacion, '%P'))
        self.B.config(textvariable= self.valB, font=("Verdana", 13), justify=CENTER, width= 5)
        self.B.grid(row= 1, column=3, pady=10)
        Label(contenedor_funcion, text="  *  x  +  ", font=("Verdana", 14), justify=CENTER, bg= color).grid(row=1, column=4, pady=10)
        self.C = Entry(contenedor_funcion, validate="key", validatecommand=(validacion, '%P'))
        self.C.config(textvariable= self.valC, font=("Verdana", 13), justify=CENTER, width= 5)
        self.C.grid(row= 1, column= 5, pady=10)
        Label(contenedor_funcion, text="  =  y  ", font=("Verdana", 14), justify=CENTER, bg= color).grid(row=1, column=6, pady=10)

        #Ingreso de limite inferior, superior e Intervalos
        cont1 = Frame(contenedor_lim, bg= color)
        cont1.grid(row= 0, column=0, padx= 11)
        cont2 = Frame(contenedor_lim, bg= color)
        cont2.grid(row= 0, column=1, padx= 25)
        cont3 = Frame(contenedor_lim, bg= color)
        cont3.grid(row= 0, column=2, padx= 10)

        self.lim_inferior = StringVar()
        self.lim_superior = StringVar()
        self.intervalos = StringVar()

        Label(cont1, text="Límite Inferior:", font=("Verdana", 11), bg= color, justify= LEFT).grid(row=0, column=0)
        self.inferior = Entry(cont1, validate="key", validatecommand=(validacion, '%P'))
        self.inferior.config(textvariable= self.lim_inferior, font=("Verdana", 13), justify=CENTER, width= 8)
        self.inferior.grid(row= 1, column=0, pady=5, padx= 4, sticky= W)
        Label(cont2, text="Límite Superior:", font=("Verdana", 11), justify=LEFT, bg= color).grid(row=0, column=0)
        self.superior = Entry(cont2, validate="key", validatecommand=(validacion, '%P'))
        self.superior.config(textvariable= self.lim_superior, font=("Verdana", 13), justify=CENTER, width= 8)
        self.superior.grid(row= 1, column=0, pady=5, padx= 4, sticky= W)
        Label(cont3, text="Nro. de Intervalos:", font=("Verdana", 11), justify=LEFT, bg= color).grid(row=0, column=0)
        self.inter = Entry(cont3, validate="key", validatecommand=(validacion, '%P'))
        self.inter.config(textvariable= self.intervalos, font=("Verdana", 13), justify=CENTER, width= 8)
        self.inter.grid(row= 1, column= 0, pady=5, padx= 4, sticky= W)

        #Botón para guardar los valores
        self.btn_guardar = Button(contenedor_btn, text="Graficar", justify= CENTER, font=("Verdana", 11), width= 12, command= self.graficar)
        self.btn_guardar.pack(padx= 25)

        #Canva_Frame donde se van a mostrar los gráficos
        self.canva_I = Canvas(self.contenedor_i, width= 400, height= 300, highlightbackground= "yellow3")
        self.canva_I.pack(padx= 10, pady= 10)
        self.canva_S = Canvas(self.contenedor_s, width= 400, height= 300, highlightbackground= "yellow3")
        self.canva_S.pack(padx= 10, pady= 10)


ventana = Tk()
ventana.wm_title("Grafico de Intervalos")
#ventana.wm_resizable(0,0)
entradas = INTERVALOS(ventana)
entradas.mainloop()

"""
#RECORDAR QUE PUEDEN ENTRAR VALORES NEGATIVOS
#Aca ingresa el multiplicador de x al cuadrado
valA = 1
#Aca ingresa el valor del multiplicador de x
valB = -2
#Aca ingresa el valor del multplicador del num
valC = 3



#El usuario ingresa el valor menor del rango
limiteInferior = 2
#El usuario ingresa el valor mayor del rango
limiteSuperior = 5
#El usuario ingresa la cantidad de particiones que va a tener el rango
cantidad_intervalos = 3




print(Riemann_inferior(limiteInferior, limiteSuperior, cantidad_intervalos+1))




print(Riemann_superior(limiteInferior, limiteSuperior, cantidad_intervalos))








#Comparamos las áreas sin usar valor absoluto
'''def calcular_error(area_exacta, area_aprox):
    if area_exacta > area_aprox:
        error = area_exacta - area_aprox
    else:
        error = area_aprox - area_exacta
    return error'''




print(Area_inferior)

valor_area_exacta = area_exacta(limiteInferior, limiteSuperior, valA,valB,valC)
#error_inf = calcular_error(valor_area_exacta,Area_inferior)

#Gráfico superior
n_intervalos = 11
Area_superior, xbar, ybar = Riemann_superior(limiteInferior, limiteSuperior, n_intervalos)
Area_exacta = area_exacta(limiteInferior, limiteSuperior, valA, valB, valC)
#Porcentaje de error
error2 = ((Area_superior - Area_exacta)/Area_exacta)*100

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
"""