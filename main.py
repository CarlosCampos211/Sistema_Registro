from model.conexion_db import ConexionDB
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys


class main(QMainWindow):
    def __init__(self):
        super().__init__()
        ConexionDB().crear_tablas
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = main()
    win.show()
    app.exec()
    