# Sistema Experto para el Diagnóstico de Fallos en Circuitos Eléctricos

## Descripción general
Proyecto para desarrollar un **sistema experto** que diagnostique fallos en circuitos electrónicos a partir de los síntomas descritos por el usuario.  
El sistema utiliza **Python** y una base de datos **SQLite** (con posibilidad de migrar a MySQL), además de módulos para **procesamiento de lenguaje natural (PLN)** e inferencia lógica.

---

## Propietarios del proyecto

- **Arreola García Vanessa Fernanda**
- **Ramírez Mireles Gustavo**

---

## Objetivos del sistema

1. Identificar fallas comunes en circuitos electrónicos y sus síntomas.  
2. Implementar una base de conocimientos estructurada en Python.  
3. Desarrollar un motor de inferencia para sugerir soluciones.  
4. Crear un módulo PLN que interprete lenguaje natural.  
5. Diseñar una interfaz gráfica para la interacción con el usuario.  

---

## Tecnologías utilizadas

- **Python 3.12+**
- **SQLite3**
- **Tkinter o PyQt5** (interfaz gráfica)
- **NLTK o spaCy** (procesamiento de lenguaje natural)
- **pytest / unittest** (pruebas)
- **JSON / YAML** (estructura de conocimiento)

---

## Estructura del proyecto

```
sistema_experto_diagnostico/
│
├── main.py                         # Punto de entrada principal
│
├── core/
│   ├── __init__.py                 # Convierte 'core' en un paquete Python
│   ├── motor_inferencia.py         # Motor de inferencia (razonamiento de reglas)
│   ├── base_conocimiento.py        # Carga y gestión de reglas y hechos
│   ├── parser_pln.py               # Procesamiento de lenguaje natural
│   ├── diagnostico.py              # Coordinador del proceso de diagnóstico
│   └── database.py                 # Conexión y consultas a la base de datos
│
├── data/
│   ├── base_conocimiento.json      # Reglas y hechos
│   ├── ejemplos_usuarios.txt       # Frases típicas de entrada
│   ├── configuracion.yaml          # Configuración general
│   ├── __init__.py (opcional)      # Solo si accedes a data desde Python
│   └── database/
│       ├── __init__.py (opcional)  # Solo si ejecutas código aquí
│       ├── schema.sql              # Definición de tablas
│       ├── data.sql                # Datos iniciales
│       └── diagnostico.db          # Base de datos SQLite
│
├── gui/
│   ├── __init__.py                 # Convierte 'gui' en paquete Python
│   ├── interfaz.py                 # Interfaz gráfica principal
│   ├── componentes/
│   │   ├── __init__.py             # Submódulos visuales
│   │   └── (otros componentes).py
│   └── recursos/                   # Imágenes, íconos, estilos
│
├── tests/
│   ├── __init__.py                 # Requerido para pytest y modularidad
│   ├── test_motor_inferencia.py    # Pruebas unitarias del motor
│   ├── test_database.py            # Pruebas de base de datos
│   ├── test_parser_pln.py          # Pruebas del PLN
│   └── test_diagnostico.py         # Pruebas del flujo completo
│
├── docs/
│   ├── manual_usuario.md           # Guía de uso
│   ├── especificacion_tecnica.md   # Diseño técnico
│   ├── bitacora_validacion.md      # Resultados de pruebas
│   └── entrevistas_expertos.md     # Aportaciones de expertos
│
├── requirements.txt                # Dependencias de Python
└── README.md                       # Descripción del proyecto
```

