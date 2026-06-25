cadastros= {}

print("===SISTEMA DE LOGIN===")

while True:
    print("\n O que você deseja fazer?")
    print("1 Cadastrar Usuário")
    print("2 Cadastrar Senha")
    print("3 Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1": 
        print("\n--CADASTRO--")
        novoUsuario = input("Digite um nome de Usuário: ")
        novaSenha = input("Digite uma senha: ")

        if novoUsuario in cadastros:
            print("Esse usuário já existe!")
        else:
            cadastros[novoUsuario] = novaSenha
            print("Usuário cadastrado com sucesso!")

    elif opcao == "2":
        print("\n--LOGIN--")
        usuarioDigitado = input("Digite seu usuário: ")
        senhaDigitada = input("Digite sua senha: ")

        if usuarioDigitado not in  cadastros:
            print("Usuário não encontrado!")
        elif cadastros[usuarioDigitado] != senhaDigitada:
            print("Senhaa incorreta!")
        else:
            print(f"Bem-vindo(a) {usuarioDigitado}! Login feito com sucesso!")

    elif opcao =="3":
        print("Saindo...")
        break

    else:
        print("Opção inválida!!")