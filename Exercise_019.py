""" DESAFIO 019 »» Nomes aleatórios """
""" Este algoritmo pede ao usuário para digitar quantos nomes ele vai adicionar, recebe o número de nomes correspondente e depois retorna um nome aleatório """

import random

count = 1
names = []
repeat = int(input("Digite quantos nomes você deseja receber: "))

while(count <= repeat):
	name = input("Digite um nome: ")
	names.append(name)

	count += 1

print("O nome sorteado foi {}".format(random.choice(names)))