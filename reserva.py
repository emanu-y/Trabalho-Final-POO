from pagamento import Pagamento



class Reserva:
    def __init__(self, id_reserva, cliente, quarto, data_checkin, data_checkout):
        self.id_reserva = id_reserva
        self.cliente = cliente
        self.quarto = quarto
        self.data_checkin = data_checkin 
        self.data_checkout = data_checkout
        self.preco_total= 0
       
    
    
    
    def getID(self):
       return self.id_reserva
    

    def informacoes(self):
      reserva = {
           'id':  self.id_reserva,
           'nome' : self.cliente.nome,
           'ID Cliente' : self.cliente.id_cliente,
           'quarto': self.quarto.get_numero_quarto(),
           'data checkin': self.data_checkin,
           'data checkout': self.data_checkout,
           


      }
      return reserva


    def calcular_total(self):
       
       dias = (self.data_checkout - self.data_checkin).days
       preco_por_dia = self.quarto.get_preco_porNoite() 
       self.preco_total = dias * preco_por_dia
       return self.preco_total
                
              
        
    def confirmar_reserva(self):
       while True:
        print('Deseja Confirmar sua Reserva?')
        print('1 - Sim')
        print('2 - Cancelar')
        resposta = input('Digite aqui : ')
        if resposta == '1':   
          if self.data_checkout > self.data_checkin:  
           self.calcular_total()
           print(f'Sua estadia fica por R${self.calcular_total()}')
           print('Deseja realizar o pagamento?')
           print('1 - Sim')
           print('2 - Cancelar')
           opcao = input('Digite aqui: ')
           if opcao == '1':
              
              pagamento = Pagamento(self.id_reserva, self.preco_total )
              pagamento.processar_pagamento()
              


              self.quarto.reservar_quarto()
           
              print(f'Reserva confirmada para {self.cliente.nome} no quarto {self.quarto.get_numero_quarto()}!!')
              return True
           
           elif opcao == '2':
              pagamento = Pagamento(self.id_reserva, self.preco_total )
              pagamento.cancelar_pagamento()
              print('Reseva não realizada.')
              
          else:
             
             print('Não é possivel reservar quarto nessa data.')
          break
         
         
        elif resposta == '2':
            self.cancelar_reserva()
            print('Reserva cancelada.')
            break 
        else:
           print("OPÇÃO INVÁLIDA. TENTE NOVAMENTE.")
           self.confirmar_reserva()

    def cancelar_reserva(self):
           self.quarto.liberar_quarto() 

      
        # preciso que quarto seja instancia de Quarto, e aqui esta sendo passado como string 
        
      
       