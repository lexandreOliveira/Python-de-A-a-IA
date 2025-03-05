## 🔤 Texto

Python pode manipular texto (representado pelo tipo str, também chamado de “strings”), bem como números. Isso inclui caracteres “!”, palavras “coelho”, nomes “Paris”, frases “Eu te protejo.”, etc. “Oba! :)”. Eles podem ser colocados entre aspas simples ('...') ou aspas duplas ("...") com o mesmo resultado

```
>>> 'd\'água'  # use \' para escapar a aspa simples...
"d'água"

>>> "d'água"  # ...ou use aspas duplas
"d'água"

>>> '"Sim", eles disseram.'
'"Sim", eles disseram.'

>>> "\"Sim\", eles disseram."
'"Sim", eles disseram.'

>>> '"Copo d\'água", eles pediram.'
'"Copo d'água", eles pediram.'

```
No shell do Python, a definição de string e a string de saída podem parecer diferentes. A função print() produz uma saída mais legível, omitindo as aspas delimitadoras e imprimindo caracteres de escape e especiais:

```
>>> s = 'Primeira linha.\nSegunda linha.'  # \n significa nova linha

>>> s  # sem print(), caracteres especiais são incluídos na string
'Primeira linha.\nSegunda linha.'

>>> print(s)  # com print(), caracteres especiais são interpretados, então \n produz nova linha
Primeira linha.
Segunda linha.
```
Se não quiseres que os caracteres sejam precedidos por \ para serem interpretados como caracteres especiais, poderás usar strings raw (N.d.T: “crua” ou sem processamento de caracteres de escape) adicionando um r antes da primeira aspa:
```
>>> print('C:\algum\nome')  # aqui \n significa nova linha!
C:\algum
ome

>>> print(r'C:\algum\nome')  # observe o r antes das aspas
C:\algum\nome

```
Strings podem ser concatenadas (coladas) com o operador +, e repetidas com *:
```
>>> # 3 vezes 'un', seguido por 'ium'

>>> 3 * 'un' + 'ium'
'unununium'

```
Duas ou mais strings literais (ou seja, entre aspas) ao lado da outra são automaticamente concatenados.
```
>>> 'Py' 'thon'
'Python'

```
Esse recurso é particularmente útil quando você quer quebrar strings longas:
```
>>> texto = ('Coloque várias strings dentro de parênteses '

         'para fazer com que elas sejam concatenadas.')

>>> texto
'Coloque várias strings dentro de parênteses para fazer com que elas sejam concatenadas.'

```
Isso só funciona com duas strings literais, não com variáveis ou expressões:
```
>>> prefixo = 'Py'

>>> prefixo 'thon'  # não é possível concatenar uma variável e um literal de string
  File "<stdin>", line 1
    prefixi 'thon'
           ^^^^^^
SyntaxError: invalid syntax

>>> ('un' * 3) 'ium'
  File "<stdin>", line 1
    ('un' * 3) 'ium'
               ^^^^^
SyntaxError: invalid syntax

```

Se você quiser concatenar variáveis ou uma variável e uma literal, use +:
```
>>> prefixo + 'thon'
'Python'

```
As strings podem ser indexadas (subscritas), com o primeiro caractere como índice 0. Não existe um tipo específico para caracteres; um caractere é simplesmente uma string cujo tamanho é 1:

```
>>> palavra = 'Python'

>>> palavra[0]  # caractere na posição 0
'P'

>>> palavra[5]  # caractere na posição 5
'n'

```
Índices também podem ser números negativos para iniciar a contagem pela direita:
```
>>> palavra[-1]  # último caractere
'n'

>>> palavra[-2]  # penúltimo caractere
'o'

>>> palavra[-6]
'P'

```
Note que dado que -0 é o mesmo que 0, índices negativos começam em -1.

