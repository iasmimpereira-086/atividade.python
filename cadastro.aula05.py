listaLogins = []
listaSenhas = []

print("\n-- LISTA DE LOGIN--")

while True:
    print("\n O que deseja fazer?")
    print("1 Cadastrar Usuário")
    print("2 Cadastrar Senha")
    print("3 Sair")

    opcao = input("Escolha uma opção desejada: ")

    if opcao == "1":
        print("\n--CADASTRO--")
        novoUsuario = input("Digite um nome de usuário: ")
        novaSenha = input("Digite uma senha: ")

        if novoUsuario in listaLogins:
            print("Esse usuário já existe!")
        else:
            listaLogins.append(novoUsuario)
            listaSenhas.append(novaSenha)
            print("Usuário cadastrado com sucesso!")

    elif opcao =="2":
        print("\n-- LOGIN --")
        usuarioDigitado = input("Digite seu usuário: ")
        senhaDigitada = input ("Digite a sua senha: ")

        if usuarioDigitado not in listaLogins:
            print("Usuário não encontrado!")
        else:
            posicao = listaLogins.index(usuarioDigitado)

            if listaSenhas[posicao]!= senhaDigitada:
                print("Senha incorreta!")
            else:
                print(f"Bem-vindo {usuarioDigitado}! Login realizado com sucesso!")
    
    elif opcao == "3":
        print("Saindo...")
        break
    else:
        print("Opção inválida!")