CREATE TABLE IF NOT EXISTS evento (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    data TEXT NOT NULL,
    local TEXT,
    vagas INTEGER
);
CREATE TABLE IF NOT EXISTS participante (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
);
CREATE TABLE IF NOT EXISTS inscricao (
    id INTEGER PRIMARY KEY,
    participante_id INTEGER NOT NULL REFERENCES participante(id),
    evento_id INTEGER NOT NULL REFERENCES evento(id),
    data_inscricao TEXT NOT NULL,
    UNIQUE (participante_id, evento_id)
);
