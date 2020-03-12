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
            es_valido = True
            with open("./registros.txt", mode="a") as archivo:
                archivo.write(f"{nombre} || {clave} || {email} || {cedula} \n")

        elif autentificador == "n":
            salir_registro = input("Desea salir del registro de usuario? (Y/N): ").lower()
            if salir_registro == "y":
                nombre = None
                clave = None
                email = None
                cedula = None
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
    volver = input("Desea volver al Menu Principal? (Y/N): ").lower()
    return True if volver == "y" else False


while True:
    volver_al_menu = False
    op_seleccionada = mostrar_menu()
    while not volver_al_menu:
        if op_seleccionada == 1: # Inicio Sesion
            print()
            linea_del_usuario = iniciar_sesion()
            print(linea_del_usuario)
            with open("./registros.txt", mode="r") as archivo:
                datos_usuario = archivo.readlines()[int(linea_del_usuario) - 1]
                datos_list_usuario = datos_usuario.split("||")
                # Usuario(Nombre, Clave, Email, Cedula)
                nuevo_usuario = Usuario(datos_list_usuario[0].strip(), datos_list_usuario[1].strip(),
                                        datos_list_usuario[2].strip(), datos_list_usuario[3].strip())
            print()
        elif op_seleccionada == 2: # Registrar Usuario
            print()
            if registrar_usuario(): print("Se ha registrado exitosamente!")
            volver_al_menu = volver_al_menu_msg()
            print()
        else: # Salir del Programa
            exit("Gracias por haber usado nuestro sistema de registro.")