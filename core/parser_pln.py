# core/parser_pln.py
import sqlite3
from .database import get_db_connection

_expresiones_cache = {}

def cargar_expresiones_cache():
    global _expresiones_cache
    if _expresiones_cache:
        return

    conn = get_db_connection()
    if not conn:
        print("Error: No se pudo conectar a la BD para cargar caché de PLN.")
        return

    try:
        cursor = conn.cursor()
        query = """
            SELECT eu.frase, s.codigo_sintoma
            FROM expresiones_usuario eu
            JOIN sintomas s ON eu.id_sintoma = s.id_sintoma;
        """
        cursor.execute(query)
        rows = cursor.fetchall()
        
        _expresiones_cache = {row["frase"].lower().strip(): row["codigo_sintoma"] for row in rows}
        print(f"Cargadas {len(_expresiones_cache)} expresiones al caché de PLN.")
        
    except sqlite3.Error as e:
        print(f"Error al cargar caché de PLN: {e}")
    finally:
        if conn:
            conn.close()

def mapear_frase_a_sintoma(frase_usuario: str) -> str | None:
    if not _expresiones_cache:
        cargar_expresiones_cache()

    frase_normalizada = frase_usuario.lower().strip()

    if frase_normalizada in _expresiones_cache:
        return _expresiones_cache[frase_normalizada]

    for frase_db, codigo in _expresiones_cache.items():
        if frase_normalizada in frase_db:
            return codigo

    palabras_usuario = set(frase_normalizada.split())
    
    mejor_coincidencia = None
    max_coincidencias = 0

    for frase_db, codigo in _expresiones_cache.items():
        palabras_db = set(frase_db.split())
        
        coincidencias = len(palabras_usuario.intersection(palabras_db))
        
        if coincidencias > max_coincidencias:
            max_coincidencias = coincidencias
            mejor_coincidencia = codigo
            
    if max_coincidencias > 0:
        return mejor_coincidencia
            
    return None