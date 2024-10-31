from tkinter import *
from tkinter import messagebox

class GaussJordan(Frame):
    def __init__(self, master=None):
        super().__init__(master, width=1350, height=700, bg="#ba5954")
        self.master = master
        self.pack_propagate(False) 
        self.pack(expand=True)
        self.interfaz()
        self.resultados = []
        self.activado = False
        self.master.protocol("WM_DELETE_WINDOW", lambda: None)

    def volver_menu(self):
        from inicio import MENU
        self.master.destroy()
        ventana = Tk()
        ventana.wm_title("Menú software estadísticas")
        ventana.wm_resizable(0,0)
        menu = MENU(ventana)
        menu.mainloop()

    def validar(self, entrada):
        if entrada == "-" or entrada == "." or entrada == "":  
            return True
        try:
            float(entrada)
            return True
        except ValueError:
            return False

    def resolver(self):
        try:
            #Almacena los coeficientes y el término independiente en listas
            A = []
            b = []
            #Recorre las filas de las entradas para obtener los valores
            for fila in [self.lista_1, self.lista_2, self.lista_3]:
                #Obtiene los valores de los coeficientes y los convierte a float
                fila_coeficientes = [float(entry.get()) for entry in fila[:-1]]  #Coeficientes
                A.append(fila_coeficientes)
                b.append(float(fila[-1].get()))  #Término independiente
            
            #Aplica el método 
            self.gauss_jordan(A, b)
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa solo números válidos.")

    def limpiar(self):
        #Limpia los valores de las entradas
        for fila in [self.lista_1, self.lista_2, self.lista_3]:
            for entry in fila:
                entry.delete(0, END)
        
        #Se reinician las listas de resultados
        self.resultados = []
        self.activado = False

        self.label_tipo_sistema.config(text="")  
        if hasattr(self, 'cont_rta'):          #Oculta el contenedor de resultados
            self.cont_rta.pack_forget() 

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

            #Guarda el valor del pivote
            pivote = A[i][i]
            #Se normaliza la fila dividiendo cada elemento de la fila por el valorde del pivote
            for j in range(n):
                A[i][j] /= pivote
            b[i] /= pivote

            #Hacer ceros en la columna del pivote.
            for j in range(n):
                #Para cada fila diferente de la fila del pivote
                if j != i:
                    #Factor=elemento
                    factor = A[j][i]       #Se calcula un factor, usando el elemento de la fila que se quiere hacer 0
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
                
            #Si la fila es [0, 0, 0 | 0] hay infinitas soluciones
            elif all(A[i][j] == 0 for j in range(n)) and b[i] == 0:
                tipo_sistema = "Sistema Compatible Indeterminado(SCI): Posee infinitas soluciones."
                break
                
        self.label_tipo_sistema.config(text=tipo_sistema)        
        self.label_tipo_sistema.pack() 

        #Si el sistema es compatible determinado, muestra los resultados
        if tipo_sistema == "Sistema Compatible Determinado":
            self.mostrar_resultado(A, b)

    def crear_entradas_resultados(self):
        self.cont_rta = Frame(self.cont_resultados, bg="PeachPuff2")
        self.cont_rta.pack_forget()
        self.resultados = []
        #Entry para mostrar resultados
        for i in range(3):
            fila_resultados = []

            for j in range(3):  #Para los coeficientes (columnas 0, 1, 2)
                entry_resultado = Entry(self.cont_rta, font=("Robot", 14), width=5, justify=CENTER)
                entry_resultado.config(bg="lightyellow", state='readonly')  
                entry_resultado.grid(row=i, column=j, padx=15,pady=5)
                fila_resultados.append(entry_resultado)  #Guarda los entries en la lista

            barra_vertical = Label(self.cont_rta, text="|", font=("Robot", 12), bg="PeachPuff2")
            barra_vertical.grid(row=i, column=3, padx=15, pady=5)

            entry_independiente = Entry(self.cont_rta, font=("Robot", 14), width=5, justify=CENTER)
            entry_independiente.config(bg="lightblue", state='readonly')  
            entry_independiente.grid(row=i, column=4, padx=15,pady=5)
            
            fila_resultados.append(entry_independiente)  #Agrega el término independiente a la fila

            self.resultados.append(fila_resultados)  #Guarda la fila en la lista de resultados

    def mostrar_resultado(self, A, b):
        self.crear_entradas_resultados()
        resultados_xyz = []
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
            resultados_xyz.append((self.resultados[i][3].get()))
        
        texto = "x = {}   y = {}   z = {}".format(*resultados_xyz)
        Label(self.cont_rta, text= texto, font=("Robot", 14), bg="PeachPuff2").grid(row=3, column=0, columnspan=5, pady=10)
        self.cont_rta.pack(pady=15)

    def interfaz(self):
        #valores usados
        self.color_fondo = "#e0cbc1"
        validacion = self.register(self.validar)
        #contenedor de todo
        self.cont_total= Label(self, bg="#e0cbc1", width= 1100, height=680)
        self.cont_total.pack(pady= 70, ipadx=20, ipady=20) 
        #contenedor ingresos
        self.cont_valores = Frame(self.cont_total, width=800, height=200, bg="#e0cbc1")
        self.cont_valores.pack_propagate(False)
        self.cont_valores.pack()
        cont_f1 = Frame(self.cont_valores, bg="#e0cbc1")
        cont_f1.grid(row=0, column=0)
        cont_f2 = Frame(self.cont_valores, bg="#e0cbc1")
        cont_f2.grid(row=1, column=0)
        cont_f3 = Frame(self.cont_valores, bg="#e0cbc1")
        cont_f3.grid(row=2, column=0)
        #contenedor resultados
        self.cont_resultados = Frame(self.cont_total, width=700, height=200, bg="#ffe0cf")
        self.cont_resultados.pack_propagate(False)
        self.cont_resultados.pack(expand=True)
        #self.crear_entradas_resultados()
        #contenedor botones
        self.cont_botones = Frame(self.cont_total, width=800, height=100, bg="#e0cbc1")
        self.cont_botones.pack(pady= 12)

        #INGRESO DE LOS VALORES
        #Listas para almacenar las entradas
        self.lista_1 = []
        self.lista_2 = []
        self.lista_3 = []

        #Primera fila de los ingresos
        Label(cont_f1, text= "⌈ ", font=("Robot", 18), justify=CENTER, bg=self.color_fondo).grid(row= 0, column=1, pady=12)
        self.entry_x1 = Entry(cont_f1, validate="key", validatecommand=(validacion, '%P'))
        self.entry_x1.config(font=("Robot", 14), width=5, justify=CENTER)
        self.entry_x1.grid(row= 0, column=2, pady=10)
        Label(cont_f1, text=" x + ", font=("Robot", 15), justify=CENTER, bg=self.color_fondo).grid(row= 0, column=3, pady=10)
        self.entry_y1 = Entry(cont_f1, validate="key", validatecommand=(validacion, '%P'))
        self.entry_y1.config(font=("Robot", 14), width=5, justify=CENTER)
        self.entry_y1.grid(row= 0, column=4, pady=10)
        Label(cont_f1, text=" y + ", font=("Robot", 15), justify=CENTER, bg=self.color_fondo).grid(row= 0, column=5, pady=10)
        self.entry_z1 = Entry(cont_f1, validate="key", validatecommand=(validacion, '%P'))
        self.entry_z1.config(font=("Robot", 14), width=5, justify=CENTER)
        self.entry_z1.grid(row= 0, column=6, pady=10)
        Label(cont_f1, text=" z =", font=("Robot", 15), justify=CENTER, bg=self.color_fondo).grid(row= 0, column=7, pady=10)
        self.entry_r1 = Entry(cont_f1, validate="key", validatecommand=(validacion, '%P'))
        self.entry_r1.config(font=("Robot", 14), width=5, justify=CENTER)
        self.entry_r1.grid(row= 0, column=8, pady=10)
        Label(cont_f1, text=" ⌉", font=("Robot", 18), justify=CENTER, bg=self.color_fondo).grid(row= 0, column=9, pady=10)
        self.lista_1.extend([self.entry_x1, self.entry_y1, self.entry_z1, self.entry_r1])

        #Segunda fila de los ingresos
        Label(cont_f2, text="|  ", font=("Robot", 17), justify=CENTER, bg=self.color_fondo).grid(row= 0, column=1, pady=12)
        self.entry_x2 = Entry(cont_f2, validate="key", validatecommand=(validacion, '%P'))
        self.entry_x2.config(font=("Robot", 14), width=5, justify=CENTER)
        self.entry_x2.grid(row= 0, column=2, pady=10)
        Label(cont_f2, text=" x + ", font=("Robot", 15), justify=CENTER, bg=self.color_fondo).grid(row= 0, column=3, pady=10)
        self.entry_y2 = Entry(cont_f2, validate="key", validatecommand=(validacion, '%P'))
        self.entry_y2.config(font=("Robot", 14), width=5, justify=CENTER)
        self.entry_y2.grid(row= 0, column=4, pady=10)
        Label(cont_f2, text=" y + ", font=("Robot", 15), justify=CENTER, bg=self.color_fondo).grid(row= 0, column=5, pady=10)
        self.entry_z2 = Entry(cont_f2, validate="key", validatecommand=(validacion, '%P'))
        self.entry_z2.config(font=("Robot", 14), width=5, justify=CENTER)
        self.entry_z2.grid(row= 0, column=6, pady=10)
        Label(cont_f2, text=" z =", font=("Robot", 15), justify=CENTER, bg=self.color_fondo).grid(row= 0, column=7, pady=10)
        self.entry_r2 = Entry(cont_f2, validate="key", validatecommand=(validacion, '%P'))
        self.entry_r2.config(font=("Robot", 14), width=5, justify=CENTER)
        self.entry_r2.grid(row= 0, column=8, pady=10)
        Label(cont_f2, text="  |", font=("Robot", 17), justify=CENTER, bg=self.color_fondo).grid(row= 0, column=9, pady=10)
        self.lista_2.extend([self.entry_x2, self.entry_y2, self.entry_z2, self.entry_r2])

        #Tercera fila de los ingresos
        Label(cont_f3, text="⌊ ", font=("Robot", 18), justify=CENTER, bg=self.color_fondo).grid(row= 0, column=1, pady=12)
        self.entry_x3 = Entry(cont_f3, validate="key", validatecommand=(validacion, '%P'))
        self.entry_x3.config(font=("Robot", 14), width=5, justify=CENTER)
        self.entry_x3.grid(row= 0, column=2, pady=10)
        Label(cont_f3, text=" x + ", font=("Robot", 15), justify=CENTER, bg=self.color_fondo).grid(row= 0, column=3, pady=10)
        self.entry_y3 = Entry(cont_f3, validate="key", validatecommand=(validacion, '%P'))
        self.entry_y3.config(font=("Robot", 14), width=5, justify=CENTER)
        self.entry_y3.grid(row= 0, column=4, pady=10)
        Label(cont_f3, text=" y + ", font=("Robot", 15), justify=CENTER, bg=self.color_fondo).grid(row= 0, column=5, pady=10)
        self.entry_z3 = Entry(cont_f3, validate="key", validatecommand=(validacion, '%P'))
        self.entry_z3.config(font=("Robot", 14), width=5, justify=CENTER)
        self.entry_z3.grid(row= 0, column=6, pady=10)
        Label(cont_f3, text=" z =", font=("Robot", 15), justify=CENTER, bg=self.color_fondo).grid(row= 0, column=7, pady=10)
        self.entry_r3 = Entry(cont_f3, validate="key", validatecommand=(validacion, '%P'))
        self.entry_r3.config(font=("Robot", 14), width=5, justify=CENTER)
        self.entry_r3.grid(row= 0, column=8, pady=10)
        Label(cont_f3, text=" ⌋", font=("Robot", 18), justify=CENTER, bg=self.color_fondo).grid(row= 0, column=9, pady=10)
        self.lista_3.extend([self.entry_x3, self.entry_y3, self.entry_z3, self.entry_r3])

        #boton resolver
        cont_resolver = Frame(self.cont_valores, bg="#e0cbc1")
        cont_resolver.grid(row=3, column=0, pady=15)
        btn_resolver = Button(cont_resolver, text="Resolver", command=self.resolver, bg="#d1867d", font=("Robot", 13, "bold"), width=12)
        btn_resolver.pack(expand=True)

        #MUESTRA DE LOS VALORES DE RESULTADO
        #Etiqueta para mostrar el tipo de sistema
        self.label_tipo_sistema = Label(self.cont_resultados, text="", font=("Robot", 14), bg="#ffe0cf", activebackground= "#ee9388")
        self.label_tipo_sistema.pack_forget()
        self.label_tipo_sistema.pack()

        #botones volver y limpiar
        btn_volver = Button(self.cont_botones, text="Volver", command=self.volver_menu, bg="#d1867d", activebackground= "#ee9388", font=("Robot", 13, "bold"), width=12)
        btn_volver.grid(row=0, column=0, padx=15)
        btn_limpiar = Button(self.cont_botones, text="Limpiar",command= self.limpiar, bg="#d1867d", activebackground= "#ee9388", font=("Robot", 13, "bold"), width=12)
        btn_limpiar.grid(row=0, column=1, padx=15)

"""ventana = Tk()
ventana.wm_title("Método Gauss-Jordan")
ventana.wm_resizable(0, 0)
ventana.geometry("+0+0")
entradas = GaussJordan(ventana)
entradas.mainloop()"""
