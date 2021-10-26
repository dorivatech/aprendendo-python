""" DESAFIO 005 »» Antecessor/Sucessor """
""" Esse algoritmo recebe um número e imprime o seu antecessor e sucessor """

print("=" * 6 + " DESAFIO 005 " + "=" * 6)

number = int(input("Digite um número: "))

print("Analisando o valor {}, seu antecessor é {} e o sucessor é {}".format(number, (number - 1), (number + 1)))