from datetime import datetime
from Dominio.clase_extra_1 import Paciente

class ServicioMedico:
    '''
          Clase que crea objetos para un servivio medico
     '''
    def __init__(self,fecha, hora, paciente):
        """ Constructor de la clase. Inicializa y valida los datos"""
        # Se define el valor del precio estandar.
        self._precio_estandar = 30

        # Asignamos a través de los setters (sin guin bajo) para validar al instanciar
        self.fecha = fecha
        self.hora = hora
        self.paciente = paciente



    # --- Propertys Setters de todos los atributos ---

    @property
    def precio_estandar(self):
        return self._precio_estandar

    @property
    def fecha(self):
        """Getter para obtener la fecha."""
        return self._fecha

    @fecha.setter
    def fecha(self, n_fecha):
        """Setter para validar el formato de fecha (DD/MM/AAAA)."""
        n_fecha = str(n_fecha).strip()
        try:
            datetime.strptime(n_fecha, '%d/%m/%Y')
        except ValueError:
            raise ValueError('La fecha insrtada es incorrecta, procure seguir el siguiente formato: DD/MM/AAAA.')
        self._fecha = n_fecha

    @property
    def hora(self):
        """Getter para obtener la hora."""
        return self._hora

    @hora.setter
    def hora(self, n_hora):
        """Setter para validar el formato de hora (HH:MM)."""
        n_hora = str(n_hora).strip()
        try:
            datetime.strptime(n_hora, '%H:%M')
        except ValueError:
            raise ValueError('La hora insertada es incorrecta, procure seguir el siguiente formato: HH:MM (ej. 14:30).')
        self._hora = n_hora

    @property
    def paciente(self):
        """Getter para obtener el objeto paciente."""
        return self._paciente

    @paciente.setter
    def paciente(self, n_paciente):
        """Setter para validar que el objeto sea instancia de Paciente."""
        if not isinstance(n_paciente, Paciente):
            raise TypeError('Error: El valor no es una instancia de la clase Paciente.')
        self._paciente = n_paciente



    # --- Métodos que serán utilizados para el encapsulamiento ---

    def precio_del_servicio(self):
        """Retorna el precio estándar definido como constante."""
        return self.precio_estandar

    def es_urgente(self):
        """
            Indica si el servicio es urgente.
             Por defecto es False en la clase padre.
        """
        return False



   # -- str de la instancia --

    def __str__(self):
        """Retorna la información del objeto."""
        return (f'- Datos del servicio  -\nFecha: {self.fecha}\nHora: {self.hora}hrs\nNombre: {self.paciente.nombre}\nApellido: {self.paciente.apellido}\n'
                f'Edad: {self.paciente.edad}\nGénero: {self.paciente.genero}\nCorreo: {self.paciente.correo}')


# Muestra de la ejecución de la clase
if __name__ == '__main__':
    paciente1 = Paciente('Jont','Zav',19,'m','jonat@gmail.com')
    paciente1_servicioMedico = ServicioMedico('7/12/2025','11:43',paciente1)
    print(paciente1_servicioMedico)
    print('\nPrecio del servicio: $',paciente1_servicioMedico.precio_del_servicio())
    print('Es urgente? ',paciente1_servicioMedico.es_urgente())
    print('Hora: ',paciente1_servicioMedico.hora,' Fecha: ',paciente1_servicioMedico.fecha)