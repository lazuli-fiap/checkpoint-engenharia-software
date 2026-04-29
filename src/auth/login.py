from werkzeug.security import check_password_hash
from src.data.database import get_connection
from src.models.domain import Usuario

def autenticar_usuario(email, senha):
    """
    Verifica as credenciais do usuário.
    Retorna (Usuario, "Mensagem de sucesso") ou (None, "Mensagem de erro").
    """
    if not email or not senha:
        return None, "E-mail e senha são obrigatórios."
        
    conn = get_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute("SELECT id, nome, email, senha_hash FROM usuarios WHERE email = ?", (email,))
        row = cursor.fetchone()
        
        if row:
            # Verifica se o hash da senha bate
            if check_password_hash(row['senha_hash'], senha):
                usuario = Usuario(id=row['id'], nome=row['nome'], email=row['email'])
                return usuario, "Login realizado com sucesso!"
            else:
                return None, "Senha incorreta."
        else:
            return None, "Usuário não encontrado."
    except Exception as e:
        return None, f"Erro ao autenticar: {e}"
    finally:
        conn.close()
