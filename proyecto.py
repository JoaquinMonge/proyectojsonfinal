import json


# ======================================================================================================================FuncionesSesionAdmin
def sesionadmin(useradmin, accesoadmin):
    user = input("Escriba el nombre de usuario \n: ")
    if user in useradmin:
        passw = input("Escriba la contrasena \n: ")
        if passw == useradmin[user]:
            accesoadmin = True
        else:
            print("Contrasena incorrecta \n")
    else:
        print("Nombre de usuario no existe \n")
    return accesoadmin


def cambuseradmin(useradmin):
    user = input("Escriba el nombre de usuario actual \n: ")
    if user in useradmin:
        passw = input("Escriba la contrasena actual \n: ")
        if passw == useradmin[user]:
            nuevouser = input("Escriba el nuevo nombre de usuario \n: ")
            useradmin[nuevouser] = useradmin.pop(user)
        else:
            print("Contrasena incorrecta \n")
    else:
        print("Nombre de usuario incorrecto \n")
    return useradmin


def cambpasswadmin(useradmin):
    user = input("Escriba el nombre de usuario actual \n: ")
    if user in useradmin:
        passw = input("Escriba la contrasena actual \n: ")
        if passw == useradmin[user]:
            nuevapassw = input("Escriba la nueva contrasena \n: ")
            useradmin[user] = nuevapassw
        else:
            print("Contrasena incorrecta \n")
    else:
        print("Nombre de usuario incorrecto \n")
    return useradmin


# ======================================================================================================================FuncionesSesionAsistente

def registroasist(asisdic):
    user = input("Escriba el nombre de usuario \n: ")
    if user in asisdic:
        print("Nombre de usuario ya existe \n")
    else:
        passw = input("Escriba la contrasena \n: ")
        asisdic[user] = passw
    return asisdic


def sesionasist(asisdic, accesoasist):
    user = input("Escriba el nombre de usuario \n: ")
    if user in asisdic:
        passw = input("Escriba la contrasena \n: ")
        if passw == asisdic[user]:
            accesoasist = True
        else:
            print("Contrasena incorrecta \n")
    else:
        print("Nombre de usuario no existe \n")
    return accesoasist


def cambuserasist(asisdic):
    user = input("Escriba el nombre de usuario \n: ")
    if user in asisdic:
        passw = input("Escriba la contrasena \n: ")
        if passw == asisdic[user]:
            nuevouser = input("Escriba el nuevo nombre de usuario \n: ")
            asisdic[nuevouser] = asisdic.pop(user)
        else:
            print("Contrasena incorrecta \n")
    else:
        print("Nombre de usuario no existe \n")
    return asisdic


def cambpasswasist(asisdic):
    user = input("Escriba el nombre de usuario \n: ")
    if user in asisdic:
        passw = input("Escriba la contrasena \n: ")
        if passw == asisdic[user]:
            nuevapassw = input("Escriba la nueva contrasena \n: ")
            asisdic[user] = nuevapassw
        else:
            print("Contrasena incorrecta \n")
    else:
        print("Nombre de usuario no existe \n")
    return asisdic


# ======================================================================================================================FuncionesSesionCliente

def registrocliente(sesioncliendic):
    sesion = True
    while sesion is True:
        cedula = input("Escriba el numero de cedula \n: ")
        if cedula in sesioncliendic:
            print("Usuario ya existe \n")
            break
        if cedula not in sesioncliendic:
            passw = input("Escriba la contrasena \n: ")
            sesioncliendic[cedula] = passw
            sesion = False
    return sesioncliendic


def sesioncliente(sesioncliendic, accesoclient, cedclien):
    cedula = input("Escriba el numero de cedula \n: ")
    if cedula in sesioncliendic:
        passw = input("Escriba la contrasena \n: ")
        if passw == sesioncliendic[cedula]:
            accesoclient = True
            cedclien = cedula
        else:
            print("Contrasena incorrecta \n")
    else:
        print("Usuario no esta registrado \n")
    return accesoclient, cedclien


def cambusercliente(sesioncliendic):
    cedula = input("Escriba el numero de cedula \n: ")
    if cedula in sesioncliendic:
        passw = input("Escriba la contrasena \n: ")
        if passw == sesioncliendic[cedula]:
            nuevouser = input("Escriba el nuevo numero de cedula \n: ")
            sesioncliendic[nuevouser] = sesioncliendic.pop(cedula)
        else:
            print("Contrasena incorrecta \n")
    else:
        print("Usuario no esta registrado \n")
    return sesioncliendic


