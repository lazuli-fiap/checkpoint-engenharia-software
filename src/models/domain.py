class Usuario:
    def __init__(self, id, nome, email, senha_hash=None):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha_hash = senha_hash

class Laboratorio:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
        
class Reserva:
    def __init__(self, id, usuario_id, laboratorio_id, data_hora):
        self.id = id
        self.usuario_id = usuario_id
        self.laboratorio_id = laboratorio_id
        self.data_hora = data_hora
