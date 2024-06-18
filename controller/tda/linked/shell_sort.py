

class ShellSort:
    
    #! --------------------------------------ORDENAMIENTO POR NUMEROS--------------------------------------------

    @staticmethod
    def shell_sort_number_ascendent(arr):
        n = len(arr)
        gap = n // 2

        while gap > 0:
            for i in range(gap, n):
                temp = arr[i]
                j = i
                while j >= gap and arr[j - gap] > temp:
                    arr[j] = arr[j - gap]
                    j -= gap
                arr[j] = temp
            gap //= 2
        return arr 

    @staticmethod
    def shell_sort_number_descendent(arr):
        n = len(arr)
        gap = n // 2

        while gap > 0:
            for i in range(gap, n):
                temp = arr[i]
                j = i
                while j >= gap and arr[j - gap] < temp:
                    arr[j] = arr[j - gap]
                    j -= gap
                arr[j] = temp
            gap //= 2
        return arr 
    
    #! -------------------------------------ORDENAMIENTO POR ATRIBUTO--------------------------------------------

    @staticmethod
    def shell_sort_asc(arr, attribute):
        n = len(arr)
        gap = n // 2

        while gap > 0:
            for i in range(gap, n):
                temp = arr[i]
                j = i
                while j >= gap and getattr(arr[j - gap], attribute) > getattr(temp, attribute):
                    arr[j] = arr[j - gap]
                    j -= gap
                arr[j] = temp
            gap //= 2
        return arr 

    @staticmethod
    def shell_sort_desc(arr, attribute):
        n = len(arr)
        gap = n // 2

        while gap > 0:
            for i in range(gap, n):
                temp = arr[i]
                j = i
                while j >= gap and getattr(arr[j - gap], attribute) < getattr(temp, attribute):
                    arr[j] = arr[j - gap]
                    j -= gap
                arr[j] = temp
            gap //= 2
        return arr 

    #? Link algoritmo basado: https://www.geeksforgeeks.org/python-program-for-shellsort/