def cambpasswcliente(sesioncliendic):
    cedula = input("Escriba el numero de cedula \n: ")
    if cedula in sesioncliendic:
        passw = input("Escriba la contrasena \n: ")
        if passw == sesioncliendic[cedula]:
            nuevapassw = input("Escriba la nueva contrasena \n: ")
            sesioncliendic[cedula] = nuevapassw
        else:
            print("Contrasena incorrecta \n")
    else:
        print("Nombre de usuario no existe \n")
    return sesioncliendic


# ======================================================================================================================FuncionesVehiculos

def agregarvehiculos(vehicdic):
    sn = "s"
    while sn == "s":
        placa = input("Escriba el numero de placa \n: ")
        if placa == "":
            print("Debe digitar el numero de placa \n")
            continue
        if placa in vehicdic:
            print("Numero de placa ya existe \n")
        else:
            marca = input("Escriba la marca del vehiculo \n: ")
            modelo = input("Escriba el modelo del vehiculo \n: ")
            color = input("Escriba el color del vehiculo \n: ")
            cant = input("Escriba la cantidad de pasajeros \n: ")
            vehicdic[placa] = {"Numero de placa": placa, "Marca": marca, "Modelo": modelo, "Color": color,
                               "Cantidad de pasajeros": cant, "Estado": "Disponible"}
            sn = input("Desea ingresar otro? S/N \n: ")
            if sn == "s" or sn == "S" or sn == "si" or sn == "SI" or sn == "Si" or sn == "sI":
                sn = "s"
            else:
                sn = "n"
    return vehicdic


def modificarvehiculos(vehicdic):
    sn = "s"
    while sn == "s":
        placa = input("Escriba el numero de placa \n: ")
        if placa == "":
            print("Debe digitar el numero de placa \n")
            continue
        if placa in vehicdic:
            dic = vehicdic.get(placa)
            print("Vehiculo encontrado: ", dic, " \n")
            estado = dic.get("Estado")
            if estado == "Disponible":
                marca = input("Escriba la marca del vehiculo \n: ")
                modelo = input("Escriba el modelo del vehiculo \n: ")
                color = input("Escriba el color del vehiculo \n: ")
                cant = input("Escriba la cantidad de pasajeros \n: ")
                vehicdic[placa] = {"Numero de placa": placa, "Marca": marca, "Modelo": modelo, "Color": color,
                                   "Cantidad de pasajeros": cant, "Estado": estado}
                sn = input("Desea realizar mas cambios? S/N \n: ")
                if sn == "s" or sn == "S" or sn == "si" or sn == "SI" or sn == "Si" or sn == "sI":
                    sn = "s"
                else:
                    sn = "n"
            else:
                print("El vehiculo debe estar en estado disponible para ser modificado \n")
        else:
            print("Numero de placa no encontrado \n")
    return vehicdic


def eliminarvehiculos(vehicdic):
    sn = "s"
    des = "s"
    while sn == "s":
        placa = input("Escriba el numero de placa \n: ")
        if placa == "":
            print("Debe digitar el numero de placa \n")
            continue
        if placa in vehicdic:
            print("Vehiculo encontrado: ", vehicdic[placa], " \n")
            des = input("Desea eliminarlo? S/N \n: ")
            if des == "s" or des == "S" or des == "si" or des == "SI" or des == "Si" or des == "sI":
                vehicdic.pop(placa)
                des = "s"
            else:
                des = "n"
            sn = input("Desea realizar mas cambios? S/N \n: ")
            if sn == "s" or sn == "S" or sn == "si" or sn == "SI" or sn == "Si" or sn == "sI":
                sn = "s"
            else:
                sn = "n"
        else:
            print("Numero de placa no encontrado \n")
    return vehicdic


# ======================================================================================================================FuncionesClientes

def agregarclientes(cliendic, sesioncliendic):
    sn = "s"
    while sn == "s":
        cedula = input("Escriba el numero de cedula \n: ")
        if cedula in sesioncliendic:
            if cedula in cliendic:
                print("Cliente ya esta registrado \n")
            else:
                nombre = input("Escriba el nombre \n: ")
                profesion = input("Escriba la profesion \n: ")
                direccion = input("Escriba la direccion de casa \n: ")
                trabajo = input("Escriba el lugar de trabajo \n: ")
                cliendic[cedula] = {"Numero de cedula": cedula, "Nombre": nombre, "Profesion": profesion,
                                    "Direccion de casa": direccion,
                                    "Lugar de trabajo": trabajo}
        else:
            reg = input("Numero de cedula no registrado. Desea registrarlo? S/N \n: ")
            if reg == "s" or reg == "S" or reg == "si" or reg == "SI" or reg == "Si" or reg == "sI":
                passw = input("Escriba la contrasena del nuevo cliente \n: ")
                sesioncliendic[cedula] = passw
                print("Ingrese los datos nuevamente \n")
                continue
            else:
                break
        sn = input("Desea ingresar otro? S/N \n: ")
        if sn == "s" or sn == "S" or sn == "si" or sn == "SI" or sn == "Si" or sn == "sI":
            sn = "s"
        else:
            sn = "n"
    return cliendic


