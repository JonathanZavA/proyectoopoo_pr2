from clase_base import ServicioMedico
from Dominio.clase_extra_1 import Paciente

class ConsultaGeneral(ServicioMedico):
    '''
         Clase que crea objetos para ver la especialidad de un servicio medico
    '''
    def __init__(self, fecha, hora, paciente, especialidad):
        super().__init__(fecha, hora, paciente)
        self.especialidad = especialidad

        # MUESTRA LOS DATOS DE LA CLASE
        self.mostrar_datos()
    #PROPIEDADES
    @property
    def especialidad(self):
        return self._especialidad

    @especialidad.setter
    def especialidad(self, valor):
        valor = str(valor).strip()
        if not valor or not valor.replace(" ", "").isalpha():
            raise ValueError("La especialidad debe contener solo letras.")
        self._especialidad = valor

    def calcular_gasto(self):
        impuesto = self.precio_estandar * 0.15
        return self.precio_estandar + impuesto

    def es_urgente(self):
        return False

    #FUNCION QUE DA FORMATO A COMO SE MOSTRARAN LOS DATOS
    def mostrar_datos(self):
        print("* CONSULTA GENERAL *")
        print("Especialidad:", self.especialidad)
        print("Fecha:", self.fecha)
        print("Hora:", self.hora)
        print(self.paciente)
        print("¿Es urgente?:", self.es_urgente())
        print(f"Total a pagar: ${self.calcular_gasto():.2f}")
        print("*********\n")


    def _str_(self):

        return (f"CONSULTA GENERAL\nEspecialidad: {self.especialidad}\n"
                f"Total: ${self.calcular_gasto():.2f}")


#MUESTRA LA EJECUCION DE ESTA CLASE
if __name__ == "__main__":
    pac = Paciente("Ana", "Lopez", 30, "f", "ana@gmail.com")
    test = ConsultaGeneral("10/10/2024", "08:00", pac, "Cardiología")