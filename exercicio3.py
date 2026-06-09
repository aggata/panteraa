# Escrever um programa que o usuário digita um número de 0 a 20 
# O programa deverá fazer uma contagem regressiva
# Não permitir que o usuário digita número maior que 20 ou menor que 1 
# Imprimir uma mensagem de "Acabou" no final
# Não permitir digitar letras

while True:
    try:
        numero = int(input("Digite um número de 1 a 20: "))
      
        if 1 <= numero <= 20:
            break
        else:
            print("Erro: O número deve estar entre 1 e 20.")
            
    except ValueError:
        print("Erro: Entrada inválida. Digite apenas números inteiros.")
for i in range(numero, -1, -1):
    print(i)

print("Acabou a contagem!")

