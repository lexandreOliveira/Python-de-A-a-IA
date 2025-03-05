# 🧮 Operadores Python

Os operadores são usados para realizar operações em variáveis e valores.

No exemplo a seguir, nós usamos o operador + para somar dois valores.
```
print(10+5)
```
Python divide os operadores nos seguintes grupos:

   * Operadores aritméticos
   * Operadores de atribuição
   * Operadores de comparação
   * Operadores lógicos
   * Operadores de identidade
   * Operadores de adesão
   * Operadores bit a bit

#### Operadores Aritméticos Python
Operadores aritméticos são usados ​​com valores numéricos para realizar operações matemáticas comuns:

| Operador | Nome | Exemplo|
|----------|------|--------|
|    +     | Adição|  x + y | 
|    -     | Subtração|  x - y | 
|    *     | Multiplicação|  x * y | 
|    /     | Divisão|  x / y | 
|    %     | Módulo|  x % y | 
|    +     | exponenciação|  x ** y | 
|    //     | Divisão inteiro|  x // y |      


#### Operadores de Atribuição Python

Operadores de atribuição são usados ​​para atribuir valores a variáveis:

| Operador | Exemplo        | Equivalente a    | Explicação |
|----------|---------------|-----------------|------------|
| `=`      | `x = 5`       | `x = 5`         | Atribui o valor 5 à variável `x`. |
| `+=`     | `x += 3`      | `x = x + 3`     | Soma `3` ao valor de `x` e armazena o resultado em `x`. |
| `-=`     | `x -= 3`      | `x = x - 3`     | Subtrai `3` do valor de `x` e armazena o resultado em `x`. |
| `*=`     | `x *= 3`      | `x = x * 3`     | Multiplica `x` por `3` e armazena o resultado em `x`. |
| `/=`     | `x /= 3`      | `x = x / 3`     | Divide `x` por `3` e armazena o resultado em `x` (resultado será `float`). |
| `%=`     | `x %= 3`      | `x = x % 3`     | Calcula o **resto da divisão** de `x` por `3` e armazena o resultado em `x`. |
| `//=`    | `x //= 3`     | `x = x // 3`    | Divide `x` por `3` e mantém **apenas a parte inteira**. |
| `**=`    | `x **= 3`     | `x = x ** 3`    | Eleva `x` à potência `3` e armazena o resultado em `x`. |
| `&=`     | `x &= 3`      | `x = x & 3`     | Faz um **"E" bit a bit** entre `x` e `3` e armazena o resultado em `x`. |
| `|=`     | `x |= 3`      | `x = x | 3`     | Faz um **"OU" bit a bit** entre `x` e `3` e armazena o resultado em `x`. |
| `^=`     | `x ^= 3`      | `x = x ^ 3`     | Faz um **"OU exclusivo" bit a bit** entre `x` e `3`. |
| `>>=`    | `x >>= 3`     | `x = x >> 3`    | **Desloca os bits** de `x` **3 posições à direita** (divide por `2**3`). |
| `<<=`    | `x <<= 3`     | `x = x << 3`    | **Desloca os bits** de `x` **3 posições à esquerda** (multiplica por `2**3`). |
| `:=`     | `print(x := 3)` | `x = 3` (exibição imediata) | Atribui `3` a `x` e **retorna o valor na mesma expressão**. |


🔥 Explicações Extras

* Operadores matemáticos (+=, -=, *= etc.) facilitam a modificação de valores sem precisar repetir x = x + algo.
* Operadores bit a bit (&=, |=, ^=, >>=, <<=) são úteis para manipulação de bits e otimização de código.
* O operador "Walrus" (:=) é usado para atribuir valores dentro de expressões, tornando o código mais eficiente.


#### Operadores de comparação Python

Operadores de comparação são usados ​​para comparar dois valores:

| Operador | Nome                         | Exemplo  | Explicação |
|----------|------------------------------|----------|------------|
| `==`     | Igual                        | `x == y` | Retorna `True` se `x` for **igual** a `y`. |
| `!=`     | Diferente                    | `x != y` | Retorna `True` se `x` for **diferente** de `y`. |
| `>`      | Maior que                    | `x > y`  | Retorna `True` se `x` for **maior** que `y`. |
| `<`      | Menor que                    | `x < y`  | Retorna `True` se `x` for **menor** que `y`. |
| `>=`     | Maior ou igual a             | `x >= y` | Retorna `True` se `x` for **maior ou igual** a `y`. |
| `<=`     | Menor ou igual a             | `x <= y` | Retorna `True` se `x` for **menor ou igual** a `y`. |


