# Coleta numero de notas
n = int(input('Digite o número de notas:'))
# Guarda a soma de todas as notas
montante = 0
for i in range(n):
    nota = float(input('digite a nota:'))
    montante = montante + nota

print('Media das notas é:',montante/n)

