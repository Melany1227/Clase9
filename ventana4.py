import sys

from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QHBoxLayout, QFormLayout, QLineEdit, QApplication, \
    QPushButton, QDialog, QDialogButtonBox, QVBoxLayout

from cliente import Cliente


class Ventana4(QMainWindow):
    def __init__(self, anterior, cedula):
        super(Ventana4, self).__init__(None)

        self.ventanaAnterior = anterior

        self.cedulaUsuario = cedula

        self.setWindowTitle("Editar usuarios")
        # Poner el icono:
        self.setWindowIcon(QtGui.QIcon("imagenes/img.png"))

        self.ancho = 1000
        self.alto = 700

        self.resize(self.ancho, self.alto)

        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        self.fondo = QLabel(self)
        self.fondo.setStyleSheet("background-color: #FFDEAD;")
        self.setCentralWidget(self.fondo)

        self.horizontal = QHBoxLayout()
        self.horizontal.setContentsMargins(30, 30, 30, 30)

        # ---------- LAYOUT IZQUIERDO ----------
        self.ladoIzquierdo = QFormLayout()

        self.letrero1 = QLabel()

        self.letrero1.setText("Editar Cliente")

        self.letrero1.setFont(QFont("Andalem Mono", 20))

        self.letrero1.setStyleSheet("color: #000000;"
                                    "background-color: #FFDEAD;")

        self.ladoIzquierdo.addRow(self.letrero1)

        self.letrero2 = QLabel()

        self.letrero2.setFixedWidth(400)

        self.letrero2.setText("Por favor ingrese la información del cliente"
                              "\nen el formulario de abajo. Los campos marcados"
                              "\ncon asterisco son obligatorios.")

        self.letrero2.setFont(QFont("Andalem Mono", 10))

        # Le ponemos el color del texto:
        self.letrero2.setStyleSheet("background-color: #FFDEAD;"
                                    "color: #000000;"
                                    "padding-bottom: 10px;"
                                    "margin-bottom: 40px;"
                                    "margin-top: 20px;"
                                    "border: 2px solid #000000;"
                                    "border-left: none;"
                                    "border-right:none;"
                                    "border-top: none;")

        self.ladoIzquierdo.addRow(self.letrero2)

        self.nombreCompleto = QLineEdit()
        self.nombreCompleto.setFixedWidth(250)

        self.ladoIzquierdo.addRow("Nombre Completo*", self.nombreCompleto)

        self.usuario = QLineEdit()
        self.usuario.setFixedWidth(250)

        self.ladoIzquierdo.addRow("Usuario", self.usuario)

        self.contra = QLineEdit()
        self.contra.setFixedWidth(250)
        self.contra.setEchoMode(QLineEdit.Password)

        self.ladoIzquierdo.addRow("Password", self.contra)

        self.contra2 = QLineEdit()
        self.contra2.setFixedWidth(250)
        self.contra2.setEchoMode(QLineEdit.Password)

        self.ladoIzquierdo.addRow("Password", self.contra2)

        self.documento = QLineEdit()
        self.documento.setFixedWidth(250)

        self.ladoIzquierdo.addRow("Documento", self.documento)

        self.correo = QLineEdit()
        self.correo.setFixedWidth(250)

        self.ladoIzquierdo.addRow("Correo", self.correo)

        # -------------Boton Editar------------------

        self.botonEditar = QPushButton("Editar")
        self.botonEditar.setFixedWidth(90)
        self.botonEditar.setStyleSheet("color: #FFFFFF;"
                                       "background-color: #000000;"
                                       "margin-top: 40px;"
                                       "padding: 10px;")
        self.botonEditar.clicked.connect(self.accion_botonEditar)

        # -------------Boton Limpiar------------------

        self.botonlimpiar = QPushButton("Limpiar")
        self.botonlimpiar.setFixedWidth(90)
        self.botonlimpiar.setStyleSheet("color: #FFFFFF;"
                                        "background-color: #000000;"
                                        "margin-top: 40px;"
                                        "padding: 10px;")
        self.botonlimpiar.clicked.connect(self.accion_botonLimpiar)

        self.ladoIzquierdo.addRow(self.botonEditar, self.botonlimpiar)

        # -------------Boton Eliminar------------------

        self.botonEliminar = QPushButton("Eliminar")
        self.botonEliminar.setFixedWidth(90)
        self.botonEliminar.setStyleSheet("color: #FFFFFF;"
                                        "background-color: #000000;"
                                        "margin-top: 40px;"
                                        "padding: 10px;")
        self.botonEliminar.clicked.connect(self.accion_botonEliminar)

        self.ladoIzquierdo.addRow(self.botonEliminar)

        # -------------Boton Volver------------------

        self.botonVolver = QPushButton("Volver")
        self.botonVolver.setFixedWidth(90)
        self.botonVolver.setStyleSheet("color: #FFFFFF;"
                                       "background-color: #000000;"
                                       "margin-top: 40px;"
                                       "padding: 10px;")

        self.botonVolver.clicked.connect(self.metodo_botonVolver)

        self.ladoIzquierdo.addRow(self.botonVolver)

        self.horizontal.addLayout(self.ladoIzquierdo)

        # ---------LADO DERECHO-------------

        self.ladoDerecho = QFormLayout()
        self.ladoDerecho.setContentsMargins(100, 0, 0, 0)
        # letreros
        self.letrero3 = QLabel()
        self.letrero3.setText("Editar Recuperar Contraseña")
        self.letrero3.setFont(QFont("Andale mono", 20))
        self.letrero3.setStyleSheet('color:#000000; '
                                    'background-color: #FFDEAD')
        self.ladoDerecho.addRow(self.letrero3)

        self.letrero4 = QLabel()
        self.letrero4.setFixedWidth(400)
        self.letrero4.setText("Por favor ingrese la informacion para recuperar"
                              "\nla contraseña sobre los campos en blanco")
        self.letrero4.setFont(QFont("Andale mono", 10))
        self.letrero4.setStyleSheet("background-color: #FFDEAD;"
                                    "color: #000000';"
                                    "padding-bottom: 10px;"
                                    "margin-bottom: 40px;"
                                    "margin-top: 20px;"
                                    "border: 2px solid #000000;"
                                    "border-left: none;"
                                    "border-right:none;"
                                    "border-top: none;")


        self.ladoDerecho.addRow(self.letrero4)

        # Bloque 1

        self.labelPregunta1 = QLabel("Pregunta de verificacion 1")
        self.ladoDerecho.addRow(self.labelPregunta1)
        self.pregunta1 = QLineEdit()
        self.pregunta1.setFixedWidth(320)
        self.ladoDerecho.addRow(self.pregunta1)

        self.labelRespuesta1 = QLabel("Respuesta de verificacion 1")
        self.ladoDerecho.addRow(self.labelRespuesta1)
        self.respuesta1 = QLineEdit()
        self.respuesta1.setFixedWidth(320)
        self.ladoDerecho.addRow(self.respuesta1)

        self.labelPregunta2 = QLabel("Pregunta de verificacion 2")
        self.ladoDerecho.addRow(self.labelPregunta2)
        self.pregunta2 = QLineEdit()
        self.pregunta2.setFixedWidth(320)
        self.ladoDerecho.addRow(self.pregunta2)

        self.labelRespuesta2 = QLabel("Respuesta de verificacion 2")
        self.ladoDerecho.addRow(self.labelRespuesta2)
        self.respuesta2 = QLineEdit()
        self.respuesta2.setFixedWidth(320)
        self.ladoDerecho.addRow(self.respuesta2)

        self.labelPregunta3 = QLabel("Pregunta de verificacion 3")
        self.ladoDerecho.addRow(self.labelPregunta3)
        self.pregunta3 = QLineEdit()
        self.pregunta3.setFixedWidth(320)
        self.ladoDerecho.addRow(self.pregunta3)

        self.labelRespuesta3 = QLabel("Respuesta de verificacion 3")
        self.ladoDerecho.addRow(self.labelRespuesta3)
        self.respuesta3 = QLineEdit()
        self.respuesta3.setFixedWidth(320)
        self.ladoDerecho.addRow(self.respuesta3)

        self.horizontal.addLayout((self.ladoDerecho))

        # --------- PONER AL FINAL -------
        self.fondo.setLayout(self.horizontal)

        self.ventanaDialogo = QDialog(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint)

        self.ventanaDialogo.resize(300, 500)

        self.botonAceptar = QDialogButtonBox.Ok
        self.opciones = QDialogButtonBox(self.botonAceptar)
        self.opciones.accepted.connect(self.ventanaDialogo.accept)

        self.ventanaDialogo.setWindowModality(Qt.ApplicationModal)

        self.vertical = QVBoxLayout()

        self.mensaje = QLabel("")

        self.mensaje.setStyleSheet('background-color: #000000; color: #FFFFFF; padding: 10px;')
        self.vertical.addWidget(self.mensaje)
        self.vertical.addWidget(self.opciones)

        self.ventanaDialogo.setLayout(self.vertical)

        self.cargar_datos()




    def accion_botonEditar(self):
        self.datosCorrectos = True
        self.ventanaDialogo.setWindowTitle("Formulario de edición")

        if (
                self.contra.text() != self.contra2.text()
        ):
            self.datosCorrectos = False

            self.mensaje.setText("Las contraseñas no son iguales")

            # Hacemos que la ventana de dialogo se vea:
            self.ventanaDialogo.exec_()

        if (
                self.nombreCompleto.text() == ''
                or self.usuario.text() == ''
                or self.contra.text() == ''
                or self.contra2.text() == ''
                or self.documento.text() == ''
                or self.correo.text() == ''
                or self.pregunta1.text() == ''
                or self.respuesta1.text() == ''
                or self.pregunta2.text() == ''
                or self.respuesta2.text() == ''
                or self.pregunta3.text() == ''
                or self.respuesta3.text() == ''
        ):
            self.datosCorrectos = False

            self.mensaje.setText("Debe seleccionar un usuario con documento válido")

            # Hacemos que la ventana de dialogo se vea:
            self.ventanaDialogo.exec_()

            self.metodo_botonVolver()

        if self.datosCorrectos:

            self.file = open('datos/clientes.txt', 'rb')
            usuarios = []

            while self.file:
                linea = self.file.readline().decode('UTF-8')
                lista = linea.split(";")
                # Separa si ya no hay mas registros en el archivo
                if linea == '':
                    break
                # creamos un objeto tipo cliente llamado u
                u = Cliente(
                    lista[0],
                    lista[1],
                    lista[2],
                    lista[3],
                    lista[4],
                    lista[5],
                    lista[6],
                    lista[7],
                    lista[8],
                    lista[9],
                    lista[10],
                )
                # metemos el objeto en la lista de usuarios:
                usuarios.append(u)

            # cerramos el archivo
            self.file.close()

            existeDocumento = False

            for u in usuarios:
                if int(u.documento) == self.cedulaUsuario:
                    u.usuario = self.usuario.text()
                    u.contra = self.contra.text()
                    u.correo = self.correo.text()
                    u.pregunta1 = self.pregunta1.text()
                    u.respuesta1 = self.respuesta1.text()
                    u.pregunta2 = self.pregunta2.text()
                    u.respuesta2 = self.respuesta2.text()
                    u.pregunta3 = self.pregunta3.text()
                    u.respuesta3 = self.respuesta3.text()
                    existeDocumento = True
                    break

            if (
                    not existeDocumento
            ):
                # escribimos el texto explicativo:
                self.mensaje.setText("No existe un usuario con este documento:\n"
                                     + str(self.cedulaUsuario))

                # hacemos que la ventanaDIalogo se vea:
                self.ventanaDialogo.exec_()

            self.file = open('datos/clientes.txt', 'wb')

            for u in usuarios:
                self.file.write(bytes(u.nombreCompleto + ";"
                                      + u.usuario + ";"
                                      + u.contra + ";"
                                      + u.documento + ";"
                                      + u.correo + ";"
                                      + u.pregunta1 + ";"
                                      + u.respuesta1 + ";"
                                      + u.pregunta2 + ";"
                                      + u.respuesta2 + ";"
                                      + u.pregunta3 + ";"
                                      + u.respuesta3, encoding='UTF-8'))
            self.file.close()

            if (
                    existeDocumento
            ):
                # escribimos el texto explicativo:
                self.mensaje.setText("Usuario actualizado correctamente!")

                self.ventanaDialogo.exec_()
                self.accion_botonLimpiar()
                self.metodo_botonVolver()

            self.file = open('datos/clientes.txt', 'rb')
            while self.file:
                linea = self.file.readline().decode('UTF-8')
                print(linea)
                if linea == '':
                    break
            self.file.close()


    def accion_botonLimpiar(self):
        self.nombreCompleto.setText('')
        self.usuario.setText('')
        self.contra.setText('')
        self.contra2.setText('')
        self.documento.setText('')
        self.correo.setText('')
        self.pregunta1.setText('')
        self.respuesta1.setText('')
        self.pregunta2.setText('')
        self.respuesta2.setText('')
        self.pregunta3.setText('')
        self.respuesta3.setText('')

    def metodo_botonVolver(self):
        self.hide()
        self.ventanaAnterior.show()

    def accion_botonEliminar(self):
        self.datosCorrectos = True

        self.eliminar = False

        if (
                self.nombreCompleto.text() == ''
                or self.usuario.text() == ''
                or self.contra.text() == ''
                or self.documento.text() == ''
                or self.correo.text() == ''
                or self.pregunta1.text() == ''
                or self.respuesta1.text() == ''
                or self.pregunta2.text() == ''
                or self.respuesta2.text() == ''
                or self.pregunta3.text() == ''
                or self.respuesta3.text() == ''
        ):
            self.datosCorrectos = False

            self.mensaje.setText("Debe seleccionar un usuario con documento válido!")

            self.ventanaDialogo.exec_()

            self.metodo_botonVolver()

        if self.datosCorrectos:
            self.ventanaDialogoEliminar = QDialog(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint)

            # Definimos el tamaño de la ventana:
            self.ventanaDialogoEliminar.resize(300, 150)

            # Configuramos la ventana para que sea modal:
            self.ventanaDialogoEliminar.setWindowModality(Qt.ApplicationModal)

            # Creamos un layout vertical:
            self.verticalEliminar = QVBoxLayout()

            # Creamos un label para los mensajes:
            self.mensajeEliminar = QLabel("¿Está seguro que desea eliminar este registro de usuario?")

            # Le ponemos estilo al label mensaje:
            self.mensajeEliminar.setStyleSheet("background-color: #000000 ; color: #FFFFFF; padding: 10px;")

            # agregamos el label de mensajes
            self.verticalEliminar.addWidget(self.mensajeEliminar)

            self.opcionesEliminar = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
            self.opcionesBox = QDialogButtonBox(self.opcionesEliminar)

            self.opcionesBox.accepted.connect(self.ok_opcion)
            self.opcionesBox.rejected.connect(self.cancel_opcion)

            # Agregamos las opciones de los botones.
            self.verticalEliminar.addWidget(self.opcionesBox)

            # Establecemos el layout para la ventana de dialogo:
            self.ventanaDialogoEliminar.setLayout(self.verticalEliminar)

            self.ventanaDialogoEliminar.exec_()

        if self.eliminar:
            # Abrimos el archivo en modo de lectura:
            self.file = open('datos/clientes.txt', 'rb')

            # Lista vacia para guardar los usuarios
            usuarios = []

            while self.file:
                linea = self.file.readline().decode('UTF-8')
                lista = linea.split(";")
                # Separa si ya no hay mas registros en el archivo
                if linea == '':
                    break
                # creamos un objeto tipo cliente llamado u
                u = Cliente(
                    lista[0],
                    lista[1],
                    lista[2],
                    lista[3],
                    lista[4],
                    lista[5],
                    lista[6],
                    lista[7],
                    lista[8],
                    lista[9],
                    lista[10],
                )
                # metemos el objeto en la lista de usuarios:
                usuarios.append(u)

                # cerramos el archivo
            self.file.close()

            existeDocumento = False

            for u in usuarios:
                if int(u.documento) == self.cedulaUsuario:
                    usuarios.remove(u)
                    existeDocumento = True
                    break

            # Abrimos el archivo en modo de lectura:
            self.file = open('datos/clientes.txt', 'wb')

            for u in usuarios:
                self.file.write(bytes(u.nombreCompleto + ";"
                                      + u.usuario + ";"
                                      + u.contra + ";"
                                      + u.documento + ";"
                                      + u.correo + ";"
                                      + u.pregunta1 + ";"
                                      + u.respuesta1 + ";"
                                      + u.pregunta2 + ";"
                                      + u.respuesta2 + ";"
                                      + u.pregunta3 + ";"
                                      + u.respuesta3, encoding='UTF-8'))
            self.file.close()

            if (
                    existeDocumento

            ):
                self.mensaje.setText("Usuario eliminado exitosamente!")

                self.ventanaDialogo.exec_()
                self.accion_botonLimpiar()
                self.metodo_botonVolver()

    def cargar_datos(self):
        self.file = open('datos/clientes.txt', 'rb')

        usuarios = []

        while self.file:
            linea = self.file.readline().decode('UTF-8')
            lista = linea.split(";")
            if linea == '':
                break
            u = Cliente(
                lista[0],
                lista[1],
                lista[2],
                lista[3],
                lista[4],
                lista[5],
                lista[6],
                lista[7],
                lista[8],
                lista[9],
                lista[10],
            )
            # metemos el objeto en la lista de usuarios:
            usuarios.append(u)

            # cerramos el archivo
        self.file.close()

        # en este punto ya tenemos la lista users con todos los usuarios

        # variable para controlar si exite el docuemento
        existeDocumento = False

        # Buscamos en la lista users por users para ver si existe la cedula:
        for u in usuarios:
            if int(u.documento) == self.cedulaUsuario:
                self.nombreCompleto.setText(u.nombreCompleto)
                # Con esto el nombre no se puede editar
                self.nombreCompleto.setReadOnly(True)
                self.usuario.setText(u.usuario)
                self.contra.setText(u.contra)
                self.contra2.setText(u.contra)
                self.documento.setText(u.documento)
                self.documento.setReadOnly(True)
                self.correo.setText(u.correo)
                self.pregunta1.setText(u.pregunta1)
                self.respuesta1.setText(u.respuesta1)
                self.pregunta2.setText(u.pregunta2)
                self.respuesta2.setText(u.respuesta2)
                self.pregunta3.setText(u.pregunta3)
                self.respuesta3.setText(u.respuesta3)
                # indicamos que encontramos el dodumento:
                existeDocumento = True
                # paramos el for
                break

        if (
                not existeDocumento
        ):
            # escribimos el texto explicativo:
            self.mensaje.setText("No existe un usuario con este documento:\n"
                                 + str(self.cedulaUsuario))

            # hacemos que la ventanaDIalogo se vea:
            self.ventanaDialogo.exec_()
            self.metodo_botonVolver()



    def ok_opcion(self):
        self.ventanaDialogoEliminar.close()
        self.eliminar = True

    def cancel_opcion(self):
        self.ventanaDialogoEliminar.close()



if __name__ == '__main__':
    # hacer que la aplicacion se genere
    app = QApplication(sys.argv)

    # crear un objeto de tipo Ventana4 con el nombre de ventana1
    ventana4 = Ventana4()
    # hacer que objeto ventana 4 se vea
    ventana4.show()

    sys.exit(app.exec_())