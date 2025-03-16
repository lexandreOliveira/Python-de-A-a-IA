
### ✅ 📌 Manipulação Prática de Listas em Python: Métodos e Funcionalidades

Com os fundamentos teóricos das listas bem estabelecidos — como sua natureza ordenada e mutável, flexibilidade de tipos e implementação como arrays dinâmicos —, é hora de explorar como elas são manipuladas na prática. Esta seção foca nos métodos embutidos, funções relacionadas e operações essenciais para criar, acessar e modificar listas, oferecendo uma visão detalhada de suas capacidades e nuances.

---

#### 1. Criando Listas: Função Construtora e Sintaxe Básica
Para começar a trabalhar com listas, é essencial saber como criá-las. Existem duas formas principais:

- **Sintaxe Literal**: Usando colchetes `[]`, a maneira mais comum e direta.
  ```python
  lista_vazia = []  # Lista vazia
  lista_simples = [1, 2, 3]  # Lista com inteiros
  lista_heterogenea = [1, "texto", 3.14, True]  # Tipos misturados
  ```
- **Função Construtora `list()`**: Converte outros iteráveis (como strings, tuplas ou ranges) em listas.
  ```python
  lista_de_string = list("Python")  # ['P', 'y', 't', 'h', 'o', 'n']
  lista_de_range = list(range(5))  # [0, 1, 2, 3, 4]
  ```

A função `list()` reflete a natureza de sequência das listas, permitindo a criação a partir de qualquer objeto que possa ser iterado. Teoricamente, isso conecta as listas ao conceito mais amplo de **iteráveis** em Python, uma abstração que veremos em ação com loops mais adiante.

---

#### 2. Comprimento de uma Lista: Função `len()`
O tamanho (ou comprimento) de uma lista é obtido com a função embutida `len()`, que retorna o número de elementos presentes. Este é um conceito essencial para manipulação e iteração.

```python
numeros = [10, 20, 30, 40]
print(len(numeros))  # Saída: 4

lista_vazia = []
print(len(lista_vazia))  # Saída: 0
```

Internamente, `len()` consulta o atributo `__len__` da lista, que é mantido atualizado pelo array dinâmico subjacente. A complexidade dessa operação é O(1), já que o tamanho é armazenado como uma propriedade da estrutura, não calculado em tempo real.

---

#### 3. Acessando Elementos: Indexação e Slicing
Como mencionado na seção teórica, a indexação e o *slicing* são pilares da manipulação de listas. Vamos detalhar isso com exemplos práticos:

- **Indexação**: Acesso direto a elementos via índices positivos ou negativos.
  ```python
  frutas = ["maçã", "banana", "laranja", "uva"]
  print(frutas[0])   # Saída: "maçã" (primeiro elemento)
  print(frutas[-1])  # Saída: "uva" (último elemento)
  print(frutas[2])   # Saída: "laranja" (terceiro elemento)
  ```

  Tentativas de acessar índices fora do intervalo resultam em um erro `IndexError`.

- **Slicing**: Extração de sublistas com a sintaxe `[inicio:fim:passo]`.
  ```python
  numeros = [0, 1, 2, 3, 4, 5]
  print(numeros[1:4])    # Saída: [1, 2, 3] (do índice 1 até antes do 4)
  print(numeros[:3])     # Saída: [0, 1, 2] (do início até antes do 3)
  print(numeros[2:])     # Saída: [2, 3, 4, 5] (do 2 até o fim)
  print(numeros[::2])    # Saída: [0, 2, 4] (todos com passo 2)
  print(numeros[::-1])   # Saída: [5, 4, 3, 2, 1, 0] (inversão da lista)
  ```

O *slicing* cria uma nova lista, preservando a original, o que reforça a mutabilidade controlada das listas: você pode extrair partes sem alterar a estrutura base.

---

#### 4. Métodos Essenciais das Listas
As listas possuem métodos embutidos que permitem manipulá-las de forma eficiente. Vamos explorá-los em categorias práticas:

##### a) Adição de Elementos
- **`append(x)`**: Adiciona um elemento ao final da lista (O(1) amortizado).
  ```python
  lista = [1, 2, 3]
  lista.append(4)
  print(lista)  # Saída: [1, 2, 3, 4]
  ```
