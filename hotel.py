from quarto import Quarto
from usuario import Usuario
class Hotel:
    def __init__(self): 
         self.quartos = [
             Quarto('101','casal', "Vista para o mar", 300, True),
            Quarto('102','familia', "Vista para o jardim", 200, True),
            Quarto('103','Solteiro', "Com varanda",320, True),
        ]
         self.usuarios =[
            
            
         ]
         
         self.clientes = [
          
         ]

         self.reservas = [
        
             
         ]



    def get_quartos(self):
        return self.quartos
    def get_clientes(self):
        return self.clientes
    

    def addCliente(self, cliente):
        self.clientes.append(cliente)

    def remover_cliente(self, cliente):
        self.clientes.remove(cliente)

    def adicionar_reserva(self, reserva):
        self.reservas.append(reserva)
    def remover_reserva(self,reserva):
        self.reservas.remove(reserva)

    def adicionar_quarto(self, quarto):
        self.quartos.append(quarto)

    def remover_quarto(self, quarto):
        self.quartos.remove(quarto)
    
    def quartos_disponiveis(self):
        encontrados = False
        for quarto in self.quartos:
          
          if quarto.getDisponivel() == True:
             print(quarto.informacoes_quarto())
             print('=======================================')
             encontrados = True
        if not encontrados:
            print('Não temos quartos disponíveis no momento.')
              

    def todos_quartos(self):
        for quarto in self.quartos:
            print(quarto.informacoes_quarto())
            print('=======================================')
   