Além da indexação, o fatiamento também é permitido. Embora a indexação seja usada para obter caracteres individuais, fatiar permite que você obtenha uma substring:
```
>>> palavra[0:2]  # caracteres da posição 0 (incluída) até 2 (excluída)
'Py'

>>> palavra[2:5]  # caracteres da posição 2 (incluída) até 5 (excluída)
'tho'

```
Os índices do fatiamento possuem padrões úteis; um primeiro índice omitido padrão é zero, um segundo índice omitido é por padrão o tamanho da string sendo fatiada:
```
>>> palavra[:2]   # caracteres do início até a posição 2 (excluída)
'Py'

>>> palavra[4:]   # caracteres da posição 4 (incluída) até o fim
'on'

>>> palavra[-2:]  # caracteres da penúltima (incluída) até o fim
'on'

```
Observe como o início sempre está incluído, e o fim sempre é excluído. Isso garante que s[:i] + s[i:] seja sempre igual a s:
```
>>> palavra[:2] + palavra[2:]
'Python'

>>> palavra[:4] + palavra[4:]
'Python'
```

Uma maneira de lembrar como fatias funcionam é pensar que os índices indicam posições entre caracteres, onde a borda esquerda do primeiro caractere é 0. Assim, a borda direita do último caractere de uma string de comprimento n tem índice n, por exemplo:
```
 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1

```
A primeira fileira de números indica a posição dos índices 0…6 na string; a segunda fileira indica a posição dos respectivos índices negativos. Uma fatia de i a j consiste em todos os caracteres entre as bordas i e j, respectivamente.

Para índices positivos, o comprimento da fatia é a diferença entre os índices, se ambos estão dentro dos limites da string. Por exemplo, o comprimento de word[1:3] é 2.

A tentativa de usar um índice que seja muito grande resultará em um erro:
```
>>> palavra[42]  # a palavra só tem 6 caracteres
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range

```
No entanto, os índices de fatiamento fora do alcance são tratados graciosamente (N.d.T: o termo original “gracefully” indica robustez no tratamento de erros) quando usados para fatiamento. Um índice maior que o comprimento é trocado pelo comprimento, um limite superior menor que o limite inferior produz uma string vazia:
```
>>> palavra[4:42]
'on'

>>> palavra[42:]
''
```
As strings do Python não podem ser alteradas — uma string é imutável. Portanto, atribuir a uma posição indexada na sequência resulta em um erro:
```
>>> palavra[0] = 'J'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment

>>> palavra[2:] = 'py'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment

```
Se você precisar de uma string diferente, deverá criar uma nova:
```
>>> 'J' + palavra[1:]
'Jython'

>>> palavra[:2] + 'py'
'Pypy'

```
A função embutida len() devolve o comprimento de uma string:
```
>>> s = 'supercalifragilisticexpialidoce'

>>> len(s)
31

```

## Python - Modificar strings

Como já sabemos, Python trata uma string como um array imutável de caracteres, onde cada caractere é acessado por um índice.

Embora possamos acessar e manipular strings usando indexação, não podemos modificar diretamente um caractere de uma string, pois elas são imutáveis. No entanto, podemos criar novas strings a partir de modificações.

Veja os exemplos abaixo:

```
# Acessando caracteres por índice
s = "Python"
print(s[0])  # Saída: P

# Tentando modificar um caractere (isso gera erro!)
s[0] = "J"  # TypeError: 'str' object does not support item assignment

# Criando uma nova string a partir da original
s_modificada = "J" + s[1:]  
print(s_modificada)  # Saída: Jython


```
🛠️ Métodos de Modificação de Strings

Neste ponto dos estudos, aprenderemos sobre alguns métodos internos que o Python possui e que podem ser aplicados a strings para facilitar sua manipulação.

🔹 Método upper()

O método upper() retorna a string com todas as letras em maiúsculas.
```
a = "Hello, World!"
print(a.upper())

# Saída esperada:
# HELLO, WORLD!

```
🔸Método lower()

O método lower() retorna a string com todas as letras em minúsculas.

```
a = "HELLO, WORLD!"
print(a.lower())

# Saída esperada:
# hello, world!

```
🔸Método strip()
O método strip() retorna a string sem os espaços antes e depois do texto em si. O espaço livre é o espaço antes e/ou depois do texto real, e muitas vezes você deseja remover esse espaço.
```
a = " Hello, World! "
print(a.strip()) # saída "Hello, World!"
```
🔸Método replace()
O método replace substitui uma string por outra string
```
a = "Hello, World!"
print(a.replace("H", "J")) # saída "Jello, World"
```
🔸Método split()
O método retorna uma lista em que o texto entre o separador especificado se torna os itens da lista.
```
a = "Hello, World!"
print(a.split(",")) # saída ['Hello', ' World!'] 
```

