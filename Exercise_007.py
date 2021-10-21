print("{:=^25}".format(" DESAFIO 007 "))
print("{:=^25}".format(" Média do aluno "))

count = 0

while(True):
	if count >= 1:
		print("Por favor use notas no intervalo 0 - 20")

	number1 = float(input("Primeira nota do aluno: "))
	number2 = float(input("Segunda nota do aluno: "))

	if 0 <= number1 <= 20 and 0 <= number2 <= 20:
		break
	
	count += 1


print("A média entre {} e {} é igual a {:.1f}".format(number1, number2, ((number1 + number2)/2)))