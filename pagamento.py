import uuid
from datetime import datetime

class Pagamento:

    def __init__(self, reserva, valor):
        self.id_pagamento =   str(uuid.uuid4())
        self.reserva = reserva
        self.valor = valor
        self.data_pagamento = None


    def processar_pagamento(self):
        self.data_pagamento = datetime.now().strftime('%Y-%m-%d %H:%M')
        
        print('Pagamento realizado')
        informaçoes_pagamento = {
            'ID Pagamento': self.id_pagamento,
            'ID Reserva' : self.reserva,
            'Valor' : self.valor,
            'Data' : self.data_pagamento 
        }
        print(informaçoes_pagamento)


    def cancelar_pagamento(self):
        print('Pagamento cancelado.')
    