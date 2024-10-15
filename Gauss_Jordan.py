from tkinter import *
from tkinter import messagebox

class GaussJordan(Frame):
    def __init__(self, master=None):
        super().__init__(master, width=1100, height=600, bg="PeachPuff2")
        self.master = master
        self.pack_propagate(False) 
        self.pack(expand=True)
        self.grid()
        

        #Contenedores
        self.cont_valores = Frame(self, width=900, height=500, bg="PeachPuff2")
        self.cont_valores.grid(row=0, column=0)
        self.cont_valores.grid_rowconfigure(0, weight=1)
        self.cont_valores.grid_columnconfigure(0, weight=1)

        self.cont_resultados = Frame(self, width=800, height=400, bg="PeachPuff2")
        self.cont_resultados.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
        self.cont_resultados.grid_remove()

        #Etiqueta para mostrar el tipo de sistema
        self.label_tipo_sistema = Label(self, text="", font=("Verdana", 14), bg="PeachPuff2")
        self.label_tipo_sistema.grid(row=3, column=0, pady=10)
        self.label_tipo_sistema.grid_remove()

        #Listas para almacenar las entradas
        self.lista_1 = []
        self.lista_2 = []
        self.lista_3 = []
        self.resultados = []

        # Crear entradas para las ecuaciones
        self.x_y_z(0, self.cont_valores)
        self.x_y_z(1, self.cont_valores)
        self.x_y_z(2, self.cont_valores)

        btn_resolver = Button(self, text="Resolver", command=self.resolver, bg="PeachPuff2", font=("Verdana", 12, "bold"))
        btn_resolver.grid(row=1, column=0, pady=10)

        btn_volver = Button(self, text="Volver", command=self.volver, bg="PeachPuff2", font=("Verdana", 12, "bold"))
        btn_volver.grid(row=4, column=0, pady=10)

        #Etiquetas para mostrar resultados
        self.crear_entradas_resultados()

    
    def crear_entradas_resultados(self):
        #Entry para mostrar resultados
        for i in range(3):
            fila_resultados = []

            for j in range(3):  #Para los coeficientes (columnas 0, 1, 2)
                entry_resultado = Entry(self.cont_resultados, font=("Verdana", 14), width=5, justify=CENTER)
                entry_resultado.config(bg="lightyellow", state='readonly')  
                entry_resultado.grid(row=i, column=j, padx=15,pady=5)
                fila_resultados.append(entry_resultado)  #Guarda los entries en la lista

            barra_vertical = Label(self.cont_resultados, text="|", font=("Verdana", 12), bg="PeachPuff2")
            barra_vertical.grid(row=i, column=3, padx=15, pady=5)

            entry_independiente = Entry(self.cont_resultados, font=("Verdana", 14), width=5, justify=CENTER)
            entry_independiente.config(bg="lightblue", state='readonly')  
            entry_independiente.grid(row=i, column=4, padx=15,pady=5)
            
            fila_resultados.append(entry_independiente)  #Agrega el término independiente a la fila

            self.resultados.append(fila_resultados)

    def validar(self, entrada):
        if entrada == "-" or entrada == ".":  
            return True
        try:
            float(entrada)
            return True
        except ValueError:
            return False

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
        Label(contenedor, text=" z =", font=("Verdana", 15), justify=CENTER, bg=color_fondo).grid(row=fila, column=7, pady=10)
        entry_r = Entry(contenedor, validate="key", validatecommand=(validacion, '%P'))
        entry_r.config(textvariable=r, font=("Verdana", 14), width=5, justify=CENTER)
        entry_r.grid(row=fila, column=8, pady=10)
        Label(contenedor, text=" ]", font=("Verdana", 15), justify=CENTER, bg=color_fondo).grid(row=fila, column=9, pady=10)

        #Guarda las referencias de las entradas en las listas
        if fila == 0:
            self.lista_1.extend([entry_x, entry_y, entry_z, entry_r])
        elif fila == 1:
            self.lista_2.extend([entry_x, entry_y, entry_z, entry_r])
        elif fila == 2:
            self.lista_3.extend([entry_x, entry_y, entry_z, entry_r])

    def resolver(self):
        try:
            #Lee los coeficientes y constantes
            A = []
            b = []

            for fila in [self.lista_1, self.lista_2, self.lista_3]:
                fila_coeficientes = [float(entry.get()) for entry in fila[:-1]]  #Coeficientes
                A.append(fila_coeficientes)
                b.append(float(fila[-1].get()))  #Término independiente
            
            # Aplicar el método de Gauss-Jordan
            self.gauss_jordan(A, b)
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa solo números válidos.")

    def gauss_jordan(self, A, b):
        n = len(A)       #Almacena el num de filas
        
        for i in range(n):
            #Verifica si el pivote es cero y busca otra fila para intercambiar
            if A[i][i] == 0:
                for j in range(i + 1, n):
                    if A[j][i] != 0:
                        A[i], A[j] = A[j], A[i]
                        b[i], b[j] = b[j], b[i]
                        
            #Verifica nuevamente después del intercambio
            if A[i][i] == 0:
                continue  #Si no hay un pivote válido en esta fila va a continuar itinerando

            #Se normaliza la fila dividiendo cada elemento de la fila por el valorde del pivote
            pivote = A[i][i]
            for j in range(n):
                A[i][j] /= pivote
            b[i] /= pivote

            #Hacer ceros en la columna del pivote.
            for j in range(n):
                if j != i:
                    factor = A[j][i]       #Calcula el factor usando el elemento de la fila que se quiere hacer 0
                    for k in range(n):
                        A[j][k] -= factor * A[i][k]       #Elemento - factor * fila del pivote
                    b[j] -= factor * b[i]
    
        #Verifica el tipo de sistema y mostrar resultados
        self.verificar_tipo_sistema(A, b)

    def verificar_tipo_sistema(self, A, b):
        n = len(A)
        tipo_sistema = "Sistema Compatible Determinado"

        for i in range(n):
            #Si la fila es [0, 0, 0 | != 0] es incompatible
            if all(A[i][j] == 0 for j in range(n)) and b[i] != 0:
                tipo_sistema = "Sistema Incompatible: No tiene solución."
                break
                #self.label_tipo_sistema.config(text=tipo_sistema)
                
                
            #Si la fila es [0, 0, 0 | 0] hay infinitas soluciones
            elif all(A[i][j] == 0 for j in range(n)) and b[i] == 0:
                tipo_sistema = "Sistema Compatible Indeterminado(SCI): Posee infinitas soluciones."
                break
                
        self.label_tipo_sistema.config(text=tipo_sistema)        
        self.label_tipo_sistema.grid() 

        #Si el sistema es compatible determinado, muestra los resultados
        if tipo_sistema == "Sistema Compatible Determinado":
            self.mostrar_resultado(A, b)

        #Muestra el tipo de sistema en la interfaz
            self.label_tipo_sistema.config(text=tipo_sistema)


    def mostrar_resultado(self, A, b):
        for i in range(3):
            for j in range(3):
                #Muestra la matriz transformada
                self.resultados[i][j].config(state=NORMAL)
                self.resultados[i][j].delete(0, END)
                self.resultados[i][j].insert(0, round(A[i][j], 2))
                self.resultados[i][j].config(state="readonly")
                
            #Muestra el vector de resultados
            self.resultados[i][3].config(state=NORMAL)
            self.resultados[i][3].delete(0, END)
            self.resultados[i][3].insert(0, round(b[i], 2))
            self.resultados[i][3].config(state="readonly")

        self.cont_resultados.grid()    
         
    def volver(self):
        for entradas in [self.lista_1, self.lista_2, self.lista_3]:
            for entry in entradas:
                entry.delete(0, END)
        self.cont_resultados.grid_remove()
        self.label_tipo_sistema.grid_remove()


'''ventana = Tk()
ventana.wm_title("Método Gauss-Jordan")
ventana.wm_resizable(0, 0)
entradas = GaussJordan(ventana)
entradas.mainloop()'''





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

            
