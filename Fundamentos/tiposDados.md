
# Uma Introdução Informal ao Python :book:

Comentários em python de apenas uma linha começam com o caractere cerquilha # e estende até o final da linha. Um comentário pode aparecer no início da linha ou após espaço em branco ou código, mas não dentro de uma string literal. O caractere cerquilha dentro de uma string literal é apenas uma cerquilha. Como os comentários são para esclarecer o código e não são interpretados pelo Python, eles podem ser omitidos ao digitar exemplos.

Alguns exemplos:


spam = 1  # e este é o segundo comentário
          # ... e agora um terceiro!
texto = "# Este não é um comentário por estar entre aspas."


# Sintaxe

Toda Linguagem de programação tem sua maneira de transliterar  a lógica de um determinado algoritmo em uma linguagem característica que será interpretada  "pelo computador", isto chamamos de sintaxe.

Toda linguagem de programação tem sua sintaxe característica, o programador deve respeitá-la até porque o interpretador é uma camada de software o qual é “programado” para entender apenas o que está sob a sintaxe correta. Outro ponto importante é que uma vez que você domina a sintaxe da linguagem ao qual está trabalhando, ainda assim haverão erros em seus códigos devido a erros de lógica.

# Tipos de dados 

##### Caso queira seguir para os exemplos e exercícios, [clique aqui 💻](tiposdados.py)
#### Tipos de dados incorporados
Na programação, o tipo de dados é um conceito importante.
As variáveis podem armazenar dados de diferentes tipos, e diferentes tipos podem fazer coisas diferentes.
O python tem os seguintes tipos de dados incorporados por padrão, nestas categorias:

``` 
Tipo de texto: 	        str
Tipos numéricos: 	    int,, , - float,, , - complex
Tipos de sequência: 	list,, , - tuple,, , - range
Tipo de Mapeamento: 	dict
Tipos de ajuste: 	    set,, , - frozenset
Tipo booleano: 	        bool
Tipos de binário: 	    bytes,, , - bytearray,, , - memoryview
Tipo de nenhum: 	    NoneTypeTipo de texto: 	str
Tipos numéricos: 	    int,, , - float,, , - complex
Tipos de sequência: 	list,, , - tuple,, , - range
Tipo de Mapeamento: 	dict
Tipos de ajuste: 	    set,, , - frozenset
Tipo booleano: 	        bool
Tipos de binário: 	    bytes,, , - bytearray,, , - memoryview
Tipo de nenhum: 	    NoneType

```

#### Mais adiante, estudaremos os tipos de dados separadamente.

Por agora veja como podemos usar a linguagem python para algumas operações matemáticas.

# Usando Python como uma calculadora

Para iniciar o interpletador no linux, apenas digite: python3 em seu terminal e aguarde o prompt primário, >>>.



### Números 
O interpretador funciona como uma calculadora bem simples: você pode digitar uma expressão e o resultado será apresentado. A sintaxe de expressões é a usual: operadores +, -, * e / podem ser usadas para realizar operações aritméticas; parênteses (()) podem ser usados para agrupar expressões. Por exemplo: 

```
>>> 2 + 2
4

>>>50 - 5*6
20

>>>(50 - 5*6) / 4
5.0

>>>8 / 5  # divisão sempre retorna um número de ponto flutuante
1.6# Uma Introdução Informal ao Python

```

Próximo tópico strings [clique aqui](strings.md)



