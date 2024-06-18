class MergeSort:
    
    #! --------------------------------------ORDENAMIENTO POR NUMEROS--------------------------------------------
    
    @staticmethod
    def merge_asc_number(left, right):
        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    @staticmethod
    def merge_desc_number(left, right):
        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] > right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    @staticmethod
    def merge_sort_asc_number(arr):
        if len(arr) < 2:
            return arr[:]
        else:
            middle = len(arr) // 2
            left = MergeSort.merge_sort_asc_number(arr[:middle])
            right = MergeSort.merge_sort_asc_number(arr[middle:])
            return MergeSort.merge_asc_number(left, right)

    @staticmethod
    def merge_sort_desc_number(arr):
        if len(arr) < 2:
            return arr[:]
        else:
            middle = len(arr) // 2
            left = MergeSort.merge_sort_desc_number(arr[:middle])
            right = MergeSort.merge_sort_desc_number(arr[middle:])
            return MergeSort.merge_desc_number(left, right)
    
    #! -------------------------------------ORDENAMIENTO POR ATRIBUTO--------------------------------------------

    @staticmethod
    def merge_asc(left, right, attribute):
        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if getattr(left[i], attribute) < getattr(right[j], attribute):
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    @staticmethod
    def merge_desc(left, right, attribute):
        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if getattr(left[i], attribute) > getattr(right[j], attribute):
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    @staticmethod
    def merge_sort_asc(arr, attribute):
        if len(arr) < 2:
            return arr[:]
        else:
            middle = len(arr) // 2
            left = MergeSort.merge_sort_asc(arr[:middle], attribute)
            right = MergeSort.merge_sort_asc(arr[middle:], attribute)
            return MergeSort.merge_asc(left, right, attribute)

    @staticmethod
    def merge_sort_desc(arr, attribute):
        if len(arr) < 2:
            return arr[:]
        else:
            middle = len(arr) // 2
            left = MergeSort.merge_sort_desc(arr[:middle], attribute)
            right = MergeSort.merge_sort_desc(arr[middle:], attribute)
            return MergeSort.merge_desc(left, right, attribute)

    #? Link algoritmo basado: https://www.freecodecamp.org/espanol/news/algoritmos-de-ordenacion-explicados-con-ejemplos-en-javascript-python-java-y-c/