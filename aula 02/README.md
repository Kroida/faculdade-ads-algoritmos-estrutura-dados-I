# Por que os nomes começam com letra maiúscula?

`No` e `Lista` são classes. Em Python, é uma convenção usar nomes de classes começando com letra maiúscula, normalmente seguindo o padrão PascalCase.

---

# No.py

A classe `No` representa um nó da lista encadeada.

## Campos

- `dado`: armazena o valor do nó.
- `prox`: armazena a referência para o próximo nó. Inicialmente recebe `None`.

---

# Lista.py

A classe `Lista` representa uma lista encadeada.

## Campos

- `inicio`: armazena a referência para o primeiro nó da lista. Inicialmente recebe `None`.

## Métodos

### `add()`

Adiciona um novo nó ao final da lista, mantendo a ordem de chegada.

Primeiro, o método recebe um valor e cria um novo objeto `No` com esse valor.

- Se `inicio` for `None`, significa que a lista está vazia. O novo nó passa a ser o primeiro da lista.
- Se o primeiro nó ainda não possuir um próximo nó (`inicio.prox` for `None`), o novo nó será ligado diretamente a ele.
- Caso contrário, `aux` começa no segundo nó e percorre a lista enquanto houver um próximo nó.
- Ao chegar ao último nó, `aux.prox` recebe o novo nó.

### `imprimir()`

Percorre a lista e imprime os valores dos nós na ordem em que foram adicionados.

- Se `inicio` for `None`, a lista está vazia.
- Caso contrário, `aux` começa apontando para `inicio`.
- Enquanto `aux` possuir um nó, seu `dado` é impresso e `aux` passa a apontar para `aux.prox`.
- Quando `aux` chegar a `None`, o percurso termina.