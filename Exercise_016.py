""" DESAFIO 016 »» Porção inteira """
""" Este algoritmo recebe um número e depois apresenta a sua parte inteira """

from math import trunc

print("{:=^25}".format(" DESAFIO 016 "))
print("{:=^25}".format(" Porção inteira "), end="\n\n")

number = float(input("Digite um valor numérico "))

print("O valor digitado foi {} e a sua porção inteira é {}".format(number, trunc(number)))