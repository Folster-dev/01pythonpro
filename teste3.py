import random

numero = random.randint(1, 100)

for i in range(5): 
    
    per = int(input("acerte um numero de 1 a 100 (voce terá 5 tentativas): "))

    if per == numero:
        print("Parabéns! Você acertou o número.")
    elif per < numero:
        print("O número é maior do que o que você escolheu.")
    elif per > numero:
        print("O número é menor do que o que você escolheu.")
    elif per < 1 or per > 100:
        print("Por favor, escolha um número entre 1 e 100.")
