print("{:=^25}".format(" DESAFIO 015 "))
print("{:=^25}".format(" Aluguel de carro "), end="\n\n")

days_rented = int(input("Quantos dias alugados "))
km_traveled = int(input("Quantos KM percorridos "))

print("O total a pagar é KZs {}".format(days_rented * 60 + km_traveled * 0.15))