from usuario import Usuario
from quarto import Quarto


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
            self.setAtualizar_perfil(self) #sempre adicionar o self quando importar metodo de otra classe
        elif oppcao == "2":
            self.fazer_reserva()
        elif oppcao == '3':
            self.pesquisar_quartos()
        elif oppcao == '4':
           self.visualizar_reservas()    
        elif oppcao == '5':
           self.cancelar_reserva()
        elif oppcao == '6':
           self.fazer_logaout()

           
        else:
            print('Opção inválida.')

         
    def pesquisar_quartos(self):
        print('-----QUARTOS DISPONIVEIS-----')
        from administrador import Administrador
        for quarto in Administrador.getQuartos(self):
            if quarto.getDisponovel == True:
              print(f'Numero: {quarto.getNumero_quarto()} ')
              print(f'Descrição {quarto.getcaracteristicas()}')
              print(f'Tipo: {quarto.getTipo()}')
              print(f'Pernoite: {quarto.getPreco_porNoite}')
              print('---------------------------------------------------')
        print('Deseja reservar algum quarto?')
        print('1 - Sim')
        print('2 - Nâõ')
        opcao = input('Digite aqui: ')
        if opcao == 1:
            self.fazer_reserva()
        elif opcao == 2:
            self.mostrar_opcoes_cliente()
        else:
            print('Opção Invalida.')
            self.mostrar_opcoes_cliente()

    def fazer_reserva(self):
        print('------Fazer Reserva-----')
        quarto = input('Digite o numero do quarto que voçe deseja reservar: ')
        from administrador import Administrador
        if quarto in Administrador.getQuartos(self):
            if  quarto.Disponibilidade == True:
                self.__historico_Reservas.append(quarto)
                quarto.setDisponibilidade(False)
                print(f'Reserva do quarto {quarto} foi realizada.')
                self.mostrar_opcoes_cliente()
            else:
                print('Quarto não esta disponivel.')
                self.mostrar_opcoes_cliente()
        else: 
            print('Quarto não encontrado.')
            self.mostrar_opcoes_cliente()

                

        # adicionar reserva no array hitorico de reservas
        pass

    def visualizar_reservas(self):
        print('------- Minhas Reservas --------')
        for reserva in self.__historico_Reservas:
            print(reserva)
        # visualizar a reserva que esta fazndo ou todas as reservas que ja foram feitas?
    
        pass

    def cancelar_reserva(self):
        print('----- CANCELAR RESERVA -----')
        reserva = input('Digite o id da reserva que deseja cancelar: ')
        if reserva == reserva.getId:
            self.__historico_Reservas.remove(reserva)
        else:
            print('Voce não possui essa reserva.')

        #remover reserva do array reserva 
        pass




    