# Primeira aula CALCULO DO IMC DE UMA PESSOA


## Introdução

O IMC de uma pessoa indica seu indice massa corpórea e é dado pela formula

IMC = PESO / ALTURA²

## Criação do código

### Comentários em python

A principal maneira de adicionar comentarios em python é com o simbolo '#', esse comentários vão ser ignorados pelo PYTHON e servem apenas para
ajudar ao programador a entender melhor o dódigo escrito, po exeplo:

```
# Isso é um comentários
```

### Sinal de IGUAL em python

Em python, o sinal de igual representa uma atribuição, dessa forma posso criar uma variável e atribuir um valor a ela utilizando esse operador, para o nosso exemplo, precisamos criar as variáveis peso e altura. Posso fazer:

```
peso_kg = 70 # Peso da pessoa em kg
altura_cm = 173 # Altura da pessoa em cm 
```

Perceba que é uma boa prática utilizar nomes significativos as variáveis. Utilizei, por exemplo, 'peso_kg' ná variável que representa o peso da pessoa, dessa forma fica fácil entender que essa variável deve conter o peso da pessoa em kg a qualquer momento que precis utilizar ela no código.

O código ficaria bem mais difícil de entender caso use nomes não significativos:

```
p = 70
a = 173
```

### Operações aritméticas em python

Podemos usar os operadores aritméticos em python:

+ adição
- subtração
* multiplicação
/ divisão
% resto da divisão
** exponenciação

Continuando nosso exemplo, vamos calcular, por exemplo, a altura ao quadrado, para facilitar o nosso calculo do IMC

```
quadrado_altura_m = altura_m*altura_m
```

O calculo foi feito, nesse caso, multiplicando a altura por ela mesmo, mas poderia ser feito utilizando o operador de exponenciação ('**') para elevar a altura a 2. Fica como uma atividade modificar o código para utilizar esse operador.

Tendo tudo que precisamos, podemos calcular o IMC:

```
imc = peso_kg / quadrado_altura_m 
```

### A função print

Para escrever na tela, o python possui uma função chamada print, que recebe como argumento valores ou variáveis que serão escritas na tela. Para escrever o imc na tela, fazemos então:

```
print(imc)
```

### Sugestão de exercícios

Fica como sugestão de exercício:

- Modificar valores de Peso e altura para calcular o IMC de pessoas da sua família

### Desafio

Criar um código em python para calcular a área de um retângulo. As variáveis de entrada devem ser os comprimetos do lado menor e do lado menor e, ao final, o valor da área deve ser escrita na tela. Não esqueça de escolher bem os nomes das variáveis.