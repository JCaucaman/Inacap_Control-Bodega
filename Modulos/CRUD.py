import pymysql

class MySql:
    def __init__(self, Host = str, User = str, NameDataBase = str, Password = '') -> None:
        self.connection = pymysql.connect(
            host = Host,
            user = User,
            password = Password,
            database = NameDataBase)
        
        self.cursor = self.connection.cursor()
        print("Conexion excitosa")
    
    def seleccionarBD(self):
        pass

    def seleccionarTodo(self):
        pass

    def ingresar(self):
        pass

    def actualizar(self):
        pass

    def borrar(self,id):
        pass
    