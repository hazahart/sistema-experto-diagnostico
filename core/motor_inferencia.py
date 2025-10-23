import sqlite3
from .database import get_db_connection

def diagnosticar(lista_codigos_sintomas: list) -> dict:
    if not lista_codigos_sintomas:
        return {"error": "No se proporcionaron síntomas."}

    conn = get_db_connection()
    if not conn:
        return {"error": "No se pudo conectar a la base de datos."}

    try:
        cursor = conn.cursor()

        placeholders = ','.join(['?'] * len(lista_codigos_sintomas))

        query = f"""
            SELECT
                f.nombre_fallo,
                f.solucion_recomendada,
                COUNT(f.id_fallo) AS coincidencias
            FROM reglas r
            JOIN sintomas s ON r.id_sintoma = s.id_sintoma
            JOIN fallos f ON r.id_fallo = f.id_fallo
            WHERE s.codigo_sintoma IN ({placeholders})
            GROUP BY f.id_fallo
            ORDER BY coincidencias DESC
            LIMIT 1;
        """
        
        cursor.execute(query, lista_codigos_sintomas)
        resultado = cursor.fetchone()

        if resultado:
            return {
                "fallo": resultado["nombre_fallo"],
                "solucion": resultado["solucion_recomendada"],
                "coincidencias": resultado["coincidencias"]
            }
        else:
            return {"fallo": "Desconocido", "solucion": "No se encontró un diagnóstico con los síntomas proporcionados."}

    except sqlite3.Error as e:
        print(f"Error en el motor de inferencia: {e}")
        return {"error": f"Error de consulta: {e}"}
    finally:
        if conn:
            conn.close()

def sugerir_siguientes_pasos(lista_codigos_sintomas: list) -> list:
    if not lista_codigos_sintomas:
        return []

    conn = get_db_connection()
    if not conn:
        return []

    try:
        cursor = conn.cursor()
        
        placeholders_actuales = ','.join(['?'] * len(lista_codigos_sintomas))
        query_fallos_posibles = f"""
            SELECT DISTINCT r.id_fallo
            FROM reglas r
            JOIN sintomas s ON r.id_sintoma = s.id_sintoma
            WHERE s.codigo_sintoma IN ({placeholders_actuales})
        """
        
        cursor.execute(query_fallos_posibles, lista_codigos_sintomas)
        fallos_posibles = [row['id_fallo'] for row in cursor.fetchall()]

        if not fallos_posibles:
            return []

        placeholders_fallos = ','.join(['?'] * len(fallos_posibles))
        query_sintomas_sugeridos = f"""
            SELECT DISTINCT s.descripcion
            FROM reglas r
            JOIN sintomas s ON r.id_sintoma = s.id_sintoma
            WHERE r.id_fallo IN ({placeholders_fallos})
              AND s.codigo_sintoma NOT IN ({placeholders_actuales})
        """

        params = fallos_posibles + lista_codigos_sintomas
        
        cursor.execute(query_sintomas_sugeridos, params)
        
        sugerencias = [row['descripcion'] for row in cursor.fetchall()]
        return sugerencias

    except sqlite3.Error as e:
        print(f"Error en sugerir_siguientes_pasos: {e}")
        return []
    finally:
        if conn:
            conn.close()

def sugerir_siguientes_pasos(lista_codigos_sintomas: list) -> list[dict]:
    if not lista_codigos_sintomas:
        return []

    conn = get_db_connection()
    if not conn:
        return []

    try:
        cursor = conn.cursor()
        
        placeholders_actuales = ','.join(['?'] * len(lista_codigos_sintomas))
        query_fallos_posibles = f"""
            SELECT DISTINCT r.id_fallo
            FROM reglas r
            JOIN sintomas s ON r.id_sintoma = s.id_sintoma
            WHERE s.codigo_sintoma IN ({placeholders_actuales})
        """
        
        cursor.execute(query_fallos_posibles, lista_codigos_sintomas)
        fallos_posibles = [row['id_fallo'] for row in cursor.fetchall()]

        if not fallos_posibles:
            return []

        placeholders_fallos = ','.join(['?'] * len(fallos_posibles))
        query_sintomas_sugeridos = f"""
            SELECT DISTINCT s.codigo_sintoma, s.descripcion
            FROM reglas r
            JOIN sintomas s ON r.id_sintoma = s.id_sintoma
            WHERE r.id_fallo IN ({placeholders_fallos})
              AND s.codigo_sintoma NOT IN ({placeholders_actuales})
        """

        params = fallos_posibles + lista_codigos_sintomas
        
        cursor.execute(query_sintomas_sugeridos, params)
        
        sugerencias = [{"codigo": row['codigo_sintoma'], "desc": row['descripcion']} for row in cursor.fetchall()]
        return sugerencias

    except sqlite3.Error as e:
        print(f"Error en sugerir_siguientes_pasos: {e}")
        return []
    finally:
        if conn:
            conn.close()

