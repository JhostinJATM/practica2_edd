import sys
import random 
import time 
from tabulate import tabulate

sys.path.append('../')
from controller.tda.linked.linkedList import LinkedList
from controller.usuarioDaoControl import UsuarioDaoControl


if __name__ == "__main__":
    
    lista = LinkedList()
        
    # for i in range(25):
    #     lista.add(random.randint(0, 25))
    # print(f"Lista orginal: {lista}")

    # for i in range(10000):
    #     lista.add(random.randint(0, 10000))
    # print(f"Lista orginal: {lista}")
    
    # for i in range(20000):
    #     lista.add(random.randint(0, 20000))
    # print(f"Lista orginal: {lista}")

    for i in range(25000):
        lista.add(random.randint(0, 25000))
    print(f"Lista orginal: {lista}")

    # Shell Sort
    start_time = time.time()
    lista_ordenada = lista.metodos_shell_sort(2)
    end_time = time.time()
    print(f"\n\nLista ordenada (SHELL SORT): {lista_ordenada}")

    # Quick Sort
    start_time2 = time.time()
    lista_ordenada3 = lista.metodos_quick_sort(2)
    end_time2 = time.time()
    print(f"\n\nLista ordenada (QUICK SORT): {lista_ordenada3}")

    # Merge Sort
    start_time3 = time.time()
    lista_ordenada5 = lista.metodos_merge_sort(2)
    end_time3 = time.time()
    print(f"\n\nLista ordenada (MERGE SORT): {lista_ordenada5}")

    time_data = [
        ["SHELL SORT", (end_time - start_time) * 1000, lista_ordenada._length],
        ["QUICK SORT", (end_time2 - start_time2) * 1000, lista_ordenada3._length],
        ["MERGE SORT", (end_time3 - start_time3) * 1000, lista_ordenada5._length]
    ]

    table_headers = ["Algoritmo", "Tiempo de ejecución (ms)", "nro. elementos"]
    print("\n")
    print(tabulate(time_data, headers=table_headers, tablefmt="pretty"))
