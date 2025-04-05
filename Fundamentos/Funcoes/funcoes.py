# Atividades

"""

🧠 Atividades: Funções e Escopo de Variáveis

1. Crie uma função que receba dois números e retorne a soma deles.
→ Teste a função com diferentes pares de números.

2. Crie uma função que receba um nome e imprima uma saudação personalizada.
→ Use um argumento padrão para o nome ("visitante").

def saudacao(nome="visitante"):
    print(f"Olá, {nome}!")

3. Crie uma função que receba três números e retorne a média.
→ Use print() para exibir a média com duas casas decimais.

4. Crie uma função chamada par_ou_impar que receba um número e diga se ele é par ou ímpar.
→ Utilize uma função aninhada para verificar a paridade.

5. Escreva uma função que imprima um menu (ex: "1 - Iniciar", "2 - Sair").
→ Encapsule o print() dentro de uma função mostrar_menu() sem argumentos.

6. Crie uma função que receba um nome e um número de vezes, e imprima a saudação repetida aquele número de vezes.
→ Faça o argumento vezes ter valor padrão 1.

7. Escreva uma função calcular_pagamento que receba valor da hora, horas trabalhadas e bônus.
→ Deixe bônus=0 como argumento padrão.
→ Retorne o valor total pago.

8. Crie uma função calculadora com comportamento diferente dependendo do operador fornecido.
→ Ex: calculadora(5, 3, operacao='subtracao')
→ Use argumentos nomeados e uma função aninhada para cada operação.


9. Crie uma função contador que contém uma função aninhada incrementar().
→ incrementar() deve acessar uma variável local ao escopo da função contador e somar 1 a cada chamada.
→ Retorne incrementar como função (função retornando função).

10. Implemente uma função fabrica_mensagens que receba um prefixo como argumento e retorne uma nova função.
→ Essa nova função deve receber uma mensagem e imprimir:
<prefixo>: <mensagem>
→ Exemplo:

erro = fabrica_mensagens("ERRO")
erro("Arquivo não encontrado")  # ERRO: Arquivo não encontrado



"""

# Questão 1
# Crie uma função que receba dois números e retorne a soma deles
def soma(a, b):
    print(f"A soma de {a = }, {b = }: = {a + b}")

# Exemplos:
soma(1, 3)

# Questão 2
# Crie uma função que receba um nome e imprima uma saudação personalizada
# Use um argumento padrão para o nome ("visitante").

def saudacao(nome='Visitante', msg='Olá'):
    print(msg, nome,"!")

saudacao("Alexandre")
saudacao()

# Questão 3
# Crie uma função que receba três números e retorne a média.
# → Use print() para exibir a média com duas casas decimais.
def media(a, b, c):
    media = (a + b + c)/3
    print(f"A média entre: {a=}, {b=}, {c=} é igual a: {media:.2f}")

media(1, 2, 3)

# Questão 4
# Crie uma função chamada par_ou_impar que receba um número e diga se ele é par ou ímpar.
# → Utilize uma função aninhada para verificar a paridade.

def par_ou_impar(number):
    def paridade():
        if number % 2 == 0:
            return "é um número par"
        else:
            return "é um número ímpar"
    return f"O número {number} {paridade()}"

print(par_ou_impar(2))


# Questão 5
#  Escreva uma função que imprima um menu (ex: "1 - Iniciar", "2 - Sair").
# → Encapsule o print() dentro de uma função mostrar_menu() sem argumentos.

def mostrar_menu():
    print("===== MENU PRINCIPAL =====")
    print("1 - Iniciar")
    print("2 - Sair")
    print("==========================")
mostrar_menu()

# Questão 6 
# Crie uma função que receba um nome e um número de vezes, e imprima a saudação repetida aquele número de vezes.
# → Faça o argumento vezes ter valor padrão 1.

def saudacao_repetida(nome, xvezes=1):
    msg = f'Olá {nome}\n' * xvezes
    return msg.rstrip()
print(saudacao_repetida('Alexandre', 3)) 
    
# Questão 7
# Escreva uma função calcular_pagamento que receba valor da hora, horas trabalhadas e bônus.
# → Deixe bônus=0 como argumento padrão.
# → Retorne o valor total pago.

def calcular_pagamento(valor_hora, horas_trabalhadas, bonus=0):
    total = (valor_hora * horas_trabalhadas) + bonus
    return total

total_pago = calcular_pagamento(20, 220)
print(f'O valor total pago é de: R${total_pago:.2f}')

# Questão 8
#  Crie uma função calculadora com comportamento diferente dependendo do operador fornecido.
# → Ex: calculadora(5, 3, operacao='subtracao')
# → Use argumentos nomeados e uma função aninhada para cada operação.

def calculadora(a, b, operacao='subtracao'):
    
    def adicao():
        return a + b

    def subtracao():
        return a - b

    def multiplicacao():
        return a * b

    def divisao():
        if b != 0:
            return a / b
        else:
            return 'Erro: divisão por zero.'
    
    if operacao == 'adicao':
        return f'O resultado da adição é: {adicao()}'
    elif operacao == 'subtracao':
        return f'O resultado da subtração é: {subtracao()}'
    elif operacao == 'multiplicacao':
        return f'O resultado da multiplicação é: {multiplicacao()}'
    elif operacao == 'divisao':
        return f'O resultado da divisão é: {divisao()}'
    else:
        return 'Operação inválida.'
    

print(calculadora(10, 5, operacao='adicao'))         
print(calculadora(10, 5, operacao='subtracao'))      
print(calculadora(10, 5, operacao='multiplicacao'))  
print(calculadora(10, 5, operacao='divisao'))        
print(calculadora(10, 0, operacao='divisao')) 



# Questão 9
#  Crie uma função contador que contém uma função aninhada incrementar().
# → incrementar() deve acessar uma variável local ao escopo da função contador e somar 1 a cada chamada.
# → Retorne incrementar como função (função retornando função).
def contador():
    x = 0
    def incrementar():
        nonlocal x
        x += 1
        return x
    return incrementar

cont = contador()
for i in range(10):
    print(cont())


# Questão 10
# Implemente uma função fabrica_mensagens que receba um prefixo como argumento e retorne uma nova função.
# → Essa nova função deve receber uma mensagem e imprimir:
# <prefixo>: <mensagem>
# → Exemplo:
# 
# erro = fabrica_mensagens("ERRO")
# erro("Arquivo não encontrado")  # ERRO: Arquivo não encontrado

def fabrica_mensagens(prefixe):
    def imprime_mensagem(msg):
        print(f'{prefixe}: {msg}')
    return imprime_mensagem

erro = fabrica_mensagens("ERRO")
aviso = fabrica_mensagens("AVISO")

aviso("Você está quase sem espaço!") 
erro("Arquivo não encontrado")    