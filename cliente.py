from usuario import Usuario

class Cliente (Usuario):
    def __init__(self, nome_usuario, senha, nome, email, telefone, id_cliente, historico_reservas):
        super().__init__(nome_usuario, senha, nome, email, telefone)
        self.id_cliente = id_cliente
        self.__historico_Reservas= historico_reservas