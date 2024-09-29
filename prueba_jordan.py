from tkinter import *
from tkinter import messagebox

class Programa(Frame):
    def __init__(self, master = None):
        super().__init__(master, width = 700, height = 400, bg = "PeachPuff2")
        self.master = master
        #self.pack_propagate(False) 
        self.pack(expand=True)
        self.ingresos()
        self.matriz = []
    
    def validar_negativo(self, texto):
        texto = texto.strip()
        if texto[0] == "-" or texto.find(",") != -1:
            return True
        else:
            return False

    def validar(self, texto):
        return texto.isdigit() or texto == "" or self.validar_negativo(texto) or len(texto) < 5

    def ingresos(self):
        validacion = self.register(self.validar)
        cont_valores = Frame(self, width= 550, height= 200, bg = "PeachPuff2")
        cont_valores.grid(row=0, column=0, columnspan=3, padx= 10, pady= 10, ipadx= 12)
        cont_boton = Frame(self, width= 100, height= 200, bg = "PeachPuff2")
        cont_boton.grid(row=0, column=3, padx=8, pady=10, ipadx= 10)
        
        color_fondo = "PeachPuff2"

        #Ingresos de los valores de la primera lista de elementos
        self.x1 = StringVar()
        self.y1 = StringVar()
        self.z1 = StringVar()
        self.r1 = StringVar()
        Label(cont_valores, text= "", bg = color_fondo).grid(row= 0, column=0, padx= 6)
        Label(cont_valores, text="[ ", font=("Verdana", 15), justify=CENTER, bg = color_fondo).grid(row= 0, column=1, pady = 12)
        self.entry_x1 = Entry(cont_valores, validate="key", validatecommand=(validacion, '%P'))
        self.entry_x1.config(textvariable= self.x1, font =("Verdana", 14), width= 5, justify= CENTER)
        self.entry_x1.grid(row= 0, column= 2, pady = 10)
        Label(cont_valores, text=" x + ", font=("Verdana", 15), justify=CENTER, bg = color_fondo).grid(row= 0, column=3, pady = 10)
        self.entry_y1 = Entry(cont_valores, validate="key", validatecommand=(validacion, '%P'))
        self.entry_y1.config(textvariable= self.y1, font =("Verdana", 14), width= 5, justify= CENTER)
        self.entry_y1.grid(row= 0, column= 4, pady = 10)
        Label(cont_valores, text=" y + ", font=("Verdana", 15), justify=CENTER, bg = color_fondo).grid(row= 0, column=5, pady = 10)
        self.entry_z1 = Entry(cont_valores, validate="key", validatecommand=(validacion, '%P'))
        self.entry_z1.config(textvariable= self.z1, font =("Verdana", 14), width= 5, justify= CENTER)
        self.entry_z1.grid(row= 0, column= 6, pady = 10)
        Label(cont_valores, text=" z |", font=("Verdana", 15), justify=CENTER, bg = color_fondo).grid(row= 0, column=7, pady = 10)
        self.entry_r1 = Entry(cont_valores, validate="key", validatecommand=(validacion, '%P'))
        self.entry_r1.config(textvariable= self.r1, font =("Verdana", 14), width= 5, justify= CENTER)
        self.entry_r1.grid(row= 0, column= 8, pady = 10)
        Label(cont_valores, text=" ]", font=("Verdana", 15), justify=CENTER, bg = color_fondo).grid(row= 0, column=9, pady = 10)
        
        #Ingreso de los valores de la segunda lista de elementos
        self.x2 = StringVar()
        self.y2 = StringVar()
        self.z2 = StringVar()
        self.r2 = StringVar()
        Label(cont_valores, text= "", bg = color_fondo).grid(row= 1, column=0, padx= 6)
        Label(cont_valores, text="[ ", font=("Verdana", 15), justify=CENTER, bg = color_fondo).grid(row= 1, column=1, pady = 12)
        self.entry_x2 = Entry(cont_valores, validate="key", validatecommand=(validacion, '%P'))
        self.entry_x2.config(textvariable= self.x2, font =("Verdana", 14), width= 5, justify= CENTER)
        self.entry_x2.grid(row= 1, column= 2, pady = 10)
        Label(cont_valores, text=" x + ", font=("Verdana", 15), justify=CENTER, bg = color_fondo).grid(row= 1, column=3, pady = 10)
        self.entry_y2 = Entry(cont_valores, validate="key", validatecommand=(validacion, '%P'))
        self.entry_y2.config(textvariable= self.y2, font =("Verdana", 14), width= 5, justify= CENTER)
        self.entry_y2.grid(row= 1, column= 4, pady = 10)
        Label(cont_valores, text=" y + ", font=("Verdana", 15), justify=CENTER, bg = color_fondo).grid(row= 1, column=5, pady = 10)
        self.entry_z2 = Entry(cont_valores, validate="key", validatecommand=(validacion, '%P'))
        self.entry_z2.config(textvariable= self.z2, font =("Verdana", 14), width= 5, justify= CENTER)
        self.entry_z2.grid(row= 1, column= 6, pady = 10)
        Label(cont_valores, text=" z |", font=("Verdana", 15), justify=CENTER, bg = color_fondo).grid(row= 1, column=7, pady = 10)
        self.entry_r2 = Entry(cont_valores, validate="key", validatecommand=(validacion, '%P'))
        self.entry_r2.config(textvariable= self.r2, font =("Verdana", 14), width= 5, justify= CENTER)
        self.entry_r2.grid(row= 1, column= 8, pady = 10)
        Label(cont_valores, text=" ]", font=("Verdana", 15), justify=CENTER, bg = color_fondo).grid(row= 1, column=9, pady = 10)

        #Ingreso de los valores de la segunda lista de elementos
        self.x3 = StringVar()
        self.y3 = StringVar()
        self.z3 = StringVar()
        self.r3 = StringVar()
        Label(cont_valores, text= "", bg = color_fondo).grid(row= 2, column=0, padx= 6)
        Label(cont_valores, text="[ ", font=("Verdana", 15), justify=CENTER, bg = color_fondo).grid(row= 2, column=1, pady = 12)
        self.entry_x3 = Entry(cont_valores, validate="key", validatecommand=(validacion, '%P'))
        self.entry_x3.config(textvariable= self.x3, font =("Verdana", 14), width= 5, justify= CENTER)
        self.entry_x3.grid(row= 2, column= 2, pady = 10)
        Label(cont_valores, text=" x + ", font=("Verdana", 15), justify=CENTER, bg = color_fondo).grid(row= 2, column=3, pady = 10)
        self.entry_y3 = Entry(cont_valores, validate="key", validatecommand=(validacion, '%P'))
        self.entry_y3.config(textvariable= self.y3, font =("Verdana", 14), width= 5, justify= CENTER)
        self.entry_y3.grid(row= 2, column= 4, pady = 10)
        Label(cont_valores, text=" y + ", font=("Verdana", 15), justify=CENTER, bg = color_fondo).grid(row= 2, column=5, pady = 10)
        self.entry_z3 = Entry(cont_valores, validate="key", validatecommand=(validacion, '%P'))
        self.entry_z3.config(textvariable= self.z3, font =("Verdana", 14), width= 5, justify= CENTER)
        self.entry_z3.grid(row= 2, column= 6, pady = 10)
        Label(cont_valores, text=" z |", font=("Verdana", 15), justify=CENTER, bg = color_fondo).grid(row= 2, column=7, pady = 10)
        self.entry_r3 = Entry(cont_valores, validate="key", validatecommand=(validacion, '%P'))
        self.entry_r3.config(textvariable= self.r3, font =("Verdana", 14), width= 5, justify= CENTER)
        self.entry_r3.grid(row= 2, column= 8, pady = 10)
        Label(cont_valores, text=" ]", font=("Verdana", 15), justify=CENTER, bg = color_fondo).grid(row= 2, column=9, pady = 10)

        self.btn_guardar = Button(cont_boton, text="Evaluar", justify= CENTER, font =("Verdana", 14), command= self.evaluar)
        self.btn_guardar.grid(row = 1, column = 0)

        cont_resultado = Frame(self, width= 600, height= 300, bg = "PeachPuff3")
        cont_resultado.grid(row= 1, columnspan=4)
                
    def evaluar(self):
        fila1 =[self.x1.get(), self.y1.get(), self.z1.get(), self.r1.get()]
        fila2 =[self.x2.get(), self.y2.get(), self.z2.get(), self.r2.get()]
        fila3 =[self.x3.get(), self.y3.get(), self.z3.get(), self.r3.get()]
        lista_total = [fila1, fila2, fila3]

        for lista in lista_total:
            for elemento in lista:
                try:
                    elemento= float(elemento)
                except:
                    if elemento == "":
                        elemento = 0
        print(lista_total)


