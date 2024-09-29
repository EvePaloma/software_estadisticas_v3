from tkinter import *

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
        self.cont_valores = Frame(self, width= 550, height= 200, bg = "PeachPuff2")
        self.cont_valores.grid(row=0, column=0, columnspan=3, padx= 10, pady= 10, ipadx= 12)
        cont_boton = Frame(self, width= 100, height= 200, bg = "PeachPuff2")
        cont_boton.grid(row=0, column=3, padx=8, pady=10, ipadx= 10)


        self.entradas = []  # Lista para almacenar los widgets de entrada de cada fila

        # Crear las filas de entradas
        for i in range(3):  # Puedes cambiar el rango si necesitas más filas
            fila_entradas = self.x_y_z(i, self.cont_valores)
            self.entradas.append(fila_entradas)
            
        self.lista_1 = []
        self.lista_2 = []
        self.lista_3 = []
        #self.lista_1[0:4] = self.x_y_z(0, cont_valores)
        #self.lista_2[0:4] = self.x_y_z(1, cont_valores) 
        #self.lista_3[0:4] = self.x_y_z(2, cont_valores)
        self.x_y_z(0, self.cont_valores)
        self.x_y_z(1, self.cont_valores) 
        self.x_y_z(2, self.cont_valores)

        #self.x1, self.y1, self.z1 = self.x_y_z(0, cont_valores)
        #self.x2, self.y2, self.z2 = self.x_y_z(1, cont_valores)
        #self.x3, self.y3, self.z3 = self.x_y_z(2, cont_valores)

        self.btn_guardar = Button(cont_boton, text="Evaluar", justify= CENTER, font =("Verdana", 14), command= self.evaluar)
        self.btn_guardar.grid(row = 1, column = 0)

        cont_resultado = Frame(self, width= 600, height= 300, bg = "PeachPuff3")
        cont_resultado.grid(row= 1, columnspan=4)

    def x_y_z(self, fila, contenedor, estado = False):
        validacion = self.register(self.validar)
        color_fondo = "PeachPuff2"
        self.x = DoubleVar()
        self.y = StringVar()
        self.z = StringVar()
        self.r = StringVar()
        Label(contenedor, text= "", bg = color_fondo).grid(row= fila, column=0, padx= 6)
        Label(contenedor, text="[ ", font=("Verdana", 15), justify=CENTER, bg = color_fondo).grid(row= fila, column=1, pady = 12)
        self.entry_x = Entry(contenedor, validate="key", validatecommand=(validacion, '%P'))
        self.entry_x.config(textvariable= self.x, font =("Verdana", 14), width= 5, justify= CENTER)
        self.entry_x.grid(row= fila, column= 2, pady = 10)
        Label(contenedor, text=" x + ", font=("Verdana", 15), justify=CENTER, bg = color_fondo).grid(row= fila, column=3, pady = 10)
        self.entry_y = Entry(contenedor, validate="key", validatecommand=(validacion, '%P'))
        self.entry_y.config(textvariable= self.y, font =("Verdana", 14), width= 5, justify= CENTER)
        self.entry_y.grid(row= fila, column= 4, pady = 10)
        Label(contenedor, text=" y + ", font=("Verdana", 15), justify=CENTER, bg = color_fondo).grid(row= fila, column=5, pady = 10)
        self.entry_z = Entry(contenedor, validate="key", validatecommand=(validacion, '%P'))
        self.entry_z.config(textvariable= self.z, font =("Verdana", 14), width= 5, justify= CENTER)
        self.entry_z.grid(row= fila, column= 6, pady = 10)
        Label(contenedor, text=" z |", font=("Verdana", 15), justify=CENTER, bg = color_fondo).grid(row= fila, column=7, pady = 10)
        self.entry_r = Entry(contenedor, validate="key", validatecommand=(validacion, '%P'))
        self.entry_r.config(textvariable= self.r, font =("Verdana", 14), width= 5, justify= CENTER)
        self.entry_r.grid(row= fila, column= 8, pady = 10)
        Label(contenedor, text=" ]", font=("Verdana", 15), justify=CENTER, bg = color_fondo).grid(row= fila, column=9, pady = 10)
        
        return(self.x, self.y, self.z, self.r)
                
    def evaluar(self):
        self.listas = [self.lista_1, self.lista_2, self.lista_3]
        for lista in self.listas:
            for elemento in lista:
                #self.matriz.append(float(elemento))
                print(self.x1)
        print(self.matriz)



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