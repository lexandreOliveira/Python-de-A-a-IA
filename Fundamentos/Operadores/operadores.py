"""
Atividade 1: Manipulação de Bits com Operadores Bit a Bit

Objetivo: Entender como os operadores bit a bit manipulam os bits de números inteiros.

Instruções:

    Crie um programa que tenha dois números inteiros como entrada do usuário.
    Utilize os operadores &, |, ^, ~, << e >> para realizar diferentes operações entre esses números.
    Exiba o resultado de cada operação e explique o que está acontecendo em cada etapa.

Exemplo:

    Entrada: x = 10, y = 5
    Resultado esperado:
        x & y
        x | y
        x ^ y
        ~x
        x << 2
        y >> 1

"""
x = int(input("Digite o primeiro número: "))
y = int(input("Digite o segundo número: "))

# Realiza a operação bit a bit

print(f"x & y: {x & y}")
print(f"x | y: {x | y}")
print(f"x ^ y: {x ^ y}")
print(f"~x: {~x}")
print(f"x << 2: {x << 2}")
print(f"y >> 2: {y >> 2}")

print(f"x em binário: {bin(x)}")
print(f"y em binário: {bin(y)}")

# 6 = 0000000000000110
# 3 = 0000000000000011
# --------------------
# 2 = 0000000000000010

"""
Atividade 2: Máscaras de Bits

Objetivo: Trabalhar com a manipulação de bits usando máscaras de bits para extrair ou modificar informações.

Instruções:

    Crie um número inteiro que represente um conjunto de dados binários.
    Use uma máscara de bits para alterar um bit específico (como 1 ou 0) e depois exiba o valor modificado.
    Implemente uma função que utilize um operador bit a bit para extrair o valor de um bit específico de um número.

Exemplo:

    Dado um número binário: x = 0b11001010
    Máscara de bit: mask = 0b00000001
    Manipule o bit mais à direita usando &, modifique-o com |, e altere o valor de um bit específico com ^.
    Mostre a manipulação de um bit específico no número.


"""
x = 0b11001010  # Número binário
mask = 0b00000011  # Máscara de bit (seleciona o dois bit mais à direita)
extracted_bit = x & mask  # Extrai os dois bit mais à direita
print(bin(extracted_bit))  # Exibe o resultado em binário (0b0 ou 0b1)

x = x | mask  # Modifica o bit mais à direita, tornando-o 1
print(bin(x))  # Exibe o número modificado em binário


x = x ^ mask  # Alterna o bit mais à direita
print(bin(x))  # Exibe o número após alternar o bit


"""

Atividade 3: Conversão de Números Binários e Decimais

Objetivo: Aplicar operadores bit a bit para realizar conversões entre números binários e decimais.

Instruções:

    Crie um programa que converta um número decimal em binário usando os operadores bit a bit (sem usar a função bin()).
    Crie um programa que converta um número binário de volta para decimal usando operações bit a bit.

Exemplo:

    Dado o número decimal 13, converta-o para binário.
    Dado o número binário 1011, converta-o de volta para decimal.

"""

x = int(input("Digite um número: "))
k = []
while x > 0:
    k.append(x % 2) 
    x = x // 2 
print("".join(str(bit) for bit in k[::-1]))

binario = input("Digite um número binário: ")  
decimal = 0  
potencia = 0  

while binario != "":  
    bit = int(binario[-1])  
    decimal += bit * (2 ** potencia)  
    potencia += 1  
    binario = binario[:-1]  

print(decimal) 

"""

Atividade 4: Implementação de Operações Lógicas

Objetivo: Aplicar operadores lógicos em uma implementação de uma tabela verdade.

Instruções:

    Crie um programa que peça para o usuário inserir dois valores booleanos (verdadeiro ou falso).
    Utilize os operadores lógicos and, or e not para gerar a tabela verdade para as combinações de entrada.
    Exiba a tabela verdade resultante para os operadores lógicos.

Exemplo:

    Entrada: True, False
    Exiba a tabela para:
        True and False
        True or False
        not True
"""