### Concatenação de strings
Para concatenar ou combinar duas strings você pode usar o operador +.

Fusão das variáveis a e b em c. 
```
a = "Hello"
b = "World"
c = a + b
print(c)
```


# Métodos de Strings - Python

Python possui um conjunto de métodos embutidos que você pode usá-los nas strings.
Todos os métodos retornam um novo valor. Eles não mudam a string original.

📌 **Métodos de strings**

| Método        | Descrição |
|--------------|-----------|
| capitalize() | Converte o primeiro caractere para maiúsculo |
| casefold() | Converte a string para minúsculas |
| center() | Retorna uma string centralizada |
| count() | Retorna o número de vezes que um valor especificado ocorre em uma string |
| encode() | Retorna uma versão codificada da string |
| endswith() | Retorna verdadeiro se a string terminar com o valor especificado |
| expandtabs() | Define o tamanho do tab na string |
| find() | Pesquisa a string por um valor especificado e retorna a posição onde foi encontrado |
| format() | Formata valores especificados em uma string |
| format_map() | Formata valores especificados em uma string |
| index() | Pesquisa a string por um valor especificado e retorna a posição onde foi encontrado |
| isalnum() | Retorna verdadeiro se todos os caracteres da string forem alfanuméricos |
| isalpha() | Retorna verdadeiro se todos os caracteres da string estiverem no alfabeto |
| isascii() | Retorna verdadeiro se todos os caracteres da string forem caracteres ASCII |
| isdecimal() | Retorna verdadeiro se todos os caracteres da string forem decimais |
| isdigit() | Retorna verdadeiro se todos os caracteres da string forem dígitos |
| isidentifier() | Retorna verdadeiro se a string for um identificador válido |
| islower() | Retorna verdadeiro se todos os caracteres da string estiverem em minúsculas |
| isnumeric() | Retorna verdadeiro se todos os caracteres da string forem numéricos |
| isprintable() | Retorna verdadeiro se todos os caracteres da string forem imprimíveis |
| isspace() | Retorna verdadeiro se todos os caracteres da string forem espaços em branco |
| istitle() | Retorna verdadeiro se a string seguir as regras de um título |
| isupper() | Retorna verdadeiro se todos os caracteres da string estiverem em maiúsculas |
| join() | Junta os elementos de um iterável ao final da string |
| ljust() | Retorna uma versão justificada à esquerda da string |
| lower() | Converte a string para minúsculas |
| lstrip() | Retorna uma versão da string sem os espaços à esquerda |
| maketrans() | Retorna uma tabela de tradução para ser usada em traduções |
| partition() | Retorna uma tupla onde a string é dividida em três partes |
| replace() | Retorna uma string onde um valor especificado é substituído por outro valor especificado |
| rfind() | Pesquisa a string por um valor especificado e retorna a última posição onde foi encontrado |
| rindex() | Pesquisa a string por um valor especificado e retorna a última posição onde foi encontrado |
| rjust() | Retorna uma versão justificada à direita da string |
| rpartition() | Retorna uma tupla onde a string é dividida em três partes |
| rsplit() | Divide a string no separador especificado e retorna uma lista |
| rstrip() | Retorna uma versão da string sem os espaços à direita |
| split() | Divide a string no separador especificado e retorna uma lista |
| splitlines() | Divide a string nas quebras de linha e retorna uma lista |
| startswith() | Retorna verdadeiro se a string começar com o valor especificado |
| strip() | Retorna uma versão da string sem espaços em branco no início e no fim |
| swapcase() | Inverte os casos, transformando minúsculas em maiúsculas e vice-versa |
| title() | Converte o primeiro caractere de cada palavra para maiúsculo |
| translate() | Retorna uma string traduzida |
| upper() | Converte a string para maiúsculas |
| zfill() | Preenche a string com um número especificado de zeros no início |

#### [Atividades de strings](stringsExe.py)