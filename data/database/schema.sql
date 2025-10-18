-- schema.sql

-- Eliminar tablas si ya existen
DROP TABLE IF EXISTS expresiones_usuario;
DROP TABLE IF EXISTS reglas;
DROP TABLE IF EXISTS fallos;
DROP TABLE IF EXISTS sintomas;

-- Tabla de sintomas
CREATE TABLE sintomas (
    id_sintoma INTEGER PRIMARY KEY AUTOINCREMENT,
    codigo_sintoma TEXT NOT NULL UNIQUE,
    descripcion TEXT NOT NULL UNIQUE,
    categoria TEXT
);

-- Tabla de fallos
CREATE TABLE fallos (
    id_fallo INTEGER PRIMARY KEY AUTOINCREMENT,
    codigo_fallo TEXT NOT NULL UNIQUE,
    nombre_fallo TEXT NOT NULL UNIQUE,
    solucion_recomendada TEXT
);

-- Tabla de reglas para asociar sintomas con fallos
CREATE TABLE reglas (
    id_fallo INTEGER,
    id_sintoma INTEGER,
    PRIMARY KEY (id_fallo, id_sintoma),
    FOREIGN KEY (id_fallo) REFERENCES fallos(id_fallo),
    FOREIGN KEY (id_sintoma) REFERENCES sintomas(id_sintoma)
);

-- Tabla de expresiones de usuario para el PLN
CREATE TABLE expresiones_usuario (
    id_expresion INTEGER PRIMARY KEY AUTOINCREMENT,
    frase TEXT NOT NULL UNIQUE,
    id_sintoma INTEGER,
    FOREIGN KEY (id_sintoma) REFERENCES sintomas(id_sintoma)
);