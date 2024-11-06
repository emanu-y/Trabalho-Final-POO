


class Usuario :
    def __init__(self, nome_usuario, senha, nome, email, telefone):
        self.__nome_usuario = nome_usuario
        self.__senha = senha
        self.nome = nome 
        self.email = email 
        self.telefone = telefone
        #adicionar o tipo de conta
                
        
    def getSenha(self):
        return self.__senha
    
    def getNome_usuario(self):
        return self.__nome_usuario
    

    def inicio (self):
        print('Bem Vindo ao SiStema de Gernciamenti de HOtel. Escolha uma opçao: ')
        print('1 - Login')
        print('1- criar conta')
        opcao = input('Digite aqui: ')
        if opcao == "1": 
            self.fazer_login()
        elif opcao == '2':
            self.fazer_login()
        else:
            print('Opção inválida.')
     
    def fazer_login(self):
        print('LOGIN')
        nome_u = input('Digite o nome de usuario: ')
        if nome_u == self.getNome_usuario():
            tentativas = 3
            # Laço para permitir até 3 tentativas de senha
            while tentativas > 0: 
             senha = input('Digite sua senha: ')
             if senha == self.getSenha(): 
                if self.getNome_usuario() in Administrador.getClientes():  
                  print('Acesso Permitido') 
                  self.mostrar_opcoes_cliente()
                    #opções para escolher
                else:
                   self.mostrar_opcoes_adm()
                                                   
                return
            
             else:
                tentativas -= 1
                print(f'Senha incorreta. Você tem mais {tentativas} tentativa(s).')
                print('tente novamente')
        else: 
            print('Ususario nao encontrado.')

   


    def mostrar_opcoes_cliente(self):
        print('/n ---- HOME ----')
        print('Escolha uma opção:')
        print('1 - Atualizar Perfil')
        print('2 - Fazer Reserva')
        print('3 - Pesuisar Quartos ')
        print('4 - Visualizar Reservas')
        print('5 - Cancelar Reservas')
        print('6 - Sair')
        oppcao = input('Digite aqui:')

        if oppcao == '1':
            self.setAtualizar_perfil()
        elif oppcao == "2":
            Cliente.fazer_reserva()
        elif oppcao == '3':
            Cliente.pesquisar_quartos()
        elif oppcao == '4':
           Cliente.visualizar_reservas()    
        elif oppcao == '5':
         Cliente.cancelar_reserva()
        elif oppcao == '6':
           self.fazer_logaout

           
        else:
            print('Opção inválida.')

    def mostrar_opcoes_adm():
       print('Gerenciamento do Hotel')
       print('Digite o numero da opçao desejada.')
       print('1 - Adicionar Cliente')
       print('2 - Adiionar Quarto')
       print('3 - Atualizar Quarto')
       print('4 - Remover Quarto')
       print('5 - Visuallizar Reservas')
       print('6 - Gerar Relatorio Mensal')
       oppcao = input('Digite aqui: ')


       if oppcao == '1':
          Administrador.adicionarCliente()
       elif oppcao == '2':
          Administrador.adicionar_quarto()
       elif oppcao == '3':
          Administrador.atualizar_quarto()
       elif oppcao == '4':
          Administrador.remover_quarto()
       elif oppcao == '5':
          Administrador.visualizar_todas_as_reservas()
       elif oppcao == '6':
          Administrador.gerar_relatorio()
       else:
          print('Opção invalida.')
            
                

    def fazer_logaout(self):
        print(f'{self.getNome_usuario()} saiu.')

        
    def setAtualizar_perfil(self):
        tentativas = 10
        while tentativas > 0: 
         print('Digite sua senha: ')
         senha= input('Digite aqui:')
         print('Confirme sua Senha:')
         confirmação_senha = input('Digite aqui:')
         if senha == self.getSenha() and confirmação_senha == self.getSenha():
            print("\n--- Atualização de Perfil ---")
            novo_nome = input("Novo nome (pressione Enter para manter o atual): ")
            novo_email = input("Novo email (pressione Enter para manter o atual): ")
            novo_telefone = input("Novo telefone (pressione Enter para manter o atual): ")
        
            if novo_nome:
               self.nome = novo_nome
            if novo_email:
                self.email = novo_email
            if novo_telefone:
              self.telefone = novo_telefone
        
            print("Perfil atualizado com sucesso.")
            self.mostrar_opcoes()
            return
        else:
            print('Senha incorreta. Tente novamente.')
 
if __name__ == '__main__':
    c1 = Usuario('emanu22', 'senhaeman', 'Emanuelly', 'emanuelly@gmail.com', 9898989)
    c1.inicio()
   



