## 🔁 Estruturas de Controle em Python

As estruturas de controle são fundamentais para criar fluxos lógicos em qualquer programa. Elas permitem que você **tome decisões** e **repita ações** com base em condições específicas. São os blocos essenciais para dar inteligência ao seu código!

### ✅ Condicionais: if, elif, else

As estruturas condicionais são utilizadas para executar diferentes blocos de código dependendo de uma condição booleana (verdadeira ou falsa).

#### if

```python
x = 10
if x > 5:
    print("x é maior que 5")
```

#### if...else

```python
x = 3
if x > 5:
    print("x é maior que 5")
else:
    print("x é menor ou igual a 5")
```

#### if...elif...else

O `elif` significa "senão se" (else if). Ele permite testar múltiplas condições:

```python
x = 5
if x > 10:
    print("Maior que 10")
elif x == 5:
    print("Igual a 5")
else:
    print("Outro valor")
```

Você pode usar quantos `elif` quiser para cobrir diversos cenários.

#### 🌟 Por que usar condicionais?

As estruturas condicionais são essenciais para:
- Tomar decisões com base em dados do usuário ou do sistema.
- Criar caminhos diferentes no código, como menus e respostas personalizadas.
- Implementar validações, autenticação, lógica de jogos, entre outros.

---

### 🔁 Estruturas de Repetição: while e for

#### while

O `while` repete um bloco de código **enquanto** uma condição for verdadeira:

```python
contador = 0
while contador < 3:
    print("Contador:", contador)
    contador += 1
```

Cuidado com loops infinitos! Sempre garanta que a condição pode se tornar falsa.

#### for

O `for` percorre itens de uma sequência (como listas, strings ou intervalos):

```python
for letra in "Python":
    print(letra)
```

Com `range()` podemos gerar sequências numéricas:

```python
for i in range(5):
    print(i)  # Vai de 0 a 4
```

---

### ⛔ Comandos de Controle de Loop

#### break
Encerra o loop imediatamente:
```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

#### continue
Pula para a próxima iteração:
```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

#### pass
Indica um bloco vazio (útil como "placeholder"):
```python
if True:
    pass  # ainda vou escrever aqui
```

---

### 🧠 Por que as Estruturas de Controle são importantes?

Elas permitem:
- Criar **fluxos inteligentes** e adaptáveis no código.
- Automatizar tarefas repetitivas (loops).
- Controlar o **comportamento de programas** baseando-se em condições reais.
- Tornar o código mais **legível e modular**.

Seja para checar uma senha, rodar um jogo, varrer uma lista ou tomar decisões em IA, estruturas de controle são a base de toda lógica computacional!

[Atividades](estrutura_of_controle.py)