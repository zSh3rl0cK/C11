nomeAluno = input('Digite seu nome: ')
mediaAluno = float(input('Digite a media do aluno: '))

alunos = {nomeAluno: mediaAluno}

if mediaAluno >= 50.0:
    alunos['situacaoAluno'] = 'AP'
else:
    alunos['situacaoAluno'] = 'RP'

print(alunos)
