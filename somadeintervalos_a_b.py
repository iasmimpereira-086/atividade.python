a = int(input("Digite o valor de a: "))
b= int(input("Digite o valor de b: "))

while a >= b:
    print(f"Erro:'a'({a}) não é menor que 'b' ({b}). Tente novamente!")
    a = int(input("Digite o valor de a: "))
    b = int(input("Digite o valor de b: "))

soma = 0
i = a
while i <= b:
    soma += i
    i += 1
print(f"A soma dos inteiros no intervalo [{a}, {b}] é: {soma}")