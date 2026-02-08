import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
# Se asume que la clase Paciente está en la carpeta Clases, archivo Dominio.py
from Dominio.clase_extra_1 import Paciente
from UI.vtnPrincipal import Ui_btn_buscar
from Datos.paciente_dao import PacienteDAO


class ServicioPacientes(QMainWindow):
    def __init__(self):
        super(ServicioPacientes, self).__init__()
        # Inicialización de la interfaz de usuario
        self.ui = Ui_btn_buscar()
        self.ui.setupUi(self)

        # Conexión de eventos a los botones
        self.ui.btn_guardar.clicked.connect(self.guardar)
        self.ui.btn_actualizar.clicked.connect(self.actualizar)
        self.ui.btn_eliminar.clicked.connect(self.eliminar)
        self.ui.btn_limpiar.clicked.connect(self.limpiar)
        # El botón de búsqueda utiliza el nombre btn_buscar_
        self.ui.btn_buscar_.clicked.connect(self.buscar)

    def limpiar(self):
        """Restablece todos los componentes de la interfaz al estado inicial."""
        self.ui.txt_nombre.setText("")
        self.ui.txt_apellido.setText("")
        self.ui.txt_edad.setText("")
        self.ui.txt_correo.setText("")
        self.ui.txt_cedula.setText("")
        self.ui.txt_buscar.setText("")
        self.ui.btn_genero.setCurrentIndex(0)
        self.ui.txt_nombre.setFocus()

    def guardar(self):
        """Captura datos, crea el objeto de dominio y lo envía al DAO."""
        nombre = self.ui.txt_nombre.text()
        apellido = self.ui.txt_apellido.text()
        edad = self.ui.txt_edad.text()
        genero = self.ui.btn_genero.currentText()
        correo = self.ui.txt_correo.text()
        cedula = self.ui.txt_cedula.text()

        # Validación de campos vacíos
        if nombre == "":
            QMessageBox.warning(self, "Advertencia", "Debe ingresar un Nombre")
        elif apellido == "":
            QMessageBox.warning(self, "Advertencia", "Debe ingresar un Apellido")
        elif edad == "":
            QMessageBox.warning(self, "Advertencia", "Debe ingresar un edad")
        elif genero == "Selecione...":
            QMessageBox.warning(self, "Advertencia", "Debe seleccionar un Sexo")
        elif correo == "":
            QMessageBox.warning(self, "Advertencia", "Debe ingresar un correo")
        elif cedula == "":
            QMessageBox.warning(self, "Advertencia", "Debe ingresar un cedua")


        else:
            try:
                # Creación del objeto de dominio
                persona = Paciente(nombre=nombre, apellido=apellido, edad=edad, genero=genero, correo=correo,
                                   cedula=cedula)

                # Inserción en la base de datos
                PacienteDAO.insertar_paciente(persona)

                # Usamos self.statusBar() directamente de QMainWindow
                QMessageBox.information(self, "Éxito", "Paciente guardado")
                self.limpiar()
            except ValueError as e:
                QMessageBox.warning(self, "Advertencia", f'Error: {e}')
            except Exception as e:
                QMessageBox.critical(self, "Error Crítico", f"Ocurrió un error: {e}")

    def buscar(self):
        """Busca al paciente por cédula y llena los campos si existe."""
        cedula = self.ui.txt_buscar.text()
        if not cedula:
            QMessageBox.warning(self, "Advertencia", "Ingrese una cédula para buscar")
            return

        registro = PacienteDAO.seleccionar_paciente(cedula)
        if registro:
            # Mapeo de columnas según la tabla SQL
            self.ui.txt_nombre.setText(str(registro[1]))
            self.ui.txt_apellido.setText(str(registro[2]))
            self.ui.txt_edad.setText(str(registro[3]))
            index = self.ui.btn_genero.findText(str(registro[4]))
            self.ui.btn_genero.setCurrentIndex(index if index >= 0 else 0)
            self.ui.txt_correo.setText(str(registro[5]))
            self.ui.txt_cedula.setText(str(registro[6]))
            self.statusBar().showMessage("Paciente encontrado", 1500)
        else:
            self.statusBar().showMessage("No se encontró el paciente", 1500)

    def actualizar(self):
        """Actualiza los datos del paciente cargado actualmente."""
        if self.ui.btn_genero.currentIndex() == 0 or not self.ui.txt_cedula.text():
            QMessageBox.warning(self, "Advertencia", "Cargue un paciente y complete los campos")
            return

        try:
            persona = Paciente(
                nombre=self.ui.txt_nombre.text(),
                apellido=self.ui.txt_apellido.text(),
                edad=self.ui.txt_edad.text(),
                genero=self.ui.btn_genero.currentText(),
                correo=self.ui.txt_correo.text(),
                cedula=self.ui.txt_cedula.text()
            )

            PacienteDAO.actualizar_paciente(persona)
            QMessageBox.information(self, "Éxito", "Paciente actualizado\n(puede verificarlo en su base de datos)")
            self.limpiar()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al actualizar: {e}")

    def eliminar(self):
        """Elimina el registro de forma directa sin confirmaciones adicionales."""
        cedula = self.ui.txt_cedula.text().strip()
        if not cedula:
            cedula = self.ui.txt_buscar.text().strip()

        if not cedula:
            QMessageBox.warning(self, "Advertencia", "Ingrese o busque una cédula para eliminar")
            return

        try:
            PacienteDAO.eliminar_paciente(cedula)
            QMessageBox.information(self, "Éxito", "Paciente eliminado")
            self.limpiar()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al eliminar: {e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = ServicioPacientes()
    ventana.show()
    sys.exit(app.exec())