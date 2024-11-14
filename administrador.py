from usuario import Usuario
from quarto import Quarto
from cliente import Cliente
from relatorio import Relatorio

class Administrador(Usuario):
    def __init__(self, nome_usuario, senha, nome, email, telefone, id_adm):
        super().__init__(nome_usuario, senha, nome, email, telefone)
        self.id_adm = id_adm
        self.clientes = []
        self.quartos = [
           Quarto(101,'casal', "Vista para o mar", 300),
            Quarto(102,'familia', "Vista para o jardim", 200),
            Quarto(103,'solteiro', "Com varanda",320),
        ]
        
        self.reservas = []


    def getClientes(self):
        return self.clientes
      
      
    def getId (self):
     return self.id_adm
    
    def getEmail(self):
       return self.email
    
        
    def getQuartos(self):
       return self.quartos
    

    
    
    def mostrar_opcoes_adm(self):
       print('Gerenciamento do Hotel')
       print('Digite o numero da opçao desejada.')
       print('1 - Cadastrar Cliente')
       print('2 - Adiionar Quarto')
       print('3 - Atualizar Quarto')
       print('4 - Remover Quarto')
       print('5 - Visuallizar Reservas')
       print('6 - Gerar Relatorio Mensal')
       print('7 - Atualizar Perfil')
       print('8 - Sair')
       oppcao = input('Digite aqui: ')


       if oppcao == '1':
           self.adicionarCliente()
       elif oppcao == '2':
          self.adicionar_quarto()
       elif oppcao == '3':
          self.setAtualizar_quarto()
       elif oppcao == '4':
          self.remover_quarto()
       elif oppcao == '5':
          self.visualizar_todas_as_reservas()
       elif oppcao == '6':
          Relatorio.gerar_relatorio(self)
       elif oppcao == '7':
          self.setAtualizar_perfil()
       elif oppcao == '8':
          self.fazer_logaout()
          
       else:
          print('Opção invalida.')
          self.mostrar_opcoes_adm()

    def adicionarCliente(self):
        print('CADASTRAR CLIENTES: ')
        nome = input('Nome: ')
        nome_u= input('nome usuario: ')
        senha = input('senha :')
        telefone = input('telefone : ')
        email = input('email: ')
        idCiente = input('id cliente: ')

        novo_cliente = Cliente(nome_u, senha, nome, email, telefone, idCiente)
        self.clientes.append(novo_cliente)
        print('Cliente foi cadastrado!')
        self.mostrar_opcoes_adm()

    
        

    def adicionar_quarto(self):
       print('ADICIONAR QUARTO: ')
       numero = input('Digite o numero do quarto: ')
       
       for quarto in self.quartos:
         if numero == quarto.getNumero_quarto():    #Quarto.getNumero_quarto()
             print('Ja existe um quarto com esse numero.')
             self.adicionar_quarto()
             return
        
       tipo = input('Tipo de quarto : ')
       preco = input('Preçp por noite: ') 
       preco = float(preco)
       caracteristicas = input('Caracteristicas: ')

       novo_quarto = Quarto(numero, tipo, caracteristicas, preco)
       #KAKAKAKKA SURTOS COM ESSA PARTE
       self.quartos.append(novo_quarto)
       print(f'Quarto {numero} foi adicionado.')
       self.mostrar_opcoes_adm()
    

       
       

        

    def setAtualizar_quarto (self):
      print('------Atualizar Quarto-----')
      numero = input('Digite o numero do quarto que deseja atualizar: ')
      for quarto in self.quartos:
         if  quarto not in self.quartos:
            print('Nao possuimos quartos cadastrados.')
         elif numero == quarto.getNumero_quarto():               #ARRUMAR OS ENUNCIADOS 
            novo_tipo = input('novo tipo:')
            nova_caract= input('NOvas Caractristicas:')
            preco_atualizado = float(input('Novo preco p/n:'))
            
            
            if novo_tipo:
               quarto.setTipo( novo_tipo)
            if nova_caract:
               quarto.setCaracteristicas( nova_caract)
            if preco_atualizado:
                try:
                 quarto.setPreco(float(preco_atualizado))
                except ValueError:
                   print('Valor Invalido.')
            self.setAtualizar_quarto()
                                                         #achar um jeito de colocar erro e voltar pro negocio de menu quando o float der errado
            print('quarto atualizado')
            self.mostrar_opcoes_adm()
         else:
            print('quarto não encontrado.')
            self.setAtualizar_quarto()  
      
    def remover_quarto(self):
       print('---- Remover Quarto-----')
       numero = input('Numero do quarto que deja remover: ')
       for quarto in self.quartos:
          if numero == quarto.getNumero_quarto():
             self.quartos.remove(quarto)
             print(f'Quarto {numero} foi removido.')
             self.mostrar_opcoes_adm()
       else:
             print('Quarto não encontrado.')
             self.mostrar_opcoes_adm()

        

        

    def visualizar_todas_as_reservas(self):
        print('-----Reserva-----')
        
        for reserva in self.reservas:
           print(f'{reserva}')
        pass
    


   #  def pesquisarQuartos(self):
   #      print('-----QUARTOS DISPONIVEIS')
              
        
       
       
   #      for quarto in self.quartos:
   #       if Quarto.verificar_disponibilidade(self) == True:
   #            print(f'Numero: {quarto.getNumero_quarto()} ')
   #            print(f'Descrição {quarto.getcaracteristicas()}')
   #            print(f'Tipo: {quarto.getTipo()}')
   #            print(f'Pernoite: {quarto.getPreco_porNoite}')
   #            print('---------------------------------------------------')

# if __name__ == '__main__':
   
   
   
#    a= Cliente ('emanu', 'adimin', 'eman', 'udeiadimin', 930490293, 999)
   
#    b= Administrador ('emanu', 'adimin', 'eman', 'udei@adimin', 930490293, 000)
    
    
   
   
#    a.inicio()
#    a.pesquisar_quartos(b)
  
 
#    quartos = [
#      Quarto('1', 'casal', 'lalalala', 12),
#      Quarto('2', 'familia', 'gggggggggg', 14),
#      Quarto('3', 'solteiro', 'ldjjdjdjdjdjnja', 125)
#    ]



   



    





    


    


 
      