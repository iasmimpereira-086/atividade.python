while True:
    numero = int(input("Digite um número inteiro positivo ou (0 para sair): "))

    if numero == 0:
        print("Encerrando o programa.")
        break

    resultado = 1 
    i = 1

    while i <= numero:
        resultado = resultado * i
        i = i + 1

    print(f"O fatorial de {numero} é {resultado}")