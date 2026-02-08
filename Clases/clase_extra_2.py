class Gestor:
    def __init__(self):
        # Inicializa la lista para guardar los servicios y los clasificados
        self.servicios = []
        self.urgentes = []
        self.no_urgentes = []

    def agregar_servicio(self, servicio):
        # Añade un nuevo servicio a la lista general
        self.servicios.append(servicio)

    def clasificar_servicios(self):
        # Separa y devuelve los servicios en dos listas: urgentes y no urgentes
        for servicio in self.servicios:
            if servicio.es_urgente():
                self.urgentes.append(servicio)
            else:
                self.no_urgentes.append(servicio)

        return self.urgentes, self.no_urgentes

    def calcular_total_gastos(self):
        # Calcula la suma total de los costos de todos los servicios
        total = 0
        for servicio in self.servicios:
            total += servicio.calcular_gasto()
        return total

    def __str__(self):
        # Muestra la información
        return f'Servicios registrados: {self.servicios}\nUrgentes:{self.urgentes}\nNo urgentes:{self.no_urgentes}'



if __name__ == '__main__':
    gestor = Gestor
    print(gestor)