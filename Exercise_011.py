print("{:=^25}".format(" DESAFIO 011 "))
print("{:=^25}".format(" Pintando Parede "), end="\n\n")

width = float(input("Largura da parede: "))
height = float(input("Altura da parede: "))
area = width * height

print("Sua parede tem a dimensão de {}X{} e sua área é de {}m².".format(width, height, area))

# Supondo que cada 2m^2 de parede precise de 1l de tinta para ser pintado
print("Para pintar essa parede, você precisará de {}l de tinta.".format((area / 2)))