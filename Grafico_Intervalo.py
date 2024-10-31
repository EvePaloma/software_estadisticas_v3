import numpy as np
import matplotlib.pyplot as plt
from tkinter import messagebox
from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.pyplot import text
from matplotlib import style

class INTERVALOS(Frame):
    def __init__(self, master = None):
        super().__init__(master, width = 1360, height = 700, bg = "#ba5954")
        self.master = master
        self.pack_propagate(False) 
        self.pack(expand=True)
        self.menu()
        self.error = True
        self.master.protocol("WM_DELETE_WINDOW", lambda: None)

    def volver_menu(self):
        from inicio import MENU
        self.master.destroy()
        ventana = Tk()
        ventana.wm_title("Menú software estadísticas")
        ventana.wm_resizable(0,0)
        menu = MENU(ventana)
        menu.mainloop()

    def str_to(self):
        try:
            self.a = float(self.valA.get())
            self.b = float(self.valB.get())
            self.c = float(self.valC.get())
            self.Li = float(self.lim_inferior.get())
            self.Ls = float(self.lim_superior.get())
            try:
                self.intervalo = int(self.intervalos.get())
                if self.intervalo <= 0:
                    messagebox.showerror("Error", "El número de intervalos debe ser un valor positivo")
                    self.error = False
                else:
                    self.error = True
            except:
                messagebox.showerror("Error", "El número de intervalos deber ser un valor entero")   
            if self.Li > self.Ls:
                messagebox.showerror("Error", "El límite inferior debe ser menor al límite superior")
        except ValueError:
            messagebox.showerror("Error", "Por favor, complete todos los campos con valores numéricos.")
            self.error = False

    def validar(self, entrada):
        if entrada == "" or entrada == "-" or entrada == ".":  
            return True
        try:
            float(entrada)
            return True
        except ValueError:
            return False
    
    def limpiar(self):
        try:
            entradas = [self.A, self.B, self.C, self.inferior, self.superior, self.inter]
            valore = [self.a, self.b, self.c, self.Li, self.Ls, self.intervalo]
            # Limpiar los valores de las entradas
            for entry in entradas:
                entry.delete(0, END)
            for val in valore:
                val = 0

            #limpia canva 1
            for widget in self.canva_I.winfo_children():
                widget.destroy()
            #limpia canva 2
            for widget in self.canva_S.winfo_children():
                widget.destroy()

            if hasattr(self, 'rta'):
                self.rta.pack_forget()
        except:
            pass

    def funcion_cuad(self, x):
        a = self.a
        b = self.b
        c = self.c
        #Función integral, ingresan los datos que de el usuario, el usuario ingresa los multiplicadores de x, x y el num
        y = a * (x**2) + b * x + c
        return (y)

    #Calculamos la integral indefinida(antiderivada) de la función cuadrática
    def integral_indefinida(self, x):
        a = self.a
        b = self.b
        c = self.c
        #Función integral, ingresan 
        #return (a / 3) * (x ** 3) + (b / 2) * (x ** 2) + c * x
        return (a * (x**3) / 3) + (b * (x ** 2) / 2) + c * x

    #Calculamos el área exacta usando la integral definida
    def area_exacta(self):
        #Calculamos la integral indefinida en los límites superior e inferior
        integral_superior = self.integral_indefinida(self.Ls)
        integral_inferior = self.integral_indefinida(self.Li)
        
        #Área exacta es la diferencia entre los limites
        area = integral_superior - integral_inferior
        return abs(area)

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
            if menor < 0:
                mayor = max(self.funcion_cuad(x[i-1]), self.funcion_cuad(x[i]))
                #2) Esquina superior izquierda
                coor_x.append(x[i-1])
                coor_y.append(mayor)
                #3) Esquina superior derecha
                coor_x.append(x[i])
                coor_y.append(mayor)
            else:
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
            if mayor < 0:
                menor = min(self.funcion_cuad(x[i-1]), self.funcion_cuad(x[i]))
                #2) Esquina superior izquierda
                coor_x.append(x[i-1])
                coor_y.append(menor)
                #3) Esquina superior derecha
                coor_x.append(x[i])
                coor_y.append(menor)                
            else:
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
        #limpia canva 1
        for widget in self.canva_I.winfo_children():
            widget.destroy()
        #limpia canva 2
        for widget in self.canva_S.winfo_children():
            widget.destroy()
        if hasattr(self, 'rta'):
            self.rta.pack_forget()

        #Gráfico inferior
        self.str_to()
        if self.error:
            n_intervalos = self.intervalo
            limI = self.Li
            limS = self.Ls

            """if self.a < 0:
                area_superior, xbarS, ybarS = self.Riemann_inferior(limI, limS, n_intervalos)
                area_inferior, xbarI, ybarI  = self.Riemann_superior(limI, limS, n_intervalos)
            else:
                area_inferior, xbarI, ybarI = self.Riemann_inferior(limI, limS, n_intervalos)
                area_superior, xbarS, ybarS = self.Riemann_superior(limI, limS, n_intervalos)"""
            
            area_inferior, xbarI, ybarI = self.Riemann_inferior(limI, limS, n_intervalos)
            area_superior, xbarS, ybarS = self.Riemann_superior(limI, limS, n_intervalos)

            if self.a < 0:
                intermedio = 0
                intermedio = area_inferior
                area_inferior = area_superior
                area_superior = intermedio

            area_exacta = self.area_exacta()

            #Porcentaje de error
            error1 = round((abs((abs(area_inferior) - area_exacta)/area_exacta)*100), 3)
            error2 = round((abs((abs(area_superior) - area_exacta)/area_exacta)*100), 3)

            x = np.linspace(limI - 1, limS + 1, 25)  #Número de puntos que usamos para graficar la curva
            #grafico inferior
            figI, axI = plt.subplots(figsize=(4.5, 3.7))
            axI.plot(x, self.funcion_cuad(x), 'k', label="f(x)")
            axI.plot(xbarI, ybarI, 'r:', label="Suma de Riemann Inferior")
            axI.set_xlabel("x")
            axI.set_ylabel("f(x)")
            axI.set_title("Gráfica de f(x)")
            axI.legend()
            # borra lo del canvas
            for widget in self.canva_I.winfo_children():
                widget.destroy()
            # pone la figura en el canvas
            cnvI = FigureCanvasTkAgg(figI, master=self.canva_I)
            cnvI.draw()
            cnvI.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)

            #Grafico superior
            figS, axS = plt.subplots(figsize=(4.5, 3.7)) 
            axS.plot(x, self.funcion_cuad(x), 'k', label="f(x)")
            axS.plot(xbarS, ybarS, 'b:', label="Suma de Riemann Superior")
            axS.set_xlabel("x")
            axS.set_ylabel("f(x)")
            axS.set_title("Gráfica de f(x)")
            axS.legend()
            # borra lo del canvas
            for widget in self.canva_S.winfo_children():
                widget.destroy()
            # pone la figura en el canvas
            cnvS = FigureCanvasTkAgg(figS, master=self.canva_S)
            cnvS.draw()
            cnvS.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)

            #ingresa loa labels al sistema
            self.rta = Frame(self.con_resultado, bg= self.color)
            self.rta.pack(expand= True)
            real = "Área Exacta: " + str(abs(round(area_exacta, 3)))
            self.label_real = Label(self.rta, text= real, font=("Verdana", 12), bg= self.color)
            self.label_real.grid(row=0, column=0, columnspan=2)
            inferior = "Área Inferior: " + str(round(abs(area_inferior), 3))
            self.label_inferior = Label(self.rta, text= inferior, font=("Verdana", 12), bg= self.color)
            self.label_inferior.grid(row=1, column=0, padx= 25, sticky= W)
            superior = "Área Superior: " + str(round(area_superior,3))
            self.label_superior = Label(self.rta, text= superior, font=("Verdana", 12), bg= self.color)
            self.label_superior.grid(row=2, column=0, padx= 25, sticky= W)
            error_inferior = "(%) Error Inferior: " + str(error1) + " %"
            self.label_errI = Label(self.rta, text= error_inferior, font=("Verdana", 12), bg= self.color)
            self.label_errI.grid(row=1, column=1, padx= 25, sticky= W)
            error_superior = "(%) Error Superior: " + str(error2) + " %"
            self.label_errS= Label(self.rta, text= error_superior, font=("Verdana", 12), bg= self.color)
            self.label_errS.grid(row=2, column=1, padx= 25, sticky= W)

            valore = [self.a, self.b, self.c, self.Li, self.Ls, self.intervalo]
            for val in valore:
                val = 0

    def menu(self):
        #contenedor principal
        validacion = self.register(self.validar)
        self.color = "#e0cbc1"
        borde = Frame(self, width= 1100, height= 680, bg= self.color)
        borde.pack_propagate(False)
        borde.pack(expand=True, padx= 15)
        
        #contenedor de los ingresos de datos
        cont_total = Frame(borde, bg= self.color)
        cont_total.pack()
        contenedor_funcion = Frame(cont_total, bg= self.color, width=600)
        contenedor_funcion.grid(row=0, column=0, columnspan= 3, padx= 15)
        contenedor_lim = Frame(cont_total, bg= self.color, width= 600)
        contenedor_lim.grid(row=1, column=1, columnspan=3, pady= 8, sticky= W)
        contenedor_btn = Frame(cont_total, bg= self.color, width= 200, height= 100)
        contenedor_btn.grid(row=0, column= 4, rowspan=2)

        #contenedor de los gráficos
        contenedor = Frame(borde, height= 500, width= 1100, background=self.color)
        contenedor.pack(pady= 5)
        self.contenedor_i = Frame(contenedor, width= 600, height= 500)
        self.contenedor_i.grid(row=0, column=0, padx= 8, pady= 8)
        self.contenedor_s = Frame(contenedor, width= 500, height= 400)
        self.contenedor_s.grid(row= 0, column=1, padx= 8, pady= 8)

        #contenedor de los resultados
        self.con_resultado = Frame(borde, width= 1100, height= 120, bg= self.color)
        self.con_resultado.pack(expand= True)

        #contenedor de los botones
        self.cont_botones = Frame(borde, width= 1100, height= 80, bg= self.color)
        self.cont_botones.pack(expand= True, pady= 10)
        
        #Ingreso de valores de la función
        self.valA = StringVar()
        self.valB = StringVar()
        self.valC = StringVar()

        Label(contenedor_funcion, text="y  =  ", font=("Verdana", 14), justify=CENTER, bg= self.color).grid(row=1, column=1)
        self.A = Entry(contenedor_funcion, validate="key", validatecommand=(validacion, '%P'))
        self.A.config(textvariable= self.valA, font=("Verdana", 13), justify=CENTER, width= 5)
        self.A.grid(row= 1, column=2, pady=10)
        Label(contenedor_funcion, text="  *  x^2  +  ", font=("Verdana", 14), justify=CENTER, bg= self.color).grid(row=1, column=3, pady=10)
        self.B = Entry(contenedor_funcion, validate="key", validatecommand=(validacion, '%P'))
        self.B.config(textvariable= self.valB, font=("Verdana", 13), justify=CENTER, width= 5)
        self.B.grid(row= 1, column=4, pady=10)
        Label(contenedor_funcion, text="  *  x  +  ", font=("Verdana", 14), justify=CENTER, bg= self.color).grid(row=1, column=5, pady=10)
        self.C = Entry(contenedor_funcion, validate="key", validatecommand=(validacion, '%P'))
        self.C.config(textvariable= self.valC, font=("Verdana", 13), justify=CENTER, width= 5)
        self.C.grid(row= 1, column= 6, pady=10)

        #Ingreso de limite inferior, superior e Intervalos
        cont1 = Frame(contenedor_lim, bg= self.color)
        cont1.grid(row= 0, column=0, padx= 11)
        cont2 = Frame(contenedor_lim, bg= self.color)
        cont2.grid(row= 0, column=1, padx= 25)
        cont3 = Frame(contenedor_lim, bg= self.color)
        cont3.grid(row= 0, column=2, padx= 10)

        self.lim_inferior = StringVar()
        self.lim_superior = StringVar()
        self.intervalos = StringVar()

        Label(cont1, text="Límite Inferior:", font=("Verdana", 12), bg= self.color, justify= LEFT).grid(row=0, column=0)
        self.inferior = Entry(cont1, validate="key", validatecommand=(validacion, '%P'))
        self.inferior.config(textvariable= self.lim_inferior, font=("Verdana", 13), justify=CENTER, width= 8)
        self.inferior.grid(row= 1, column=0, pady=5, padx= 4, sticky= W)
        Label(cont2, text="Límite Superior:", font=("Verdana", 12), justify=LEFT, bg= self.color).grid(row=0, column=0)
        self.superior = Entry(cont2, validate="key", validatecommand=(validacion, '%P'))
        self.superior.config(textvariable= self.lim_superior, font=("Verdana", 13), justify=CENTER, width= 8)
        self.superior.grid(row= 1, column=0, pady=5, padx= 4, sticky= W)
        Label(cont3, text="Nro. de Rectángulos:", font=("Verdana", 12), justify=LEFT, bg= self.color).grid(row=0, column=0)
        self.inter = Entry(cont3, validate="key", validatecommand=(validacion, '%P'))
        self.inter.config(textvariable= self.intervalos, font=("Verdana", 13), justify=CENTER, width= 8)
        self.inter.grid(row= 1, column= 0, pady=5, padx= 4, sticky= W)

        #Botón para guardar los valores
        self.btn_guardar = Button(contenedor_btn, text="Graficar", justify= CENTER, font=("Verdana", 12, "bold"), width= 12, command= self.graficar,  bg="#d1867d", activebackground= "#ee9388")
        self.btn_guardar.pack(padx= 25)

        #Canva_Frame donde se van a mostrar los gráficos
        self.canva_I = Canvas(self.contenedor_i, width= 460, height= 350)
        self.canva_I.pack(padx= 10)
        self.canva_S = Canvas(self.contenedor_s, width= 460, height= 350)
        self.canva_S.pack(padx= 10)

        #botones
        btn_volver = Button(self.cont_botones, text="Volver", bg="#d1867d", activebackground= "#ee9388", font=("Verdana", 13, "bold"), width=12, command= self.volver_menu)
        btn_volver.grid(row=0, column=0, padx=20)
        btn_limpiar = Button(self.cont_botones, text="Limpiar", bg="#d1867d", activebackground= "#ee9388", font=("Verdana", 13, "bold"), width=12, command= self.limpiar)
        btn_limpiar.grid(row=0, column=1, padx=20)


"""ventana = Tk()
ventana.wm_title("Cálculo de área")
ventana.wm_resizable(0,0)
entradas = INTERVALOS(ventana)
entradas.mainloop()"""