class Quarto:
    def __init__(self, numero_quarto, tipo_quarto, caracteristicas, preco_por_noite):
        self.numero_quarto = numero_quarto
        self.tipo_quarto = tipo_quarto
        self.caracteristicas = caracteristicas
        self.preco_por_noite = float(preco_por_noite)
        self.disponibilidade = True

    def getNumero_quarto(self):
        return self.numero_quarto

    def getDisponivel(self):
        return self.disponibilidade 
    
    def getPreco_porNoite(self):
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
        print('DIGITE O NUMERO DO QUARTO')
        numero = input('Digite aqui: ')
        if numero in numero: #lista de quartoos 
        
         if self.getDisponivel() == True:
            return 'O quarto está disponível.'
         else:
            return 'o quarto está reservado.'
        else:
            print('Quarto nao encontrado.')
        
    def reservar_quarto(self):
        print('DIGITE O NUMERO DO QUARTO')
        numero = input('Digite aqui: ')
        #  if numero in lista de quartos
        if self.getDisponivel() == True:
            self.setDisponivel(False)
            print('Seu Quarto foi reservado.')
        else:
            return 'Quarto Indisponível.'
        
       
    def liberar_quarto(self):
        print('DIGITE O NUMERO DO QUARTO')
        numero = input('Digite aqui: ')
        # if numero in lista de quartos: 
        if self.getDisponivel() == False:
               self.setDisponivel(True)
               print('O quarto foi liberado.')
        else:
               print('Esse quarto já está disponível.')
           





        







