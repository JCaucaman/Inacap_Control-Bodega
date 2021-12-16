import pymysql

class MySql:
    def __init__(self, NameDataBase = str, Password = '', Host = 'localhost', User = 'root') -> None:
        self.connection = pymysql.connect(
            host = Host,
            user = User,
            password = Password,
            database = NameDataBase)
        
        self.cursor = self.connection.cursor()
        print("Conexion excitosa")


    def seleccionarTodo(self, nombre_tabla):
        sql = 'select * from {}'.format(nombre_tabla)
        try:
            self.cursor.execute(sql)
            rows = self.cursor.fetchall()
            for row in rows:
                for j in row:
                    print(j, end=' ')
                print()

        except Exception as e:
            print('error')

    def ingresar(self, Nombre_Tabla , dato1 = '', dato2 = '', dato3 = '', dato4 = '', dato5 = '', dato6 = '', dato7 = '', dato8 = ''):
        try:
            if(Nombre_Tabla == 'empleado' ):
                sql = "insert intro empleado (id_empleado, rut, nombreCompleto, fechadenaciminto, fotoCarnet, contraseña, nombreusurio, puesto) values ({},{},{},{},{},{},{},{})".format(dato1, dato2, dato3, dato4, dato5, dato6, dato7, dato8)
                self.cursor.execute(sql)
                self.connection.commit()
            elif(Nombre_Tabla == 'bodega'):
                sql = "insert intro bodega (id_bodega, Capacidad, Direccion, Jefe_Bodega) values ({}, {}, '{}', '{}')".format(dato1, dato2, dato3, dato4)
                self.cursor.execute(sql)
                self.connection.commit()
            elif(Nombre_Tabla == 'productos'):
                sql = "insert intro productos (id_productos, codigo_De_Barras, Nombre_Producto, Categoria, Marca, Precio_Unitario, Cantidad_Total, Stock_Critico) values ({},'{}','{}','{}','{}',{},{},{})".format(dato1, dato2, dato3, dato4, dato5, dato6, dato7, dato8)
                self.cursor.execute(sql)
                self.cursor.execute(sql)
                self.connection.commit()
            elif(Nombre_Tabla == 'ordenes'):
                sql = "insert intro ordenes (id_ordenes, Folio, Productos, Cantidad_Por_Producto, Precio_Total) values ({},'{}', '{}', {}, {})".format(dato1, dato2, dato3, dato4, dato5)
                self.cursor.execute(sql)
                self.connection.commit()
            elif(Nombre_Tabla == 'cliente'):
                sql = "insert into cliente (id_cliente, Nombre, Rut, Direccion, telefono, Correo) values ({}, '{}', '{}', '{}', '{}', '{}')".format(dato1, dato2, dato3, dato4, dato5, dato6)
                self.cursor.execute(sql)
                self.connection.commit()
        except Exception as e:
            print("El valor ya existe", e)

    def actualizar(self,id,puesto):
        sql = "update empleado set puesto='{}' where id_empleado={}".format(puesto,id)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            print('error')

    def borrar(self, Nombre_Tabla = str, id = int):
        sql = "delete from {} where id = {}".format(Nombre_Tabla, id)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            print("El valor ya existe",e)
            raise

      
    def cerrar(self):
        self.connection.close()
        print('Conexion cerrada')

Database_MySql = MySql('controlbodegapy')