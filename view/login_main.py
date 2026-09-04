from PyQt5.QtWidgets import QFrame, QApplication, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import sys

class main(QFrame):
    def __init__(self):
        super().__init__()

        self.setupUi()
        self.crear_campos()

    def setupUi(self):
        # Atributos Principales de la Ventana
        self.setWindowTitle("Iniciar Sesión")                # Título de la Ventana
        self.setFixedSize(800, 600)                          # Tamaño de la Ventana en Pixeles
        self.setStyleSheet("background-color: #B2FFFF;")     # Color de Fondo de la Ventana

        # Layout Principal
        self.main_layout = QVBoxLayout(self) # Layout Principal Vertical
        self.setLayout(self.main_layout)    # Añadir el Layout Principal a la Ventana


    def crear_campos(self):
        self.layout_login = QVBoxLayout() # Layout Vertical para el Login
        self.main_layout.addLayout(self.layout_login) # Añadir el Layout del Login al Layout Principal

        # Imagen del Login
        self.label_imagen = QLabel() # Etiqueta para la Imagen del Login
        self.pixmap_imagen = QPixmap("Resources/img/login_icon.png") # Cargar la Imagen del Login
        self.label_imagen.setPixmap(self.pixmap_imagen) # Añadir la Imagen a la Etiqueta
        self.label_imagen.setAlignment(Qt.AlignCenter) # Alinear la Imagen al Centro
        self.layout_login.addWidget(self.label_imagen) # Añadir la Imagen al Layout del
        
        self.label_title = QLabel("Iniciar Sesión") # Título del Login
        self.label_title.setStyleSheet("font-size: 30px; font-weight: bold; color: #000000; border: 1px solid #222; border-radius: 5px;") # Estilo del Título
        self.label_title.setAlignment(Qt.AlignCenter) # Alinear el Título al Centro
        self.layout_login.addWidget(self.label_title) # Añadir el Título al Layout del Login

        self.layout_h_username = QHBoxLayout() # Layout Horizontal para los Campos de Usuario y Contraseña
        self.layout_login.addLayout(self.layout_h_username) # Añadir el Layout Horizontal al Layout del



        self.label_username = QLabel("Nombre de Usuario:") # Etiqueta para el Nombre de Usuario
        self.label_username.setStyleSheet("font-size: 20px; font-weight: bold; color: #000000;") # Estilo de la Etiqueta
        self.label_username.setAlignment(Qt.AlignLeft) # Alinear la Etiqueta a la Izquierda
        self.layout_h_username.addWidget(self.label_username) # Añadir la Etiqueta al Layout Horizontal

        self.entry_username = QLineEdit() # Entrada de Texto para el Nombre de Usuario
        self.entry_username.setPlaceholderText("Nombre de Usuario") # Texto de Ayuda para el Nombre de Usuario
        self.entry_username.setStyleSheet("max-width: 300px; min-width: 20px; font-size: 20px; padding: 10px; background-color: #FFFFFF; border: 1px solid #222; border-radius: 5px;") # Estilo de la Entrada de Texto
        self.layout_h_username.addWidget(self.entry_username) # Añadir la Entrada de Texto al Layout Horizontal

        self.layout_h_password = QHBoxLayout() # Layout Horizontal para la Contraseña
        self.layout_login.addLayout(self.layout_h_password) # Añadir el Layout Horizontal al Layout del Login

        self.label_password = QLabel("Contraseña:") # Etiqueta para la Contraseña
        self.label_password.setStyleSheet("font-size: 20px; font-weight: bold; color: #000000;") # Estilo de la Etiqueta
        self.label_password.setAlignment(Qt.AlignLeft) # Alinear la Etiqueta a la Izquierda
        self.layout_h_password.addWidget(self.label_password) # Añadir la Etiqueta al Layout Horizontal

        self.layout_login.addLayout(self.layout_h_password) # Añadir el Layout Horizontal al Layout del Login

        self.entry_password = QLineEdit() # Entrada de Texto para el Nombre de Usuario
        self.entry_password.setPlaceholderText("Contraseña") # Texto de Ayuda para el Nombre de Usuario
        self.entry_password.setStyleSheet("max-width: 300px; min-width: 20px; font-size: 20px; padding: 10px; background-color: #FFFFFF; border: 1px solid #222; border-radius: 5px;") # Estilo de la Entrada de Texto
        self.entry_password.setEchoMode(QLineEdit.Password) # Ocultar el Texto de la Contraseña
        self.layout_h_password.addWidget(self.entry_password) # Añadir la Entrada de Texto al Layout Horizontal

        self.btn_login = QPushButton("Iniciar Sesión") # Botón de Iniciar Sesión
        self.btn_login.setStyleSheet("font-size: 20px; padding: 15px; background-color: #00FF00; border: 1px solid #222; border-radius: 5px;") # Estilo del Botón
        self.layout_login.addWidget(self.btn_login) # Añadir el Botón al Layout del Login






if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = main()
    win.show()
    app.exec()
    