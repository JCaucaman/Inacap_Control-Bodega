from Modulos import CRUD
from Modulos.CRUD import * 

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

    def GuardadoDataBaseEmpleados(self):
        pass


#Subclases

class JefeDeBodega(Empleado):
    def __init__(self, RUN, NombreCompleto, FechaDeNacimiento, FotoCarnet, contraseña):
        Empleado(RUN, NombreCompleto, FechaDeNacimiento, FotoCarnet, contraseña).__init__(RUN, NombreCompleto, FechaDeNacimiento, FotoCarnet, contraseña)

    def NuevoProducto(self):
        CRUD.Crud.ingresar()

class Administrador(Empleado):
    def __init__(self, RUN, NombreCompleto, FechaDeNacimiento, FotoCarnet, contraseña):
        Empleado(RUN, NombreCompleto, FechaDeNacimiento, FotoCarnet, contraseña).__init__(RUN, NombreCompleto, FechaDeNacimiento, FotoCarnet, contraseña)

    def NuevoProductos(self):
        CRUD.Crud.ingresar()

    def EliminarProductos(self):
        CRUD.Crud.borrar()

    def NuevaOrden(self):  
        pass

    def EliminarOrden(self): 
        pass

#Visualizar

    def VerInventario(self):
        pass

    def VerOrdenes(self):
        pass

    def VerClientes(self):
        pass

    def VerBodegas(self):
        pass
    
    def VerEmpledos(self):
        pass

class Gestor(Empleado):
    def __init__(self, RUN, NombreCompleto, FechaDeNacimiento, FotoCarnet, contraseña):
        Empleado(RUN, NombreCompleto, FechaDeNacimiento, FotoCarnet, contraseña).__init__(RUN, NombreCompleto, FechaDeNacimiento, FotoCarnet, contraseña)
    
    def VerInventario(self):
        pass

    def VerOrdenes(self):
        pass


