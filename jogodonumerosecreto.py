import random

numero_secreto = random.randint(1,10)
chances = 3
tentativas = 0

print("Adivinhe o número entre 1 e 10!")
print(f"Você tem {chances} chances.")
print("-" * 30)

while tentativas < chances:
    chute = int(input("Digite um número: "))
    tentativas = tentativas + 1

    if chute == numero_secreto:
        print("Parabéns, você acertouu!!")
        break
    elif tentativas == chances:
        print("Você errou!")
        print(f"Você perdeu! Fim de jogo. O número era {numero_secreto}.")
    elif chute > numero_secreto:
        print("Você errou!")
        print("Tente um número menor")
        print(f"Tentatiavs restantes:{chances - tentativas}")
    else:
        print("você errou!")
        print("Tente um número maior")
        print(f"Tentativas restantes: {chances - tentativas}")