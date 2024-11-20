from usuario import Usuario
from quarto import Quarto
from reserva import Reserva
from hotel import Hotel
from datetime import datetime
import uuid



class Cliente (Usuario):
    def __init__(self, nome_usuario, senha, nome, email, telefone):
        super().__init__(nome_usuario, senha, nome, email, telefone)
        self.id_cliente =  str(uuid.uuid4())
        self.__historico_Reservas = []
        self.hotel = Hotel()
    def get_nome(self):
       return self.nome
    def get_email(self):
       return self.email
    def get_telefone(self):
       return self.telefone
    def get_id(self):
       return self.id_cliente
 
    def get_historico(self, reserva):
     self.__historico_Reservas.remove(reserva)


    def set_nome(self, nome):
       self.nome = nome
    def set_telefone(self, telefone):
       self.telefone = telefone
    def set_email(self, email):
       self.email = email
    def set_nome_usuario(self, nome):
       self.__nome_usuario = nome
   
    @staticmethod
    def mostrar_opcoes_cliente(self):
        print('/n ---- HOME ----')
        print('Escolha uma opção:')
        print('1 - Atualizar Perfil')
        print('2 - Buscar Quartos Disponíveis')
        print('3 - Fazer Reserva ')
        print('4 - Visualizar Reservas')
        print('5 - Cancelar Reserva')
        print('6 - Pesquisa por Tipo')
        print('7 - Sair')
        oppcao = input('Digite aqui:')

        if oppcao == '1':
            self.setAtualizar_perfil() #sempre adicionar o self quando importar metodo de otra classe
        elif oppcao == "2":
            self.pesquisar_quartos()
        elif oppcao == '3':
            self.fazer_reserva()
        elif oppcao == '4':
           self.visualizar_reservas()    
        elif oppcao == '5':
           self.cancelar_reserva()
        elif oppcao == '6':
           self.pesquisa_tipo()
        elif oppcao == '7':
           self.fazer_logaout()

           
        else:
            print('Opção inválida')
            self.mostrar_opcoes_cliente(self)

    def pesquisar_quartos(self):
         print('-------Pesquisar Quartos------')
         print('Buscando quartos disponíveis...')
         self.hotel.quartos_disponiveis()
         self.mostrar_opcoes_cliente(self)

    def pesquisa_tipo(self):
        print('/n ------- Pesquisando por Tipo de Quarto -------')
        print('1 - Solteiro')
        print('2 - Casal')
        print('3 - Família')
        tipo = input('Digite o tipo de quarto que você procura: ')
        tipo_encontrado = False
   
       
        if tipo == '1':
          for quarto in self.hotel.quartos:
            if quarto.getTipo() == 'Solteiro':
             print(quarto.informacoes_quarto())
             tipo_encontrado = True
             self.mostrar_opcoes_cliente(self)
            
             
        elif tipo == '2':
           for quarto in self.hotel.quartos:
             if quarto.getTipo() == 'Casal':
                 print(quarto.informacoes_quarto())
                 tipo_encontrado = True
                 self.mostrar_opcoes_cliente(self)
             
        elif tipo == '3':
          for quarto in self.hotel.quartos:
              if quarto.getTipo() == 'Família':
                 print(quarto.informacoes_quarto())
                 tipo_encontrado =True
                 self.mostrar_opcoes_cliente(self)
              
        else:
              print('OPÇAO INVÁLIDA.')
              self.pesquisa_tipo()

        if tipo_encontrado == False:
           print('Não possuimos esse tipo de quarto no momento.')
           self.mostrar_opcoes_cliente(self)
       
       

    def fazer_reserva(self):
         print('------Fazer Reserva-----')
         numero_quarto = input('Qual quarto deseja reservar? (Insira somente o número do quarto): ')
         quarto_encontrado = None
         for quarto in self.hotel.quartos:
            if quarto.get_numero_quarto() == numero_quarto:
             if quarto.getDisponivel():
               quarto_encontrado = quarto
               break
             else:
                print('Quarto nao disponivel para reserva.')
                return  # Sai do método aqui, não permitindo o processo de reserva
           
         if quarto_encontrado:

             data_checkin = input('Informe a data de checkin(AAAA-MM-DD): ')
             data_checkout = input('Informe a data de check_out(AAAA-MM-DD): ')



             try:
                # Converte as strings de data para objetos datetime para comparar
                data_checkin = datetime.strptime(data_checkin, '%Y-%m-%d')
                data_checkout = datetime.strptime(data_checkout, '%Y-%m-%d')
             except ValueError:
                print("Formato de data inválido. Por favor, insira as datas no formato 'ano-mes-dia'.")
                self.fazer_reserva()
                return
             
         
        
             nova_reserva = Reserva(
                id_reserva=len(self.__historico_Reservas) + 1,
                cliente=self,
                quarto=quarto,
                data_checkin=data_checkin,
                data_checkout=data_checkout

             )
             
             if nova_reserva.confirmar_reserva() == True:
              self.__historico_Reservas.append(nova_reserva)
              self.hotel.adicionar_reserva(nova_reserva)
        
             self.mostrar_opcoes_cliente(self)
             
              
       
         if not quarto_encontrado:
            print('Quarto não encontrado.')
            self.mostrar_opcoes_cliente(self)
        

    def visualizar_reservas(self):
        print('------- Minhas Reservas --------')
        for reserva in self.__historico_Reservas:
            print(f"{reserva.informacoes()} ")
            print('---------------------')
        if not self.__historico_Reservas:
           print('Você não possui nenhuma reserva.')
        
        self.mostrar_opcoes_cliente(self)
    
        

    def cancelar_reserva(self):
        id = float(input('Digite o ID da sua reserva: '))
        reserva_encontrada = False
        for reserva in self.__historico_Reservas:
            if reserva.getID()== id:
              reserva.cancelar_reserva()
              self.__historico_Reservas.remove(reserva)
              self.hotel.remover_reserva(reserva)
              print(f'Reserva {reserva.getID()} cancelada')
              print(reserva.informacoes())
              reserva_encontrada = True
              self.mostrar_opcoes_cliente(self)
              break
        if not reserva_encontrada:  # Se a reserva não foi encontrada
            print('Reserva não encontrada. Verifique o ID e tente novamente.')
            self.mostrar_opcoes_cliente(self)
        

    def cadastro(self, novo_cliente):
      
       self.hotel.addCliente(novo_cliente)
       print('Cliente cadastrado!')
       self.mostrar_opcoes_cliente(self)
       

    def informacoes_cliente(self):
   
     informacoes = {
      'ID Cliente': self.id_cliente,
      "Nome": self.nome,
      'Nome de usuário' : self.getNome_usuario(),
      'Telefone': self.telefone,
      'Email': self.email,
      
    }
     print(informacoes)
    



     