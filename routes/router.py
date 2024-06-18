
import time
from controller.usuarioDaoControl import UsuarioDaoControl
from flask import Flask, Blueprint, url_for, jsonify, make_response, request, render_template, redirect, abort
from config.logging_config import log
import colorama

router = Blueprint('router', __name__)

#! -------------------PAGINAS_VER(GET)---------------------

#* Pagina principal
@router.route('/')
def home():
    return render_template('template.html')

#* Listar a todos los Usuarios
@router.route('/usuarios')
def lista_persona():
    uc = UsuarioDaoControl()
    return render_template('comando/lista.html', lista=uc.to_dict())

#* Listar a todos los Usuarios con ordenamiento, mediante parametros
@router.route('/usuarios/<tipo_ordenar>/<atributo>/<orden>')
def lista_persona_ordenar(tipo_ordenar, atributo, orden):
    uc = UsuarioDaoControl()
    print(tipo_ordenar) #shell, merge, quick
    print(atributo) #apellido, nombre, edad, email
    print(orden) #ascendente, descendente
    
    if tipo_ordenar == "shell":
        lista = uc._list().shell_models(atributo, int(orden))
    elif tipo_ordenar == "merge":
        lista = uc._list().merge_models(atributo, int(orden))
    elif tipo_ordenar == "quick":
        lista = uc._list().quick_models(atributo, int(orden))

    return make_response(
        jsonify({"msg":"OK", "code": 200, "data": uc.to_dic_lista(lista)}),
        200
    )

#* Listar a todos los Usuarios mediante busqueda lineal o lineal_binaria, mediante parametros
@router.route('/usuarios/busqueda/<tipo_busqueda>/<atributo>/<valor_busqueda>')
def lista_persona_busqueda(tipo_busqueda, atributo, valor_busqueda):
    uc = UsuarioDaoControl()
    print(f"Tipo busqueda: {tipo_busqueda}") #binaria o lineal_binaria
    print(f"Atributo: {atributo}") #edad, nombre, apellido, emial
    print(f"Valor a buscar:{valor_busqueda}") #Brienne
    
    diccionario_busqueda = {
        "1": uc._list().busqueda_combinada(atributo, valor_busqueda),
        "2": uc._list().busqueda_binaria(atributo, valor_busqueda),
    }
    lista_nueva = diccionario_busqueda[tipo_busqueda]
    return make_response(
        jsonify({"msg":"OK", "code": 200, "data": uc.to_dic_lista(lista_nueva)}),
        200
    )

#* Ingresar al formulario para guardar un usuario
@router.route('/usuarios/ver')
def ver_guardar():
    return render_template('comando/guardar.html')

#* Ingresar al formulario para agregar un nuevo comando a un usuario mediante id
@router.route('/usuarios/ver/codigo/<user_id>')
def ver_guardar_codigo(user_id):
    return render_template('comando/guardar_codigo.html', user_id=user_id)

#* Para ver los codigos de un usuario por id
@router.route('/usuarios/lista_codigos/<user_id>')
def lista_persona_codigos(user_id):
    uc = UsuarioDaoControl()
    datos_persona = uc.lista_persona_codigos(user_id)
    comandos_list, nombre = datos_persona
    return render_template('comando/lista_codigos.html', data=comandos_list, nombre=nombre, user_id=user_id)



#! --------------------ACCIONES (POST)----------------------

#* Para guardar un usuario desde el formulario
@router.route('/usuarios/guardar', methods = ['POST'])  
def guardar_persona():
    start_time = time.time()
    uc = UsuarioDaoControl()
    data = request.form
    if not "nombre_usuario" in data.keys():
       abort(400)
    #TODO ...Validar 
    uc._usuario._nombre_usuario = data['nombre_usuario']
    uc._usuario._apellido_usuario = data['apellido_usuario']
    uc._usuario._edad = data['edad']
    uc._usuario._email = data['email']
    uc.save
    end_time = time.time()
    print(f"Tiempo de ejecución de guardar_atencion (GET): {end_time - start_time} segundos")
    return redirect("/usuarios", code=302)

#* Para agregar un nuevo comando a un usuario
@router.route('/usuarios/comando_guardar/<user_id>', methods = ['POST'])  
def guardar_comando(user_id):
    try:
        uc = UsuarioDaoControl()
        data = request.form
        print("ID DE USUARIO: ", user_id)
        if not "nombre_comando" in data.keys():
            abort(400)
            #TODO ...Validar 
        id = int(user_id) - 1
        # print(colorama.Fore.RED + f"\n\n\n\nId: {id}" + colorama.Fore.RESET)
        # print(colorama.Fore.RED + f"Id: {type(id)}\n\n\n\n" + colorama.Fore.RESET)
        # usuario = uc._list().get(id)
        usuario = uc._list().get(id)
        uc._usuario = usuario
        comando = data['nombre_comando']
        uc.agregar_comando(comando)
        # print(colorama.Fore.RED + f"Comando: {data['nombre_comando']}" + colorama.Fore.RESET)
        uc.merge(id)
        user_id = int(user_id)
        # print(colorama.Fore.RED + f"Id: {user_id}" + colorama.Fore.RESET)
        # print(colorama.Fore.RED + f"Type Id: {type(user_id)}" + colorama.Fore.RESET)
        return redirect("/usuarios/lista_codigos/" + str(user_id) + "", code=302)
    except Exception as e:
        print(f"Error en: {e}")
        
        
        
# @router.route('/usuarios/editar/<pos>')
# def ver_editar(pos):
#     uc = UsuarioDaoControl()
#     comando = uc._list().get(int(pos) - 1)
#     return render_template('comando/editar.html', data=comando)

# @router.route('/personas/modificar', methods = ['POST'])  
# def modifcar_personas():
#     start_time = time.time()
#     uc = UsuarioDaoControl()
#     data = request.form
#     pos_int = int(data["id"])
#     comando = uc._list().get(pos_int - 1)
#     if not "nombre_comando" in data.keys():
#         abort(400)
#     #TODO ...Validar 
#     uc._historial_comando = comando
#     uc._historial_comando._nombre_comando = data['nombre_comando']
#     uc.merge(pos_int - 1)
#     end_time = time.time()
#     print(f"Tiempo de ejecución de guardar_atencion (GET): {end_time - start_time} segundos")
#     return redirect("/personas", code=302)



#! --------------------OBSOLETO---------------------

#? Para stack
# @router.route('/usuarios/comando_guardar/<user_id>', methods = ['POST'])  
# def guardar_comando(user_id):
#     try:
#         uc = UsuarioDaoControl()
#         data = request.form
#         if not "nombre_comando" in data.keys():
#             abort(400)
#             #TODO ...Validar 
#         id = int(user_id) - 1
#         print(colorama.Fore.RED + f"\n\n\n\nId: {id}" + colorama.Fore.RESET)
#         print(colorama.Fore.RED + f"Id: {type(id)}\n\n\n\n" + colorama.Fore.RESET)
#         usuario = uc._list().get(id)
#         uc._usuario = usuario
#         comando = data['nombre_comando']
#         uc.agregar_comando(comando)
#         print(colorama.Fore.RED + f"Comando: {data['nombre_comando']}" + colorama.Fore.RESET)
#         uc.merge(id)
#         user_id = int(user_id)
#         print(colorama.Fore.RED + f"Id: {user_id}" + colorama.Fore.RESET)
#         print(colorama.Fore.RED + f"Type Id: {type(user_id)}" + colorama.Fore.RESET)
#         return redirect("/usuarios/lista_codigos/" + str(user_id) + "", code=302)
#     except Exception as e:
#         print(f"Error en: {e}")
