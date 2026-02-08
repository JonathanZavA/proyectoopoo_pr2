from Datos.conexion import Conexion
import sys


class PacienteDAO:
    """
    Clase DAO (Data Access Object) para la entidad Paciente.
    Centraliza todas las operaciones CRUD contra la base de datos SQL Server.
    """

    # Sentencias SQL constantes
    _SELECCIONAR = "SELECT * FROM Pacientes WHERE cedula = ?"
    _INSERTAR = "INSERT INTO Pacientes (nombre, apellido, edad, genero, correo, cedula) VALUES (?, ?, ?, ?, ?, ?)"
    _ACTUALIZAR = "UPDATE Pacientes SET nombre=?, apellido=?, edad=?, genero=?, correo=? WHERE cedula=?"
    _ELIMINAR = "DELETE FROM Pacientes WHERE cedula = ?"

    @classmethod
    def seleccionar_paciente(cls, cedula):
        """Busca un paciente por su cédula y devuelve un registro."""
        try:
            with Conexion.obtenerCursor() as cursor:
                cursor.execute(cls._SELECCIONAR, (cedula,))
                return cursor.fetchone()
        except Exception as e:
            print(f"Error al seleccionar paciente: {e}")
            return None

    @classmethod
    def insertar_paciente(cls, paciente):
        """Inserta un nuevo registro utilizando un objeto de tipo Paciente."""
        try:
            with Conexion.obtenerCursor() as cursor:
                # Mapeo de atributos del objeto a la tupla de datos
                datos = (
                    paciente.nombre,
                    paciente.apellido,
                    paciente.edad,
                    paciente.genero,
                    paciente.correo,
                    paciente.cedula
                )
                cursor.execute(cls._INSERTAR, datos)
                Conexion.obtenerConexion().commit()
                return cursor.rowcount
        except Exception as e:
            print(f"Error al insertar paciente: {e}")
            return 0

    @classmethod
    def actualizar_paciente(cls, paciente):
        """Actualiza los datos de un paciente basado en su cédula."""
        try:
            with Conexion.obtenerCursor() as cursor:
                datos = (
                    paciente.nombre,
                    paciente.apellido,
                    paciente.edad,
                    paciente.genero,
                    paciente.correo,
                    paciente.cedula  # Se usa para el WHERE
                )
                cursor.execute(cls._ACTUALIZAR, datos)
                Conexion.obtenerConexion().commit()
                return cursor.rowcount
        except Exception as e:
            print(f"Error al actualizar paciente: {e}")
            return 0

    @classmethod
    def eliminar_paciente(cls, cedula):
        """Elimina un registro de la base de datos dada una cédula."""
        try:
            with Conexion.obtenerCursor() as cursor:
                cursor.execute(cls._ELIMINAR, (cedula,))
                Conexion.obtenerConexion().commit()
                return cursor.rowcount
        except Exception as e:
            print(f"Error al eliminar paciente: {e}")
            return 0


