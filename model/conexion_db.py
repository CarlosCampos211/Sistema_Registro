import os
import sqlite3

# Determina como se hace la base de datos
class ConexionDB:
    def __init__(self, nombre_db="database/Sistema_Registro.db"):
        proyecto_raiz = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        self.base_datos = os.path.abspath(os.path.join(proyecto_raiz, nombre_db))
        carpeta_db = os.path.dirname(self.base_datos)
        if carpeta_db and not os.path.exists(carpeta_db):
            os.makedirs(carpeta_db, exist_ok=True)
        self.conexion = sqlite3.connect(self.base_datos)
        self.cursor = self.conexion.cursor()
        self.crear_tablas()

    # Método que Crea las Tablas de la Base de Datos
    def crear_tablas(self):
        """Crea todas las tablas de la base de datos"""
        try:
            conn = self.conexion
            cursor = conn.cursor()
        
            # Tabla Usuario
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Usuario (
                    id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
                    cedula TEXT UNIQUE NOT NULL,
                    contraseña TEXT NOT NULL,
                    id_preguntas_seguridad INTENGER,
                    id_configuracion INTENGER,
                    FOREIGN KEY (id_preguntas_seguridad) REFERENCES Preguntas_Seguridad (id_preguntas_seguridad)
                    FOREIGN KEY (id_configuracion) REFERENCES Configuracion (id_configuracion)
                )
            ''')

            cursor.execute('''
                    CREATE TABLE IF NOT EXISTS Ingresantes (
                        cedula INTENGER PRIMARY KEY,
                        nombre TEXT UNIQUE NOT NULL,
                        apellido TEXT UNIQUE NOT NULL,
                        id_pnf INTENGER, 
                        id_sexo INTENGER NOT NULL,
                        id_rol INTENGER NOT NULL,
                        FOREIGN KEY (id_pnf) REFERENCES Pnf (id_pnf),
                        FOREIGN KEY (id_sexo) REFERENCES Sexo (id_sexo),
                        FOREIGN KEY (id_rol) REFERENCES Rol (id_rol)
                    )
                        ''')

            # Tabla Pnf
            cursor.execute('''
                        CREATE TABLE IF NOT EXISTS Pnf (
                            id_pnf INTENGER PRIMARY KEY,
                            pnf NOT NULL
                        )
                        ''')

            # Tabla Sexo
            cursor.execute('''
                        CREATE TABLE IF NOT EXISTS Sexo (
                            id_sexo INTENGER PRIMARY KEY,
                            sexo NOT NULL
                                    )
                                    ''')

            # Tabla Rol
            cursor.execute('''
                        CREATE TABLE IF NOT EXISTS Rol (
                            id_rol INTENGER PRIMARY KEY,
                            rol NOT NULL
                        )
                        ''')

            # Tabla Registros
            cursor.execute('''
                        CREATE TABLE IF NOT EXISTS Registros (
                            cedula INTENGER PRIMARY KEY,
                            maquina INTENGER NOT NULL, 
                            id_horario INTENGER NOT NULL,
                            FOREIGN KEY (id_horario) REFERENCES Horario (id_horario)
                        )
                            ''')

            # Tabla Horario
            cursor.execute('''
                        CREATE TABLE IF NOT EXISTS Horario (
                            id_horario INTENGER PRIMARY KEY,
                            hora_entrada INTENGER NOT NULL,
                            hora_salida  INTENGER NOT NULL
                        )
                                    ''')

            
            # Tabla Tema
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Tema (
                    id_tema INTEGER PRIMARY KEY AUTOINCREMENT,
                    tema TEXT NOT NULL
                )
            ''')
            
            # Tabla Fuente
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Fuente (
                    id_fuente INTEGER PRIMARY KEY AUTOINCREMENT,
                    tamano INTEGER,
                    famila TEXT,
                    font TEXT
                )
            ''')
                     
            # Tabla Configuración
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Configuracion (
                    id_configuracion INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_tema INTEGER,
                    id_fuente INTEGER,
                    FOREIGN KEY (id_tema) REFERENCES Tema (id_tema),
                    FOREIGN KEY (id_fuente) REFERENCES Fuente (id_fuente),
                )
            ''')

            # Asegurar que la columna resolucion exista en bases de datos antiguas
            cursor.execute("PRAGMA table_info(Configuracion)")
            columnas_config = [fila[1] for fila in cursor.fetchall()]
            if "resolucion" not in columnas_config:
                cursor.execute("ALTER TABLE Configuracion ADD COLUMN resolucion TEXT")

            conn.commit()
        except sqlite3.Error:
            pass

    def Cerrar(self):
        self.conexion.commit()
        self.conexion.close()