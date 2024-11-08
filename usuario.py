
class Usuario ():
    def __init__(self, nome_usuario, senha, nome, email, telefone):
        self.__nome_usuario = nome_usuario
        self.__senha = senha
        self.nome = nome 
        self.email = email 
        self.telefone = telefone
        self.tipo = 'adimin' if email.endswith('@adimin') else 'cliente'
        # self.tipo = 'adimin' or 'cliente'
        # if self.email == f'{self.getNome_usuario}@adimin':
        #    self.tipo == 'adimin'
        # else:
        #    self.tipo == 'cliente'
        # #adicionar o tipo de conta
                
        
    def getSenha(self):
        return self.__senha
    
    def getNome_usuario(self):
        return self.__nome_usuario
    

    def inicio (self):
        print('Bem Vindo ao SiStema de Gernciamenti de HOtel. Escolha uma opçao: ')
        print('1 - Login')
        print('1- criar conta')
        print('3 - sair')
        opcao = input('Digite aqui: ')
        if opcao == "1": 
            self.fazer_login()
        elif opcao == '2':
            self.fazer_login()
        elif opcao == '3':
           self.fazer_logaout()
        else:
            print('OPÇÃO INVÁLIDA.')
            self.inicio()
        
        

     
    def fazer_login(self):
        print('LOGIN')
        nome_u = input('Digite o nome de usuario: ')
        if nome_u == self.getNome_usuario():
            tentativas = 3
            # Laço para permitir até 3 tentativas de senha
            while tentativas > 0: 
             senha = input('Digite sua senha: ')
             if senha == self.getSenha(): 
                
                if self.tipo == 'adimin':  
                  print('Acesso Permitido')
                  from administrador import Administrador
                   # Cria uma instância de Administrador e chama o método de opções
                  adm = Administrador(self.__nome_usuario, self.__senha, self.nome, self.email, self.telefone, 222)
                  adm.mostrar_opcoes_adm() 
                         #sempre adicionar o self quando importar metodo de otra classe         
                   #opções para escolher
                elif self.tipo == 'cliente':
                 from cliente import Cliente
                 Cliente.mostrar_opcoes_cliente(self)
                        #sempre adicionar o self quando importar metodo de otra classe                                            
                return
            
             else:
                tentativas -= 1
                print(f'Senha incorreta. Você tem mais {tentativas} tentativa(s).')
                print('tente novamente')
        else: 
            print('Ususario nao encontrado.')
            self.inicio()


            
                

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
            if self.tipo == 'adimin':                     #mudanças para retornar ao menu que pertence a cada classe
             from administrador import Administrador
             adm = Administrador(self.__nome_usuario, self.__senha, self.nome, self.email, self.telefone, 222)
             adm.mostrar_opcoes_adm() 
            else:
          
             from cliente import Cliente
             Cliente.mostrar_opcoes_cliente(self)
            return
        else:
            print('Senha incorreta. Tente novamente.')
 
if __name__ == '__main__':
    c1 = Usuario('emanu22', 'senhaeman', 'Emanuelly', 'emanuelly@gmail.com', 9898989)
    adm = Usuario ('emanu', 'adimin', 'eman', 'udeid@adimin', 930490293)

    adm.inicio()
    
     #arrumar um jeito de nao precisar instanciar
   



