""" DESAFIO 020 »» Lista aleatória """
""" Este algoritmo pede ao usuário para digitar quantos nomes ele vai adicionar, recebe o número de nomes correspondente e depois retorna uma lista destes nomes aleatória """

import random

count = 1
names = []
repeat = int(input("Digite quantos nomes você deseja receber: "))

while(count <= repeat):
	name = input("Digite o {}º nome: ".format(count if (count > 9) else "0" + str(count)))
	names.append(name)

	count += 1

random.shuffle(names)
print("A lista de nomes aleatória é: ")
print(names)