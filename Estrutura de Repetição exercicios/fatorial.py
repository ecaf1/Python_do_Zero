# Coleta o numero 
n = int(input(' Qual numero vc deseja calcular o fatorial:'))

# Inicia um contador 
x=1
for i in range(2, n+1):
    x *= i
print('O fatorial de ', n,'é',x )