# from controller.tda.stack.StackO import StackO as Stack
from controller.tda.linked.linkedList import LinkedList

class Usuario:
    def __init__(self) -> None:
        self.__id = 0
        self.__nombre_usuario = ""
        self.__apellido_usuario = ""
        self.__edad = 0
        self.__email = ""
        self.__comandos = LinkedList()

    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _nombre_usuario(self):
        return self.__nombre_usuario

    @_nombre_usuario.setter
    def _nombre_usuario(self, value):
        self.__nombre_usuario = value

    @property
    def _apellido_usuario(self):
        return self.__apellido_usuario

    @_apellido_usuario.setter
    def _apellido_usuario(self, value):
        self.__apellido_usuario = value

    @property
    def _edad(self):
        return self.__edad

    @_edad.setter
    def _edad(self, value):
        self.__edad = value

    @property
    def _email(self):
        return self.__email

    @_email.setter
    def _email(self, value):
        self.__email = value

    @property
    def _comandos(self):
        return self.__comandos

    @_comandos.setter
    def _comandos(self, value):
        self.__comandos = value

    def __str__(self) -> str:
        return f"nombre: {self._nombre_usuario}\napellido: {self._apellido_usuario}\nedad: {self._edad}\nemail: {self._email}\n\n"
 
    @property
    def serializable(self):
        comandos_serializados = []
        for i in range(self._comandos._length):
            comando = self._comandos.get(i)
            fecha_creacion = comando.get("fecha_creacion", "")
            if fecha_creacion:
                fecha_creacion = fecha_creacion.split(".")[0] 
            comandos_serializados.append({
                "id": comando["id"],
                "nombre_comando": comando["nombre_comando"],
                "fecha_creacion": fecha_creacion
            })
            
        return {
            "id": self._id,
            "nombre_usuario": self._nombre_usuario,
            "apellido_usuario": self._apellido_usuario,
            "edad": self._edad,
            "email": self._email,
            "comandos": comandos_serializados            
        }

    @staticmethod
    def deserializar(data):
        usuario = Usuario()
        usuario._id = data["id"]
        usuario._nombre_usuario = data["nombre_usuario"]
        usuario._apellido_usuario = data["apellido_usuario"]
        usuario._edad = data["edad"]
        usuario._email = data["email"]
        # usuario._direccion = data["direccion"]
        for comando in data["comandos"]:
            usuario._comandos.add(comando)
        
        return usuario


    
    
    