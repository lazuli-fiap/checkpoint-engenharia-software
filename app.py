from datetime import datetime

class Usuario:
    def __init__(self, nome):
        self.nome = nome

class Laboratorio:
    def __init__(self, nome):
        self.nome = nome
        self.reservas = []

class Reserva:
    def __init__(self, usuario, laboratorio, data_hora):
        self.usuario = usuario
        self.laboratorio = laboratorio
        self.data_hora = data_hora

class SistemaReserva:
    def __init__(self):
        self.usuarios = []
        self.laboratorios = []

    def cadastrar_usuario(self, nome):
        user = Usuario(nome)
        self.usuarios.append(user)
        print("Usuário cadastrado!")

    def cadastrar_laboratorio(self, nome):
        lab = Laboratorio(nome)
        self.laboratorios.append(lab)
        print("Laboratório cadastrado!")

    def listar_labs(self):
        for i, lab in enumerate(self.laboratorios):
            print(f"{i} - {lab.nome}")

    def reservar(self, user_index, lab_index, data_str):
        usuario = self.usuarios[user_index]
        laboratorio = self.laboratorios[lab_index]
        data = datetime.strptime(data_str, "%d/%m/%Y %H:%M")

        # Verifica conflito
        for r in laboratorio.reservas:
            if r.data_hora == data:
                print("Horário já reservado!")
                return

        reserva = Reserva(usuario, laboratorio, data)
        laboratorio.reservas.append(reserva)
        print("Reserva realizada com sucesso!")

    def listar_reservas(self, lab_index):
        lab = self.laboratorios[lab_index]
        for r in lab.reservas:
            print(f"{r.usuario.nome} - {r.data_hora}")

# Execução simples
sistema = SistemaReserva()

while True:
    print("\n1-Cadastrar usuário")
    print("2-Cadastrar laboratório")
    print("3-Reservar")
    print("4-Listar laboratórios")
    print("5-Ver reservas")
    print("0-Sair")

    op = input("Escolha: ")

    if op == "1":
        nome = input("Nome: ")
        sistema.cadastrar_usuario(nome)

    elif op == "2":
        nome = input("Nome do lab: ")
        sistema.cadastrar_laboratorio(nome)

    elif op == "3":
        sistema.listar_labs()
        u = int(input("ID usuário: "))
        l = int(input("ID lab: "))
        data = input("Data (dd/mm/yyyy hh:mm): ")
        sistema.reservar(u, l, data)

    elif op == "4":
        sistema.listar_labs()

    elif op == "5":
        sistema.listar_labs()
        l = int(input("ID lab: "))
        sistema.listar_reservas(l)

    elif op == "0":
        break