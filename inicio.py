from tkinter import messagebox
from tkinter import *
from Grafico_Intervalo import*

class MENU(Frame):
    def __init__(self, master = None):
        super().__init__(master, width = 950, height = 600, bg = "DeepSkyBlue4")
        self.master = master
        self.pack_propagate(False) 
        self.pack(expand=True)
        self.menu()

    def mostrar_grafico(self):
        self.master.destroy()
        ventana = Tk()
        ventana.wm_title("Grafico de Intervalos")
        #ventana.wm_resizable(0,0)
        entradas = INTERVALOS(ventana)
        entradas.mainloop()

    def menu(self):
        color = "PaleTurquoise3"
        borde = Frame(self, width= 800, height= 500, bg= color)
        borde.pack_propagate(False)
        borde.pack(expand=True, padx= 15, pady=15)
        
        cont_texto = Frame(borde, bg="red", height= 100, width= 500)
        cont_texto.pack()
        cont_botones = Frame(borde, bg= "White", height= 400, width= 500)
        cont_botones.pack()

        Label(cont_texto, text="Menú", font=("Verdana", 20)).pack()
        Label(cont_texto, text="Seleccione que desea utilizar", font=("Verdana", 17)).pack()

        boton_grafico= Button(cont_botones, text="Gráfico de Intervalos", justify= CENTER, font=("Verdana", 15), width= 20, height= 5, command= self.mostrar_grafico)
        boton_grafico.pack()


ventana = Tk()
ventana.wm_title("Menú software estadísticas")
#ventana.wm_resizable(0,0)
entradas = MENU(ventana)
entradas.mainloop()