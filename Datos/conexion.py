import pyodbc as bd
import sys


class Conexion:
    """
    Clase para gestionar la conexión a SQL Server utilizando el patrón Singleton
    con métodos de clase para optimizar el uso de recursos.
    """
    # Constantes de conexión (Clase)
    SERVIDOR = 'DESKTOP-84GONM3'
    BBDD = 'Hospital'
    USUARIO = 'proyecto_2bd'
    PASSWORD = '1234'

    # Atributos de clase para mantener la instancia única
    _conexion = None
    _cursor = None


    @classmethod
    def obtenerConexion(cls):
        if cls._conexion is None:
            try:
                cls._conexion = bd.connect(
                    f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={cls.SERVIDOR};DATABASE={cls.BBDD};UID={cls.USUARIO};PWD={cls.PASSWORD};TrustServerCertificate=yes'
                )
            except Exception as e:
                print(f"Error de conexión: {e}")
                return None # Retornamos None en lugar de sys.exit()
        return cls._conexion



    @classmethod
    def obtenerCursor(cls):
        try:
            con = cls.obtenerConexion()
            if con:
                if cls._cursor is None:
                    cls._cursor = con.cursor()
                return cls._cursor
        except Exception as e:
            print(f"Error al obtener cursor: {e}")
        return None

