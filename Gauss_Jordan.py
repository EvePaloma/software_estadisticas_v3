def gaussJordan(matriz):
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
    tipo_sistema = determinar_tipo_sistema(resultado)
    print(f"\nEl sistema es: {tipo_sistema}")
    
    if tipo_sistema == "Compatible determinado":
        mostrar_matriz(resultado)  # Mostrar la matriz sin las soluciones
        mostrar_soluciones(resultado)  # Mostrar las soluciones separadas

            
