class Quarto:
    def __init__(self, numero_quarto, tipo_quarto, caracteristicas, preco_por_noite):
        self.numero_quarto = numero_quarto
        self.tipo_quarto = tipo_quarto
        self.caracteristicas = caracteristicas
        self.preco_por_noite = preco_por_noite
        self.disponibilidade = True

    def getNumero_quarto(self):
        return self.numero_quarto

    def getDisponivel(self):
        return self.disponibilidade
    
    def setDisponivel(self, status):
        self.disponibilidade = status


    def verificar_disponibilidade(self):
        if self.getDisponivel == True:
            return 'O quarto está disponível.'
        else:
            return 'o quarto está reservado.'
        
    def reservar_quarto(self):
        #mudar a disponibilidade
        pass

    def liberar_quarto(self):
        pass


qua = Quarto(434,'seila')