ventana = Tk()
ventana.wm_title("Calculadora 2")
ventana.wm_resizable(0,0)
entradas = Programa(ventana)
entradas.mainloop()

"""def gaussJordan(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])

    for i in range(filas):
        if matriz[i][i] == 0:
            print("El sistema es Incompatible o Compatible indeterminado.")
            return None
        #Pivote toma el valor del elemento de la diagonal principal en la fila i.
        #Divide cada elemento de la fila por el pivote.
        pivote = matriz[i][i]
        for j in range(columnas):
            matriz[i][j] /= pivote
        
        #Verifica las demas filas(k), diferentes a las filas(i).
        #Calcula el factor qUe es el coeficiente de col(i) en fila(k).
        #Actualiza la fila(k) restando el producto del factor y los elementos de la fila(i).
        for k in range(filas):
            if k != i:
                factor = matriz[k][i]
                for j in range(columnas):
                    matriz[k][j] -= factor * matriz[i][j]
    return matriz

def tipo_sistema(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])

    #Verifica si alguna fila es cero excepto en la columna de resultados (Incompatible)
    for i in range(filas):
        es_cero = True
        for j in range(columnas - 1):
            if matriz[i][j] != 0:
                es_cero = False
                break
        if es_cero and matriz[i][-1] != 0:
            return "Incompatible"

    #Verifica si alguna fila es completamente cero (Compatible indeterminado)
    for i in range(filas):
        todo_cero = True
        for j in range(columnas):
            if matriz[i][j] != 0:
                todo_cero = False
                break
        if todo_cero:
            return "Compatible indeterminado"

    # Si no se encontraron las condiciones anteriores, el sistema es compatible determinado
    return "Compatible determinado"

def ingresar_matriz():
    matriz = []
    print("Ingrese los coeficientes y los valores independientes de las ecuaciones.")
    for i in range(3):
        ecuacion = []
        print(f"\nEcuación {i + 1}:")
        x = float(input(f"Ingrese el coeficiente de x: "))
        y = float(input(f"Ingrese el coeficiente de y: "))
        z = float(input(f"Ingrese el coeficiente de z: "))
        igualdad = float(input("Ingrese el valor de la igualdad: "))
        ecuacion.extend([x, y, z, igualdad])#Agrega los valores a la lista como elementos individuales.
        matriz.append(ecuacion)#Agrega la lista ecuación completa a la matriz.
    return matriz

def mostrar_matriz(matriz):
    print("\nMatriz final:")
    for fila in matriz:
        #Muestra la fila sin la última columna (las soluciones)
        for num in fila[:-1]:
            print(round(num, 2), end=" ")  
        print()  #Nueva línea después de cada fila

def mostrar_soluciones(matriz):
    print("\n" + "-"*30)
    print("Soluciones (valores independientes):")
    variables = ['x', 'y', 'z']
    
    for i in range(len(variables)):
        print(variables[i], "=", round(matriz[i][-1], 2))
        
    print("-"*30)

# Ingreso de la matriz aumentada por el usuario
matriz = ingresar_matriz()

# Aplicar el método de Gauss-Jordan
resultado = gaussJordan(matriz)

if resultado:
    tipo_sistema = tipo_sistema(resultado)
    print(f"\nEl sistema es: {tipo_sistema}")
    
    if tipo_sistema == "Compatible determinado":
        mostrar_matriz(resultado)  # Mostrar la matriz sin las soluciones
        mostrar_soluciones(resultado)  # Mostrar las soluciones separadas
"""