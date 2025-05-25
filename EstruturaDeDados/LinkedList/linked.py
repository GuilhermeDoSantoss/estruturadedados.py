'''

Uma Linked List (Lista Ligada) em Python é uma estrutura de dados linear composta por nós, onde cada nó armazena um valor e uma referência (ponteiro) para o próximo nó da sequência. Diferente de arrays, as listas ligadas não armazenam elementos em posições contíguas de memória, o que facilita inserções e remoções em tempo constante (O(1)), desde que se tenha a referência ao nó anterior.

Principais características:

Dinâmica: cresce e diminui conforme necessário.
Não possui acesso direto por índice (acesso sequencial).
Ideal para cenários com muitas inserções/remoções no início/meio da lista.
Exemplo de implementação de uma Linked List simples em Python:

class Node:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class LinkedList:
    def __init__(self):
        self.cabeca = None

    def inserir_no_inicio(self, valor):
        novo_no = Node(valor)
        novo_no.proximo = self.cabeca
        self.cabeca = novo_no

    def inserir_no_fim(self, valor):
        novo_no = Node(valor)
        if not self.cabeca:
            self.cabeca = novo_no
            return
        atual = self.cabeca
        while atual.proximo:
            atual = atual.proximo
        atual.proximo = novo_no

    def remover(self, valor):
        atual = self.cabeca
        anterior = None
        while atual and atual.valor != valor:
            anterior = atual
            atual = atual.proximo
        if not atual:
            return  # Valor não encontrado
        if not anterior:
            self.cabeca = atual.proximo
        else:
            anterior.proximo = atual.proximo

    def exibir(self):
        atual = self.cabeca
        while atual:
            print(atual.valor, end=" -> ")
            atual = atual.proximo
        print("None")

# Exemplo de uso:
lista = LinkedList()
lista.inserir_no_inicio(3)
lista.inserir_no_inicio(2)
lista.inserir_no_fim(4)
lista.exibir()  # Saída: 2 -> 3 -> 4 -> None
lista.remover(3)
lista.exibir()  # Saída: 2 -> 4 -> None

Resumo dos métodos:

inserir_no_inicio: insere elemento no início.
inserir_no_fim: insere elemento no final.
remover: remove o primeiro nó com o valor especificado.
exibir: imprime todos os elementos da lista.
Vantagens:

Inserção/remoção eficiente no início.
Estrutura flexível.
Desvantagens:

Acesso sequencial (não é eficiente para busca por índice).
Consome mais memória devido aos ponteiros.

'''