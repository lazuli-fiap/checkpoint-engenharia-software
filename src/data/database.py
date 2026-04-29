import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), 'lab_reserva.db')

def get_connection():
    """Retorna uma conexão com o banco de dados SQLite."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Inicializa as tabelas do banco de dados."""
    conn = get_connection()
    cursor = conn.cursor()
    
    # Tabela de Usuários
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        senha_hash TEXT NOT NULL
    )
    ''')
    
    # Tabela de Laboratórios
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS laboratorios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT UNIQUE NOT NULL
    )
    ''')
    
    # Tabela de Reservas
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS reservas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario_id INTEGER NOT NULL,
        laboratorio_id INTEGER NOT NULL,
        data_hora TEXT NOT NULL,
        FOREIGN KEY (usuario_id) REFERENCES usuarios (id),
        FOREIGN KEY (laboratorio_id) REFERENCES laboratorios (id)
    )
    ''')
    
    # Inserir alguns dados padrão se não existirem
    cursor.execute('SELECT COUNT(*) FROM laboratorios')
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO laboratorios (nome) VALUES ('Lab Informatica 1')")
        cursor.execute("INSERT INTO laboratorios (nome) VALUES ('Lab Quimica')")
        cursor.execute("INSERT INTO laboratorios (nome) VALUES ('Lab Maker')")
        
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
    print("Banco de dados inicializado com sucesso!")
