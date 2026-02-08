from clase_base import ServicioMedico
from Dominio.clase_extra_1 import Paciente

class Urgencia(ServicioMedico):
    '''
         Clase que crea objetos para verificar el tipo de urgencia de un servicio medico
    '''
    def __init__(self, fecha, hora, paciente, nivel_gravedad):
        super().__init__(fecha, hora, paciente)
        self.nivel_gravedad = nivel_gravedad

        #MUESTRA LOS DATOS DE LA CLASE
        self.mostrar_datos()

    #PROPIEDADES
    @property
    def nivel_gravedad(self):
        return self._nivel_gravedad

    @nivel_gravedad.setter
    def nivel_gravedad(self, valor):
        valor = str(valor).strip().lower()

        if valor not in ("baja", "media", "alta"):
            raise ValueError("El nivel de gravedad esta fuera del rango debe ingresar: baja, media o alta.")

        self._nivel_gravedad = valor

    #METODO PARA CALCULAR EL GASTO
    def calcular_gasto(self):
        impuesto = self.precio_estandar * 0.15
        return self.precio_estandar + impuesto + 10  # Extra de urgencia

    #METODO PARA VERIFICAR SI ES URGENTE
    def es_urgente(self):
        return True

    #FUNCION QUE DA FORMATO A COMO SE MOSTRARAN LOS DATOS
    def mostrar_datos(self):
        print("*** URGENCIA ***")
        print("Nivel de gravedad:", self.nivel_gravedad)
        print("Fecha:", self.fecha)
        print("Hora:", self.hora)
        print(self.paciente)
        print("¿Es urgente?:", self.es_urgente())
        print(f"Total a pagar: ${self.calcular_gasto():.2f}")
        print("**********\n")


    def _str_(self):
        return (f"URGENCIA\n"
                f"Gravedad: {self.nivel_gravedad}\n"
                f"Total: ${self.calcular_gasto():.2f}")


#MUESTRA LA EJECUCION DE ESTA CLASE
if __name__ == "_main_":
    pac = Paciente("Mario", "Pérez", 40, "m", "mperez@gmail.com")
    test = Urgencia("15/10/2024", "09:45", pac, "alta")