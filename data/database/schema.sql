-- schema.sql
-- Eliminar tablas si ya existen
DROP TABLE IF EXISTS historial_diagnosticos;
DROP TABLE IF EXISTS reglas; -- ELIMINADA: La lógica ahora está en Prolog
DROP TABLE IF EXISTS expresiones_usuario;
DROP TABLE IF EXISTS fallos;
DROP TABLE IF EXISTS sintomas;

-- Tabla de sintomas (Catálogo maestro para traducción y PLN)
CREATE TABLE sintomas (
    id_sintoma INTEGER PRIMARY KEY AUTOINCREMENT,
    codigo_sintoma TEXT NOT NULL UNIQUE,
    descripcion TEXT NOT NULL UNIQUE,
    categoria TEXT
);

-- Tabla de fallos (Catálogo de posibles soluciones)
CREATE TABLE fallos (
    id_fallo INTEGER PRIMARY KEY AUTOINCREMENT,
    codigo_fallo TEXT NOT NULL UNIQUE,
    nombre_fallo TEXT NOT NULL UNIQUE,
    solucion_recomendada TEXT
);

-- Tabla de expresiones de usuario para el PLN (Diccionario de sinónimos)
CREATE TABLE expresiones_usuario (
    id_expresion INTEGER PRIMARY KEY AUTOINCREMENT,
    frase TEXT NOT NULL UNIQUE,
    id_sintoma INTEGER,
    FOREIGN KEY (id_sintoma) REFERENCES sintomas(id_sintoma)
);

-- NUEVA TABLA: Historial / Log de diagnósticos (Persistencia)
CREATE TABLE historial_diagnosticos (
    id_historial INTEGER PRIMARY KEY AUTOINCREMENT,
    fecha_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    sintomas_reportados TEXT,    -- Códigos reportados (ej: "S-001,S-004")
    fallo_detectado TEXT,        -- El nombre del fallo que dio Prolog
    solucion_ofrecida TEXT
);