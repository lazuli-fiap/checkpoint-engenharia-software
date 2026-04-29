from werkzeug.security import generate_password_hash
from src.data.database import get_connection

def registrar_usuario(nome, email, senha):
    """
    Registra um novo usuário no banco de dados.
    Retorna (True, "Mensagem de sucesso") ou (False, "Mensagem de erro").
    """
    if not nome or not email or not senha:
        return False, "Todos os campos são obrigatórios."
        
    senha_hash = generate_password_hash(senha)
    
    conn = get_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute(
            "INSERT INTO usuarios (nome, email, senha_hash) VALUES (?, ?, ?)",
            (nome, email, senha_hash)
        )
        conn.commit()
        return True, "Usuário cadastrado com sucesso!"
    except Exception as e:
        if "UNIQUE constraint failed: usuarios.email" in str(e):
            return False, "Este e-mail já está em uso."
        return False, f"Erro ao cadastrar: {e}"
    finally:
        conn.close()
