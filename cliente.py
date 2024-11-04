from usuario import Usuario

class Cliente (Usuario):
    def __init__(self, nome_usuario, senha, nome, email, telefone, id_cliente, historico_reservas):
        super().__init__(nome_usuario, senha, nome, email, telefone)
        self.id_cliente = id_cliente
        self.__historico_Reservas = []
        

    def pesquisar_quartos(self):
        pass 

    def fazer_reserva(self):
        # adicionar reserva no array hitorico de reservas
        pass

    def visualizar_reservas(self):
        # visualizar a reserva que esta fazndo ou todas as reservas que ja foram feitas?
    
        pass

    def cancelar_reserva(self):
        #remover reserva do array reserva 
        pass

    