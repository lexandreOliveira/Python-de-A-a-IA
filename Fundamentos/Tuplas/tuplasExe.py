"""

1. Criando uma Tupla a Partir do Input
Solicite ao usuário que insira uma sequência de números separados por espaço e armazene-os em uma tupla.

2. Acessando Elementos da Tupla
Dada uma tupla com vários valores, peça ao usuário um índice e exiba o elemento correspondente.

3. Soma e Média dos Elementos
Crie uma tupla com números inteiros e calcule a soma e a média dos valores.

4. Encontrando o Maior e o Menor Valor
Dada uma tupla numérica, determine o maior e o menor valor contido nela.

5. Verificando a Ocorrência de um Número
Crie uma tupla com valores repetidos e peça ao usuário um número. Informe quantas vezes esse número aparece na tupla.

6. Concatenando Tuplas
Dadas duas tuplas diferentes, una ambas em uma única tupla e exiba o resultado.

7. Invertendo os Elementos da Tupla
Crie uma tupla e gere uma nova tupla com seus elementos na ordem inversa.

8. Encontrando o Índice de um Elemento
Dada uma tupla com nomes, solicite um nome ao usuário e exiba o índice onde ele se encontra na tupla.

9. Removendo Duplicatas de uma Tupla
Dada uma tupla com valores repetidos, crie uma nova tupla contendo apenas elementos únicos.

10. Convertendo uma Tupla em String
Dada uma tupla contendo caracteres, transforme-a em uma única string.

"""

# Desafio 1
dados_usuario = tuple(input("Digite 3 números separados por espaços: "))
print(dados_usuario)

# Desafio 2
dados_id = (73, 14, 92, 36, 58, 27, 81, 45, 19, 63)
busca_elemento = int(input("Digite um índice para descobri qual número é: "))
dados_id = dados_id[busca_elemento]
print(dados_id)

# Desafio 3
notas = (73, 14, 92, 36, 58, 27, 81, 45, 19, 63)
#soma = sum(notas)
soma = 0
for x in notas:
    soma = soma + x
media = soma/len(notas)
print(f"Soma dos números: {soma} Média dos números: {media}")

# Desafio 4
idades = (73, 14, 92, 36, 58, 27, 81, 45, 19, 63)
print(f"Menor número: {min(idades)}, Maior Número: {max(idades)}")

# Desafio 5
repeticoes = (73, 14, 92, 36, 58, 19, 27, 81, 19, 45, 19, 63, 63)
contagem = int(input("Digite um número: "))
print(f"Quantidade de x que aparece o número {contagem} é: {repeticoes.count(contagem)} vezes!")

# Desafio 6
tupla_1, tupla_2 = (73, 14, 92, 36, 58, 19), (27, 81, 19, 45, 19, 63, 63)
tupla_3 = tupla_1 + tupla_2
print(tupla_3)

# Desafio 7
tupla_1 = (73, 14, 92, 36, 58, 19)
tupla_inversa = tupla_1[::-1]
print(tupla_inversa)

# Desafio 8
nomes = ("Ana", "Bruno", "Carlos", "Daniela", "Eduardo", "Fernanda", "Gabriel", "Helena", "Igor", "Juliana")
procurar = input("Digite um nome para saber a posição dele na tupla: ").capitalize()
print(nomes.index(procurar))

# Desafio 9
tupla = (1, 2, 2, 3, 4, 4, 5, 5, 6)
unicos = []

for elemento in tupla:
    if elemento not in unicos:
        unicos.append(elemento)

tupla_sem_duplicatas = tuple(unicos)
print(tupla_sem_duplicatas)

# Desafio 10
tupla = ('P', 'y', 't', 'h', 'o', 'n')
resultado = ''.join(tupla)
print(resultado)
