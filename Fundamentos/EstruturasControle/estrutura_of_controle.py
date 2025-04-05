# Atividades sobre Estruturas de Controle


"""1. Par ou Ímpar

Escreva um programa que leia um número inteiro e diga se ele é par ou ímpar."""


"""2. Maior de Dois Números

Peça dois números ao usuário e exiba qual é o maior deles. Se forem iguais, mostre uma mensagem informando isso."""


"""3. Calculadora Simples com Condicional

Peça dois números e uma operação (+, -, *, /). Use if, elif, else para realizar a operação e mostrar o resultado."""


"""4. Verificador de Idade

Peça a idade do usuário e diga em qual faixa ele se encontra:

    0 a 12 anos → Criança

    13 a 17 anos → Adolescente

    18 a 59 anos → Adulto

    60+ anos → Idoso """



"""5. Contagem com while

Escreva um programa que conte de 1 até 10 usando um while."""


"""6. Tabuada com for

Peça um número ao usuário e mostre a tabuada dele (de 1 a 10) usando for."""


"""7. Soma de Números Pares

Peça ao usuário um número inteiro positivo e use um for para somar todos os números pares de 1 até esse número."""


"""8. Contador de Vogais

Peça uma palavra ao usuário e conte quantas vogais ela possui. Use um for e if."""


"""9. Login Simples com Tentativas

Implemente um sistema de login com nome de usuário e senha. O usuário tem no máximo 3 tentativas."""



"""10. Número Secreto com Loop

Gere um número aleatório entre 1 e 20. Peça ao usuário para adivinhar, informando se ele errou ou acertou. Repita até acertar."""



# Resolução das atividades.

# Questão 1:
num_inteiro = 11
if num_inteiro % 2 == 0:
    print("O número é par")
else: 
    print("O número é ímpar")

# Podemos usar operação ternária: <valor> if <condicao> else <outro_valor>
# Ficaria assim:
print(f"O número {num_inteiro} é par" if num_inteiro % 2 == 0 else f"O número {num_inteiro} é impar")

# Questão 2
entrada = input("Digite dois números separados por espaço (Ex: 1 2): ")
print(entrada)
primeiro_num, segundo_num = entrada.split() 
primeiro_num = int(primeiro_num)
segundo_num = int(segundo_num)
if int(primeiro_num) > int(segundo_num):
    print(f"O número {primeiro_num} é maior que o número {segundo_num}")
elif int(primeiro_num) == int(segundo_num):
    print(f"Os números são iguais")
else:
    print(f"O número {segundo_num} é maior que o número {primeiro_num}")

# Questão 3
calcula = input("Digite dois números separados por espaço (Ex: 1 2): ")
num_um, num_dois = calcula.split()
num_um = int(num_um)
num_dois = int(num_dois)
operador = input("Escolha um dos operadores para realizar o cáculo: ( 1 -> +, 2 -> -, 3 -> *, 4 -> / ) ")
if operador == "1":
    print(f"Soma: {num_um + num_dois}")
elif operador == "2":
    print(f"Subtração: {num_um - num_dois}")
elif operador == "3":
    print(f"Multiplicação: {num_um * num_dois}")
else:
    print(f"Divisão: {num_um / num_dois}")

# Questão 4
idade = int(input("Qual sua idade? "))
if idade >= 0 and idade <= 12:
    print("Você é criança!")
elif idade >= 13 and idade <= 17:
    print("Você é adolescente!")
elif idade >= 18 and idade <= 59:
    print("Você é adulto!")
else:
    print("Você é idoso!")

# Questão 5
cont = 1
while cont <= 10:
    print(cont, end=" ")
    cont +=1

# Questão 6
tabuada = int(input("Digite um número para verificar a tabuada dele: "))
for i in range(1, 11, 1):
    print(f"{i} * {tabuada} = {i * tabuada}") 

# Questão 7
soma_pares = int(input("Digite um número: "))
soma = 0
for i in range(2, soma_pares + 1, 2):
    soma += i
print(soma) 

# Questão 8
# Peça uma palavra ao usuário e conte quantas vogais ela possui. Use um for e if.
palavra = input("Digite uma palavra: ")
vogais = "aeiou"
contagem_vogais = 0
for vogal in palavra:
    if vogal in vogais:
        contagem_vogais +=1
print(f"A palavra digitada possui {contagem_vogais} vogais") 

# Questão 9
user = 'Alexandre'
password = '12345'
tentativas = 0
while tentativas < 3:
    usuario = input("Digite seu usuário: ")
    senha = input("Digite sua senha: ")
    if usuario == user and senha == password:
        print("Usuário logado no sistema!")
        break
    else:
        tentativas +=1
        print(f"Usuário ou senha incorretos.\nVocê possui mais {3 - tentativas} tentativas") 

# Questão 10
# Gere um número aleatório entre 1 e 20. Peça ao usuário para adivinhar, informando se ele errou ou acertou. Repita até acertar.
import random

numero_aleatorio = random.randint(1, 20)
print(numero_aleatorio)
while True:
    escolha_usuario = int(input("Adivinhe o número escolhido: "))
    if escolha_usuario == numero_aleatorio:
        print("Você acertou!")
        break
    else:
        print("Tente novamente!")