def modificarclientes(cliendic):
    sn = "s"
    while sn == "s":
        cedula = input("Escriba el numero de cedula \n: ")
        if cedula in cliendic:
            print("Cliente encontrado: ", cliendic[cedula], " \n")
            nombre = input("Escriba el nombre \n: ")
            profesion = input("Escriba la profesion \n: ")
            direccion = input("Escriba la direccion de casa \n: ")
            trabajo = input("Escriba el lugar de trabajo \n: ")
            cliendic[cedula] = {"Numero de cedula": cedula, "Nombre": nombre, "Profesion": profesion,
                                "Direccion de casa": direccion,
                                "Lugar de trabajo": trabajo}
            sn = input("Desea realizar mas cambios? S/N \n: ")
            if sn == "s" or sn == "S" or sn == "si" or sn == "SI" or sn == "Si" or sn == "sI":
                sn = "s"
            else:
                sn = "n"
        else:
            print("Numero de cedula no encontrado \n")
    return cliendic


def eliminarclientes(cliendic):
    sn = "s"
    des = "s"
    while sn == "s":
        cedula = input("Escriba el numero de cedula \n: ")
        if cedula in cliendic:
            print("Cliente encontrado: ", cliendic[cedula], " \n")
            des = input("Desea eliminarlo? S/N \n: ")
            if des == "s" or des == "S" or des == "si" or des == "SI" or des == "Si" or des == "sI":
                cliendic.pop(cedula)
                des = "s"
            else:
                des = "n"
            sn = input("Desea realizar mas cambios? S/N \n: ")
            if sn == "s" or sn == "S" or sn == "si" or sn == "SI" or sn == "Si" or sn == "sI":
                sn = "s"
            else:
                sn = "n"
        else:
            print("Numero de cedula no encontrado \n")
    return cliendic


# ======================================================================================================================FuncionesAlquileres

def nuevoalquiler(cliendic, vehicdic, alqudic):
    cedula = input("Escriba el numero de cedula del cliente \n: ")
    if cedula in cliendic:
        print("Cliente encontrado: ", cliendic[cedula], " \n")
        placa = input("Escriba el numero de placa \n: ")
        if placa in vehicdic:
            print("Vehiculo encontrado: ", vehicdic[placa], " \n")
            dic = vehicdic.get(placa)
            estado = dic.get("Estado")
            if estado == "Disponible":
                sn = input("Desea registrar el alquiler? S/N \n: ")
                if sn == "s" or sn == "S" or sn == "si" or sn == "SI" or sn == "Si" or sn == "sI":
                    fechentr = input("Escriba la de entrega del vehiculo (DD/MM/AAAA) \n: ")
                    fechdev = input("Escriba la fecha de devolucion del vehiculo (DD/MM/AAAA) \n: ")
                    monto = input("Ingrese el monto por dia de alquiler \n :")
                    tarj = input("Ingrese el numero de tarjeta de credito \n: ")
                    venc = input("Escriba la fecha de vencimiento de la tarjeta (MM/AAAA) \n: ")
                    alqudic[cedula] = {"Placa del vehiculo": placa, "Entrega": fechentr, "Devolucion": fechdev,
                                       "Monto por dia": monto, "Numero de tarjeta": tarj, "Fecha de vencimiento": venc}
                    dic["Estado"] = "Preparado"
                    vehicdic[placa] = dic
                    print(alqudic)
                else:
                    sn = "n"
            else:
                print("El vehiculo debe estar en estado disponible para realizar el alquiler \n")
        else:
            print("Placa no encontrada \n")
    else:
        print("Numero de cedula no encontrado \n")
    return alqudic, vehicdic


def entralquiler(alqudic, vehicdic):
    cedula = input("Escriba el numero de cedula del cliente \n: ")
    if cedula in alqudic:
        alq = alqudic.get(cedula)
        placa = alq.get("Placa del vehiculo")
        print("Alquiler encontrado:", alqudic[cedula], "\n Vehiculo:", vehicdic[placa], "\n")
        sn = input("Desea realizar la entrega? S/N \n: ")
        if sn == "s" or sn == "S" or sn == "si" or sn == "SI" or sn == "Si" or sn == "sI":
            dic = vehicdic.get(placa)
            dic["Estado"] = "Activo"
            vehicdic[placa] = dic
        else:
            sn = "n"
    else:
        print("Cedula no encontrada o alquiler no registrado \n")
    return alqudic, vehicdic


