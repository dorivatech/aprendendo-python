print("{:=^25}".format(" DESAFIO 013 "))
print("{:=^25}".format(" Reajuste Salarial "), end="\n\n")

wage = float(input("Qual é o salário do funcionário? KZs "))
increase = float(input("Quanto de aumento o funcionário vai receber? % "))

wage_with_increase = wage + ((wage * increase) / 100)

print("Um funcionário que ganhava KZs {:.2f}, com {}% de aumento, passa a receber KZs {:.2f}".format(wage, increase, wage_with_increase))