from usuario import Usuario
from quarto import Quarto
from cliente import Cliente
from relatorio import Relatorio

class Administrador(Usuario):
    def __init__(self, nome_usuario, senha, nome, email, telefone, id_adm):
        super().__init__(nome_usuario, senha, nome, email, telefone)
        self.id_adm = id_adm
        self.clientes = []
        self.quartos =[]
        self.reservas = []


    def getClientes(self):
        for cliente in self.clientess:
            print(f'{cliente.getNome_usuario()}')
    
    
    def mostrar_opcoes_adm(self):
       print('Gerenciamento do Hotel')
       print('Digite o numero da opçao desejada.')
       print('1 - Cadastrar Cliente')
       print('2 - Adiionar Quarto')
       print('3 - Atualizar Quarto')
       print('4 - Remover Quarto')
       print('5 - Visuallizar Reservas')
       print('6 - Gerar Relatorio Mensal')
       print('7 - Atualizar Perfil')
       print('8 - Sair')
       oppcao = input('Digite aqui: ')


       if oppcao == '1':
           self.adicionarCliente()
       elif oppcao == '2':
          self.adicionar_quarto()
       elif oppcao == '3':
          self.atualizar_quarto()
       elif oppcao == '4':
          self.remover_quarto()
       elif oppcao == '5':
          self.visualizar_todas_as_reservas()
       elif oppcao == '6':
          Relatorio.gerar_relatorio(self)
       elif oppcao == '7':
          Usuario.setAtualizar_perfil(self)
       elif oppcao == '8':
          Usuario.fazer_logaout(self)
          
       else:
          print('Opção invalida.')

    def adicionarCliente(self):
        print('CADASTRAR CLIENTES: ')
        nome = input('Nome: ')
        nome_u= input('nome usuario: ')
        senha = input('senha :')
        telefone = input('telefone : ')
        email = input('email: ')
        idCiente = input('id cliente: ')

        novo_cliente = Cliente(nome_u, senha, nome, email, telefone, idCiente)
        self.clientes.append(novo_cliente)
        print('Cliente foi cadastrado!')
        self.mostrar_opcoes_adm()

    
        

    def adicionar_quarto(self):
       print('ADICIONAR QUARTO: ')
       numero = input('Digite o numero do quarto: ')
       
       for quarto in self.quartos:
         if numero == quarto.getNumero_quarto():
             print('Ja existe um quarto com esse numero.')
             self.adicionar_quarto()
             return
        
       tipo = input('Tipo de quarto : ')
       preco = float(input('Preçp por noite: '))
       caracteristicas = input('Caracteristicas: ')

       novo_quarto = Quarto(numero, tipo, caracteristicas, preco)
       #KAKAKAKKA SURTOS COM ESSA PARTE
       self.quartos.append(novo_quarto)
       print(f'Quarto {numero} foi adicionado.')
       self.mostrar_opcoes_adm()
    

       
       

        

    def atualizar_quarto (self):
      print('------Atualizar Quarto-----')
      numero = input('Digite o numero do quarto que deseja atualizar: ')
      for quarto in self.quartos:
         if numero == Quarto.getNumero_quarto(self):
          novoNumero = input('Novo numero: ')
          quarto.numero = novoNumero
          tipo  = input('Novo tipo: ')
          quarto.tipo = tipo
          novaCaracteristicas = input('Novo carat: ')
          quarto.caracteristicas = novaCaracteristicas
          novoPreco = float(input('Novo preço P/ noite: '))
          quarto.preco = novoPreco
          print('Quarto Atualizado')
          return
         else:
            ('Quarto não encontrado.')


    
      
    
    def remover_quarto(self):
       print('---- Remover Quarto-----')
       numero = input('Numero do quarto que deja remover: ')
       for quarto in self.quartos:
          if numero == quarto.getNumero_quarto():
             self.quartos.remove(quarto)
             print(f'Quarto {numero} foi removido.')
          else:
             print('Quarto não encontrado.')

        

        

    def visualizar_todas_as_reservas(self):
        print('-----Reserva-----')
        
        for reserva in self.reservas:
           print(f'`{reserva}')
        pass

    





    


    


 
         