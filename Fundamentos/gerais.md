## 🫠 Por quê Python?
Python é uma linguagem interpletada, por isso você pode economizar um tempo considerável durante o desenvolvimento, uma vez que não há necessidade de compilação e ligação(linking). O interpretador pode ser usado interativamente, o que torna fácil experimentar diversas características da linguagem, escrever programas "descartáveis", ou testar funções em um desenvolvimento debaixo pra cima(bottom-up). É também uma útil calculadora de mesa.

Python permite a escrita de programas compactos e legíveis. Programas escritos em Python são tipicamente mais curtos do que seus equivalentes em C, C++ ou Java, por diversas razões:
    - Os tipos de alto nível permitem que você expresse operações complexas em um único comando;
    - A definição de bloco é feita por indentação ao invés de marcadores de início e fim de bloco;
    -Não há necessidade de declaração de variáveis ou parâmetros formais.

Python foi desenvolvida para ser descomplicada e ao mesmo tempo suprir necessidades de resolução de problemas computacionais com facilidade e eficiência. Aqui cabe facilmente a pergunta: - E por quê fazer as coisas da forma mais difícil se existem ferramentas para torná-las mais fáceis?

Existe até mesmo uma piada interna do pessoal que programa em Python que diz:

“- A vida é curta demais para programar em outra linguagem de programação, senão em Python.“

Como exemplo veja três situações, um simples programa que exibe em tela a mensagem “Olá Mundo!!!” escrito em C, em JAVA, e por fim em Python.

<mark>Hello World!!! em C</mark>

```c
#include <stdio.h>
int main(void) {
    printf("Hello World\n");
    return 0;
}
```
<mark style="background:red; color:white;">Hello World!!! em Java</mark>
```j
class Main {
    public static void main(String[] args) {
        System.out.println("Hello World");
    }
}
```

<mark style="background:blue; color:white;">Hello World!!! em Python</mark>
```p
print("Hello World!")
```
Em todos os exemplos acima o retorno será uma mensagem exibida em tela para o usuário dizendo: Hello World!!!  (*Garanto que agora a piada sobre outras linguagens fez sentido...)

[Próximo Tópico](TiposDados/tiposDados.md) 