from cliente import Cliente
from quarto import Quarto 
from administrador import Administrador


class Reserva:
    def __init__(self, id_reserva, cliente, quarto, data_checkin, data_checkout):
        self.id_reserva = id_reserva
        self.cliente = cliente
        self.quarto = quarto
        self.data_checkin = data_checkin 
        self.data_checkout = data_checkout
        self.preco_total= []
    

    def info(self):
        pass

    def calcular_total(self):
        print('CALCULAR PREÇO')
        quarto = input('Digite o numero do quarto que deseja fazer a reserva: ')
        data_checkin = float(input('Digite a data de checkin (data de chegada) : '))
        data_checkout =float(input('Digite a data de checkout (data de saída): '))

        quartos_disponiveis = Administrador.getQuartos(self)
        for quarto in quartos_disponiveis:
            if quarto == quarto.getNumero_quarto():
                dias = data_checkout - data_checkin
                total = dias * quarto.getpreco_porNoite()
                self.preco_total = total 
                print(f'Sua estadia fica por {total}')
            else:
                print('Quarto não encontrado.')

    def confirmar_reserva(self):
        print('Deseja Confirmar sua Reserva?')
        print('1 - Sim')
        print('2 - Não')
        resposta = input('Digite aqui : ')
        if resposta == '1':
          print('reserva confirmada')
        elif resposta == '2':
            print('Você tem até 3 semanas antes da data de checkin para confirmar sua reserva. ')

    def cancelar_reserva(self):
        print('------Cancelar Reserva----------')
        id = input('Digite o Id da sua reserva: ')
        print('Reserva cancelada.')
       