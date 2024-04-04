# Solicita uma entrada do usuario 
n = int(input("Digite um número para calcular o n-esimo termo da sequência de Fibonacci: "))
# define os dois primeiros termoa da sequência
a1, a2 = 1, 1
# Realizando tratamento para o caso de n=1 ou n=2
if n == 1 or n == 2:
    print('O n=esimo termo da sequência de Fibonacci é:', a1)
else:
    for i in range (3, n+1):
        a3 = a1 + a2
        a1 = a2
        a2 = a3
    print('O n=esimo termo da sequência de Fibonacci é:', a3)