- **`insert(i, x)`**: Insere um elemento na posição `i`, deslocando os subsequentes (O(n)).
  ```python
  lista = [1, 2, 4]
  lista.insert(2, 3)  # Insere 3 na posição 2
  print(lista)  # Saída: [1, 2, 3, 4]
  ```
- **`extend(iterable)`**: Adiciona todos os elementos de um iterável ao final da lista.
  ```python
  lista = [1, 2]
  lista.extend([3, 4])
  print(lista)  # Saída: [1, 2, 3, 4]
  ```

##### b) Remoção de Elementos
- **`remove(x)`**: Remove a primeira ocorrência do valor `x` (O(n)).
  ```python
  lista = [1, 2, 3, 2]
  lista.remove(2)
  print(lista)  # Saída: [1, 3, 2]
  ```
- **`pop(i)`**: Remove e retorna o elemento no índice `i` (O(n) se não for o final; O(1) se for).
  ```python
  lista = [1, 2, 3]
  elemento = lista.pop(1)
  print(elemento)  # Saída: 2
  print(lista)     # Saída: [1, 3]
  ```
- **`clear()`**: Remove todos os elementos, esvaziando a lista (O(1)).
  ```python
  lista = [1, 2, 3]
  lista.clear()
  print(lista)  # Saída: []
  ```

##### c) Ordenação e Inversão
- **`sort()`**: Ordena a lista in-place (O(n log n), usando Timsort).
  ```python
  numeros = [3, 1, 4, 2]
  numeros.sort()
  print(numeros)  # Saída: [1, 2, 3, 4]
  ```
  Pode aceitar o parâmetro `reverse=True` para ordem decrescente.
- **`reverse()`**: Inverte a ordem dos elementos in-place (O(n)).
  ```python
  lista = [1, 2, 3]
  lista.reverse()
  print(lista)  # Saída: [3, 2, 1]
  ```

##### d) Pesquisa e Contagem
- **`index(x)`**: Retorna o índice da primeira ocorrência de `x` (O(n)).
  ```python
  lista = ["a", "b", "a"]
  print(lista.index("a"))  # Saída: 0
  ```
- **`count(x)`**: Conta quantas vezes `x` aparece na lista (O(n)).
  ```python
  lista = [1, 2, 2, 3]
  print(lista.count(2))  # Saída: 2
  ```

##### e) Cópia
- **`copy()`**: Cria uma cópia rasa (*shallow copy*) da lista (O(n)).
  ```python
  lista = [1, 2, [3, 4]]
  copia = lista.copy()
  copia[2][0] = 5
  print(lista)  # Saída: [1, 2, [5, 4]] (o original é afetado em sublistas)
  print(copia)  # Saída: [1, 2, [5, 4]]
  ```
  Isso destaca a questão das referências mencionada na seção teórica: sublistas ainda apontam para os mesmos objetos.

---

#### 5. Operações Adicionais com Listas
Além dos métodos, listas suportam operações úteis com operadores:
- **Concatenação (`+`)**: Junta duas listas, criando uma nova (O(n)).
  ```python
  a = [1, 2]
  b = [3, 4]
  c = a + b
  print(c)  # Saída: [1, 2, 3, 4]
  ```
- **Repetição (`*`)**: Repete a lista um número de vezes (O(n)).
  ```python
  lista = [1, 2]
  print(lista * 3)  # Saída: [1, 2, 1, 2, 1, 2]
  ```
- **Pertinência (`in`)**: Verifica se um elemento está na lista (O(n)).
  ```python
  lista = [1, 2, 3]
  print(2 in lista)  # Saída: True
  ```

---

#### 6. Iteração sobre Listas
A capacidade de iterar sobre listas é um dos motivos de sua importância teórica. Existem duas abordagens principais:
- **Por índices (usando `range` e `len`)**:
  ```python
  frutas = ["maçã", "banana", "uva"]
  for i in range(len(frutas)):
      print(f"Índice {i}: {frutas[i]}")
  ```
- **Diretamente sobre elementos**:
  ```python
  for fruta in frutas:
      print(fruta)
  ```

A segunda forma é mais "pythônica" e reflete a abstração de iteráveis, enquanto a primeira é útil quando precisamos dos índices.

---

#### 7. Conclusão Prática 
Com essas ferramentas, você pode criar, acessar, modificar e iterar sobre listas de maneira eficiente. Os métodos e operações apresentados equilibram flexibilidade e desempenho, como previsto pela implementação de arrays dinâmicos.

[**Atividades**](listasExe.py)