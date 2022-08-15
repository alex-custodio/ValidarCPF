cpf = str(input("Digite o seu cpf: "))
somaDigito1, somaDigito2 = 0,0
for valorEnumerado, valor in enumerate(cpf[0:9], -10):
    somaDigito1 += abs(valorEnumerado) * int(valor)
    somaDigito2 += abs(valorEnumerado -1) * int (valor)
operacao1 = 11 - (somaDigito1 % 11)
digito1 = 0 if operacao1 > 9 else operacao1
digito2 = 11 - (somaDigito2 % 11)
novoCpf = cpf[0:9] + str(digito1) + str(digito2)
print('Validado!' if novoCpf == cpf else 'Não validado')