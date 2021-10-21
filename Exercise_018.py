from math import sin, cos, tan, radians

print("{:=^30}".format(" DESAFIO 018 "))
print("{:=^30}".format(" Razões trigonométricas "), end="\n\n")

angle = float(input("Digite o ângulo que você deseja: "))

print("A ângulo de {} tem o Seno de {:.3}".format(angle, sin(radians(angle))))
print("A ângulo de {} tem o Cosseno de {:.3}".format(angle, cos(radians(angle))))
print("A ângulo de {} tem o Tangente de {:.3}".format(angle, tan(radians(angle))))