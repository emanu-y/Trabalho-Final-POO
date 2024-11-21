from usuario import Usuario
from quarto import Quarto
from cliente import Cliente
from relatorio import Relatorio
from hotel import Hotel
import uuid 

class Administrador(Usuario):
    def __init__(self, nome_usuario, senha, nome, email, telefone, id_adm):
        super().__init__(nome_usuario, senha, nome, email, telefone)
        self.id_adm = id_adm
        self.reservas = []
        self.hotel = Hotel()


    def getClientes(self):
        return self.clientes
      
      
    def getId (self):
     return self.id_adm
    
    def getEmail(self):
       return self.email
    
        
    def getQuartos(self):
       return self.quartos
    

    
    @staticmethod
    def mostrar_opcoes_adm(self):
       print('Gerenciamento do Hotel')
       print('Digite o numero da opção desejada.')
       print('1 - Cadastrar Cliente')
       print('2 - Adicionar Quarto')
       print('3 - Atualizar Quarto')
       print('4 - Remover Quarto')
       print('5 - Visualizar Reservas')
       print('6 - Gerar Relatorio')
       print('7 - Atualizar Perfil')
       print('8 - Remover Cliente')
       print('9 - Visualizar Clientes')
       print('10 - Atualizar Cliente')
       print('11- Sair')
       

       oppcao = input('Digite aqui: ')


       if oppcao == '1':
           self.adicionarCliente()
       elif oppcao == '2':
          self.adicionar_quarto()
       elif oppcao == '3':
          self.setAtualizar_quarto()
       elif oppcao == '4':
          self.remover_quarto()
       elif oppcao == '5':
          self.visualizar_todas_as_reservas()
       elif oppcao == '6':
          Relatorio.gerar_relatorio(self, self.hotel)
       elif oppcao == '7':
          self.setAtualizar_perfil()
       elif oppcao == '8':
          self.remover_cliente()
      
       elif oppcao == '9':
          self.visualizar_clientes()
       elif oppcao == '10':
          self.atualizar_cliente()
       elif oppcao == '11':
          self.fazer_logaout()
          
       else:
          print('OPÇÃO INVÁLIDA.')
          self.mostrar_opcoes_adm(self)

    def adicionarCliente(self):
        print('/n ---------Cadastrar Clientes------- ')
        nome = input('Nome: ')
        nome_u= input('Nome de Usuário: ')
        senha = str(uuid.uuid4())
        telefone = input('Telefone : ')
        email = input('Email: ')
        

        novo_cliente = Cliente(nome_u, senha, nome, email, telefone)
       

        print('Cliente foi cadastrado!')
        self.hotel.addCliente(novo_cliente)
        self.mostrar_opcoes_adm(self)

    def visualizar_clientes(self):
      
      print('\n ----- Clientes -----')
      if not self.hotel.get_clientes():
        print('O hotel não possui clientes.')
      else:
        for cliente in self.hotel.get_clientes():
            cliente.informacoes_cliente()
            print('=====================')

      self.mostrar_opcoes_adm(self)
      

    def atualizar_cliente(self):
       print('------- Atualizar Dados de Cliente -------')
       id = input('Digite o ID do cliente que deseja atualizar: ')
       cliente_encontrado = None 
       for cliente in self.hotel.clientes:
          if cliente.get_id() == id:
              cliente_encontrado = cliente
              nome = input('Digite seu nome (aperte enter para permanecer com o mesmo): ')
              nome_u = input('Digite seu nome de usuário(aperte enter para permanecer com o mesmo): ')
              telefone = input('Digite seu telefone (aperte enter para permanecer com o mesmo): ')
              email = input('Digite seu email (aperte enter para permanecer com o mesmo): ')

              if nome:
                 cliente.set_nome(nome)
              if nome_u:
                 cliente.set_nome_usuario(nome_u)
              if telefone: 
                 cliente.set_telefone(telefone)
              if email:
                 cliente.set.email(email)
              print('Perfil atualizado com secesso!!')
              self.mostrar_opcoes_adm(self)
       if  not cliente_encontrado :
          print('Cliente não encontrado.')
          self.mostrar_opcoes_adm(self)
              
    def remover_cliente(self):
       print('---- Remover Cliente-----')
       id = input('Digite o ID do cliente que deseja remover: ')
       for cliente in self.hotel.clientes:
          if id == cliente.get_id():
             self.hotel.clientes.remove(cliente)
             print(f'O cliente foi removido.')
             self.mostrar_opcoes_adm(self)
             return
       else:
             print('Cliente não encontrado.')
             self.mostrar_opcoes_adm(self)
       
                    
              


    
        

    def adicionar_quarto(self):
       print('/n ---------- Adicionar Quarto ---------- ')
       numero = input('Digite o numero do quarto: ')
       
       for quarto in self.hotel.quartos:
         if numero == quarto.get_numero_quarto():    #Quarto.getNumero_quarto()
             print('Já existe um quarto com esse numero.')
             self.adicionar_quarto()
             
             return
        
       tipo = input('Tipo de Quarto (Casal, Solteiro, Fámilia) : ') 
       caracteristicas = input('Características: ')
       while True:
        try:
            preco = float(input('Preço por noite: R$ '))
            break

        except ValueError:
            print("Entrada inválida. Digite um valor numérico para o preço.")

       novo_quarto = Quarto(numero, tipo, caracteristicas, preco, True)
       #KAKAKAKKA SURTOS COM ESSA PARTE
       self.hotel.adicionar_quarto(novo_quarto)
       print(f'Quarto {numero} foi adicionado.')
       self.mostrar_opcoes_adm(self)
    

       
       

        

    def setAtualizar_quarto (self):
      print('------Atualizar Quarto-----')
      numero = input('Digite o numero do quarto que deseja atualizar: ')
      for quarto in self.hotel.quartos:
        
         if int(numero) == int(quarto.get_numero_quarto()):
            print(f'Tipo Atual: {quarto.getTipo()} ')               #ARRUMAR OS ENUNCIADOS 
            novo_tipo = input('Atualizar Tipo:')
            print(f'Características Atuais: {quarto.getCaracteristicas()} ') 
            nova_caract= input('Atualizar Caractristicas:')
            print(f'Preço Atual: {quarto.get_preco_porNoite()} ') 
            while True:
               try:
                   preco_atualizado = float(input('Atualizar Preço (Diária): R$'))
                   break
               except:
                  print('Digite um valor númerico válido.')
         
            
            if novo_tipo:

               quarto.setTipo( novo_tipo)
            if nova_caract:
               quarto.setCaracteristicas( nova_caract)
            if preco_atualizado:
                try:
                 quarto.setPreco(float(preco_atualizado))
                except ValueError:
                   print('Valor Invalido.')
                   self.setAtualizar_quarto()
            print(f'Quarto {quarto.get_numero_quarto()} atualizado com sucesso!!')
            self.mostrar_opcoes_adm(self)                                          #achar um jeito de colocar erro e voltar pro negocio de menu quando o float der errado
            
         
      print('Quarto não encontrado.')
      self.mostrar_opcoes_adm(self)  
      
    def remover_quarto(self):
       print('---- Remover Quarto-----')
       numero = input('Numero do quarto que deseja remover: ')
       for quarto in self.hotel.quartos:
          if numero == quarto.get_numero_quarto():
             self.hotel.quartos.remove(quarto)
             print(f'Quarto {numero} foi removido.')
             self.mostrar_opcoes_adm(self)
             return
       else:
             print('Quarto não encontrado.')
             self.mostrar_opcoes_adm(self)
             

        

        
    def cancelar_reserva(self):
        reserva_id = input('Digite o numero da reserva que deseja cancelar: ')
        for reserva in self.hotel.reservas:
           if reserva_id == reserva.get_ID():
              print(reserva.informacoes())
              print('Deseja cancelar essa reserva? ')
              print('1 - Sim')
              print('2 - Não')
              opcao = input('Digite aqui: ')
              if opcao == '1':
                 reserva.cancelar_reserva()
                 self.hotel.remover_reserva(reserva)
                 print('Reserva cancelada.')
              elif opcao == '2':
                 self.mostrar_opcoes_adm(self)
              else:
                 print('OPÇAO INVÁLIDA.')
           else:
              print('Reserva não encotrada.')
              self.mostrar_opcoes_adm(self)


    def visualizar_todas_as_reservas(self):
        print('----- Reservas -----')
        for reserva in self.hotel.reservas:
           print(f'{reserva.informacoes()}')
        else:
           print('Hotel não possui reservas.')
        self.mostrar_opcoes_adm(self)
   
 
   
        