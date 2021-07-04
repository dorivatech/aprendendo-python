print("{:=^25}".format(" DESAFIO 014 "))
print("{:=^25}".format(" Conversor de Temperatura "), end="\n\n")

celsius = float(input("Digite a temperatura em Celsius: "))
celsius_to_fahrenheit = celsius * 1.8 + 32
celsius_to_kelvin = celsius + 273

print("{:=^20}".format(" Resultados "))
print("{} celsius equivale a: {} fahrenheit e {} kelvin".format(celsius, celsius_to_fahrenheit, celsius_to_kelvin), end="\n\n")

fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
fahrenheit_to_celsius = (fahrenheit - 32) / 1.8
fahrenheit_to_kelvin = (fahrenheit - 32) * 5/9 + 273

print("{:=^20}".format(" Resultados "))
print("{} fahrenheit equivale a: {} celsius e {} kelvin".format(fahrenheit, fahrenheit_to_celsius, fahrenheit_to_kelvin), end="\n\n")

kelvin = float(input("Digite a temperatura em kelvin: "))
kelvin_to_celsius = kelvin - 273
kelvin_to_fahrenheit = kelvin_to_celsius * 1.8 + 32

print("{:=^20}".format(" Resultados "))
print("{} kelvin equivale a: {} celsius e {} fahrenheit".format(kelvin, kelvin_to_celsius, kelvin_to_fahrenheit))