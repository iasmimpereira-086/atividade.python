primeiro_termos = int(input("Digite o primeiro termo (a1): "))
quantidade_termos = int(input("Digite a quantidade de termos: "))
razao = int(input("Digite a razão (r): "))

print("Progressão Aritmética: ")

termo = primeiro_termos
contador = 1

while contador <= quantidade_termos:
    print(termo)
    termo = termo + razao
    contador = contador + 1