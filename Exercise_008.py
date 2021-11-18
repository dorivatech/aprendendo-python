""" DESAFIO 008 »» Conversor de unidades (cumprimento) """
""" Este algoritmo recebe um valor em metros e converte para outras unidades de cumprimento, como: km, hm, dam e outras """

print("{:=^25}".format(" DESAFIO 008 "))
print("{:=^25}".format(" Conversor de unidades "))

number = float(input("Digite um valor em metros: "))

print("O valor {} m vale: ".format(number))
print("{:.2f} km".format((number / 1000)))
print("{:.2f} hm".format((number / 100)))
print("{:.2f} dam".format((number / 10)))
print("{:.2f} dm".format((number * 10)))
print("{:.2f} cm".format((number * 100)))
print("{:.2f} mm".format((number * 1000)))