a = input("Digite True ou False para o primeiro valor: ").strip().capitalize()
b = input("Digite True ou False para o segundo valor: ").strip().capitalize()


if a == "True":
    a = True
else:
    a = False

if b == "True":
    b = True
else:
    b = False


print("\nTabela Verdade:")
print(f"{a} AND {b} → {a and b}")
print(f"{a} OR {b} → {a or b}")
print(f"NOT {a} → {not a}")
print(f"NOT {b} → {not b}")


"""

Atividade 5: Contagem de Bits 1

Objetivo: Contar o número de bits 1 em um número binário.

Instruções:

    Crie um programa que, dado um número binário, conte quantos bits 1 ele contém utilizando operadores bit a bit.
    Utilize o operador & para verificar cada bit individualmente e contar quantos bits 1 estão presentes.

Exemplo:

    Entrada: x = 0b110101
    Saída esperada: 4 (pois há 4 bits 1 em 110101)

"""

binario = input("Digite um número binário: ")
x = int(binario, 2)
contagem = 0
while x > 0:
    contagem += x & 1  
    x >>= 1  
    print(x)
print("Número de bits 1:", contagem)


"""

Atividade 6: Manipulação de Pixels com Operadores Bit a Bit

Objetivo: Trabalhar com manipulação de pixels de imagens (operação similar ao que seria feito com IA no hardware).

Instruções:

    Imagine que você tem uma imagem com valores de pixel representados como números binários (por exemplo, 8 bits por pixel).
    Crie um programa que simula o ajuste de brilho de uma imagem utilizando operadores bit a bit. O brilho pode ser aumentado utilizando o operador | ou diminuído utilizando o operador &.
    Simule a manipulação de contraste invertendo os bits de cada pixel utilizando o operador ^.

Exemplo:

    Dado um valor de pixel em binário: pixel = 0b11001010, aplique uma manipulação simples de brilho e contraste usando os operadores.

"""
pixel = 0b11001010  
     

brilho_1 = pixel | 0b00000001  
brilho_2 = pixel | 0b00000011  
brilho_3 = pixel | 0b00001111  


escuro_1 = pixel & 0b11111110  
escuro_2 = pixel & 0b11111100  
escuro_3 = pixel & 0b11110000  

contraste = pixel ^ 0b11111111

# Exibir resultados
print(f"Pixel original  : {bin(pixel)} ({pixel})")
print(f"Brilho +1 bit  : {bin(brilho_1)} ({brilho_1})")
print(f"Brilho +2 bits : {bin(brilho_2)} ({brilho_2})")
print(f"Brilho +4 bits : {bin(brilho_3)} ({brilho_3})")

print(f"Escuro -1 bit  : {bin(escuro_1)} ({escuro_1})")
print(f"Escuro -2 bits : {bin(escuro_2)} ({escuro_2})")
print(f"Escuro -4 bits : {bin(escuro_3)} ({escuro_3})")

print(f"Contraste: {bin(contraste)[2:].zfill(8)} ({contraste})")


"""

Atividade 7: Verificação de Paridade de Bits

Objetivo: Trabalhar com a paridade de bits (número de bits 1 em um número).

Instruções:

    Crie uma função que receba um número inteiro como parâmetro e retorne True se a quantidade de bits 1 no número for par e False se for ímpar.
    Utilize operadores bit a bit para realizar a contagem de bits 1.

Exemplo:

    Entrada: x = 0b11001010
    Saída esperada: True (pois há 4 bits 1, um número par)

"""

x = int(input("Digite um número inteiro: "))  # Entrada do usuário em decimal
contador = 0  

while x:  
    contador += x & 1  
    x >>= 1  
if contador % 2 == 0:
    print(True, f"pois há {contador} bits 1, um número par")  
else:
    print(False, f"pois há {contador} bits 1, um número ímpar")  


