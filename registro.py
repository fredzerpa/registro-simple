class Usuario:
    def __init__(self, nombre, clave, email, cedula):
        self.nombre = nombre
        self.clave = clave
        self.email = email
        self.cedula = cedula

    def get_nombre(self):
        return self.nombre

    def get_clave(self):
        return self.clave

    def get_email(self):
        return self.email

    def get_cedula(self):
        return  self.cedula

def mostrar_menu():
    es_valido = False
    print("Bienvenidos al Sistema Aritmetico de Usuarios")
    while not es_valido:
        print()
        print("Por favor escoja una opcion a realizar:")
        print(" 1. Iniciar Sesion.")
        print(" 2. Registrar un Usuario.")
        print(" 3. Salir")
        op = int(input("Opcion: "))
        es_valido = True if (1 <= op <= 3) else False
    return op


def registrar_usuario():
    print("    REGISTRO DE USUARIO    ")
    es_valido = False
    while not es_valido:
        print()
        print("Por favor siga los pasos:")
        nombre = input("Indique su Usuario: ").strip()
        clave = input("Indique su Clave: ").strip()
        email = input("Indique su Email: ").strip()
        cedula = input("Indique su Cedula: V-").strip()

        print()
        print("Los Datos")
        print(f"Usuario: {nombre}")
        print(f"Usuario: {clave}")
        print(f"Usuario: {email}")
        print(f"Usuario: {cedula}")
        autentificador = input("Son correctos? (Y/N): ").lower()
        if autentificador == "y":
            # Buscador de palabras en una lista
            buscador_de_palabras = lambda palabra, string: True if palabra in string else False

            with open("./registros.txt", mode="r") as archivo:
                for registro in archivo.readlines():
                    es_repetido = buscador_de_palabras(nombre, registro)
                    if es_repetido:
                        break

            with open("./registros.txt", mode="a") as archivo:
                if not es_repetido:
                    es_valido = True
                    archivo.write(f"{nombre} || {clave} || {email} || {cedula} \n")
                else:
                    print("Usuario ya existente, por favor intente con otro nombre")

        elif autentificador == "n":
            while not es_valido:
                salir_registro = input("Desea salir del registro de usuario? (Y/N): ").lower()
                if salir_registro == "y":
                    nombre = None
                    clave = None
                    email = None
                    cedula = None
                    es_valido = True
                elif salir_registro == "n":
                    es_valido = True
    return es_valido

def iniciar_sesion():
    es_valido = False
    contador = 0
    print("     INICIAR SESION     ")
    while not es_valido:
        if contador > 0:
            if contador >= 3: exit("Muchos intentos fallidos.")
            print("Su Usuario y Clave no Coinciden!")
            print(f"Intento #{contador}: Al tercer intento sera sacado del sistema")

        input_usuario = input(" Usuario: ")
        input_clave = input(" Clave: ")

        # Verifica que los datos sean los mismos
        son_iguales = lambda data1, data2: True if data1 == data2 else False

        try:
            with open("./registros.txt", mode="r") as archivo:
                registros_list = archivo.readlines()
                linea_actual = 0 # Llevar un control de en que linea se esta trabajando en el archivo
                for registro in registros_list:
                    linea_actual += 1
                    usuario_valido = son_iguales(input_usuario.strip(), registro.split("||")[0].strip())
                    clave_valido = son_iguales(input_clave.strip(), registro.split("||")[1].strip())
                    if usuario_valido and clave_valido:
                        es_valido = True
                        break
            if not es_valido:
                contador += 1
        except FileNotFoundError as err:
            exit(f"Nombre de Archivo Incorrecto o no Existe. \n{err}")
    return linea_actual


def volver_al_menu_msg():
    while True:
        volver = input("Desea volver al Menu Principal? (Y/N): ").lower()
        if volver == "y":
            return True
        elif volver == "n":
            return False


