## 👉 Funções e Escopo de Variáveis em Python

Em Python, **funções** são blocos de código reutilizáveis que executam uma tarefa específica. Elas ajudam a organizar o programa, evitar repetição de código e facilitam testes e manutenção.

### 💪 Criando uma função

A palavra-chave `def` é usada para definir uma função:

```python
def saudacao():
    print("Olá, seja bem-vindo!")
```

Para chamar a função:

```python
saudacao()  # Executa a função
```

### 📥 Funções com parâmetros

Funções podem receber valores (chamados **parâmetros**) para trabalhar com diferentes dados:

```python
def saudacao(nome):
    print(f"Olá, {nome}!")

saudacao("Alice")
saudacao("Bob")
```

### 🔁 Funções com retorno

Funções podem retornar um valor usando `return`:

```python
def soma(a, b):
    return a + b

resultado = soma(5, 3)
print(resultado)  # Saída: 8
```

---

## 🎯 Escopo de Variáveis

O **escopo** determina onde uma variável pode ser usada. Existem dois tipos principais:

### 1. 📦 Escopo Local

Variáveis declaradas **dentro** de uma função só existem **dentro daquela função**:

```python
def minha_funcao():
    mensagem = "Olá"  # variável local
    print(mensagem)

minha_funcao()
# print(mensagem)  # Isso dá erro! 'mensagem' não existe fora da função
```

### 2. 🌍 Escopo Global

Variáveis criadas **fora de funções** podem ser acessadas por **todo o código**:

```python
mensagem = "Oi, mundo!"

def mostrar_mensagem():
    print(mensagem)  # Acessando variável global

mostrar_mensagem()
```

### ⚠️ Usando `global`

Se quiser **modificar** uma variável global dentro de uma função, use `global`:

```python
contador = 0

def incrementar():
    global contador
    contador += 1

incrementar()
print(contador)  # Saída: 1
```

> 🧐 **Dica**: Use variáveis globais com cuidado! Prefira passar e retornar valores nas funções para evitar confusão.

---

## ✨ Vantagens de Usar Funções

- **Organização**: Divide o programa em partes menores e compreensíveis.
- **Reutilização**: Evita repetir código.
- **Facilidade para testar**: Permite testar partes individuais do código.
- **Legibilidade**: O nome da função ajuda a entender o que ela faz.

---



## 🧠 Argumentos Nomeados, Padrões (Default) e Funções Aninhadas

### 🔸 Argumentos Nomeados e Padrões (Default)

Em Python, é possível definir **valores padrão** para os parâmetros de uma função. Esses valores são usados quando o argumento correspondente não é fornecido na chamada da função. Esse recurso torna as funções mais flexíveis e fáceis de usar.

#### ✅ Exemplo básico:
```python
def saudacao(nome, mensagem="Olá"):
    print(f"{mensagem}, {nome}!")

saudacao("Carlos")               # Usa o valor padrão "Olá"
saudacao("Joana", "Bem-vinda")  # Substitui o valor padrão
```

### 📌 Vantagens dos parâmetros com valores padrão:
- Permite que funções sejam chamadas com menos argumentos.
- Facilita o uso de argumentos opcionais.
- Melhora a legibilidade e a manutenibilidade do código.

> 🧠 Lembre-se: os parâmetros com valores padrão **devem vir após os parâmetros obrigatórios** na definição da função.

```python
def exemplo(a, b=10):  # OK
    pass

def exemplo_invalido(a=10, b):  # Erro de sintaxe
    pass
```

### 🔹 Argumentos Nomeados

Ao chamar uma função, você pode especificar os argumentos usando seus **nomes**, o que permite mudar a ordem dos argumentos e aumenta a clareza do código.

```python
def cadastrar_usuario(nome, idade, cidade):
    print(f"{nome} tem {idade} anos e mora em {cidade}.")

cadastrar_usuario("Ana", 28, "Recife")
cadastrar_usuario(cidade="Curitiba", nome="João", idade=32)  # Ordem diferente
```

### 🎯 Importância
- Argumentos nomeados são extremamente úteis em funções com muitos parâmetros.
- Evitam erros causados pela ordem incorreta de argumentos.
- Deixam o propósito de cada argumento mais claro.

---

## 🔁 Funções Aninhadas (Nested Functions)

Em Python, é possível definir funções dentro de outras funções. Essas são chamadas de **funções aninhadas**. Elas são úteis para **encapsular** lógica que só faz sentido dentro de uma função maior.

### ✅ Exemplo:
```python
def saudacao_com_horario(nome):
    def mensagem():
        from datetime import datetime
        hora = datetime.now().hour
        if hora < 12:
            return "Bom dia"
        elif hora < 18:
            return "Boa tarde"
        else:
            return "Boa noite"

    print(f"{mensagem()}, {nome}!")
```

### 🧠 Por que usar funções aninhadas?
- Organização: Agrupa funções relacionadas dentro de um contexto.
- Escopo restrito: Funções internas não são acessíveis fora da função externa.
- Criação de **closures**: Quando a função interna "lembra" valores do escopo externo.

### 🔒 Escopo e `nonlocal`
Funções aninhadas têm acesso às variáveis do escopo da função externa, mas **não podem modificá-las diretamente** sem a palavra-chave `nonlocal`.

```python
def contador():
    total = 0

    def incrementa():
        nonlocal total
        total += 1
        return total

    return incrementa

cont = contador()
print(cont())  # 1
print(cont())  # 2
```

### 🎯 Conclusão
- Funções aninhadas ajudam na modularização e clareza do código.
- São amplamente utilizadas em programação funcional (como closures e decorators).
- Entender o escopo é essencial para evitar bugs e tornar seu código mais robusto.

---
[Atividades](funcoes.py)







