# coleta numero de turmas
n = int(input("digite o numero de turmas: "))
num_alunos_total = 0
i = 0
while i < n:
    # Monte de alunos
    num_alunos_turma = int(input('Numeros de alunos da turma: '))
    num_alunos_total +=  num_alunos_turma
    i+=1
print('media de aluno:',num_alunos_total/n)