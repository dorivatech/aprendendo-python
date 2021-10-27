""" DESAFIO 006 »» Operações aritméticas (* && sqrt) """
""" Esse algoritmo recebe um número e apresenta o seu dobro, triplo e raíz quadrada """

print("{:=^25}".format(" DESAFIO 006 "))

number = int(input("Digite um número: "))
print("O dobro de {1} vale {0}".format(number * 2, number))
print("O triplo de {1} vale {0}".format(number * 3, number))
print("A raíz quadrada de {1} é igual a {0:.3f}".format(pow(number, 1/2), number))