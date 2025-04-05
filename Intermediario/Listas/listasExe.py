"""
Atividades

1. Soma dos Elementos
Crie uma lista com 5 números e calcule a soma de todos os elementos.

2. Maior e Menor Número
Peça ao usuário para inserir 5 números e armazene-os em uma lista. Depois, exiba o maior e o menor número da lista.

3. Contagem de Elementos
Crie uma lista com alguns nomes e peça ao usuário um nome. Verifique quantas vezes esse nome aparece na lista.

4. Removendo Duplicatas
Dada uma lista com números repetidos, crie um código que remova os números duplicados e exiba a lista sem repetições.

5. Invertendo a Lista
Crie um programa que peça ao usuário 5 palavras e armazene em uma lista. Depois, exiba a lista na ordem inversa.

6. Média dos Números
Peça ao usuário para inserir 6 números, armazene em uma lista e exiba a média desses números.

7. Pares e Ímpares
Crie uma lista de números e separe os valores pares dos ímpares em listas diferentes.

8. Mesclando Listas
Dadas duas listas de números, crie uma terceira lista que contenha os elementos intercalados das duas listas.

9. Elementos Únicos
Dada uma lista, exiba apenas os elementos que aparecem uma única vez.

10. Produto dos Elementos
Crie uma lista com 4 números e calcule o produto de todos os elementos da lista.


"""
# Desafio 1  // Lembrando que há outras maneiras de serem aplicadas para resolver a atividade, inclusive uma função interna de Python sum()
lista = [1, 2, 3, 4]
soma = 0
for x in lista:
    soma = soma + x
print(soma)

# Desafio 2
num = ["1º", "2º", "3º", "4º", "5º"]
lista_usuario = [int(input("Digite o {0} números: ".format(num[x]))) for x in range(5)]
lista_usuario.sort()
print(f"Menor número da Lista: {lista_usuario[0]}, Maior Número da Lista: {lista_usuario[-1]}")

# Desafio 3
frutas = ["banana", "manga", "banana", "morango", "jaca"]
escolhe_fruta = input("Escolha um nome de uma fruta: ").lower()
print(frutas.count(escolhe_fruta))

# Desafio 4
numeros_repetidos = [1, 1, 3, 4, 5, 5, 6]
numeros_unicos = []
[numeros_unicos.append(x) for x in numeros_repetidos if x not in numeros_unicos]
print(numeros_unicos)

# # Desafio 5
nomes = ["1º", "2º", "3º", "4º", "5º"]
lista_nomes_usuario = [(input("Digite o {0} nome: ".format(nomes[x]))) for x in range(5)]
lista_nomes_usuario.reverse()
print(lista_nomes_usuario)

# Desafio 6
num = ["1º", "2º", "3º", "4º", "5º"]
lista_numeros_usuario = [int(input("Digite o {0} número: ".format(num[x]))) for x in range(5)]
soma = 0
for x in lista_numeros_usuario:
    soma = soma + x
media = soma/2
print(media)

# Desafio 7
numeros_mistos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = []
impares = []
[pares.append(x) if x%2 ==0 else impares.append(x) for x in numeros_mistos]
print(pares,"\n",impares)

# Desafio 8
lista_1 = [1, 3, 5, 7]
lista_2 = [2, 4, 6, 8]
lista_3 = [x for dupla in zip(lista_1, lista_2) for x in dupla]
print(lista_3)

# Desafio 9
numeros_mistos = [1, 2, 3, 3, 4, 4, 5, 5]
unicos = []
for x in numeros_mistos:
    if numeros_mistos.count(x) == 1:
        unicos.append(x)
print(unicos)

# Desafio 10
lista = [2, 3, 4, 5]
produto = 1
for x in lista:
    produto = produto * x
print(produto)