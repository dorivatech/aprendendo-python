print("{:=^25}".format(" DESAFIO 009 "))
print("{:=^25}".format(" Conversor de moedas "), end="\n\n")

amount = float(input("Quanto você tem em carteira? KZs "))

print("{:*^20}".format(" Resultados "))
print("KZ {} equivale a $ {:.2f}".format(amount, (amount / 648)))
print("KZ {} equivale a € {:.2f}".format(amount, (amount / 773.46)))
print("KZ {} equivale a R$ {:.2f}".format(amount, (amount / 131.32)))