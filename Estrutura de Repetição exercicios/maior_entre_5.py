#Guarda o maior numero
Maior = 0
for i in range(5):
    x = float(input('Digite um numero: '))
    if x > Maior:
        Maior = x 
print('O maior numero é:', Maior)