
class Empleado:
    def __init__(self,RUN, NombreCompleto, FechaDeNacimiento, FotoCarnet, contraseña):
        self.Rut = RUN
        self.Nombre = str(NombreCompleto)
        self.FechaDeNaciminto = FechaDeNacimiento
        self.FotoCarnet = FotoCarnet
        self.__contraseña = str(contraseña)
        self.NombreUsuario = str(NombreCompleto).split(' ')[0] + str(NombreCompleto).split(' ')[2]

    def login(self, Usuario, Clave):
        if (Usuario == self.NombreUsuario and self.__contraseña == Clave):
            print("Acceso Permitido")
            return False
        else: 
            print("Acceso Denegado")
            return True

#Subclases

class JefeDeBodega(Empleado):
    def __init__(self, RUN, NombreCompleto, FechaDeNacimiento, FotoCarnet, contraseña):
        Empleado(RUN, NombreCompleto, FechaDeNacimiento, FotoCarnet, contraseña).__init__(RUN, NombreCompleto, FechaDeNacimiento, FotoCarnet, contraseña)



class Administrador(Empleado):
    def __init__(self, RUN, NombreCompleto, FechaDeNacimiento, FotoCarnet, contraseña):
        Empleado(RUN, NombreCompleto, FechaDeNacimiento, FotoCarnet, contraseña).__init__(RUN, NombreCompleto, FechaDeNacimiento, FotoCarnet, contraseña)



class Gestor(Empleado):
    def __init__(self, RUN, NombreCompleto, FechaDeNacimiento, FotoCarnet, contraseña):
        Empleado(RUN, NombreCompleto, FechaDeNacimiento, FotoCarnet, contraseña).__init__(RUN, NombreCompleto, FechaDeNacimiento, FotoCarnet, contraseña)