📝 Explicação

* Operadores de comparação são usados para comparar dois valores e retornam True ou False.
* São muito utilizados em estruturas condicionais (if, while) e expressões booleanas. 🚀😃



#### Operadores Lógicos Python

Operadores lógicos são usados ​​para combinar instruções condicionais:

| Operador | Descrição                                  | Exemplo                   | Explicação |
|----------|-------------------------------------------|---------------------------|------------|
| `and`    | Retorna `True` se **ambas** as condições forem verdadeiras | `x < 5 and x < 10` | Retorna `True` se `x` for **menor que 5** e **menor que 10** ao mesmo tempo. |
| `or`     | Retorna `True` se **pelo menos uma** das condições for verdadeira | `x < 5 or x < 4`  | Retorna `True` se `x` for **menor que 5** **ou** **menor que 4**. |
| `not`    | Inverte o resultado, retorna `False` se a condição for verdadeira | `not (x < 5 and x < 10)` | Se `x` for menor que `5` e `10`, `not` inverte para `False`. |


📝 Explicação

*   and (E lógico) → Só retorna True se ambas as condições forem verdadeiras.
*   or (OU lógico) → Retorna True se pelo menos uma das condições for verdadeira.
*   not (Negação lógica) → Inverte o valor booleano (True vira False e vice-versa).

Esses operadores são essenciais para estruturas condicionais (if, while) e lógica booleana. 🚀😃

#### Operadores de identidade Python

Os operadores de identidade são usados ​​para comparar os objetos, não se forem iguais, mas se forem realmente o mesmo objeto, com a mesma localização de memória:

| Operador  | Descrição                                        | Exemplo   | Explicação |
|-----------|-------------------------------------------------|-----------|------------|
| `is`      | Retorna `True` se ambas as variáveis forem o **mesmo objeto** na memória | `x is y` | Retorna `True` se `x` e `y` apontarem para o **mesmo local na memória**. |
| `is not`  | Retorna `True` se as variáveis **não forem o mesmo objeto** na memória | `x is not y` | Retorna `True` se `x` e `y` forem **objetos diferentes** na memória. |


📝 Explicação

*   is verifica se duas variáveis apontam para o mesmo objeto na memória, e não apenas se seus valores são iguais.
*   is not faz o oposto: retorna True se as variáveis não forem o mesmo objeto na memória.

📌 Exemplo prático:
```
a = [1, 2, 3]
b = a       # `b` aponta para o mesmo objeto que `a`
c = [1, 2, 3]  # `c` tem o mesmo valor, mas é um objeto diferente

print(a is b)   # True (mesmo objeto)
print(a is c)   # False (objetos diferentes, mas valores iguais)
print(a == c)   # True (valores iguais)
print(a is not c)  # True (objetos diferentes)
```
Isso é muito útil para verificar identidade de objetos em Python! 🚀😃


#### Operadores de associação Python

Operadores de associação são usados ​​para testar se uma sequência é apresentada em um objeto:
| Operador  | Descrição                                                         | Exemplo     |
|-----------|-------------------------------------------------------------------|-------------|
| `in`      | Retorna `True` se uma sequência com o valor especificado estiver presente no objeto. | `x in y`    |
| `not in`  | Retorna `True` se uma sequência com o valor especificado **não** estiver presente no objeto. | `x not in y` |


#### Operadores bit a bit Python

Operadores bit a bit são usados ​​para comparar números (binários):

| Operador | Nome | Descrição | Exemplo |
|----------|------|-----------|---------|
| `&`      | AND  | Define cada bit como 1 se ambos os bits forem 1. | `x & y` |
| `|`      | OR   | Define cada bit como 1 se um dos dois bits for 1. | `x | y` |
| `^`      | XOR  | Define cada bit como 1 se **somente** um dos dois bits for 1. | `x ^ y` |
| `~`      | NOT  | Inverte todos os bits. | `~x` |
| `<<`     | Zero fill left shift | Desloca os bits para a esquerda preenchendo com zeros à direita e deixando os bits à esquerda caírem. | `x << 2` |
| `>>`     | Signed right shift | Desloca os bits para a direita preenchendo com cópias do bit mais à esquerda e deixando os bits à direita caírem. | `x >> 2` |


#### [Atividades](operadores.py)

#### [Próximo tema](operadores.py)


