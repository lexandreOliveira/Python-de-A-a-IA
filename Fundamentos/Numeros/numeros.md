## 🔢 Números em Python  

O interpretador do Python pode ser usado como **uma calculadora simples**, permitindo operações matemáticas básicas e avançadas.  

### 🧮 **Operações Aritméticas**  

A sintaxe segue os operadores matemáticos usuais:  
- `+` (soma)  
- `-` (subtração)  
- `*` (multiplicação)  
- `/` (divisão - retorna float)  
- `//` (divisão inteira)  
- `%` (módulo - resto da divisão)  
- `**` (potenciação)  

📌 **Exemplos no terminal Python:**  
```python
>>> 2 + 2  
4  

>>> 50 - 5 * 6  
20  

>>> (50 - 5 * 6) / 4  
5.0  

>>> 8 / 5  # divisão sempre retorna um float  
1.6  
```

🏷️ **Tipos Numéricos**  

Os principais tipos numéricos no Python são:

    int → números inteiros (ex.: 2, 4, 20)
    float → números com parte decimal (ex.: 5.0, 1.6)
    complex → números complexos (ex.: 3+5j)

📌 **Verificando o tipo de um número:**
```python
x, y, z = 2, 3.5, 1j  

print(type(x))  # <class 'int'>  
print(type(y))  # <class 'float'>  
print(type(z))  # <class 'complex'>  
```

➗ **Divisão Inteira e Módulo**  

    Divisão / → retorna float.
    Divisão inteira // → descarta a parte decimal.
    Módulo % → retorna o resto da divisão.

📌 **Exemplo:**
```python
>>> 17 / 3  # divisão normal  
5.666666666666667  

>>> 17 // 3  # divisão inteira  
5  

>>> 17 % 3  # resto da divisão  
2  
```

🏗 **Potenciação e Atribuições**  

    Potência (**) → usada para elevar números a um expoente.
    Atribuição (=) → armazena valores em variáveis.

📌 **Exemplo:**
```python
>>> 5 ** 2  # 5²  
25  

>>> 2 ** 7  # 2 elevado a 7  
128  

>>> largura = 20  
>>> altura = 5 * 9  
>>> largura * altura  
900  
```

⚠️ **Erro ao usar variáveis não definidas:**
```python
>>> n  # tenta acessar uma variável não definida  
Traceback (most recent call last):  
  File "<stdin>", line 1, in <module>  
NameError: name 'n' is not defined  
```

🔄 **Conversão de Tipos (Type Casting)**  

Podemos converter valores entre int, float e complex usando:

    int(valor) → converte para inteiro
    float(valor) → converte para ponto flutuante
    complex(valor) → converte para número complexo

📌 **Exemplo:**
```python
print(int(3.6))   # 3  
print(float(7))   # 7.0  
print(complex(2)) # (2+0j)  
```

🔢 **Última Expressão Avaliada (_)**  

No modo interativo do Python, o valor da última expressão pode ser acessado pela variável especial `_`.

📌 **Exemplo de uso na calculadora Python:**
```python
>>> taxa = 12.5 / 100  
>>> preço = 100.50  
>>> preço * taxa  
12.5625  

>>> preço + _  
113.0625  

>>> round(_, 2)  # arredonda para 2 casas decimais  
113.06  
```

🔀 **Números Aleatórios com random**  

O Python possui o módulo `random` para geração de números aleatórios.

📌 **Exemplo de uso:**
```python
import random

print(random.randint(1, 10))  # Retorna um número inteiro aleatório entre 1 e 10
print(random.random())  # Retorna um número float entre 0 e 1
print(random.uniform(1.5, 5.5))  # Retorna um float entre os valores especificados
print(random.choice(["maçã", "banana", "uva"]))  # Escolhe aleatoriamente um item da lista
```

📌 **Resumo Rápido**

| Operação          | Símbolo | Exemplo   | Resultado      |
|------------------|---------|----------|---------------|
| Soma            | `+`     | `2 + 3`  | `5`           |
| Subtração       | `-`     | `7 - 4`  | `3`           |
| Multiplicação   | `*`     | `3 * 5`  | `15`          |
| Divisão        | `/`     | `10 / 3` | `3.3333...`   |
| Divisão Inteira | `//`    | `10 // 3` | `3`           |
| Resto (Módulo)  | `%`     | `10 % 3` | `1`           |
| Potenciação     | `**`    | `2 ** 3` | `8`           |

📖 **Conclusão**

O Python oferece suporte completo para números e operações matemáticas, tornando-o ideal tanto para cálculos simples quanto para computação científica. 🚀

