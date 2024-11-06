from usuario import Usuario
from quarto import Quarto
from hotel import Hotel

class Administrador(Usuario):
    def __init__(self, nome_usuario, senha, nome, email, telefone, id_adm):
        super().__init__(nome_usuario, senha, nome, email, telefone)
        self.id_adm = id_adm
        self.clientes = []
        self.quartos = []

    def getClientes(self):
        for clientes in self.clientes:
            print(f'{Usuario.getNome_usuario()}')

    def adicionarCliente(self):
        self.clientes.append(Usuario.getNome_usuario())
        

    def adicionar_quarto(self):
        self.quartos.append(Quarto.getNumero_quarto())

        

    def atualizar_quarto (self):
        Quarto.setDados(input(""))
    
    def remover_quarto(self):
        self.quartos.remove(Quarto.getNumero_quarto())

        

    def visualizar_todas_as_reservas(self):
        for reserrva in reservas:
            pass

    def gerar_relatorio(self):
        pass





    


    


 
         