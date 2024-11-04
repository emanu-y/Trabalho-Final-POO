from usuario import Usuario

class Administrador(Usuario):
    def __init__(self, nome_usuario, senha, nome, email, telefone, id_adm):
        super().__init__(nome_usuario, senha, nome, email, telefone)
        self.id_adm = id_adm

    def adicionar_quarto(self):
        pass

    def atualizar_quarto (self):
        pass
    
    def remover_quarto(self):
        pass

    def visualizar_todas_as_reservas(self):
        pass

    def gerar_relatorio(self):
        pass





    


    


 
         