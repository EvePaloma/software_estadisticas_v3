from tkinter import messagebox
from tkinter import *
from Gauss_Jordan import *

class MENU(Frame):
    def __init__(self, main = None):
        super().__init__(main, width = 1200, height = 700, bg = "#b191b3")
        self.main = main
        self.pack_propagate(False) 
        self.pack(expand=True, fill='both')
        self.menu()
        self.main.state('zoomed')
        
    def mostrar_grafico(self):
        from Grafico_Intervalo import INTERVALOS
        self.main.destroy()
        ventana = Tk()
        ventana.wm_title("Cálculo de Área")
        ventana.wm_resizable(0,0)
        ventana.wm_geometry("+0+0")
        entradas = INTERVALOS(ventana)
        entradas.mainloop()

    def mostrar_gauss(self):
        from Gauss_Jordan import GaussJordan
        self.main.destroy()
        ventana = Tk()
        ventana.wm_title("Método de Gauss-Jordan")
        ventana.wm_resizable(0,0)
        ventana.wm_geometry("+0+0")
        entradas = GaussJordan(ventana)
        entradas.mainloop()

    def menu(self):
        color = "#b191b3"
        borde = Frame(self, bg= color, height= 600, width= 1000)
        borde.pack_propagate(False)
        borde.pack(expand=True, padx= 40, pady=40)
        #"#c9adcb"
        cont_texto = Frame(borde, bg= "#c9adcb", height= 200, width= 500)
        cont_texto.pack(fill='both', expand=True)
        cont_botones = Frame(borde, bg= "#c9adcb", height= 400, width= 500)
        cont_botones.pack(fill='both', expand=True)

        Label(cont_texto, text="", font=("Verdana", 2),bg="#c9adcb").pack(ipady= 20) #label colocado para poder separar el texto del borde, no supe que más ponerle
        Label(cont_texto, text="Menú", font=("Verdana", 20),bg="#c9adcb").pack()
        Label(cont_texto, text="Seleccione que desea utilizar", font=("Verdana", 17),bg="#c9adcb").pack()

        boton_grafico= Button(cont_botones, text="Gráfico de Área", justify= CENTER, font=("Verdana", 15),bg="#ede3ee", width= 20, height= 5, command= self.mostrar_grafico)
        boton_grafico.pack(pady=40)

        boton_gauss= Button(cont_botones, text="Método de Gauss-Jordan", justify= CENTER, font=("Verdana", 15),bg="#ede3ee", width= 20, height= 5, command= self.mostrar_gauss)
        boton_gauss.pack(pady=40)

if __name__ == "__main__":
    ventana = Tk()
    ventana.wm_title("Menú software estadísticas")
    ventana.wm_resizable(0,0)
    menu = MENU(ventana)
    menu.mainloop()