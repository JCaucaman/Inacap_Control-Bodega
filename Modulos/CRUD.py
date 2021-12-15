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

    def seleccionarTodo(self):
        pass
#por modificar
    def ingresar(self, id, nombre, edad):
        sql = "insert into empledos (id_empledo,Nombre_Completo,rut) values ({}, '{}', {})".format(id,nombre,edad)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            print("El valor ya existe",e)
            raise

    def borrar(self, Nombre_Bd = str, id = int):
        sql = "delete from {} where id = {}".format(Nombre_Bd, id)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            print("El valor ya existe",e)
            raise