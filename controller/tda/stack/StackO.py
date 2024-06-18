
from controller.tda.linked.linkedList import LinkedList
from controller.exception.LinkedEmpty import LinkedEmpty
import colorama 

colorama.init()
class StackO(LinkedList):
    def __init__(self, tope = 20):
        super().__init__() 
        self.__tope = tope

    @property
    def _tope(self):
        return self.__tope

    @_tope.setter
    def _tope(self, value):
        self.__tope = value

    @property
    def verify_top(self):
        # print(colorama.Fore.CYAN + f"Dentro de verify_top: {self._length}" + colorama.Fore.RESET)
        return self._length < self._tope
    
    def push(self, data):
        if self.verify_top:
            self.add(data, 0)
        else:
            raise LinkedEmpty('Stack full')
    
    @property 
    def pop(self):
        if self.isEmpty:
            raise LinkedEmpty('Stack empty')
        else:
            return self.delete(0)
        
        