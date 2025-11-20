import tkinter as tk
from tkinter import scrolledtext, font

# Importamos tu lógica existente
# Inicialización de DB
from core.database import init_db
# Lógica de diagnóstico y sugerencias
from core.motor_inferencia import diagnosticar, sugerir_siguientes_pasos
# Procesamiento de lenguaje natural
from core.parser_pln import mapear_frase_a_sintoma

class SistemaExpertoGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema Experto de Diagnóstico - Circuitos Electrónicos")
        self.root.geometry("700x600")
        self.root.configure(bg="#f0f0f0")

        # Variables de estado (igual que en tu main.py)
        self.sintomas_detectados = []
        self.sugerencias_actuales = []

        # Inicializar base de datos al arrancar
        try:
            init_db()
        except Exception as e:
            self.agregar_mensaje(f"Error de BD: {e}", "sistema")

        self._setup_ui()
        self.agregar_mensaje("Bienvenido. Describe los síntomas de tu circuito (ej: 'no prende', 'huele quemado').", "sistema")

    def _setup_ui(self):
        # --- Área de Historial (Chat) ---
        # Cumple el requisito: "Tanto la consulta como el resultado se observan en la misma pantalla"
        frame_chat = tk.Frame(self.root, bg="#f0f0f0")
        frame_chat.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.chat_display = scrolledtext.ScrolledText(
            frame_chat, 
            state='disabled', 
            height=20, 
            font=("Consolas", 10),
            wrap=tk.WORD
        )
        self.chat_display.pack(fill=tk.BOTH, expand=True)
        
        # Configuración de etiquetas (colores para diferenciar usuario y sistema)
        self.chat_display.tag_config("usuario", foreground="blue", font=("Arial", 10, "bold"))
        self.chat_display.tag_config("sistema", foreground="black", font=("Arial", 10))
        self.chat_display.tag_config("exito", foreground="green", font=("Arial", 10, "bold"))
        self.chat_display.tag_config("error", foreground="red", font=("Arial", 10, "italic"))

        # --- Panel de Síntomas Detectados (Visualización de estado) ---
        # Para que el usuario vea qué ha entendido el sistema sin abrir ventanas
        lbl_info = tk.Label(self.root, text="Síntomas detectados actualmente:", bg="#f0f0f0", font=("Arial", 9, "bold"))
        lbl_info.pack(anchor="w", padx=10)

        self.lbl_sintomas = tk.Label(self.root, text="Ninguno", bg="#e0e0e0", fg="#333333", anchor="w", padx=5)
        self.lbl_sintomas.pack(fill=tk.X, padx=10, pady=(0, 10))

        # --- Área de Entrada ---
        frame_input = tk.Frame(self.root, bg="#d0d0d0", bd=1)
        frame_input.pack(fill=tk.X, side=tk.BOTTOM)

        self.entry_msg = tk.Entry(frame_input, font=("Arial", 12))
        self.entry_msg.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=10, pady=10)
        # Permite enviar con la tecla Enter
        self.entry_msg.bind("<Return>", self.procesar_entrada)

        btn_enviar = tk.Button(frame_input, text="Enviar", command=self.procesar_entrada, bg="#0078D7", fg="white")
        btn_enviar.pack(side=tk.LEFT, padx=(0, 10))

        btn_diagnosticar = tk.Button(frame_input, text="DIAGNOSTICAR", command=self.ejecutar_diagnostico, bg="#28a745", fg="white", font=("Arial", 9, "bold"))
        btn_diagnosticar.pack(side=tk.LEFT, padx=(0, 10))

        btn_reset = tk.Button(frame_input, text="Reiniciar", command=self.reiniciar_sistema, bg="#dc3545", fg="white")
        btn_reset.pack(side=tk.LEFT, padx=(0, 10))

    def agregar_mensaje(self, texto, tag):
        """Agrega texto al área de scroll sin borrar lo anterior."""
        self.chat_display.config(state='normal')
        prefix = "TÚ: " if tag == "usuario" else "SISTEMA: "
        if tag in ["exito", "error"]: prefix = ">> "
        
        self.chat_display.insert(tk.END, f"{prefix}{texto}\n\n", tag)
        self.chat_display.see(tk.END) # Auto-scroll al final
        self.chat_display.config(state='disabled')

    def actualizar_lista_sintomas(self):
        """Actualiza la barra gris con los códigos detectados."""
        if not self.sintomas_detectados:
            self.lbl_sintomas.config(text="Ninguno")
        else:
            self.lbl_sintomas.config(text=", ".join(self.sintomas_detectados))

    def procesar_entrada(self, event=None):
        frase = self.entry_msg.get().strip()
        if not frase:
            return

        self.agregar_mensaje(frase, "usuario")
        self.entry_msg.delete(0, tk.END)

        # Lógica adaptada de tu main.py
        # 1. Verificar si es una selección numérica de sugerencia
        codigo_sintoma = None
        if frase.isdigit() and self.sugerencias_actuales:
            try:
                idx = int(frase) - 1
                if 0 <= idx < len(self.sugerencias_actuales):
                    codigo_sintoma = self.sugerencias_actuales[idx]['codigo']
                else:
                    self.agregar_mensaje("Número fuera de rango.", "error")
                    return
            except ValueError:
                pass
        
        # 2. Si no es número, usar PLN
        if not codigo_sintoma:
            codigo_sintoma = mapear_frase_a_sintoma(frase)

        # 3. Procesar el síntoma encontrado
        if codigo_sintoma:
            if codigo_sintoma not in self.sintomas_detectados:
                self.sintomas_detectados.append(codigo_sintoma)
                self.actualizar_lista_sintomas()
                self.agregar_mensaje(f"Entendido. Síntoma registrado: {codigo_sintoma}", "exito")
                
                # Buscar siguientes pasos
                self.sugerencias_actuales = sugerir_siguientes_pasos(self.sintomas_detectados)
                
                if self.sugerencias_actuales:
                    msg = "Para confirmar, ¿ves algo de esto? (Escribe el número):\n"
                    for i, sug in enumerate(self.sugerencias_actuales):
                        msg += f"{i+1}. {sug['desc']}\n"
                    self.agregar_mensaje(msg, "sistema")
                else:
                    self.agregar_mensaje("No tengo más preguntas específicas. Presiona 'DIAGNOSTICAR' para ver el resultado.", "sistema")
                    self.sugerencias_actuales = []
            else:
                self.agregar_mensaje("Ese síntoma ya lo habías mencionado.", "error")
        else:
            self.agregar_mensaje("No reconozco ese síntoma. Intenta describirlo con otras palabras.", "error")

    def ejecutar_diagnostico(self):
        if not self.sintomas_detectados:
            self.agregar_mensaje("Aún no has reportado síntomas.", "error")
            return

        self.agregar_mensaje("Analizando base de conocimientos...", "sistema")
        
        # Llamada al motor de inferencia
        resultado = diagnosticar(self.sintomas_detectados)
        
        resp = f"""
 RESULTADO DEL DIAGNÓSTICO:
 --------------------------
 FALLO: {resultado.get('fallo')}
 SOLUCIÓN: {resultado.get('solucion')}
        """
        self.agregar_mensaje(resp, "exito")
        
        # Limpiar estado post-diagnóstico
        self.sintomas_detectados = []
        self.sugerencias_actuales = []
        self.actualizar_lista_sintomas()
        self.agregar_mensaje("El sistema se ha reiniciado para una nueva consulta.", "sistema")

    def reiniciar_sistema(self):
        self.sintomas_detectados = []
        self.sugerencias_actuales = []
        self.actualizar_lista_sintomas()
        self.chat_display.config(state='normal')
        self.chat_display.delete(1.0, tk.END)
        self.chat_display.config(state='disabled')
        self.agregar_mensaje("Sistema reiniciado. Describe un problema.", "sistema")

if __name__ == "__main__":
    root = tk.Tk()
    app = SistemaExpertoGUI(root)
    root.mainloop()