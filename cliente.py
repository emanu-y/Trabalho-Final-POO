from usuario import Usuario

class Cliente (Usuario):
    def __init__(self, nome_usuario, senha, nome, email, telefone, id_cliente):
        super().__init__(nome_usuario, senha, nome, email, telefone)
        self.id_cliente = id_cliente
        self.__historico_Reservas = []

    def mostrar_opcoes_cliente(self):
        print('/n ---- HOME ----')
        print('Escolha uma opção:')
        print('1 - Atualizar Perfil')
        print('2 - Fazer Reserva')
        print('3 - Pesuisar Quartos ')
        print('4 - Visualizar Reservas')
        print('5 - Cancelar Reservas')
        print('6 - Sair')
        oppcao = input('Digite aqui:')

        if oppcao == '1':
            Usuario.setAtualizar_perfil(self) #sempre adicionar o self quando importar metodo de otra classe
        elif oppcao == "2":
            self.fazer_reserva()
        elif oppcao == '3':
            self.pesquisar_quartos()
        elif oppcao == '4':
           self.visualizar_reservas()    
        elif oppcao == '5':
         self.cancelar_reserva()
        elif oppcao == '6':
           Usuario.fazer_logaout

           
        else:
            print('Opção inválida.')


    
        
        
  
         
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




    