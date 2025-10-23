# ...existing code...
import sys
from core.database import init_db
from core.motor_inferencia import diagnosticar, sugerir_siguientes_pasos 
from core.parser_pln import mapear_frase_a_sintoma

def main():
    try:
        print("Inicializando base de datos...")
        init_db()
        print("Base de datos lista.")
    except Exception as e:
        print(f"Error fatal al inicializar la base de datos: {e}")
        sys.exit(1)

    print("\n--- Sistema Experto de Diagnóstico (Prueba de Consola) ---")
    print("Describe los síntomas uno por uno. Escribe 'diagnosticar' para ver el resultado o 'salir'.")

    sintomas_detectados = []
    sugerencias_actuales = []

    while True:
        frase = input(">> ").strip()

        if frase == 'salir' or frase == 'exit':
            print("Saliendo...")
            break
        
        if frase == 'diagnosticar':
            if not sintomas_detectados:
                print("No se han reportado síntomas aún.")
                continue
                
            print(f"\nRealizando diagnóstico con: {sintomas_detectados}...")
            resultado = diagnosticar(sintomas_detectados)
            
            print("\n--- DIAGNÓSTICO ---")
            print(f"FALLO PROBABLE: {resultado.get('fallo')}")
            print(f"SOLUCIÓN: {resultado.get('solucion')}")
            print("-------------------\n")
            sintomas_detectados = []
            sugerencias_actuales = []
            continue

        codigo_sintoma = None

        if frase.isdigit() and sugerencias_actuales:
            try:
                indice_seleccionado = int(frase) - 1
                if 0 <= indice_seleccionado < len(sugerencias_actuales):
                    codigo_sintoma = sugerencias_actuales[indice_seleccionado]['codigo']
                else:
                    print("[Número fuera del rango de sugerencias.]")
            except ValueError:
                pass
        
        if not codigo_sintoma:
            codigo_sintoma = mapear_frase_a_sintoma(frase)

        if codigo_sintoma:
            if codigo_sintoma not in sintomas_detectados:
                print(f"[SÍNTOMA DETECTADO: {codigo_sintoma}]")
                sintomas_detectados.append(codigo_sintoma)
                
                print("Buscando qué más revisar...")
                sugerencias_actuales = sugerir_siguientes_pasos(sintomas_detectados)
                
                if sugerencias_actuales:
                    print("\n-> Para confirmar, ¿ves algo de esto? (Escribe el número o describe)")
                    for i, sug in enumerate(sugerencias_actuales):
                        print(f"{i+1}. {sug['desc']}") 
                    print("")
                else:
                    print("(No hay más sugerencias, prueba a 'diagnosticar')\n")
                    sugerencias_actuales = []
                    
            else:
                print(f"[SÍNTOMA YA REGISTRADO]")
        else:
            print("[No se reconoce ese síntoma. Intenta describirlo de otra forma.]")


if __name__ == '__main__':
    main()