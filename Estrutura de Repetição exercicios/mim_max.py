# Numero de entradas
n = int(input('Numero de entradas:'))
maior, menor, montante = 0, 0, 0

for i in range(n):
    numero = int(input('Digite o numero:'))
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
    montante += numero

print(f"Maior: {maior}\n Menor: {menor}\n Soma:{montante}")
