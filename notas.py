

nomealunos = []
notalunos = []
mai = 0
men = 0

cont_alunos = int(input('Quantos alunos são: '))


for _ in range(cont_alunos):
    nomealunos.append(str(input('Nome do aluno: ')))
    notalunos.append(float(input('Nota: ')))

nota_maxima = 0
nota_minima = 10
media = 0
aprovados = 0
nota_aprovacao = 5

for nota in notalunos:
    if nota > nota_maxima:
        nota_maxima = nota
    if nota < nota_minima:
        nota_minima = nota
    media = media + nota/cont_alunos
    if nota >= nota_aprovacao:
        aprovados +=1
print(nota_maxima,nota_minima, media, aprovados)