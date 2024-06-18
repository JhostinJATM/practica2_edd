import sys
import random 
import time 
from tabulate import tabulate

sys.path.append('../')
from controller.tda.linked.linkedList import LinkedList

if __name__ == "__main__":
    
    lista = LinkedList()
        
    for i in range(30):
        lista.add(random.randint(0, 10))
    print(f"Lista orginal: {lista}")
    
    # for i in range(10000):
    #     lista.add(random.randint(0, 1000))
    # print(f"Lista orginal: {lista}")
    
    # for i in range(20000):
    #     lista.add(random.randint(0, 20000))
    # print(f"Lista orginal: {lista}")

    # for i in range(25000):
    #     lista.add(random.randint(0, 2500))
    # print(f"Lista orginal: {lista}")


    # Ordenar la lista con Quick Sort
    lista_ordenada = lista.quick_numbers(1)
    
    # Obtener un número aleatorio de la lista
    random_number = random.choice(lista_ordenada.toArray)

    print(f"Lista ordenada: {lista_ordenada}\n")

    # Imprimir el número aleatorio obtenido
    print(f"\n\nNúmero aleatorio de la lista: {random_number}")
    
    start_time = time.time()
    valor_encontrado = lista_ordenada.busqueda_secuencial_lineal(random_number)
    end_time = time.time()
    print(f"\n\nValor encontrado: {valor_encontrado}")

    start_time2 = time.time()
    valores_encontrados = lista_ordenada.busqueda_lineal_numeric(random_number)
    end_time2 = time.time()
    print(f"\n\nValor encontrado: {valores_encontrados}")


    time_data = [
        ["BUSQUEDA LINEAL O SECUENCIAL", (end_time2 - start_time2) * 1000, valor_encontrado._length],
        ["BUSQUEDA LINEAL BINARIA", (end_time2 - start_time2) * 1000, valores_encontrados._length],
    ]

    table_headers = ["Algoritmo", "Tiempo de ejecución (ms)", "nro. elementos"]
    print("\n")
    print(tabulate(time_data, headers=table_headers, tablefmt="pretty"))
    
    