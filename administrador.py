from usuario import Usuario

class Administrador(Usuario):
    def __init__(self, nome_usuario, senha, nome, email, telefone, id_adm):
        super().__init__(nome_usuario, senha, nome, email, telefone)
        self.id_adm = id_adm
        self.clientes = []
        self.quartos = []

    def getClientes(self):
        for clientes in self.clientes:
            print(f'{Usuario.getNome_usuario()}')
    
    @staticmethod
    def mostrar_opcoes_adm(self):
       print('Gerenciamento do Hotel')
       print('Digite o numero da opçao desejada.')
       print('1 - Adicionar Cliente')
       print('2 - Adiionar Quarto')
       print('3 - Atualizar Quarto')
       print('4 - Remover Quarto')
       print('5 - Visuallizar Reservas')
       print('6 - Gerar Relatorio Mensal')
       oppcao = input('Digite aqui: ')


       if oppcao == '1':
           self.sd
       elif oppcao == '2':
          self.adicionar_quarto()
       elif oppcao == '3':
          self.atualizar_quarto()
       elif oppcao == '4':
          self.remover_quarto()
       elif oppcao == '5':
          self.visualizar_todas_as_reservas()
       elif oppcao == '6':
          self.gerar_relatorio()
       else:
          print('Opção invalida.')

    def adicionarCliente(self):
        self.clientes.append(Usuario.getNome_usuario())
        

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





    


    


 
         