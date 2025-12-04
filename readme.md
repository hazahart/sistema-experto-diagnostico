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
- **PySwip**

---

## Estructura del proyecto

```
sistema_experto_diagnostico/
│
├── main.py                         # Punto de entrada principal
|
├── gui.py                          # Interfaz gráfica
│
├── core/
│   ├── __init__.py                 # Convierte 'core' en un paquete Python
│   ├── motor_inferencia.py         # Motor de inferencia (razonamiento de reglas)
|   ├── motor_prolog.py             # Motor de integración de prolog
│   ├── parser_pln.py               # Procesamiento de lenguaje natural
│   └── database.py                 # Conexión y consultas a la base de datos
│
├── data/
│   ├── base_conocimiento.json      # Reglas y hechos
│   ├── base_conocimiento.pl        # Carga y gestión de reglas y hechos
│   └── database/
│       ├── __init__.py (opcional)  # Solo si ejecutas código aquí
│       ├── schema.sql              # Definición de tablas
│       ├── data.sql                # Datos iniciales
│       └── diagnostico.db          # Base de datos SQLite
│
└── README.md                       # Descripción del proyecto
```