def recalquiler(alqudic, vehicdic):
    cedula = input("Escriba el numero de cedula del cliente \n: ")
    if cedula in alqudic:
        alq = alqudic.get(cedula)
        placa = alq.get("Placa del vehiculo")
        print("Alquiler encontrado:", alqudic[cedula], "\n Vehiculo:", vehicdic[placa], "\n")
        sn = input("Desea proceder con la devolucion? S/N \n: ")
        if sn == "s" or sn == "S" or sn == "si" or sn == "SI" or sn == "Si" or sn == "sI":
            dic = vehicdic.get(placa)
            dic["Estado"] = "Disponible"
            vehicdic[placa] = dic

        else:
            sn = "n"
    else:
        print("Cedula no encontrada o alquiler no registrado \n")
    return alqudic, vehicdic

"""def estado(alqudic, vehicdic):
    est=input("Digite el estado que busca")
    if est in alqudic:
        alq=alqudic.get(cedula)"""


# ======================================================================================================================FuncionAlquilerCliente

def alquclien(alqudic, vehicdic, cedclien):
    placa = input("Escriba el numero de placa del vehiculo que desee alquilar \n: ")
    dic = vehicdic.get(placa)
    if dic["Estado"] == "Disponible":
        if placa in vehicdic:
            print("Vehiculo seleccionado:", vehicdic[placa])
            sn = input("Desea realizar la solicitud? S/N \n: ")
            if sn == "s" or sn == "S" or sn == "si" or sn == "SI" or sn == "Si" or sn == "sI":
                fechentr = input("Escriba la de entrega del vehiculo (DD/MM/AAAA) \n: ")
                fechdev = input("Escriba la fecha de devolucion del vehiculo (DD/MM/AAAA) \n: ")
                monto = input("Ingrese el monto por dia de alquiler \n :")
                tarj = input("Ingrese el numero de tarjeta de credito \n: ")
                venc = input("Escriba la fecha de vencimiento de la tarjeta (MM/AAAA) \n: ")
                alqudic[cedclien] = {"Placa del vehiculo": placa, "Entrega": fechentr, "Devolucion": fechdev,
                                     "Monto por dia": monto, "Numero de tarjeta": tarj, "Fecha de vencimiento": venc}
                dic["Estado"] = "Preparado"
                vehicdic[placa] = dic
                print("Solicitud registrada \n")
            else:
                sn = "n"
        else:
            print("Placa no encontrada \n")
    else:
        print("Solo vehiculos en estado disponible pueden ser alquilados \n")
    return alqudic, vehicdic


# ----------------------------------------------------------------------------------------------------------------------DefVariables
# »╒╕╘╛═│╡╞¿?

sesion = True
accesoadmin = False
accesoasist = False
accesoclient = False
useradmin = {"admin": "admin"}
asisdic = {}
sesioncliendic = {}
vehicdic = {}
cliendic = {}
alqudic = {}
bitlis = []

