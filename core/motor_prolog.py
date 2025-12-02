# core/motor_prolog.py
import sys
import re
from pathlib import Path
from pyswip import Prolog
from .database import get_db_connection, BASE_DIR

class MotorProlog:
    def __init__(self):
        self.prolog = Prolog()
        # Ruta al archivo .pl
        self.ruta_conocimiento = BASE_DIR / "data" / "base_conocimientos.pl"
        
        try:
            ruta_str = str(self.ruta_conocimiento).replace("\\", "/")
            if not Path(ruta_str).exists():
                 raise FileNotFoundError(f"Archivo .pl no encontrado en: {ruta_str}")

            self.prolog.consult(ruta_str)
            print(f"Base de conocimiento Prolog cargada desde: {ruta_str}")
        except FileNotFoundError as e:
            raise ConnectionError(f"Error CRÍTICO: Archivo .pl no encontrado: {e.args[0]}")
        except Exception as e:
            raise ConnectionError(f"Error CRÍTICO al cargar Prolog: {e}")

    def _obtener_descripcion_sintoma(self, codigo_sintoma: str) -> str | None:
        """Busca descripción dado un código (S-001 -> 'El dispositivo...')"""
        conn = get_db_connection()
        if not conn: return None
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT descripcion FROM sintomas WHERE codigo_sintoma = ?", (codigo_sintoma,))
            row = cursor.fetchone()
            return row['descripcion'] if row else None
        finally:
            if conn: conn.close()

    def _obtener_codigo_por_descripcion(self, descripcion: str) -> str | None:
        """(NUEVO) Busca código dada una descripción ('El dispositivo...' -> S-001)"""
        conn = get_db_connection()
        if not conn: return None
        try:
            cursor = conn.cursor()
            # Usamos LIKE para ser tolerantes con espacios extra o mayúsculas
            cursor.execute("SELECT codigo_sintoma FROM sintomas WHERE descripcion LIKE ?", (descripcion,))
            row = cursor.fetchone()
            return row['codigo_sintoma'] if row else None
        finally:
            if conn: conn.close()

    def diagnosticar(self, lista_codigos_sintomas: list) -> dict:
        """Realiza el diagnóstico utilizando el motor Prolog."""
        if not lista_codigos_sintomas:
            return {"fallo": "No hay síntomas", "solucion": "Describe un síntoma."}

        self.prolog.retractall("verificar(_)")
        
        for codigo in lista_codigos_sintomas:
            descripcion = self._obtener_descripcion_sintoma(codigo)
            if descripcion:
                desc_clean = descripcion.replace("'", "\\'")
                self.prolog.assertz(f"verificar('{desc_clean}')")

        try:
            resultados = list(self.prolog.query("diagnostico(Cod, Nom, Sol)"))
            if resultados:
                mejor_res = resultados[0]
                return {
                    "fallo": mejor_res["Nom"],
                    "solucion": mejor_res["Sol"]
                }
            else:
                return {
                    "fallo": "Desconocido", 
                    "solucion": "No encontré una regla exacta para esta combinación."
                }
        except Exception as e:
            return {"fallo": "Error de Motor", "solucion": f"Error interno: {e}"}

    def sugerir_siguientes_pasos(self, lista_codigos_sintomas: list) -> list[dict]:
        """
        (MEJORADO) Lee el archivo .pl para encontrar qué síntomas acompañan
        a los que el usuario ya reportó.
        """
        if not lista_codigos_sintomas:
            return []

        # 1. Obtenemos la descripción del ÚLTIMO síntoma que dijo el usuario
        ultimo_codigo = lista_codigos_sintomas[-1]
        desc_actual = self._obtener_descripcion_sintoma(ultimo_codigo)
        
        if not desc_actual:
            return []

        sintomas_relacionados_desc = set()
        
        try:
            # 2. Leemos el archivo .pl como texto para buscar coincidencias
            with open(self.ruta_conocimiento, "r", encoding="utf-8") as f:
                contenido = f.read()

            # 3. Separamos por reglas (cada regla termina en punto)
            # Normalizamos espacios para facilitar búsqueda
            contenido = contenido.replace("\n", " ")
            reglas = contenido.split("regla(")

            # 4. Buscamos reglas que contengan el síntoma actual
            for regla in reglas:
                if desc_actual in regla:
                    # ¡Encontramos una regla relevante!
                    # Extraigamos todos los textos dentro de verificar('...')
                    coincidencias = re.findall(r"verificar\('([^']+)'\)", regla)
                    for c in coincidencias:
                        if c != desc_actual: # No sugerir lo que ya tiene
                            sintomas_relacionados_desc.add(c)

        except Exception as e:
            print(f"Error analizando archivo .pl: {e}")
            return []

        # 5. Convertimos las descripciones encontradas a códigos S-XXX
        sugerencias = []
        codigos_ya_reportados = set(lista_codigos_sintomas)

        for desc in sintomas_relacionados_desc:
            codigo = self._obtener_codigo_por_descripcion(desc)
            if codigo and codigo not in codigos_ya_reportados:
                sugerencias.append({
                    "codigo": codigo,
                    "desc": desc
                })

        # 6. Devolvemos máximo 5 sugerencias INTELIGENTES
        return sugerencias[:5]