def menu_usuario(nombre_usuario):
    es_valido = False
    print(f"Bienvenido {nombre_usuario}")
    while not es_valido:
        print()
        print("Por favor escoja una opcion a realizar:")
        print(" 1. Realizar Operacion Aritmetica.")
        print(" 2. Desloguearse.")
        op = int(input("Opcion: "))
        es_valido = True if (1 <= op <= 2) else False
    return op


def menu_admin(nombre_usuario):
    es_valido = False
    print(f"Bienvenido {nombre_usuario}")
    while not es_valido:
        print()
        print("Por favor escoja una opcion a realizar:")
        print(" 1. Leer datos de usuarios.")
        print(" 2. Desloguearse.")
        op = int(input("Opcion: "))
        es_valido = True if (1 <= op <= 2) else False
    return op


def menu_operaciones_aritmeticas():
    es_valido = False
    while not es_valido:
        print()
        print("Por favor escoja una operacion a realizar:")
        print(" 1. Suma (a + b)")
        print(" 2. Resta (a - b)")
        print(" 3. Multiplicacion (a x b)")
        print(" 4. Division (a / b)")
        print(" 5. Volver.")
        op = int(input("Opcion: "))
        es_valido = True if (1 <= op <= 5) else False
    return op



while True:
    volver_al_menu = False
    op_seleccionada = mostrar_menu()
    while not volver_al_menu:
        if op_seleccionada == 1: # Inicio Sesion
            print()
            linea_del_usuario = iniciar_sesion()
            with open("./registros.txt", mode="r") as archivo:
                datos_usuario = archivo.readlines()[int(linea_del_usuario) - 1]
                datos_list_usuario = datos_usuario.split("||")
                # Usuario(Nombre, Clave, Email, Cedula)
                nuevo_usuario = Usuario(datos_list_usuario[0].strip(), datos_list_usuario[1].strip(),
                                        datos_list_usuario[2].strip(), datos_list_usuario[3].strip())
                es_admin = True if nuevo_usuario.get_nombre() == "admin" else False
            while not volver_al_menu:
                print()
                if not es_admin: # Si es un usuario comun
                    op_usuario = menu_usuario(nuevo_usuario.get_nombre())
                    print()
                    if op_usuario == 1:
                        operacion_seleccionada = menu_operaciones_aritmeticas()
                        if 1 <= operacion_seleccionada <= 4:
                            print("Numeros a calcular: ")
                            a = int(input(" Primer Numero: "))
                            b = int(input(" Segundo Numero: "))
                            if operacion_seleccionada == 1: # Suma
                                resultado = a + b
                                tipo_operacion = "Suma"
                                simbolo = "+"
                            elif operacion_seleccionada == 2: # Resta
                                resultado = a - b
                                tipo_operacion = "Resta"
                                simbolo = "-"
                            elif operacion_seleccionada == 3: # Multiplicacion
                                resultado = a * b
                                tipo_operacion = "Multiplicacion"
                                simbolo = "*"
                            elif operacion_seleccionada == 4: # Division
                                resultado = a / b
                                tipo_operacion = "Division"
                                simbolo = "/"
                            print()
                            print(f"Tipo de operacion \"{tipo_operacion}\": \n"
                                  f"Total: {a} {simbolo} {b} = {resultado}")

                            volver_al_menu = volver_al_menu_msg()

                        else:
                            volver_al_menu = True
                    else:
                        volver_al_menu = True

                else: # Si es administrador
                    op_admin = menu_admin(nuevo_usuario.get_nombre())
                    print()
                    if op_admin == 1:
                        with open("./registros.txt", mode="r") as archivo:
                            posicion_linea = 0
                            for datos_usuario_linea in archivo.readlines():
                                posicion_linea += 1
                                print(f"{posicion_linea}. {datos_usuario_linea.replace(' || ', ', ')}")
                    else:
                        volver_al_menu = True

        elif op_seleccionada == 2: # Registrar Usuario
            print()
            if registrar_usuario(): print("Se ha registrado exitosamente!")
            volver_al_menu = volver_al_menu_msg()
            print()
        else: # Salir del Programa
            exit("Gracias por haber usado nuestro sistema de registro.")