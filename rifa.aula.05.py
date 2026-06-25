import random

participantes = []

print("===SORTEIO DE RIFA===")
print("Digite o nome dos participantes:  \n")

while True:
    nome = input("Nome: ")
    if nome == "":
        break
    participantes.append(nome)

ganhador = random.choice(participantes)
print(f"O ganhador é: {ganhador} ")