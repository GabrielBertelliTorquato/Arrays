'''1) Inicializar um vetor de inteiros com números de 0 a 99.'''

lista = list(range(100))
print (lista)

"""2) Escreva um algoritmo que leia um conjunto de 10 notas, armazene-as em uma variável
composta chamada NOTA e calcule e imprima a sua média.
"""

notas = [0,0,0,0,0,0,0,0,0,0]
soma = 0.0
for i in range(10):
  notas[i] = float(input(f'Entre com a nota[{i}]: '))
  soma = soma + notas[i]

media = soma / 10.0
for i in range(len(notas)):
  print(f'Nota[{i}] = {notas[i]:.2f} - media = {media:.2f}')

"""3) Repita o algoritmo acima, porém imprima quantos valores estão acima da média."""

notas = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
soma = 0.0

for i in range(10):
  notas[i] = float(input(f'Entre com a nota[{i}]: '))
  soma = soma + notas[i]

media = soma / 10.0
contador_acima_media = 0

for i in range(len(notas)):
  print(f'Nota[{i}] = {notas[i]:.2f} - média = {media:.2f}')
  if notas[i] > media:
    contador_acima_media += 1

print(f'Quantidade de valores acima da média: {contador_acima_media}')

"""4) Faça um algoritmo que leia um vetor que contém as notas de 30 alunos. Imprima o maior
valor, o menor valor, a média da turma e a quantidade de notas abaixo da média.
"""

notas = []

for i in range(30):
    nota = float(input(f'Entre com a nota do aluno {i+1}: '))
    notas.append(nota)

maior = max(notas)

menor = min(notas)

media = sum(notas) / len(notas)

contador_abaixo_media = 0
for nota in notas:
    if nota < media:
        contador_abaixo_media += 1

print(f'Maior valor: {maior}')
print(f'Menor valor: {menor}')
print(f'Média da turma: {media:.2f}')
print(f'Quantidade de notas abaixo da média: {contador_abaixo_media}')

"""5) Ler um vetor de 100 elementos numéricos e verificar se existem elementos iguais a 30. Se
existirem, escrever as posições em que estão armazenados.
"""

vetor = []

for i in range(100):
  vetores = float(input(f'Entre com um vetor {i+1}: '))
  vetor.append(vetores)

contador_trinta = 0
for vetores in range(len(vetor)):
  if vetor[vetores] == 30:
    print(vetores)

"""6) Fazer um algoritmo que calcule e escreva o somatório dos valores armazenados numa variável
composta unidimensional (vetor) A, de 100 elementos numéricos a serem lidos do dispositivo
de entrada.
"""

vetor_a = []
soma = 0.0
for i in range(100):
  vetor_a = float(input(f'Entre com o número: '))
  soma = soma + vetor_a

print(f'A soma dos valores armazenados no vetor é: {soma}')

"""7) Escreva um algoritmo que leia um vetor de 200 valores numéricos reais e os imprima na
ordem contrária em que foi lida.
"""

vetor = []

for i in range(200):
  vetor.append (float(input(f'Digite um número {i+1}: ')))


vetor.reverse()
print (vetor)

"""8) Escreva um algoritmo para fazer a soma de dois vetores de 10 elementos reais lidos do
teclado. O primeiro elemento do primeiro vetor deverá ser adicionado ao primeiro elemento do
segundo vetor e, o resultado deverá ser acumulado em um terceiro vetor também de 10
elementos. Imprimir os três vetores conforme layout de impressão abaixo:

VETOR 1: __ __ __ __ __ __ __ __ __ __

VETOR 2: __ __ __ __ __ __ __ __ __ __

VETOR 3: __ __ __ __ __ __ __ __ __ __
"""

vetor = []
vetor2 = []
vetor3 = []
resultado = []

for i in range(10):
    vetor.append(int(input(f"Digite o valor{i+1} do primeiro vetor: ")))
for i in range(10):
    vetor2.append(int(input(f"Digite o valor{i+1} do segundo vetor: ")))


for i in range(len(vetor)):
    soma = vetor[i] + vetor2[i]
    vetor3.append(soma)

print("vetor: ")
for i in range(10):
    print(f"{vetor[i]}")

print("vetor2:")
for i in range(10):
    print(f"{vetor2[i]}")

print("vetor3")
for i in range(10):
    print(f"{vetor3[i]}")

"""9) Fazer um algoritmo que:
a) Leia duas variáveis compostas unidimensionais, contendo, cada uma, 25 elementos numéricos;
b) intercale os elementos desses dois conjuntos formando uma nova variável composta
unidimensional de 50 elementos;
c) Escreva o resultado obtido.
"""

vetor = []
vetor2 = []

for i in range(10):
    vetor.append(int(input(f'Digite o valor{i+1} do primeiro vetor: ')))

for i in range(10):
    vetor2.append(int(input(f'Digite o valor{i+1} do segundo vetor: ')))

