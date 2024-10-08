from tkinter import *
from tkinter import messagebox


class GaussJordan(Frame):
    def __init__(self, master=None):
        super().__init__(master, width=700, height=400, bg="PeachPuff2")
        self.master = master
        self.grid(row=0, column=0, sticky="nsew")
        self.createWidgets()
        #Almacena los valores de las entradas
        self.lista_1 = []
        self.lista_2 = []
        self.lista_3 = []
        #Crea las entradas para las 3 ecuaciones
        self.x_y_z(0, self.cont_valores)
        self.x_y_z(1, self.cont_valores)
        self.x_y_z(2, self.cont_valores)

    
    #Validación de entrada
    def validar(self, entrada):
        if entrada == "" or entrada == "-" or entrada == ".":  
            return True
        try:
            float(entrada)
            return True
        except ValueError:
            return False

    # Método para calcular el resultado del sistema de ecuaciones
    def calcular(self):
        try:
            #Lee los valores y resultados de la entrada
            x1 = float(self.lista_1[0].get())
            y1 = float(self.lista_1[1].get())
            z1 = float(self.lista_1[2].get())
            r1 = float(self.lista_1[3].get())

            x2 = float(self.lista_2[0].get())
            y2 = float(self.lista_2[1].get())
            z2 = float(self.lista_2[2].get())
            r2 = float(self.lista_2[3].get())

            x3 = float(self.lista_3[0].get())
            y3 = float(self.lista_3[1].get())
            z3 = float(self.lista_3[2].get())
            r3 = float(self.lista_3[3].get())

            #Construye la matriz inicial
            matriz = [[x1, y1, z1, r1],
                      [x2, y2, z2, r2],
                      [x3, y3, z3, r3]]

            #Aplica el método de Gauss-Jordan
            tipo_sistema, solucion = self.gauss_jordan(matriz)

            #Mostramos los resultados
            self.mostrar_resultados(matriz, tipo_sistema, solucion)
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores válidos.")

    # Método para aplicar el método de Gauss-Jordan
    def gauss_jordan(self, matriz):
        #Convierte a forma escalonada
        for i in range(3):
            #Hacer que el elemento de la diagonal sea 1
            piv = matriz[i][i]
            if piv == 0:
                #Si hay un 0 en la diagonal, buscaremos otra fila para intercambiar
                for j in range(i + 1, 3):
                    if matriz[j][i] != 0:
                        matriz[i], matriz[j] = matriz[j], matriz[i]
                        piv = matriz[i][i]
                        break

            for j in range(len(matriz[i])):
                matriz[i][j] /= piv

            #Hacer ceros en la columna de la variable actual
            for j in range(3):
                if j != i:
                    factor = matriz[j][i]
                    for k in range(len(matriz[i])):
                        matriz[j][k] -= factor * matriz[i][k]

        #Verificamos el tipo de sistema
        if matriz[0][0] == 0 and matriz[0][3] != 0:
            return "Incompatible"  #No hay solución
        elif matriz[0][0] == 0 and matriz[0][3] == 0:
            
            return "Compatible indeterminado", (x, y, z)  #Infinitas soluciones
        else:
            #Solución única
            x = matriz[0][3]
            y = matriz[1][3]
            z = matriz[2][3]
            return "Compatible determinado", (x, y, z)

    #Mostramos los resultados y la matriz
    def mostrar_resultados(self, matriz, tipo_sistema, solucion):
        matriz_str = "\n".join(["\t".join([f"{num:.2f}" for num in fila]) for fila in matriz])
        self.matriz_label.config(text=f"Matriz transformada:\n{matriz_str}", font=("Verdana", 12, "bold"))

        self.tipo_sistema_label.config(text=f"Tipo de sistema: {tipo_sistema}", font=("Verdana", 12, "bold"))

        if tipo_sistema == "Compatible determinado":
            self.resultado_label.config(text=f"Resultados:\n x = {solucion[0]:.2f}\n y = {solucion[1]:.2f}\n z = {solucion[2]:.2f}", font=("Verdana", 12, "bold"))
        else:
            self.resultado_label.config(text=f"Tipo de sistema: {tipo_sistema}", font=("Verdana", 12, "bold"))

    #Función para generar las entradas de las ecuaciones
    def x_y_z(self, fila, contenedor):
        validacion = self.register(self.validar)
        color_fondo = "PeachPuff2"
        x = StringVar()
        y = StringVar()
        z = StringVar()
        r = StringVar()

        Label(contenedor, text="[ ", font=("Verdana", 15), justify=CENTER, bg=color_fondo).grid(row=fila, column=1, pady=12)
        entry_x = Entry(contenedor, validate="key", validatecommand=(validacion, '%P'))
        entry_x.config(textvariable=x, font=("Verdana", 14), width=5, justify=CENTER)
        entry_x.grid(row=fila, column=2, pady=10)
        Label(contenedor, text=" x + ", font=("Verdana", 15), justify=CENTER, bg=color_fondo).grid(row=fila, column=3, pady=10)
        entry_y = Entry(contenedor, validate="key", validatecommand=(validacion, '%P'))
        entry_y.config(textvariable=y, font=("Verdana", 14), width=5, justify=CENTER)
        entry_y.grid(row=fila, column=4, pady=10)
        Label(contenedor, text=" y + ", font=("Verdana", 15), justify=CENTER, bg=color_fondo).grid(row=fila, column=5, pady=10)
        entry_z = Entry(contenedor, validate="key", validatecommand=(validacion, '%P'))
        entry_z.config(textvariable=z, font=("Verdana", 14), width=5, justify=CENTER)
        entry_z.grid(row=fila, column=6, pady=10)
        Label(contenedor, text=" z |", font=("Verdana", 15), justify=CENTER, bg=color_fondo).grid(row=fila, column=7, pady=10)
        entry_r = Entry(contenedor, validate="key", validatecommand=(validacion, '%P'))
        entry_r.config(textvariable=r, font=("Verdana", 14), width=5, justify=CENTER)
        entry_r.grid(row=fila, column=8, pady=10)
        Label(contenedor, text=" ]", font=("Verdana", 15), justify=CENTER, bg=color_fondo).grid(row=fila, column=9, pady=10)

        #Guardar las referencias de las entradas en las listas
        if fila == 0:
            self.lista_1.extend([entry_x, entry_y, entry_z, entry_r])
        elif fila == 1:
            self.lista_2.extend([entry_x, entry_y, entry_z, entry_r])
        elif fila == 2:
            self.lista_3.extend([entry_x, entry_y, entry_z, entry_r])

    def createWidgets(self):
        self.cont_valores = Frame(self,  width= 550, height= 200,bg="PeachPuff2")
        self.cont_valores.grid(row=0, column=0)

        self.cont_resultados = LabelFrame(self, width= 600, height= 600,bg="PeachPuff3")
        self.cont_resultados.grid(row=2, column=0,padx=10,pady=10, sticky="nsew")

        btn = Button(self, text="Calcular", command=self.calcular, bg = "PeachPuff2",font=("Verdana", 12, "bold"))
        btn.grid(row=1, column=0, pady=10)

        self.tipo_sistema_label = Label(self.cont_resultados, text="", bg="PeachPuff3", font=("Verdana", 12))
        self.tipo_sistema_label.grid(row=0, column=1)
        
        self.resultado_label = Label(self.cont_resultados, text="", bg="PeachPuff3", font=("Verdana", 12))
        self.resultado_label.grid(row=1, column=1)

        self.matriz_label = Label(self.cont_resultados, text="", bg="PeachPuff3", font=("Verdana", 12))
        self.matriz_label.grid(row=2, column=1)


ventana = Tk()
ventana.wm_title("Método Gauss-Jordan")
ventana.wm_resizable(0, 0)
entradas = GaussJordan(ventana)
entradas.mainloop()












'''def gaussJordan(matriz):
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
        mostrar_soluciones(resultado)  # Mostrar las soluciones separadas'''

            
