
CREATE TABLE IF NOT EXISTS crudbasetable (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    row_name CHARACTER(63) UNIQUE,
    row_value INTEGER,
    row_weight REAL
);

CREATE TABLE IF NOT EXISTS administrators (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_name CHARACTER(50) UNIQUE,
    password CHARACTER(64)
);

CREATE TABLE IF NOT EXISTS alumnos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre CHARACTER(50),
    apellido_paterno CHARACTER(50),
    apellido_materno CHARACTER(50),
    expediente CHARACTER(50) UNIQUE,
    grupo_id INTEGER,
    FOREIGN KEY(grupo_id) REFERENCES grupos(id)
);

CREATE TABLE IF NOT EXISTS profesores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre CHARACTER(50),
    apellido_paterno CHARACTER(50),
    apellido_materno CHARACTER(50),
    expediente CHARACTER(50) UNIQUE
);

CREATE TABLE IF NOT EXISTS grupos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    grupo CHARACTER(50) UNIQUE
);

CREATE TABLE IF NOT EXISTS equipos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    codigo CHARACTER(256) UNIQUE,
    descripcion TEXT,
    hvi INT2
);

CREATE TABLE IF NOT EXISTS laboratorios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre CHARACTER(50),
    seccion CHARACTER(50)
);

CREATE TABLE IF NOT EXISTS grupos_profesores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    profesor_id INTEGER,
    grupo_id INTEGER,
    FOREIGN KEY(profesor_id) REFERENCES profesores(id),
    FOREIGN KEY(grupo_id) REFERENCES grupos(id)
);

CREATE TABLE IF NOT EXISTS calendar (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    laboratory CHARACTER(50),
    group_name CHARACTER(50),
    start_date TEXT,
    end_date TEXT,
    start_time TEXT,
    end_time TEXT
);

CREATE TABLE IF NOT EXISTS historial (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    alumno_id INTEGER,
    equipo_id INTEGER,
    fecha_incial TEXT,
    fecha_final TEXT,
    hora_inicial TEXT,
    hora_final TEXT,
    retraso INT2,
    FOREIGN KEY(alumno_id) REFERENCES alumnos(id),
    FOREIGN KEY(equipo_id) REFERENCES equipos(id)
);

INSERT INTO administrators (id, user_name, password) VALUES(NULL, "boot", "ce8f5a764a51a77c7e11566ee189b20e282b6678f05a27e2965a35315e4a264f");
