class Quarto:
    def __init__(self, numero_quarto, tipo_quarto, caracteristicas, preco_por_noite, disponivel):
        self.numero_quarto = numero_quarto
        self.tipo_quarto = tipo_quarto
        self.caracteristicas = caracteristicas
        self.preco_por_noite = float(preco_por_noite)
        self.disponibilidade = disponivel

    def get_numero_quarto(self):
        return self.numero_quarto

    def getDisponivel(self):
        return self.disponibilidade 
    
    def get_preco_porNoite(self):
        return self.preco_por_noite
    
    def getCaracteristicas(self):
        return self.caracteristicas
    
    def getTipo(self):
        return self.tipo_quarto
        
    def setTipo (self, n_tipo):
        self.tipo_quarto = n_tipo

    def setCaracteristicas(self, N_cara):
        self.caracteristicas = N_cara
    
    def setPreco(self, valor):
        self.preco_por_noite = valor

    def setDisponivel(self, status):
        self.disponibilidade = status


    def verificar_disponibilidade(self):
        if self.disponibilidade == True:
            return True
        elif self.disponibilidade == False:
            print('O quarto esta indisponovel')

    def informacoes_quarto(self):
        informacoes = {
            'Número ': self.get_numero_quarto(),
            'Tipo de Quarto ': self.getTipo(),
            'Caractrísticas ': self.getCaracteristicas(),
            'Preço por noite' : self.get_preco_porNoite()

        }
        return informacoes
    

        
    
       
       

    
         
        
           
        
    def reservar_quarto(self):
        if self.getDisponivel() == True:
            self.setDisponivel(False)
        
            
        
       
    def liberar_quarto(self):
        if not self.disponibilidade:
            self.disponibilidade = True
           





        