# ----------------------------------------------------------------------------------------------------------------------MenuInicioSesion
while sesion is True:
    try:
        with open("accesoadmin.json", "r") as archadmin:
            useradmin = json.load(archadmin)
    except FileNotFoundError:
        with open("accesoadmin.json", "w") as archadmin:
            json.dump(useradmin, archadmin)
    try:
        with open("vehiculos.json", "r") as archvehic, open("clientes.json", "r") as archcl, open("alquileres.json",
                                                                                                  "r") as archalqu:
            vehicdic = json.load(archvehic)
            cliendic = json.load(archcl)
            alqudic = json.load(archalqu)
    except FileNotFoundError:
        with open("vehiculos.json", "w") as archvehic, open("clientes.json", "w") as archcl, open("alquileres.json",
                                                                                                  "w") as archalqu:
            json.dump(vehicdic, archvehic)
            json.dump(cliendic, archcl)
            json.dump(alqudic, archalqu)
    sel = 0
    inicio = 0
    admin = True
    asistente = True
    cliente = True
    menuadmin = True
    menuclient = True
    cedclien = 0
    print(" \n"
          "╒════════ALCARSA════════╕\n"
          "│ ¿Como desea ingresar? │\n"
          "╞»1. Administrador      │\n"
          "╞»2. Asistente          │\n"
          "╞»3. Usuario            │\n"
          "╞»4. Salir              │\n"
          "╘═══════════════════════╛\n")
    try:
        sel = int(input(": "))
        print("...")
        if sel not in (1, 2, 3, 4):
            print("Opcion incorrecta \n...")
    except ValueError:
        print("Opcion incorrecta \n...")
    # ------------------------------------------------------------------------------------------------------------------MenuSesionAdmin
    if sel == 1:
        while admin is True:
            print(" \n"
                  "╒════════════ALCARSA════════════╕\n"
                  "╞»1. Iniciar sesion             │\n"
                  "╞»2. Cambiar nombre de usuario  │\n"
                  "╞»3. Cambiar contraseña         │\n"
                  "╞»4. Volver                     │\n"
                  "╘═══════════════════════════════╛\n")
            try:
                inicio = int(input(": "))
                print("...")
                if inicio not in (1, 2, 3, 4):
                    print("Opcion incorrecta \n...")
            except ValueError:
                print("Opcion incorrecta \n...")
            if inicio == 1:
                accesoadmin = sesionadmin(useradmin, accesoadmin)
                if accesoadmin is True:
                    admin = False
                    sesion = False
                else:
                    print("Acceso denegado \n")
            if inicio == 2:
                with open("accesoadmin.json", "r") as archadmin:
                    useradmin = json.load(archadmin)
                useradmin = cambuseradmin(useradmin)
                with open("accesoadmin.json", "w") as archadmin:
                    json.dump(useradmin, archadmin)
            if inicio == 3:
                useradmin = cambpasswadmin(useradmin)
            if inicio == 4:
                admin = False
    # ------------------------------------------------------------------------------------------------------------------MenuSesionAsistente
    if sel == 2:
        while asistente is True:
            print(" \n"
                  "╒════════════ALCARSA════════════╕\n"
                  "╞»1. Iniciar sesion             │\n"
                  "╞»2. Cambiar nombre de usuario  │\n"
                  "╞»3. Cambiar contraseña         │\n"
                  "╞»4. Volver                     │\n"
                  "╘═══════════════════════════════╛\n")
            try:
                inicio = int(input(": "))
                print("...")
                if inicio not in (1, 2, 3, 4):
                    print("Opcion incorrecta \n...")
            except ValueError:
                print("Opcion incorrecta \n...")
            if inicio == 1:
                try:
                    with open("accesoasist.json", "r") as archasist:
                        asisdic = json.load(archasist)
                except FileNotFoundError:
                    print("No hay asistentes registrados \n")
                    with open("accesoasist.json", "w") as archasist:
                        json.dump(asisdic, archasist)
                accesoasist = sesionasist(asisdic, accesoasist)
                if accesoasist is True:
                    asistente = False
                    sesion = False
                else:
                    print("Acceso denegado \n")
            if inicio == 2:
                try:
                    with open("accesoasist.json", "r") as archasist:
                        asisdic = json.load(archasist)
                except FileNotFoundError:
                    print("No hay asistentes registrados \n")
                    with open("accesoasist.json", "w") as archasist:
                        json.dump(asisdic, archasist)
                asisdic = cambuserasist(asisdic)
                with open("accesoasist.json", "w") as archasist:
                    json.dump(asisdic, archasist)
            if inicio == 3:
                try:
                    with open("accesoasist.json", "r") as archasist:
                        asisdic = json.load(archasist)
                except FileNotFoundError:
                    print("No hay asistentes registrados \n")
                    with open("accesoasist.json", "w") as archasist:
                        json.dump(asisdic, archasist)
                asisdic = cambpasswasist(asisdic)
                with open("accesoasist.json", "w") as archasist:
                    json.dump(asisdic, archasist)
            if inicio == 4:
                asistente = False
    # ------------------------------------------------------------------------------------------------------------------MenuSesionCliente
    if sel == 3:
        while cliente is True:
            print(" \n"
                  "╒════════════ALCARSA════════════╕\n"
                  "╞»1. Iniciar sesion             │\n"
                  "╞»2. Registrarse                │\n"
                  "╞»3. Cambiar nombre de usuario  │\n"
                  "╞»4. Cambiar contraseña         │\n"
                  "╞»5. Volver                     │\n"
                  "╘═══════════════════════════════╛\n")
            try:
                inicio = int(input(": "))
                print("...")
                if inicio not in (1, 2, 3, 4, 5):
                    print("Opcion incorrecta \n...")
            except ValueError:
                print("Opcion incorrecta \n...")
            if inicio == 1:
                try:
                    with open("accesoclien.json", "r") as archclien:
                        sesioncliendic = json.load(archclien)
                except FileNotFoundError:
                    with open("accesoclien.json", "w") as archclien:
                        json.dump(sesioncliendic, archclien)
                accesoclient, cedclien = sesioncliente(sesioncliendic, accesoclient, cedclien)
                if accesoclient is True:
                    cliente = False
                    sesion = False
                else:
                    print("Acceso denegado \n")
            if inicio == 2:
                try:
                    with open("accesoclien.json", "r") as archclien:
                        sesioncliendic = json.load(archclien)
                except FileNotFoundError:
                    with open("accesoclien.json", "w") as archclien:
                        json.dump(sesioncliendic, archclien)
                sesioncliendic = registrocliente(sesioncliendic)
                with open("accesoclien.json", "w") as archclien:
                    json.dump(sesioncliendic, archclien)
            if inicio == 3:
                try:
                    with open("accesoclien.json", "r") as archclien:
                        sesioncliendic = json.load(archclien)
                except FileNotFoundError:
                    with open("accesoclien.json", "w") as archclien:
                        json.dump(sesioncliendic, archclien)
                sesioncliendic = cambusercliente(sesioncliendic)
                with open("accesoclien.json", "w") as archclien:
                    json.dump(sesioncliendic, archclien)
            if inicio == 4:
                try:
                    with open("accesoclien.json", "r") as archclien:
                        sesioncliendic = json.load(archclien)
                except FileNotFoundError:
                    with open("accesoclien.json", "w") as archclien:
                        json.dump(sesioncliendic, archclien)
                sesioncliendic = cambpasswcliente(sesioncliendic)
                with open("accesoclien.json", "w") as archclien:
                    json.dump(sesioncliendic, archclien)
            if inicio == 5:
                cliente = False
    # ------------------------------------------------------------------------------------------------------------------SalirDelPrograma
    if sel == 4:
        sesion = False
    # ------------------------------------------------------------------------------------------------------------------MenuAdminYAsistente
    # »╒╕╘╛═│╡╞¿?
    if accesoadmin is True or accesoasist is True:
        print("Bienvenid@ \n")
        if accesoadmin is True:
            with open("bitacora.txt", "a") as archbit:
                archbit.write("Entrada Admin \n")
        if accesoasist is True:
            with open("bitacora.txt", "a") as archbit:
                archbit.write("Entrada Asistente \n")
        while menuadmin is True:
            sel = 0
            inicio = 0
            vehiculos = True
            clientes = True
            alquileres = True
            reportes = True
            print(" \n"
                  "╒════════════ALCARSA════════════╕\n"
                  "╞»1. Registrar nuevo asistente  │\n"
                  "╞»2. Vehiculos                  │\n"
                  "╞»3. Clientes                   │\n"
                  "╞»4. Alquileres                 │\n"
                  "╞»5. Reportes                   │\n"
                  "╞»6. Cerrar sesion              │\n"
                  "╘═══════════════════════════════╛\n")
            try:
                sel = int(input(": "))
                print("...")
                if sel not in (1, 2, 3, 4, 5, 6):
                    print("Opcion incorrecta \n...")
            except ValueError:
                print("Opcion incorrecta \n...")
            # ----------------------------------------------------------------------------------------------------------RegistrarAsistente
            if sel == 1:
                try:
                    with open("accesoasist.json", "r") as archasist:
                        asisdic = json.load(archasist)
                except FileNotFoundError:
                    with open("accesoasist.json", "w") as archasist:
                        json.dump(asisdic, archasist)
                asisdic = registroasist(asisdic)
                with open("accesoasist.json", "w") as archasist:
                    json.dump(asisdic, archasist)
            # ----------------------------------------------------------------------------------------------------------MenuVehiculos
            if sel == 2:
                while vehiculos is True:
                    print(" \n"
                          "╒════════════Vehiculos════════════╕\n"
                          "╞»1. Agregar nuevos vehiculos     │\n"
                          "╞»2. Modificar datos de vehiculos │\n"
                          "╞»3. Eliminar datos de vehiculos  │\n"
                          "╞»4. Volver                       │\n"
                          "╘═════════════════════════════════╛\n")
                    try:
                        inicio = int(input(": "))
                        print("...")
                        if inicio not in (1, 2, 3, 4):
                            print("Opcion incorrecta \n...")
                    except ValueError:
                        print("Opcion incorrecta \n...")
                    if inicio == 1:
                        try:
                            with open("vehiculos.json", "r") as archvehic:
                                vehicdic = json.load(archvehic)
                        except FileNotFoundError:
                            with open("vehiculos.json", "w") as archvehic:
                                json.dump(vehicdic, archvehic)
                        vehicdic = agregarvehiculos(vehicdic)
                        with open("vehiculos.json", "w") as archvehic:
                            json.dump(vehicdic, archvehic)
                    if inicio == 2:
                        try:
                            with open("vehiculos.json", "r") as archvehic:
                                vehicdic = json.load(archvehic)
                        except FileNotFoundError:
                            with open("vehiculos.json", "w") as archvehic:
                                json.dump(vehicdic, archvehic)
                        vehicdic = modificarvehiculos(vehicdic)
                        with open("vehiculos.json", "w") as archvehic:
                            json.dump(vehicdic, archvehic)
                    if inicio == 3:
                        try:
                            with open("vehiculos.json", "r") as archvehic:
                                vehicdic = json.load(archvehic)
                        except FileNotFoundError:
                            with open("vehiculos.json", "w") as archvehic:
                                json.dump(vehicdic, archvehic)
                        vehicdic = eliminarvehiculos(vehicdic)
                        with open("vehiculos.json", "w") as archvehic:
                            json.dump(vehicdic, archvehic)
                    if inicio == 4:
                        vehiculos = False
            # ----------------------------------------------------------------------------------------------------------MenuModCliente
            if sel == 3:
                while clientes is True:
                    print(" \n"
                          "╒════════════Clientes════════════╕\n"
                          "╞»1. Agregar nuevos clientes     │\n"
                          "╞»2. Modificar datos de clientes │\n"
                          "╞»3. Eliminar datos de clientes  │\n"
                          "╞»4. Volver                      │\n"
                          "╘════════════════════════════════╛\n")
                    try:
                        inicio = int(input(": "))
                        print("...")
                        if inicio not in (1, 2, 3, 4):
                            print("Opcion incorrecta \n...")
                    except ValueError:
                        print("Opcion incorrecta \n...")
                    if inicio == 1:
                        try:
                            with open("clientes.json", "r") as archcl:
                                cliendic = json.load(archcl)
                        except FileNotFoundError:
                            with open("clientes.json", "w") as archcl:
                                json.dump(cliendic, archcl)
                        cliendic = agregarclientes(cliendic, sesioncliendic)
                        with open("clientes.json", "w") as archcl:
                            json.dump(cliendic, archcl)
                    if inicio == 2:
                        try:
                            with open("clientes.json", "r") as archcl:
                                cliendic = json.load(archcl)
                        except FileNotFoundError:
                            with open("clientes.json", "w") as archcl:
                                json.dump(cliendic, archcl)
                        cliendic = modificarclientes(cliendic)
                        with open("clientes.json", "w") as archcl:
                            json.dump(cliendic, archcl)
                    if inicio == 3:
                        try:
                            with open("clientes.json", "r") as archcl:
                                cliendic = json.load(archcl)
                        except FileNotFoundError:
                            with open("clientes.json", "w") as archcl:
                                json.dump(cliendic, archcl)
                        cliendic = eliminarclientes(cliendic)
                        with open("clientes.json", "w") as archcl:
                            json.dump(cliendic, archcl)
                    if inicio == 4:
                        clientes = False
            # ----------------------------------------------------------------------------------------------------------MenuAlquileresAdmin
            if sel == 4:
                while alquileres is True:
                    print(" \n"
                          "╒══════════Alquileres══════════╕\n"
                          "╞»1. Registrar nuevo alquiler  │\n"
                          "╞»2. Entregar alquiler         │\n"
                          "╞»3. Recibir alquiler          │\n"
                          "╞»4. Volver                    │\n"
                          "╘══════════════════════════════╛\n")
                    try:
                        inicio = int(input(": "))
                        print("...")
                        if inicio not in (1, 2, 3, 4):
                            print("Opcion incorrecta \n...")
                    except ValueError:
                        print("Opcion incorrecta \n...")
                    if inicio == 1:
                        try:
                            with open("alquileres.json", "r") as archalqu:
                                alqudic = json.load(archalqu)
                        except FileNotFoundError:
                            with open("alquileres.json", "w") as archalqu:
                                json.dump(alqudic, archalqu)
                        alqudic, vehicdic = nuevoalquiler(cliendic, vehicdic, alqudic)
                        with open("alquileres.json", "w") as archalqu:
                            json.dump(alqudic, archalqu)
                    if inicio == 2:
                        try:
                            with open("alquileres.json", "r") as archalqu:
                                alqudic = json.load(archalqu)
                        except FileNotFoundError:
                            with open("alquileres.json", "w") as archalqu:
                                json.dump(alqudic, archalqu)
                        alqudic, vehicdic = entralquiler(alqudic, vehicdic)
                        with open("alquileres.json", "w") as archalqu:
                            json.dump(alqudic, archalqu)
                    if inicio == 3:
                        try:
                            with open("alquileres.json", "r") as archalqu:
                                alqudic = json.load(archalqu)
                        except FileNotFoundError:
                            with open("alquileres.json", "w") as archalqu:
                                json.dump(alqudic, archalqu)
                        alqudic, vehicdic = recalquiler(alqudic, vehicdic)
                        with open("alquileres.json", "w") as archalqu:
                            json.dump(alqudic, archalqu)
                    if inicio == 4:
                        alquileres = False
            # ----------------------------------------------------------------------------------------------------------Reportes
            if sel == 5:
                while reportes is True:
                    print(" \n"
                          "╒════Reportes════╕\n"
                          "╞»1. Vehiculos   │\n"
                          "╞»2. Clientes    │\n"
                          "╞»3. Alquileres  │\n"
                          "╞»4. Bitacora    │\n"
                          "╞»5. Volver      │\n"
                          "╘════════════════╛\n")
                    try:
                        inicio = int(input(": "))
                        print("...")
                        if inicio not in (1, 2, 3, 4, 5):
                            print("Opcion incorrecta \n...")
                    except ValueError:
                        print("Opcion incorrecta \n...")
                    if inicio == 1:
                        try:
                            with open("vehiculos.json", "r") as archvehic:
                                vehicdic = json.load(archvehic)
                        except FileNotFoundError:
                            print("No hay vehiculos para mostrar \n")
                        for i, j in vehicdic.items():
                            print(j)
                    if inicio == 2:
                        try:
                            with open("clientes.json", "r") as archcl:
                                cliendic = json.load(archcl)
                        except FileNotFoundError:
                            print("No hay clientes para mostrar \n")
                        for i, j in cliendic.items():
                            print(j)
                    if inicio == 3:
                        try:
                            with open("alquileres.json", "r") as archalqu:
                                alqudic = json.load(archalqu)
                        except FileNotFoundError:
                            print("No hay alquileres para mostrar \n")
                        for i, j in alqudic.items():
                            print(j)
                    if inicio == 4:
                        with open("bitacora.txt", "r") as archbit:
                            print(archbit.read())
                    if inicio == 5:
                        reportes = False
            # ----------------------------------------------------------------------------------------------------------CerrarSesion
            if sel == 6:
                accesoadmin = False
                accesoasist = False
                sesion = True
                break
    # ------------------------------------------------------------------------------------------------------------------MenuCliente
    if accesoclient is True:
        print("Bienvenid@ \n")
        with open("bitacora.txt", "a") as archbit:
            archbit.write("Entrada Usuario \n")
        while menuclient is True:
            vehiculos = True
            alquileres = True
            sel = 0
            inicio = 0
            print(" \n"
                  "╒══════════ALCARSA══════════╕\n"
                  "╞»1. Vehiculos disponibles  │\n"
                  "╞»2. Solicitar alquiler     │\n"
                  "╞»3. Cerrar sesion          │\n"
                  "╘═══════════════════════════╛\n")
            try:
                sel = int(input(": "))
                print("...")
                if sel not in (1, 2, 3):
                    print("Opcion incorrecta \n...")
            except ValueError:
                print("Opcion incorrecta \n...")
            # ----------------------------------------------------------------------------------------------------------VerVehicDisp
            if sel == 1:
                try:
                    with open("vehiculos.json", "r") as archvehic:
                        vehicdic = json.load(archvehic)
                except FileNotFoundError:
                    print("Aun no hay vehiculos para mostrar \n")
                for i, j in vehicdic.items():
                    print("Los vehiculos en estado Preparado o Activo no se encuentran disponibles \n", j)
            # ----------------------------------------------------------------------------------------------------------AlquClient
            if sel == 2:
                try:
                    with open("alquileres.json", "r") as archalqu:
                        alqudic = json.load(archalqu)
                except FileNotFoundError:
                    with open("alquileres.json", "w") as archalqu:
                        json.dump(alqudic, archalqu)
                alqudic, vehicdic = alquclien(alqudic, vehicdic, cedclien)
                with open("alquileres.json", "w") as archalqu:
                    json.dump(alqudic, archalqu)
            # ----------------------------------------------------------------------------------------------------------CerrarSesion
            if sel == 3:
                accesoclient = False
                sesion = True
                break