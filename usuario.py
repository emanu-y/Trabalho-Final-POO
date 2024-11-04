class Usuario :
    def __init__(self, nome_usuario, senha, nome, email, telefone):
        self.nome_usuario = nome_usuario
        self.__senha = senha
        self.nome = nome 
        self.email = email 
        self.telefone = telefone

    def getSenha(self):
        return self.__senha
               

    def fazer_login(self):
        pass

    def fazer_logaout(self):
        pass
    
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



        

