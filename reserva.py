from cliente import Cliente
from quarto import Quarto 
from administrador import Administrador

class Reserva:
    def __init__(self, id_reserva, cliente, quarto, data_checkin, data_checkout):
        self.id_reserva = id_reserva
        self.cliente = Cliente
        self.quarto = Quarto
        self.data_checkin = data_checkin 
        self.data_checkout = data_checkout
        self.preco_total= []
    

    def info(self):
        pass

    def calcular_total(self):
        print('CALCULAR PREÇO')
        numero = input('Digite o numero do quarto que voçe deseja alugar')
        dias = input(f'Informe quantos dias deseja alugar o quarto {numero} : ')
        
        for numero in Administrador.self.quartos(self):
            if numero == Quarto.getNumero_quarto(self):
                total = dias * Quarto.getPreco_porNoite(self)
                print(f'Sua estadia fica por {total}')
            else:
                print('Quarto não encontrado.')

    def confirmar_reserva(self):
        print('reserva confirmada')

    def cancelar_reserva(self):
        print('reserva cancelada.')
       