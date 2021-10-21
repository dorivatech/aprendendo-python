import math

print("{:=^25}".format(" DESAFIO 016 "))
print("{:=^25}".format(" Porção inteira "), end="\n\n")

number = float(input("Digite um valor numérico "))

print("O valor digitado foi {} e a sua porção inteira é {:.0f}".format(number, math.trunc(number)))