variavel = []

for vetor, vetor2 in zip(vetor , vetor2):
    variavel.append(vetor)
    variavel.append(vetor2)

print(variavel)

"""10)"""

a = []


for i in range(5):
    a.append(float(input(f'Digite o valor {i+1} do vetor: ')))

s = 0
contador = 0
for i in range(5):
    termo = i/a[i]
    s += termo
    if i < a[i]:
        contador += 1


print("O valor de S é:", s)
print("O número de termos com numerador menor do que o denominador é:", contador)

"""11) Faça um algoritmo que leia um conjunto de 10 elementos reais e os coloque em um vetor.
Construa um segundo vetor formado da seguinte maneira:
• Os elementos de ordem par são os correspondentes do primeiro vetor multiplicados por 3.
• Os elementos de ordem ímpar são os correspondentes do primeiro vetor divididos por 2.
• Imprima os dois vetores.
"""

vetor = []
vetor2 = []

for i in range(10):
    vetor.append(float(input(f'Digite o {i+1}o valor: ')))

for i in range(10):
    if i % 2 == 00:
        vetor2.append(vetor[i] * 3)
    else:
        vetor2.append(vetor[i] / 2)

print('Primeiro vetor', vetor)
print('Segundo vetor', vetor2)

"""12)"""

A = []
for i in range(20):
    elemento = int(input("Digite o elemento {}: ".format(i)))
    A.append(elemento)

S = 0
for i in range(10):
    diferenca = A[i] - A[19 - i]
    S += diferenca ** 2

print("O valor de S é:", S)

"""13) Escreva um algoritmo que:
a) leia uma frase de 50 caracteres;
b) conte quantos brancos existem na frase;
c) conte quantas vezes a letra “A” aparece;
d) imprima o que foi calculado nos itens b e c.
"""

frase = input("Digite uma frase de 50 caracteres: ")

contador_brancos = 0
for caractere in frase:
    if caractere == ' ':
        contador_brancos += 1

contador_A = 0
for caractere in frase:
    if caractere == 'A' or caractere == 'a': 
        contador_A += 1

print("Quantidade de espaços em branco na frase:", contador_brancos)
print("Quantidade de vezes que a letra 'A' aparece na frase:", contador_A)

"""14)"""

preco = [10, 80, 32, 31, 3]
armazem = [300, 30, 400, 54, 59]

faturamento = 0
for i in range(5):
    faturamento += armazem[i] * preco[i]


print("O faturamento mensal do armazém é:", faturamento, "R$")

"""15) Classificar um vetor numérico VET de 20 elementos em ordem crescente."""

Vet = []

for i in range(20):
    Vet.append(float(input(f'Digite o valor {i+1} do vetor: ')))

vetor = sorted(Vet)

print(vetor)

"""16) Dado um vetor de 128 elementos, verificar se existe um elemento igual a K (chave) no vetor.
Se existir, imprimir a posição onde foi encontrada a chave; se não; imprimir a mensagem:
“CHAVE K NÃO ENCONTRADA”. O vetor A e a chave K são lidos a partir de uma unidade de
entrada.
"""

vetor = []

for i in range (5):
    vetor.append(float(input('Digite o elemento do vetor: ')))

chave = int(input('Digite a chave: '))

encontrada = False
posicao = -1
for i in range(5):
    if vetor[i] == chave:
        encontrada = True
        posicao = i
        break

if encontrada:
    print("A chave", chave, "foi encontrada na posição", posicao)
else:
    print("CHAVE", chave, "NÃO ENCONTRADA")

"""17) Refaça o algoritmo acima otimizando-o usando uma técnica conhecida por Pesquisa Binária.
Suponha primeiramente que o vetor já esteja ordenado. Procuramos então o elemento K
dividindo o vetor em duas partes e testando em qual das duas partes ele deveria estar.
Procede-se então, da mesma forma para a parte provável, e assim sucessivamente.
Obs.: na pesquisa sequencial simples (problema 16), o número médio de comparações que
devem ser feitas até encontrar a chave é N/2, onde N é o número de elementos do vetor. No
nosso caso, no algoritmo 16, teríamos, em média, 128/2 = 64 comparações. Na pesquisa
binária, o número máximo de comparações é log2N. Teríamos, então, log2128=7 comparações,
no máximo.
"""

vetor = []
for _ in range(5):
    elemento = int(input("Digite um elemento do vetor: "))
    vetor.append(elemento)

chave = int(input("Digite a chave: "))

encontrada = False
inicio = 0
fim = 4

while inicio <= fim:
    meio = (inicio + fim) // 2  

    if vetor[meio] == chave:
        encontrada = True
        posicao = meio
        break
    elif vetor[meio] < chave:
        inicio = meio + 1
    else:
        fim = meio - 1

if encontrada:
    print("A chave", chave, "foi encontrada na posição", posicao)
else:
    print("CHAVE", chave, "NÃO ENCONTRADA")