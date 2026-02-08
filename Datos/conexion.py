import pyodbc as bd
import sys


class Conexion:
    """
    Clase para gestionar la conexión a SQL Server utilizando el patrón Singleton
    con métodos de clase para optimizar el uso de recursos.
    """
    # Constantes de conexión (Clase)
    SERVIDOR = '16.0.1000.6'
    BBDD = 'Hospital'
    USUARIO = 'proyecto_2bd'
    PASSWORD = '1234'

    # Atributos de clase para mantener la instancia única
    _conexion = None
    _cursor = None

    @classmethod
    def obtenerConexion(cls):
        """
        Obtiene la conexión a la BBDD con los parámetros pasados como constantes.
        """
        if cls._conexion is None:
            try:
                # Se utiliza el driver 'ODBC Driver 17 for SQL Server' común en instalaciones modernas
                cls._conexion = bd.connect(
                    'DRIVER={ODBC Driver 17 for SQL Server};' +
                    'SERVER=' + cls.SERVIDOR +
                    ';DATABASE=' + cls.BBDD +
                    ';UID=' + cls.USUARIO +
                    ';PWD=' + cls.PASSWORD +
                    ';TrustServerCertificate=yes'
                )
                return cls._conexion
            except Exception as e:
                print(f"Ocurrió una excepción al obtener la conexión: {e}")
                sys.exit()
        else:
            return cls._conexion

    @classmethod
    def obtenerCursor(cls):
        """
        Obtiene el cursor único para ejecutar sentencias SQL.
        """
        if cls._cursor is None:
            try:
                cls._cursor = cls.obtenerConexion().cursor()
                return cls._cursor
            except Exception as e:
                print(f"Ocurrió una excepción al obtener el cursor: {e}")
                sys.exit()
        else:
            return cls._cursor
