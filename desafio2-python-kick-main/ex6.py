# Faça um programa em que o usuário digita um número inteiro e o programa exibe todos os
# números ímpares do 1 até o valor inserido.

numero = int(input("Digite um número inteiro: "))

i = 1

while i <= numero:
    if i % 2 != 0:
        print(i)
    i += 1