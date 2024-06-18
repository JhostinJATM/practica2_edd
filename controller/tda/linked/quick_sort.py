
class QuickSort:
    
    #! --------------------------------------ORDENAMIENTO POR NUMEROS--------------------------------------------
    
    @staticmethod
    def quick_sort_number_ascendent(array):
        if len(array) <= 1:
            return array
        else:
            pivot = array[len(array) // 2]
            less = [x for x in array if x < pivot]
            equal = [x for x in array if x == pivot]
            greater = [x for x in array if x > pivot]
            return QuickSort.quick_sort_number_ascendent(less) + equal + QuickSort.quick_sort_number_ascendent(greater)

    @staticmethod
    def quick_sort_number_descendent(array):
        if len(array) <= 1:
            return array
        else:
            pivot = array[len(array) // 2]
            less = [x for x in array if x > pivot]
            equal = [x for x in array if x == pivot]
            greater = [x for x in array if x < pivot]
            return QuickSort.quick_sort_number_descendent(less) + equal + QuickSort.quick_sort_number_descendent(greater)
    
    #! -------------------------------------ORDENAMIENTO POR ATRIBUTO--------------------------------------------
    
    @staticmethod
    def quick_sort_attribute_ascendent(array, attribute):
        if len(array) <= 1:
            return array
        else:
            pivot = array[len(array) // 2]
            less = [x for x in array if getattr(x, attribute) < getattr(pivot, attribute)]
            equal = [x for x in array if getattr(x, attribute) == getattr(pivot, attribute)]
            greater = [x for x in array if getattr(x, attribute) > getattr(pivot, attribute)]
            return QuickSort.quick_sort_attribute_ascendent(less, attribute) + equal + QuickSort.quick_sort_attribute_ascendent(greater, attribute)
    
    @staticmethod
    def quick_sort_attribute_descendent(array, attribute):
        if len(array) <= 1:
            return array
        else:
            pivot = array[len(array) // 2]
            less = [x for x in array if getattr(x, attribute) > getattr(pivot, attribute)]
            equal = [x for x in array if getattr(x, attribute) == getattr(pivot, attribute)]
            greater = [x for x in array if getattr(x, attribute) < getattr(pivot, attribute)]
            return QuickSort.quick_sort_attribute_descendent(less, attribute) + equal + QuickSort.quick_sort_attribute_descendent(greater, attribute)

    #? Link algoritmo basado: https://www.freecodecamp.org/espanol/news/algoritmos-de-ordenacion-explicados-con-ejemplos-en-javascript-python-java-y-c/