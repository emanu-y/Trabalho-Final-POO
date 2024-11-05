from usuario import Usuario
from quarto import Quarto
from hotel import Hotel

class Administrador(Usuario):
    def __init__(self, nome_usuario, senha, nome, email, telefone, id_adm):
        super().__init__(nome_usuario, senha, nome, email, telefone)
        self.id_adm = id_adm

    def adicionarCliente(self):
        Hotel.adicionar(Usuario) 

    def adicionar_quarto(self):
        Hotel.addQuarto.append(Quarto)

        

    def setatualizar_quarto (self):
        Quarto.setDados(input(""))
    
    def remover_quarto(self):
        pass

    def visualizar_todas_as_reservas(self):
        for reserrva in reservas:
            pass

    def gerar_relatorio(self):
        pass





    


    


 
         