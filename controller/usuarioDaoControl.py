from typing import Type
from controller.dao.daoAdapter import DaoAdapter
from controller.tda.linked.linkedList import LinkedList
from model.usuario import Usuario
from config.logging_config import log
from datetime import datetime
import colorama

class UsuarioDaoControl(DaoAdapter):
    def __init__(self):
        super().__init__(Usuario)
        self.__usuario = None

    @property
    def _usuario(self):
        if self.__usuario == None:
            self.__usuario = Usuario()
        return self.__usuario

    @_usuario.setter
    def _usuario(self, value):
        self.__usuario = value

    @property
    def _lista(self):
        return self._list()
    
    def merge(self, pos):
        self._merge(self._usuario, pos)
    
    def agregar_comando(self, nombre_comando):
        if nombre_comando:
            nuevo_id_comando = self._usuario._comandos._length + 1
            if nuevo_id_comando == 21:
                fecha_creacion = datetime.now()
                self._usuario._comandos.deleteLast()
                self._usuario._comandos.add({"id": 20, "nombre_comando": nombre_comando ,"fecha_creacion": str(fecha_creacion)})
            else:
                fecha_creacion = datetime.now()
                self._usuario._comandos.add({"id": nuevo_id_comando, "nombre_comando": nombre_comando, "fecha_creacion": str(fecha_creacion)})
              
    def lista_persona_codigos(self, user_id):
        print(colorama.Fore.RED + f"\n\n\nID: {user_id}\n\n\n\n" + colorama.Fore.RESET)
        uc = UsuarioDaoControl()
        numero_usuairo = int(user_id) - 1
        usuario = uc._list().get(numero_usuairo) 
        nombre = usuario._nombre_usuario 
        if usuario:
            stack_comandos = usuario._comandos
            comandos_list = []
            for i in range(stack_comandos._length):
                comando = stack_comandos.get(i)
                comando_dict = {"id": comando['id'], "comando": comando['nombre_comando'], "fecha_creacion": comando['fecha_creacion']}
                # comandos_list.add(comando_dict)
                comandos_list.append(comando_dict)
            comandos_list_sorted = sorted(comandos_list, key=lambda x: x['id'], reverse=True)
            return comandos_list_sorted, nombre
        else:    
            return

    @property
    def save(self):
        try:
            log.debug(colorama.Fore.RED + f"iD: {self._lista._length}" + colorama.Fore.RESET)
            self._usuario._id = self._lista._length + 1 
            log.info(colorama.Fore.BLUE + f"nuevo id = {self._usuario._id}" + colorama.Fore.RESET)
            self._save(self._usuario)
        except Exception as e:
            log.debug(colorama.Fore.GREEN + f"Error en save es: {e}" + colorama.Fore.RESET)
