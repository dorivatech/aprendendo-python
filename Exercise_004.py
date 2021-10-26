""" DESAFIO 004 »» Características de um valor aleatório """
""" Esse algoritmo recebe um valor qualquer digitado pelo usuário e depois verifica um monte de características deste """

print("====== DESAFIO 004 ======")

something = input("Escreva alguma coisa ")

print("\nNúmeros")
print("IsNumeric", something.isnumeric())
print("IsDecimal", something.isdecimal())

print("\nStrings")
print("IsAlpha", something.isalpha())
print("IsAlphaNumeric", something.isalnum())
print("IsUpper", something.isupper())
print("IsLower", something.islower())
print("IsSpace", something.isspace())

print("\nOutros")
print("IsTitle", something.istitle())
print("IsAscii", something.isascii())
print("IsDigit", something.isdigit())
print("IsIdentifier", something.isidentifier())
print("IsPrintable", something.isprintable())
