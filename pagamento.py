from reserva import Reserva

class Pagamento:

    def __init__(self, id_pagamento, reserva, valor, data_pagamento):
        self.id_pagamento = id_pagamento
        self.reserva = reserva
        self.valor = valor
        self.data_pagamento = data_pagamento
        self.status = "pendente"  # Novo atributo para status do pagamento

    def validar_dados(self):
        if not isinstance(self.reserva, Reserva):
            raise ValueError("Reserva inválida.")
        if self.valor <= 0:
            raise ValueError("O valor do pagamento deve ser positivo.")
        # Verificação adicional para a data (opcional)

    def processar_pagamento(self):
        self.validar_dados()  # Valida os dados antes de processar
        # Simulação do processamento de pagamento
        try:
            # Lógica de integração com sistema de pagamento (exemplo fictício)
            self.status = "processado"
            print(f"Pagamento {self.id_pagamento} processado com sucesso.")
        except Exception as e:
            self.status = "falha"
            print(f"Erro ao processar pagamento {self.id_pagamento}: {e}")

    def cancelar_pagamento(self):
        if self.status == "processado":
            print("Não é possível cancelar um pagamento já processado.")
        else:
            self.status = "cancelado"
            print(f"Pagamento {self.id_pagamento} foi cancelado.")

# from reserva import Reserva

# class Pagameto:

#     def __init__(self, id_pagamento, reserva, valor, data_pagamento):
#         self.id_pagamento= id_pagamento
#         self.reserva = reserva
#         self.valor = valor
#         self.data_pagamento = data_pagamento


#     def processar_pagamento(self):
#         pass