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
           





        


qua = Quarto(434,'seila')




