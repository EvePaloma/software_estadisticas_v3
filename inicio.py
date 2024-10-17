from tkinter import messagebox
from tkinter import *
from Grafico_Intervalo import*
from Gauss_Jordan import *

class MENU(Frame):
    def __init__(self, master = None):
        super().__init__(master, width = 1100, height = 600, bg = "#b191b3")
        self.master = master
        self.pack_propagate(False) 
        self.pack(expand=True)
        self.menu()
        self.master.state('zoomed')
        
    def mostrar_grafico(self):
        ventana = Tk()
        ventana.wm_title("Cálculo de Área")
        ventana.wm_resizable(0,0)
        ventana.wm_geometry("+0+0")
        entradas = INTERVALOS(ventana)
        entradas.mainloop()

    def mostrar_gauss(self):
        ventana = Tk()
        ventana.wm_title("Método de Gauss-Jordan")
        ventana.wm_resizable(0,0)
        ventana.wm_geometry("+150+50")
        entradas = GaussJordan(ventana)
        entradas.mainloop()

    def menu(self):
        color = "#b191b3"
        borde = Frame(self, width= 900, height= 500, bg= color)
        borde.pack_propagate(False)
        borde.pack(fill='both',expand=True, padx= 15, pady=15)
        
        cont_texto = Frame(borde, bg="#c9adcb", height= 100, width= 500)
        cont_texto.pack(fill='x')
        cont_botones = Frame(borde, bg= "#c9adcb", height= 400, width= 500)
        cont_botones.pack(fill='both', expand=True)

        Label(cont_texto, text="Menú", font=("Verdana", 20),bg="#c9adcb").pack()
        Label(cont_texto, text="Seleccione que desea utilizar", font=("Verdana", 17),bg="#c9adcb").pack()

        boton_grafico= Button(cont_botones, text="Gráfico de Intervalos", justify= CENTER, font=("Verdana", 15),bg="#ede3ee", width= 20, height= 5, command= self.mostrar_grafico)
        boton_grafico.pack(pady=40)

        boton_gauss= Button(cont_botones, text="Método de Gauss-Jordan", justify= CENTER, font=("Verdana", 15),bg="#ede3ee", width= 20, height= 5, command= self.mostrar_gauss)
        boton_gauss.pack(pady=40)

if __name__ == "__main__":
    ventana = Tk()
    ventana.wm_title("Menú software estadísticas")
    ventana.wm_resizable(0,0)
    menu = MENU(ventana)
    menu.mainloop()