import random

caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

ncar = int(input("insira o numero de caracteres da senha: "))
senha = ""
for i in range(ncar):
    senha += random.choice(caracteres)
print("Senha gerada:", senha)

