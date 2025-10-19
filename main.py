import sys
from core.database import init_db

def main():
    try:
        init_db()
    except Exception as e:
        print(f"Error al inicializar la base de datos: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()