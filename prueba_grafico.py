"""import numpy as np
import matplotlib.pyplot as plot
import tkinter as tk
import math

ventana = tk.Tk()
ventana.title("Contador Decreciente")
ventana.geometry("700x500")
ventana.resizable(False, False)
ventana.configure(bg="PeachPuff4")

def funcion_cuad(a, b, c, x):
    #Función integral, ingresan los datos que de el usuario, el usuario ingresa los multiplicadores de x, x y el num
    y = a * (x**2) + b * x + c
    return (y)

x = np.array(range(500))*0.1
y = np.zeros(len(x))

for i in range(len(x)):
    y[i] = math.sin(x[i])

# Creamos el gráfico
plot.ion()
plot.plot(x,y)

ventana.mainloop()"""

import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Función para mostrar el gráfico en la interfaz
def crear_grafico():
    # Generar algunos datos usando numpy
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    # Crear una figura de Matplotlib
    fig, ax = plt.subplots()
    ax.plot(x, y)

    # Añadir el gráfico a la ventana de Tkinter usando FigureCanvasTkAgg
    canvas = FigureCanvasTkAgg(fig, master=ventana)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Gráficos en Tkinter con Matplotlib")
ventana.geometry("600x400")

# Botón para generar el gráfico
boton = ttk.Button(ventana, text="Generar Gráfico", command=crear_grafico)
boton.pack()

# Ejecutar la ventana
ventana.mainloop()

