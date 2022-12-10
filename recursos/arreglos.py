import numpy
import numpy as np

def print_menu():  ## Diseño del menu
    print (30 * "-", "MENU", 30 * "-")
    print ("1. Rellenar arreglo multidimensional")
    print ("2. Eliminar fila del arreglo")
    print ("3. Eliminar columna del arreglo")
    print ("4. Reemplazar elemento del arreglo")
    print ("5. Cerrar programa")
    print (67 * "-")

loop = True ## Definimos la variable loop que sera usada como condicion para la ejecucion del programa

while loop:  ## Este loop seguira ejecutandose hasta que loop = false
    print_menu()  ## Imprimimos el menu
    choice = int(input("Ingrese una opcion del [1-5]: "))

    if choice == 1: ## Esta opcion pide al usuario las dimensiones de la matriz y los elementos de la misma.
        print ("Opcion 1 seleccionada")
        n_filas = int(input("Ingrese numero de filas:"))
        n_columnas = int(input("Ingrese numero de columnas:"))
        matriz = []
        for i in range(n_filas):
            a = []
            for j in range(n_columnas):
                val=int(input("Ingrese el valor:"))
                a.append(val)
            matriz.append(a)
        matrizOrdenada = numpy.array(matriz)
        print((matrizOrdenada))

    elif choice == 2: ## Esta opcion elimina una fila seleccionada por el usuario.
        print ("Opcion 2 seleccionada - Eliminar fila")
        n_filas = int(input("Ingrese la fila que desea eliminar:"))
        matrizOrdenada = np.delete(matrizOrdenada, n_filas, axis=0)
        print(matrizOrdenada)

    elif choice == 3: ## Esta opcion elimina una columna seleccionada por el usuario.
        print ("Opcion 3 seleccionada - Eliminar columna")
        n_columnas = int(input("Ingrese la columna que desea eliminar:"))
        matrizOrdenada = np.delete(matrizOrdenada, n_columnas, axis=1)
        print(matrizOrdenada)

    elif choice == 4:
        print ("Opcion 4 - Reemplazar elemento")
        n_filas = int(input("Ingrese numero de filas:"))
        n_columnas = int(input("Ingrese numero de columnas:"))
        v =  int(input("Ingrese el valor:"))
        matrizOrdenada[n_filas, n_columnas] = v
        print(matrizOrdenada)

    elif choice == 5:
        print ("Opcion 5 - Finalizar programa")
        loop = False  # Cargamos el valor False en loop lo cual es nuestra condicion para terminar el loop
    else:
        ## Si el input seleccionado no es del 1 al 5, se despliega un error y se vuelve a solicitar el input
        print ("Opcion incorrecta. Seleccione una opcion del [1-5]")
