import random
import time
import matplotlib.pyplot as plt

def bubble_sort(lista):
    n = len(lista)

    for i in range(n):
        swap = False

        for j in range(0, n - i - 1):

            if lista[j] > lista[j + 1]:

                aux = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = aux

                swap = True

        if swap == False:
            break

    return lista


def selection_sort(lista):
    n = len(lista)

    for i in range(n):

        min_idx = i

        for j in range(i + 1, n):

            if lista[min_idx] > lista[j]:
                min_idx = j

        aux = lista[i]
        lista[i] = lista[min_idx]
        lista[min_idx] = aux

    return lista

def insertion_sort(lista):
    n = len(lista)
    for i in range(1, n):
        actual = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > actual:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = actual
    return lista

def quick_sort(lista):
    if len(lista) <= 1: #se fija que el largo de la lista sea mayor a 1
        return lista
    pivote = lista[0] #elije el numero pivote, en este caso el primero
    menores = [] # crea 2 listas en memoria para aplicar recursividad
    mayores = []
    for i in range(1, len(lista)): #agarra toda la lista y la divide en las listas en memoria menores y mayores
        if lista[i] < pivote: #para eso compara con el num pivot, sies mayor se agrega a mayores si es menor a menores
            menores.append(lista[i])
        else:
            mayores.append(lista[i])
    return quick_sort(menores) + [pivote] + quick_sort(mayores)#aplica quicksort a estas nuevas listas y las printea los menores a la izq,luego el pivot y luego los mayores



tamaños = list(range(100, 1000, 100))

tiempos_bubble = []
tiempos_selection = []
tiempos_insertion = []
tiempos_quick =[]

repeticiones = 5

for n in tamaños:

    total_bubble = 0
    total_selection = 0
    total_insertion = 0
    total_quick= 0

    for _ in range(repeticiones):

        lista_original = random.sample(range(n * 2), n)

        # Bubble Sort

        lista_bubble = lista_original.copy()
        inicio = time.perf_counter()
        bubble_sort(lista_bubble)
        fin = time.perf_counter()
        total_bubble += (fin - inicio)

        # Selection Sort

        lista_selection = lista_original.copy()
        inicio = time.perf_counter()
        selection_sort(lista_selection)
        fin = time.perf_counter()
        total_selection += (fin - inicio)

        #Insertion sort
        lista_insertion = lista_original.copy()
        inicio = time.perf_counter()
        insertion_sort(lista_insertion)
        fin = time.perf_counter()
        total_insertion += (fin - inicio)
        
        #quick sort
        lista_quick=lista_original.copy()
        inicio = time.perf_counter()
        quick_sort(lista_quick)
        fin = time.perf_counter()
        total_quick += (fin-inicio)

    tiempos_bubble.append(total_bubble / repeticiones)
    tiempos_selection.append(total_selection / repeticiones)
    tiempos_insertion.append(total_insertion / repeticiones)
    tiempos_quick.append(total_quick/repeticiones)


plt.figure(figsize=(10,5))
plt.plot(tamaños, tiempos_bubble, label="Bubble Sort")
plt.plot(tamaños, tiempos_selection, label="Selection Sort")
plt.plot(tamaños, tiempos_insertion, label="Insertion Sort")
plt.plot(tamaños, tiempos_quick, label="quick Sort")

plt.title("Comparación de algoritmos de ord")
plt.xlabel("Tamaño de la lista")
plt.ylabel("Tiempo (segundos)")
plt.legend()
plt.grid()
plt.show()