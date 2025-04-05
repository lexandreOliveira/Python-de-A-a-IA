# ✅ 📌 Manipulação Prática de conjuntos em Python: Métodos e Funcionalidades

Após compreender os aspectos teóricos dos conjuntos (*sets*) em Python, é hora de explorar sua manipulação prática. Os conjuntos oferecem ferramentas poderosas para lidar com coleções de elementos únicos, com foco em operações matemáticas e verificações rápidas. Esta seção detalha como criar conjuntos, medir seu tamanho, verifcar elemetos, utilizar métodos essesnciais e iterar sobre eles, tudo ilustrado com exemplos práticos.

### 1️⃣ Função Construtora e Sintaxe Básica
Os conjuntos podem ser criados de duas formas principais: usando chaves `{}` ou a função construtora `set()`.

- Usando chaves `{}`

```python
    frutas = {"maçã", "banana", "laranja"}

```
Os elementos são separados por vírgulas. Note que `{}` cria um *dicionário vazio*, não um conjunto; para um conjunto vazio, use set().

- Usando a função `set()`: Converte iteráveis (como listas, strings ou tuplas) em conjunto, removendo duplicatas automaticamente:

```Python
texto = set("Python") # {'P', 'y', 't', 'h', 'o', 'n'}
lista = set([1, 2, 2, 3]) # {1, 2, 3}

```

### 2️⃣ Comprimento do Conjunto

A função len() retorna o número de elementos em um conjunto:

```Python
frutas = {"maçã", "banana", "laranja"}
print(len(frutas))  # Saída: 3
```
O resultado reflete a quantidade de itens únicos, já que duplicatas não são permitidas.

### 3️⃣ Acessando Elementos

Diferentemente das listas, os conjuntos não suportam indexação ou slicing, pois não possuem ordem definida. Em vez disso, o acesso é feito por verificação de pertinência com os operadores in e not in:

```Python
frutas = {"maçã", "banana", "laranja"}
print("maçã" in frutas)  # Saída: True
print("uva" not in frutas)  # Saída: True
```
Essa operação é extremamente eficiente (O(1) em média), graças à implementação como tabela de hash, sendo ideal para testar a existência de elementos.

### 4️⃣ Métodos Essenciais dos Conjuntos

Os conjuntos possuem métodos úteis para adicionar, remover e manipular elementos.

➕ Adição de Elementos

-   add(elem) → Adiciona um elemento ao conjunto, ignorando se já existe.
```Python
frutas = {"maçã", "banana"}
frutas.add("laranja")
print(frutas)  # {'maçã', 'banana', 'laranja'}

```
➖ Remoção de Elementos

-   remove(elem) → Remove o elemento especificado; gera erro se não existir.

```Python
frutas.remove("banana")
print(frutas)  # {'maçã', 'laranja'}

```

- discard(elem) → Remove o elemento especificado; não gera erro se não existir.

```Python
frutas.discard("uva")  # Não faz nada, pois "uva" não está no conjunto
```

- pop() → Remove e retorna um elemento aleatório do conjunto.
```Python
elemento = frutas.pop()
print(elemento)  # Saída imprevisível, pois a ordem do conjunto não é fixa
```

### 🔄 Operações entre Conjuntos
Os conjuntos permitem operações matemáticas, semelhantes às da Teoria dos Conjuntos.
- União (union() ou |) → Retorna um novo conjunto contendo elementos dos dois conjuntos.

```Python
A = {1, 2, 3}
B = {3, 4, 5}
print(A | B)  # {1, 2, 3, 4, 5}
print(A.union(B))  # {1, 2, 3, 4, 5}
```

- Interseção (intersection() ou &) → Retorna um conjunto com os elementos comuns.
```Python
print(A & B)  # {3}
print(A.intersection(B))  # {3}
```

- Diferença (difference() ou -) → Retorna os elementos que estão no primeiro conjunto, mas não no segundo.
```Python
print(A - B)  # {1, 2}
print(A.difference(B))  # {1, 2}
```

- Diferença Simétrica (symmetric_difference() ou ^) → Retorna os elementos que estão em um dos conjuntos, mas não em ambos.
```Python
print(A ^ B)  # {1, 2, 4, 5}
print(A.symmetric_difference(B))  # {1, 2, 4, 5}
```

### 🔄 Métodos para Modificar Conjuntos

- update(iterável) → Adiciona elementos de um iterável ao conjunto.
```Python
A.update([4, 5, 6])
print(A)  # {1, 2, 3, 4, 5, 6}
```

- intersection_update(outro_conjunto) → Mantém apenas os elementos em comum.
```Python
A.intersection_update(B)
print(A)  # {3}
```

- difference_update(outro_conjunto) → Remove os elementos presentes no outro conjunto.

```Python
A = {1, 2, 3, 4}
A.difference_update({3, 4})
print(A)  # {1, 2}
```

### 5️⃣ Iteração sobre Conjuntos
Os conjuntos são iteráveis e podem ser percorridos com for:
```Python
numeros = {10, 20, 30, 40}
for numero in numeros:
    print(numero)
```
⚠️ A ordem de saída não é garantida! Como os conjuntos não são ordenados, a sequência dos elementos pode variar.

### 6️⃣ Cópia e Remoção Total

- copy() → Retorna uma cópia do conjunto.

```Python
novo_conjunto = numeros.copy()
``` 
- clear() → Remove todos os elementos do conjunto.
```Python
numeros.clear()
print(numeros)  # set()
```

🎯 Conclusão

Os conjuntos são estruturas de dados eficientes para armazenar elementos únicos e realizar operações matemáticas. Conhecer seus métodos ajuda a otimizar código e escrever soluções mais rápidas e elegantes.

[Atividades](conjuntos.py)