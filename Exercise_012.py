print("{:=^25}".format(" DESAFIO 012 "))
print("{:=^25}".format(" Cálculo de desconto "), end="\n\n")

price = float(input("Qual é o preço do produto? KZs "))
discount = float(input("Quanto de desconto tem o produto? % "))

price_with_discount = price - ((price * discount) / 100)

print("O produto que custava KZs {:.2f}, na promoção com desconto de {}% agora custa KZs {:.2f}".format(price, discount, price_with_discount))