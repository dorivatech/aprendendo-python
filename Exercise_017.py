from math import hypot

print("{:=^25}".format(" DESAFIO 017 "))
print("{:=^25}".format(" Cálculo da hipotenusa "), end="\n\n")

opposite_leg = float(input("Comprimento do cateto oposto: "))
adjacent_leg = float(input("Comprimento do cateto adjacente: "))

# hypotenuse = ((opposite_leg ** 2) + (adjacent_leg ** 2)) ** (1/2)
hypotenuse = hypot(opposite_leg, adjacent_leg)

print("Com o CO igual a {} e CA {} a hipotenusa equivale a {:.2f}".format(opposite_leg, adjacent_leg, hypotenuse))