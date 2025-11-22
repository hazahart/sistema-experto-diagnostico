import sqlite3
import sys
from pathlib import Path

def get_base_path():
    """ 
    Obtiene la ruta base correcta.
    Si está ejecutándose como .exe (PyInstaller), usa sys._MEIPASS.
    Si está en desarrollo, usa la ruta del archivo actual.
    """
    if hasattr(sys, '_MEIPASS'):
        return Path(sys._MEIPASS)
    return Path(__file__).resolve().parent.parent

BASE_DIR = get_base_path()

# Rutas a la base de datos y al esquema
DB_DIR = BASE_DIR / "data" / "database"
DB_PATH = DB_DIR / "diagnostico.db"
SCHEMA_PATH = DB_DIR / "schema.sql"
DATA_SQL_PATH = DB_DIR / "data.sql"

def get_db_connection() -> sqlite3.Connection | None:
    try:
        # Se asegura de que el directorio de la base de datos exista
        DB_DIR.mkdir(parents=True, exist_ok=True)

        conn = sqlite3.connect(DB_PATH, check_same_thread=False)
        conn.row_factory = sqlite3.Row

        # Habilitar el soporte de llaves foráneas
        conn.execute("PRAGMA foreign_keys = ON;")

        return conn
    except sqlite3.Error as e:
        print(f"Error fatal al conectar con la base de datos en {DB_PATH}: {e}")
        return None


def init_db():
    # Verificar si el archivo de esquema existe antes de continuar
    if not SCHEMA_PATH.exists():
        print(f"Error: No se encontró el archivo de esquema en {SCHEMA_PATH}")
        print("Verifica que el archivo 'schema.sql' esté en 'data/database/'.")
        return

    try:
        # Leer el contenido completo del archivo SQL
        with open(SCHEMA_PATH, 'r', encoding='utf-8') as f:
            schema_sql = f.read()
    except Exception as e:
        print(f"Error al leer el archivo schema.sql: {e}")
        return

    # Obtener conexión y ejecutar el script
    conn = None
    try:
        conn = get_db_connection()
        if conn:
            conn.executescript(schema_sql)
            conn.commit()
            print(f"Esquema creado correctamente en: {DB_PATH}")

            print(f"Intentando cargar datos iniciales desde: {DATA_SQL_PATH}")
            if not DATA_SQL_PATH.exists():
                print(f"Advertencia: No se encontró archivo 'data.sql' en {DATA_SQL_PATH}.")
                print("La base de datos se creó, pero está vacía.")
            else:
                try:
                    with open(DATA_SQL_PATH, 'r', encoding='utf-8') as f:
                        data_sql = f.read()
                    
                    conn.executescript(data_sql)
                    conn.commit()
                    print("Datos cargados correctamente.")
                except sqlite3.Error as e:
                    print(f"Error al ejecutar el script de datos (data.sql): {e}")

        else:
            print("No se pudo obtener la conexión a la base de datos.")
            
    except sqlite3.Error as e:
        print(f"Error al ejecutar el script de inicialización: {e}")
    finally:
        if conn:
            conn.close()