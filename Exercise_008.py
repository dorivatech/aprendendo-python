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