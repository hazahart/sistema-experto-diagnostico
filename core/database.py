import sqlite3
from pathlib import Path

try:
    # Ruta al archivo actual
    CURRENT_FILE_PATH = Path(__file__).resolve()

    # Ruta al directorio 'core/'
    CORE_DIR = CURRENT_FILE_PATH.parent
    # Ruta al directorio raíz del proyecto 'sistema_experto_diagnostico/'
    BASE_DIR = CORE_DIR.parent
except NameError:
    BASE_DIR = Path.cwd()

# Rutas a la base de datos y al esquema
DB_DIR = BASE_DIR / "data" / "database"
DB_PATH = DB_DIR / "diagnostico.db"
SCHEMA_PATH = DB_DIR / "schema.sql"


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
    print(f"Intentando inicializar la base de datos desde: {SCHEMA_PATH}")

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
            # .executescript() es necesario para ejecutar múltiples sentencias SQL
            conn.executescript(schema_sql)
            conn.commit()
            print(f"Base de datos inicializada exitosamente en: {DB_PATH}")
        else:
            print("No se pudo obtener la conexión a la base de datos para la inicialización.")
    except sqlite3.Error as e:
        print(f"Error al ejecutar el script de inicialización: {e}")
    finally:
        if conn:
            conn.close()