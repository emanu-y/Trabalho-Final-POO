#Classe que cria objetos de usuarios


class Usuario ():
    def __init__(self, nome_usuario, senha, nome, email, telefone):
        self.__nome_usuario = nome_usuario
        self.__senha = senha
        self.nome = nome 
        self.email = email 
        self.telefone = telefone
        self.tipo = 'adimin' if email.endswith('@adimin') else 'cliente'
        
    def getSenha(self):
        return self.__senha
    
    def getNome_usuario(self):
        return self.__nome_usuario
    def get_tipo(self):
       return self.tipo
    
    
    def fazer_login(self, usuario, senha):   
         if usuario == self.getNome_usuario():          
             if senha == self.getSenha():       
                if self.tipo == 'adimin':  
                  print('Acesso Permitido')
                  from administrador import Administrador
    
                  Administrador.mostrar_opcoes_adm(self) 
                elif self.tipo == 'cliente':
                 from cliente import Cliente
                 Cliente.mostrar_opcoes_cliente(self)

                        #sempre adicionar o self quando importar metodo de otra classe                                            
                return
         else: 
            print('Senha ou nome de usuário incorreto. Tente Novamente.')
          

            
                

    def fazer_logaout(self):
        print(f'{self.getNome_usuario()} saiu.')
        

        
    def setAtualizar_perfil(self):
        print('/n -------- Atualizar Perfil --------')
        print('Confirme sua senha para atualizar perfil:')
        while True > 0: 
         senha= input('Digite sua senha:')
         confirmação_senha = input(' Confirme sua senha:')
         if senha == self.getSenha() and confirmação_senha == self.getSenha():
            print("\n--- Atualizando Perfil ---")
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
 