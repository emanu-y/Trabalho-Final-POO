# from hotel import Hotel
class Usuario :
    def __init__(self, nome_usuario, senha, nome, email, telefone):
        self.__nome_usuario = nome_usuario
        self.__senha = senha
        self.nome = nome 
        self.email = email 
        self.telefone = telefone
        #adicionar o tipo de conta

        #  print('Digite o numero da opção desejada:')
        #         print('1 - Atualizar Perfil')
        #         print('2 - Fazer Reserva')
                
        
    def getSenha(self):
        return self.__senha
    
    def getNome_usuario(self):
        return self.__nome_usuario
    
    # def inicio (self):
    #     print('Bem Vindo ao SiStema de Gernciamenti de HOtel. Escolha uma opçao: ')
    #     print('1 - Login')
    #     print('1- criar conta')
        
    
   
    def fazer_login(self):
        print('LOGIN')
        nome_u = input('Digite o nome de usuario: ')
        if nome_u == self.getNome_usuario():
            tentativas = 3
            # Laço para permitir até 3 tentativas de senha
            while tentativas > 0: 
             senha = input('Digite sua senha: ')
             if senha == self.getSenha(): 
                print('Acesso Permitido') 
                self.mostrar_opcoes()
                #opções para escolher
                                                   
                return
            
             else:
                tentativas -= 1
                print(f'Senha incorreta. Você tem mais {tentativas} tentativa(s).')
                print('tente novamente')
        else: 
            print('Ususario nao encontrado.')


    def mostrar_opcoes(self):
        print('Escolha uma opção:')
        print('1- Atualizar Perfil')
        print('2- Fazer Reserva')
        print('3- Sair')
        oppcao = input('Digite aqui:')

        if oppcao == '1':
            self.setAtualizar_perfil()
        elif oppcao == "2":
            #clienre.fazer_reserva()
            pass 
        elif oppcao == '3':
            self.fazer_logaout()
        else:
            print('Opção inválida.')
            
             
          
    
    
    
    


        


    
  
    
        

    def fazer_logaout(self):
        print(f'{self.getNome_usuario()} saiu.')

        
    
    def setAtualizar_perfil(self):
        print('Digite Sua Senha:')
        # senha = input('Senha: ')
        # if senha == self.getSenha:
        #  nomeUsuario = input('Nome: ')
        #  novaSenha = input('N')
        # self.__senha = senha
        # self.nome = nome 
        # self.email = email 
        # self.telefone = telefone
        #   print('Atualizar Perfil:')


        #   self.nome
    
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







if __name__ == '__main__':
    c1 = Usuario('emanu22', 'senhaeman', 'Emanuelly', 'emanuelly@gmail.com', 9898989)
    c1.inicio()

