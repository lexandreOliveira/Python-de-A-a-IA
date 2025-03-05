# 🚀 Atividades de Manipulação de Strings em Python

# Cada atividade vem com uma descrição e um espaço para implementar a solução.

"""
📝 1. Capitalização e Formatação

Crie um programa que solicite ao usuário seu nome completo e o exiba de diferentes formas:

    Todo em maiúsculas
    Todo em minúsculas
    Apenas a primeira letra de cada palavra em maiúscula

"""
nome = input("Digite seu nome completo: ")
# Implemente as formatações aqui
print(nome.upper())
print(nome.lower())
print(nome.title())

"""
🔍 2. Contagem de Caracteres

Solicite ao usuário uma frase e pergunte qual caractere ele deseja contar. 
Exiba quantas vezes esse caractere aparece na frase.

"""
frase = input("Digite uma frase: ")
caractere = input("Qual caractere deseja contar? ")
# Implemente a contagem aqui
print(frase.count(caractere))


"""
✂ 3. Extração de Dados

Dado um e-mail no formato usuario@dominio.com, extraia e exiba separadamente:

    O nome do usuário
    O domínio do e-mail

"""
email = input("Digite seu e-mail: ")
# Extraia e exiba as partes do e-mail
nomeEmail = email.split("@")
print(nomeEmail[0]+"\n"+nomeEmail[1])

"""
🔄 4. Substituição de Palavras

Peça uma frase ao usuário e substitua todas as ocorrências de uma palavra específica por outra.

"""
frase = input("Digite uma frase: ")
palavra_antiga = input("Palavra a ser substituída: ")
palavra_nova = input("Nova palavra: ")
# Substitua e exiba a nova frase
if palavra_antiga in frase:
    frase = frase.replace(palavra_antiga, palavra_nova)
    print(frase)



"""
🎭 5. Verificação de Palíndromo

Crie um programa que verifica se uma palavra digitada pelo usuário é um palíndromo (ou seja, 
pode ser lida da mesma forma de trás para frente).

"""
palavra = input("Digite uma palavra: ").strip().lower()
# Verifique se é um palíndromo
if palavra == palavra[::-1]:
    print("É um palíndromo!")  
else:  
    print(palavra[::-1])
    print("Não é um palíndromo!") 

 
"""
🔢 6. Extração de Números

Dada uma string contendo um texto misturado com números, extraia apenas os números e exiba-os.
"""
texto = input("Digite um texto com números misturados: ").strip()

# Filtra apenas os caracteres numéricos e junta em uma string
numeros = "".join([char for char in texto if char.isdigit()])

# Exibe o resultado
if numeros:
    print(f"Números extraídos: {numeros}")
else:
    print("Nenhum número encontrado no texto.")




"""
📜 7. Verificação de Caracteres

Peça ao usuário para digitar um texto e verifique:

    Se contém apenas letras (isalpha())
    Se contém apenas números (isdigit())
    Se contém apenas espaços (isspace())

"""
texto = input("Digite um texto: ")
# Faça as verificações
if texto.isalpha():
    print("O texto possui apenas letras")
elif texto.isdigit():
    print("O texto contém apenas números")
elif texto.isspace():
    print("O texto possui apenas espaços")
else: 
    print("Nenhuma das opções")
"""


🏷️ 8. Gerador de Hashtag

Peça ao usuário uma frase e transforme-a em uma hashtag no estilo das redes sociais 
(sem espaços e com cada palavra capitalizada).

"""
frase = input("Digite uma frase: ").title()
frase = input("Digite uma frase: ").title()
hashtag = "#"+frase.replace(" ", "")
print(hashtag)




"""
📆 9. Formatação de Datas

Dado uma string no formato "dd/mm/aaaa", converta para o formato "aaaa-mm-dd".

"""

data = input("Digite uma data (dd/mm/aaaa): ").strip()

dia, mes, ano = data.split("/")
print(f"{ano}-{mes}-{dia}")


"""
🔀 10. Embaralhador de Palavras

Peça ao usuário uma palavra e embaralhe aleatoriamente suas letras.

"""
import random

palavra = input("Digite uma palavra: ")
letras = [x for x in palavra]
random.shuffle(letras)
palavra_nova = ''.join(letras)
print(palavra_nova)

"""
1️1 Contagem de Caracteres

🔹 Peça ao usuário para digitar um texto e conte quantos caracteres ele tem, ignorando espaços.

✅ Exemplo:
Entrada: "Python é incrível!"
Saída: 16 caracteres (sem espaços)
"""
texto = input("Digite um texto: ")
qnd = len(texto.replace(" ", ""))
print(qnd)

"""
12 Primeira e Última Letra

🔹 Peça uma palavra e exiba apenas a primeira e a última letra.

✅ Exemplo:
Entrada: "computador"
Saída: "c r"
"""
palavra = input("Digite uma palavra: ")
print(palavra[0], palavra[-1])  

"""
13 Texto em Caixa Alternada

🔹 Transforme um texto digitado pelo usuário em um formato alternado entre maiúsculas e minúsculas.

✅ Exemplo:
Entrada: "python"
Saída: "PyThOn"

"""
texto = input("Digite um texto: ")
texto_mod = ''.join(y.upper() if x%2==0 else y.lower() for x, y in enumerate(texto))
print(texto_mod)

"""
14 Últimas Três Letras

🔹 Peça ao usuário para digitar uma palavra e exiba somente os últimos três caracteres.

✅ Exemplo:
Entrada: "programação"
Saída: "ção"

"""
palavra = input("Digite uma palavra: ")
print(palavra[-3:])

"""


15️ Texto Espelhado

🔹 Peça uma frase e inverta toda a ordem dos caracteres.

✅ Exemplo:
Entrada: "Python é legal"
Saída: "lageL é nohtyP"

"""
texto = input("Digite um texto: ")
print(texto[::-1])


"""
16 Substituição de Vogais

🔹 Substitua todas as vogais de uma palavra por "*".

✅ Exemplo:
Entrada: "código"
Saída: "c*d*g*"

"""
palavra = input("Digite uma palavra: ")
vogais = "aeiouAEIOU"  
text_cod = ''.join("*" if x in vogais else x for x in palavra)
print(text_cod)


"""
17 Repetição de Texto

🔹 Peça uma palavra ao usuário e exiba ela repetida três vezes, separada por hífen -.

✅ Exemplo:
Entrada: "Python"
Saída: "Python-Python-Python"

"""
resultado = "-".join([palavra] * 3)

print(resultado)


"""
18 Contador de Vogais

🔹 Peça ao usuário para digitar uma frase e conte quantas vogais existem nela.

✅ Exemplo:
Entrada: "Aprendendo Python"
Saída: "6 vogais"

"""
texto = input("Digite um texto: ").lower()

vogais = "aeiou"

contagem = sum(1 for x in texto if x in vogais)
print(f"{contagem} vogais")


"""
19 Removendo Caracteres

🔹 Peça uma palavra e remova todas as ocorrências da letra "a".

✅ Exemplo:
Entrada: "banana"
Saída: "bnn"


"""
texto = input("Digite um texto: ").lower()
print(texto.replace("a", ""))