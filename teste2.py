for i in range(1, 6):
	print("*" * i)



nome = input("Digite seu nome: ")

print('*********')
print(f'*{nome}*')
print('*********')
 

def calcular_soma():
    try:
        
        entrada = input("Digite um número inteiro positivo (n): ")
        n = int(entrada)

        if n < 1:
            print("Por favor, digite um número maior ou igual a 1.")
            return

       
        soma = 0
        for i in range(1, n + 1):
            soma += i

      
        print(f"A soma de 1 até {n} é: {soma}")

    except ValueError:
        print("Erro: Você precisa digitar um número válido!")


if __name__ == "__main__":
    calcular_soma()