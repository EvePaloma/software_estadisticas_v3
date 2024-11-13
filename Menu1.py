from Funciones import *
from Funciones1 import *

while True:
    print("**********************************************")
    print("****      ESTADÍSTICA DESCRIPTIVA Y       ****")
    print("****      PROBABILIDAD Y ESTADÍSTICA      ****")
    print("**********************************************")

    print("\n* Seleccione el módulo que desea utilizar:")
    
    print("\n1 = Estadística Descriptiva")
    print("2 = Probabilidad y Estadística")
    print("3 = Salir")
    seleccion = input("* Ingrese el número de su opción: ")

    if seleccion == "1":
        print("Ha seleccionado Estadística Descriptiva.")
        # Estas lineas son las que permiten que el usuario ingrese los datos, los cuales se almacenan en una lista, la cual se ordena de menor a mayor, y solo permite valores numéricos.
        lista_muestras = []
        lista_muestras = AGREGAR_ELEMENTOS_INPUT(lista_muestras)
        numero_muestra = len(lista_muestras)
        #En pantalla se imprime la lista de los elementos dados por el usuario y la cantidad de elementos que se ingresaron
        print("Muestra: ", lista_muestras)
        print("Cantidad de datos: ", numero_muestra)
        
        # Este es el main del código, aca se ejecuta todo el programa y se hacen las llamadas al documento "Funciones", del cual extraemos las funciones necesarias   
        while True: #Este while le permite al usuario utilizar tantas veces quiera las opciones que se ofrecen
            #La variable respuesta le permite al usuario escribir el valor de que tipo de informacion desea recibir de la lista de muestras
            respuesta = input("¿Que medidas desea conocer? \n1 = MEDIDAS DE POSICIÓN \n2 = MEDIDAS DE DISPERCIÓN \n3 = FRECUENCIAS \n4 = Volver a menú principal. \n ==> ")
            if int(respuesta) == 1:
                print("Seleccionaste < Medidas de Posición >")
                resultado = MEDIDAS_POSICION(lista_muestras)
            elif int(respuesta) == 2:
                print("Seleccionaste < Medidas de Disperción >")
                resultado = MEDIDAS_DISPERCION(lista_muestras)
            elif int(respuesta) == 3:
                print("Seleccionaste < Frecuencias >")
                resultado = TABLAS_FRECUENCIAS(lista_muestras)
            elif int(respuesta) == 4:
                break
            else:
                print("Comando no válido, intente de nuevo")

    elif seleccion == "2":
        print("\n* Ha seleccionado Probabilidad y Estadísticas")
        print("* Seleccione qué distribución quiere calcular.")
        while True:
            print("\nSeleccion de funcion a probar:")
            print("1. Calcular Probabilidad Binomial")
            print("2. Calcular Probabilidad Hipergeométrica")
            print("3. Poisson.")
            print("4. Coeficiente de Curtosis")
            print("5. Normal o Gaussiana")
            print("6. Salir.")

            opcion = input("Ingrese una opción: ")

            if opcion == "1":
                print("Probabilidad Binomial")
                n = val_numeros("Ingrese el número de ensayos (n): ", True)
                p = val_numeros("Ingrese la probabilidad de éxito (entre 0 y 1) (p): ", False)
                while p < 0 or p > 1:
                    print("Error. La probabilidad p debe estar entre 0 y 1.")
                    p = val_numeros("Ingrese la probabilidad de éxito (entre 0 y 1) (p): ", False)
                
                print("En caso de ser un solo caso, poner el mismo número en ambos limites")
                limiteI = val_numeros("Ingrese el valor mínimo de éxitos k: ", True)
                limiteS = val_numeros("Ingrese el valor máximo de éxitos k: ", True)
                while limiteI > limiteS or limiteS > n:
                    print("Error. El límite inferior debe ser menor o igual al límite superior.")
                    limiteI = val_numeros("Ingrese el valor mínimo de éxitos k: ", True)
                    limiteS = val_numeros("Ingrese el valor máximo de éxitos k: ", True)
                print(f"Probabilidad Binomial en el rango [{limiteI}, {limiteS}] es: {probabilidad_binomial(n, p, limiteI, limiteS)}")
            
            elif opcion == "2":
                print("Probabilidad Hipergeométrica")
                N = val_numeros("Ingrese el tamaño de la población (N): ", True)
                M = val_numeros("Ingrese el número de éxitos en la población (M): ", True)
                while M > N:
                    print("Error: M (éxitos en la población) no puede ser mayor que N (tamaño de la población).")
                    M = val_numeros(f"Ingrese un valor para M (menor o igual a {N}): ", True)
                n = val_numeros("Ingrese el tamaño de la muestra (n): ", True)
                while n > N:
                    print("Error: n (tamaño de la muestra) no puede ser mayor que N.")
                    n = val_numeros(f"Ingrese un valor para n (menor o igual a {N}): ", True)
                limiteI = val_numeros("Ingrese el valor mínimo de éxitos k: ", True)
                limiteS = val_numeros("Ingrese el valor máximo de éxitos k: ", True)
                while limiteI > limiteS or limiteI < 0 or limiteS > n or limiteS > M:
                    print("Error. El límite inferior debe ser menor o igual al límite superior.")
                    limiteI = val_numeros("Ingrese el valor mínimo de éxitos k: ", True)
                    limiteS = val_numeros("Ingrese el valor máximo de éxitos k: ", True)
                print(f"Probabilidad Hipergeométrica en el rango [{limiteI}, {limiteS}] es: {probabilidad_hipergeometrica(N, M, n, limiteI, limiteS)}")    

            elif opcion == "3":
                print("Poisson")
                print("Recuerde que la probabilidad de ocurrencia debe ser un numero entero mayor que 0")
                #Se ingresa el valor de lamda, o lo que se espera
                cantidad = val_numeros("Promedio de ocurrencias en x intervalo (lamda): ", False)
                print("Ingrese la probabilidad de ocurrencia de cuales casos quiere calcular. ejemplo; que ingresen desde 2 hasta 4 personas.")
                print("En caso de ser un solo caso, poner el mismo número en ambos límites.")
                #Definimos los límites. si es un solo número, se pone lo mismo en ambos.
                limiteI = val_numeros("Valor mínimo \nx = ", True)
                limiteF = val_numeros("Valor máximo \nx = ", True)
                while limiteI > limiteF:
                    print("Error. El límite inferior debe ser menor o igual al límite superior.")
                    limiteI = val_numeros("Valor mínimo \nx = ", True)
                    limiteF = val_numeros("Valor máximo \nx = ", True) 
                resultado = 0
                for i in range(limiteI, limiteF + 1):
                    resultado += Poisson(cantidad, i)
                    print(f"La probabilidad de Poisson para x = {i} es: {round(Poisson(cantidad, i), 4)}")
                print(f"El resultado es: ", round(resultado, 4)) 
        
            elif opcion == "4":
                print("Coeficiente de Curtosis")
                def input_float_list(prompt):
                    while True:
                        try:
                            # Tomamos la entrada del usuario y convertimos a lista de flotantes
                            datos = list(map(float, input(prompt).split()))
                            return datos
                        except ValueError:
                            print("Error: Ingrese solo números separados por espacios.")
                
                datos = input_float_list("Ingrese los datos separados por espacios: ")
                while len(datos) < 4:
                    print("No se puede calcular la curtosis con menos de 4 datos.")
                    datos = input_float_list("Ingrese los datos separados por espacios: ")
                    break
                while len(set(datos)) == 1:
                    print("No se puede calcular la curtosis si todos los datos son iguales.")
                    datos = input_float_list("Ingrese los datos separados por espacios: ")

                curtosis_redondeada, tipo_curtosis = calcular_curtosis(datos)
                print("\nEl coeficiente de curtosis es: ",curtosis_redondeada," y según su resultado es,", tipo_curtosis)

            elif opcion == "5":
                print("Distribución Normal o Gaussiana")
                # Solicitar los parámetros al usuario
                mu_original = val_numeros("Ingrese la media/mu (μ) de la distribución: ",False)
                while True:
                    sigma_original =val_numeros("Ingrese la desviación estándar/sigma (σ) de la distribución: ",False)
                    if sigma_original == 0:
                        print("La desviación estandar o sigma no pude ser igual a 0")
                    else:
                        break
                #Se solicitan los limites para luego estandarizar y calcular la integral
                while True:
                    a = input("Ingrese el límite inferior (a) de integración: ")
                    try:
                        valor = float(a)
                        a = valor
                    except:
                        print("Ingrese valores numéricos")   

                    b = input("Ingrese el límite superior (b) de integración: ")
                    try:
                        valor = float(b)
                        b = valor
                    except:
                        print("Ingrese valores numéricos")   
                    if a>b:
                        print("El limite inferior no pude ser mayor al superior. Ingrese nuevamente los datos.")
                    if a==b:
                        print("El limite inferior y el limite superior no pueden ser iguales. Ingrese nuevamente los datos.")
                    else:
                        resultado_normal=calcular_integral_gaussiana(mu_original, sigma_original, a, b)
                        print(f"La Normal o Gaussiana es: {resultado_normal}")
                        break

            elif opcion == "6":
                print("Volver al menú principal.")
                break
            else:          
                print("Ingrese una opción válida. Intente de nuevo.")
    else:
        print("Opcion no valida. Intente de nuevo.")
            

