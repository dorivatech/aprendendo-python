print("{:=^25}".format(" DESAFIO 007 "))
print("{:=^25}".format(" Média do aluno "))

number1 = float(input("Primeira nota do aluno: "))
number2 = float(input("Segunda nota do aluno: "))

print("A média entre {} e {} é igual a {:.1f}".format(number1, number2, ((number1 + number2)/2)))