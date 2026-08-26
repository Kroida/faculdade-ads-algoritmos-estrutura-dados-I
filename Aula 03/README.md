# Por que os nomes começam com letra maiúscula?

`No` e `Lista` são classes. Em Python, é uma convenção usar nomes de classes começando com letra maiúscula, normalmente seguindo o padrão PascalCase.

---

# No.py

A classe `No` representa um nó da lista encadeada.

## Campos

* `dado`: armazena o valor do nó.


* `prox`: armazena a referência para o próximo nó. Inicialmente recebe `None`.



---

# Lista.py

A classe `Lista` representa uma lista encadeada.

## Campos

* `inicio`: armazena a referência para o primeiro nó da lista. Inicialmente recebe `None`.



## Métodos

### `add()`

Adiciona um novo nó ao final da lista, mantendo a ordem de chegada.

Primeiro, o método recebe um valor e cria um novo objeto `No` com esse valor.

* Se `inicio` for `None`, significa que a lista está vazia. O novo nó passa a ser o primeiro da lista.


* Se o primeiro nó ainda não possuir um próximo nó (`inicio.prox` for `None`), o novo nó será ligado diretamente a ele.


* Caso contrário, `aux` começa no segundo nó e percorre a lista enquanto houver um próximo nó.


* Ao chegar ao último nó, `aux.prox` recebe o novo nó.



### `imprimir()`

Percorre a lista e imprime os valores dos nós na ordem em que foram adicionados.

* Se `inicio` for `None`, a lista está vazia.


* Caso contrário, `aux` começa apontando para `inicio`.


* Enquanto `aux` possuir um nó, seu `dado` é impresso e `aux` passa a apontar para `aux.prox`.


* Quando `aux` chegar a `None`, o percurso termina.



### `remover()`

Busca e remove um nó específico da lista a partir do seu valor.

* Primeiramente, verifica se `inicio` é `None`; caso seja, avisa que "A lista está vazia".


* Se o item a ser removido for o primeiro da lista (`inicio.dado == valor`), a variável `inicio` passa a apontar para o próximo nó (`inicio.prox`) e o nó original é deletado da memória.


* Caso o valor não esteja no primeiro nó, o método usa duas variáveis para percorrer a lista: `ant` (nó anterior) e `aux` (nó atual).


* Enquanto percorre a lista, se encontrar o nó com o valor desejado (`aux.dado == valor`), o ponteiro do nó anterior é redirecionado para o próximo nó (`ant.prox = aux.prox`), o nó atual é deletado e o loop é encerrado.


* Ao final da execução, caso a remoção tenha sido feita, imprime "Item ( valor ) removido com sucesso!". Se o valor não existir em nenhum nó da lista, imprime "Item ( valor ) não encontrado!".