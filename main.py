from administrador import Administrador
from cliente import Cliente
from quarto import Quarto
from hotel import Hotel

def login():
    print("Bem-vindo ao Sistema de Gestão de Reservas!")
    print("Escolha o tipo de login:")
    print("1 - Administrador")
    print("2 - Cliente")
    print("3 - Cadastrar")
    print('4 - Sair')
    opcao = input("Digite sua opção: ")

    if opcao == "1":
          usuario = input("Digite seu nome de usuário: ")
          senha = input("Digite sua senha: ")
          for user in usuarios:    
             if isinstance(user, Administrador):
                 user.fazer_login(usuario, senha)
             else:
                    print('Senha ou nome de usuário incorreto. Tente novamente.')
                    login()
                    return       
        
    try:

     if opcao == "2":
        usuario = input("Digite seu nome de usuário: ")
        senha = input("Digite sua senha: ")
        for user in usuarios:
            if isinstance(user, Cliente):
                if user.fazer_login(usuario, senha):
                    break
                    
                else:
                    login()
                    return
    except:
        print("Você não está cadastrado como Cliente.")
        login() 

    
    if opcao == '3':
        cliente = False
        print('------ Cadastro ------')
        nome = input('Digite seu nome: ')
        nome_u = input('Digite seu nome de usuário: ')
        telefone = input('Digite seu telefone: ')
        email = input('Digite seu email: ')
        senha = input('Digite sua senha: ')
        senha = input('Confirme sua senha: ')
        cliente = True
        if cliente == True:
         novo_cliente= Cliente(nome_u, senha, nome, email, telefone)
         novo_cliente.cadastro(novo_cliente)

        else:
            
            print('Você precisa inserir valores válidos para cadastrar cliente.')
            login()
        

    if opcao == '4':
        print('Saindo...')
        exit() 
        return 
       

    else:
        print("Opção inválida.")
        






if __name__ == '__main__':
   
   
   hotel = Hotel()

usuarios =  [

     Administrador('yas', 'senha', 'eman', 'udei@adimin', 930490293, 000),
     Cliente('emanu', 'adimin', 'eman', 'udeiadimin', 930490293)
             ]
login()

  





