while True:
    print('Gerenciador de Senhas')
    print('1 - Cadastrar nova senha')
    print('2 - Listar senhas cadastradas')
    print('3 - Buscar senha por serviço')
    print('4 - Sair')
    
    
    opcao = input('Escolha uma opção:')

    if opcao == '1':
        servico = input('Qual é o serviço?')
        usuario = input('Qual a usuario?')
        senha = input('Qual a senha?')

        with open('senhas.txt', 'a') as arquivo:
            arquivo.write(f'{servico} | {usuario} | {senha}\n')
        
    elif opcao == '2':
        print('Senhas cadastradas:')
        with open('senhas.txt','r') as arquivo:
            print('Serviço | Usuário | Senha')
            print('-' * 30)
            for linha in arquivo:
                print(linha.strip())

    elif opcao  == '3':
        buscar = input('Digite o nome do serviço para buscar a senha:')
        with open('senhas.txt', 'r') as arquivo:
            encontrado = False
            for linha in arquivo:
                if buscar.lower() in linha.lower():
                    print('Senha encontrada:')
                    print('Serviço | Usuário | Senha')
                    print('-' * 20)
                    print(linha.strip())
                    encontrado = True
            if not encontrado:
                print('Serviço não encontrado.')
        
    
    elif opcao == '4':
        print('Saindo do gerenciador de senhas...')
        break