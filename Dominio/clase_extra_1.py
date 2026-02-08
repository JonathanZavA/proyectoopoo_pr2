class Paciente:
    '''
             Clase que crea objetos para los datos de un paciente
    '''
    def __init__(self,nombre,apellido,edad,genero,correo,cedula):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.genero = genero
        self.correo = correo
        self.cedula = cedula


    # --- Propertys y Setters de nombre, apellido y edad ---
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, n_nombre):
        """Valida que el nombre no tenga números ni caracteres especiales."""
        n_nombre = ' '.join(str(n_nombre).split())
        if not n_nombre:
            raise ValueError('El nombre no puede estar vacío')

        if not n_nombre.replace(' ','').isalpha():
            raise ValueError('El nombre no puede tener números ni carácteres especiales.')

        self._nombre = n_nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, n_apellido):
        """Valida que el apellido no tenga números ni caracteres especiales."""
        n_apellido = ' '.join(str(n_apellido).split())
        if not n_apellido:
            raise ValueError('El apellido no puede estar vacío.')
        if not n_apellido.replace(' ','').isalpha():
            raise ValueError('El apellido no puede tener numeros ni carácteres especiales.')

        self._apellido = n_apellido

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, n_edad):
        """Valida que la edad sea un entero positivo entre 0 y 123."""
        str_edad = str(n_edad).replace(' ','')
        if str_edad.isdigit():
            n_edad = int(str_edad)
            if 0 <= n_edad <= 123:
                self._edad = n_edad
            else:
                raise ValueError('La edad no está dentro del rango permitido.')
        else:
            raise ValueError('Error: La edad tiene que ser un numero positivo y unicamente entero, enténtelo de nuevo.')



   # ---- Properys y Setters de genero y correo ----

    @property
    def genero(self):
        return self._genero

    @genero.setter
    def genero(self, n_genero):
        """Valida que el género sea 'm' o 'f'."""
        n_genero = str(n_genero).lower().strip()
        if n_genero not in ('m', 'f'):
            raise ValueError('El género está dentro de los valores permitidos (m,f)')

        self._genero = n_genero

    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, n_correo):
        """Valida formato básico de correo (sin espacios y con @)."""
        n_correo = str(n_correo).strip()
        if not n_correo or ' ' in n_correo:
            raise ValueError('El correo no puede estar vacío ni contener espacios.')

        dividido = n_correo.split('@')
        if len(dividido) != 2 or '.' not in dividido[1] or not dividido[0] or not dividido[1]:
            raise ValueError('Formato de correo incorrecto.')

        self._correo = n_correo


    @property
    def cedula(self):
        return self._cedula

    @cedula.setter
    def cedula(self,n_cedula):
        if not n_cedula:
            raise ValueError('Debe ingresar una cédula.')
        elif not n_cedula.isdigit():
            raise ValueError('Solo se permiten números (recuerde que el tamaño máximo son de 10 dígitos correspondiente al formato de una cédula, si no es así, saltará otro error.')
        elif n_cedula < 0 or n_cedula > 10:
            raise ValueError('Fuera del rango (10 digitos)')
        self._cedula = n_cedula



    # --- str de la instancia ---

    def __str__(self):
        # Información del paciente
        return f'- Datos del paciente -\nNombre: {self._nombre}\nApellido: {self._apellido}\nEdad: {self._edad}\nGénero: {self._genero}\nCorreo: {self._correo}'


# Muestra de la ejecución de la clase
if __name__ == '__main__':
    pac = Paciente('Maria', 'Merc',19,'f','merch@gmail.com')
    print(pac)