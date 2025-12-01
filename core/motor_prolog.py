# core/motor_prolog.py
import sys
from pathlib import Path
from pyswip import Prolog
from .database import get_db_connection, BASE_DIR

class MotorProlog:
    def __init__(self):
        self.prolog = Prolog()
        
        # Ruta corregida, asumiendo que base_conocimientos.pl está en la carpeta 'data' 
        ruta_conocimiento = BASE_DIR / "data" / "base_conocimientos.pl"
        
        try:
            ruta_str = str(ruta_conocimiento).replace("\\", "/")
            if not Path(ruta_str).exists():
                 raise FileNotFoundError(f"Archivo .pl no encontrado en: {ruta_str}")

            self.prolog.consult(ruta_str)
            print(f"Base de conocimiento Prolog cargada desde: {ruta_str}")
        except FileNotFoundError as e:
            raise ConnectionError(f"Error CRÍTICO: Archivo de base de conocimiento no encontrado: {e.args[0]}. Asegúrate de que '{ruta_conocimiento.name}' esté en la carpeta 'data/'.")
        except Exception as e:
            raise ConnectionError(f"Error CRÍTICO al cargar Prolog: {e}. Asegúrate de tener SWI-Prolog instalado y en el PATH.")

    def _obtener_descripcion_sintoma(self, codigo_sintoma: str) -> str | None:
        """
        Busca en SQLite la descripción textual exacta de un síntoma dado su código (Ej: 'S-001').
        """
        conn = get_db_connection()
        if not conn: 
            return None
        try:
            cursor = conn.cursor()
            query = "SELECT descripcion FROM sintomas WHERE codigo_sintoma = ?"
            cursor.execute(query, (codigo_sintoma,))
            row = cursor.fetchone()
            return row['descripcion'] if row else None
        except Exception as e:
            print(f"Error consultando descripción de síntoma en SQLite: {e}")
            return None
        finally:
            if conn:
                conn.close()

    def diagnosticar(self, lista_codigos_sintomas: list) -> dict:
        """
        Realiza el diagnóstico utilizando el motor Prolog.
        """
        if not lista_codigos_sintomas:
            return {"fallo": "No hay síntomas", "solucion": "Por favor, describe un síntoma."}

        # 1. Limpiar memoria de trabajo de Prolog de consultas anteriores
        self.prolog.retractall("verificar(_)")

        # 2. Traducir códigos a descripciones y afirmar hechos
        hechos_agregados = 0
        for codigo in lista_codigos_sintomas:
            descripcion = self._obtener_descripcion_sintoma(codigo)
            if descripcion:
                # Escapamos comillas simples
                desc_clean = descripcion.replace("'", "\\'")
                
                # Inyección del hecho: verificar('Descripcion del sintoma')
                self.prolog.assertz(f"verificar('{desc_clean}')")
                hechos_agregados += 1

        if hechos_agregados == 0:
            return {"fallo": "Error de Datos", "solucion": "No se pudieron interpretar los síntomas en el catálogo."}

        # 3. Consultar reglas: diagnostico(Codigo, Fallo, Solucion)
        try:
            # La consulta devuelve el primer resultado que cumple TODAS las condiciones
            resultados = list(self.prolog.query("diagnostico(Cod, Nom, Sol)"))

            if resultados:
                mejor_res = resultados[0]
                return {
                    "fallo": mejor_res["Nom"],
                    "solucion": mejor_res["Sol"],
                    "coincidencias": len(lista_codigos_sintomas)
                }
            else:
                return {
                    "fallo": "Desconocido", 
                    "solucion": "La combinación de síntomas no coincide con ninguna regla exacta en la base de conocimiento."
                }
        except Exception as e:
            return {"fallo": "Error de Motor", "solucion": f"Error interno en motor Prolog: {e}"}

    def sugerir_siguientes_pasos(self, lista_codigos_sintomas: list) -> list[dict]:
        """
        Sugerir síntomas pendientes utilizando el catálogo de la BD.
        Devuelve una lista limitada de síntomas que aún no han sido reportados.
        """
        conn = get_db_connection()
        if not conn:
            return []

        try:
            # 1. Obtener los códigos de todos los síntomas posibles del catálogo
            cursor = conn.cursor()
            cursor.execute("SELECT codigo_sintoma, descripcion FROM sintomas")
            all_sintomas = cursor.fetchall()

            # 2. Convertir la lista de síntomas reportados a un set para búsqueda rápida
            sintomas_reportados_set = set(lista_codigos_sintomas)

            # 3. Filtrar los síntomas: solo devolver aquellos que NO han sido reportados
            sugerencias_pendientes = []
            for row in all_sintomas:
                if row['codigo_sintoma'] not in sintomas_reportados_set:
                    sugerencias_pendientes.append({
                        "codigo": row['codigo_sintoma'],
                        "desc": row['descripcion']
                    })

            # 4. Limitar la lista a las primeras 5 sugerencias (para no abrumar la GUI)
            return sugerencias_pendientes[:5]

        except Exception as e:
            print(f"Error en la sugerencia de siguientes pasos: {e}")
            return []
        finally:
            if conn:
                conn.close()