from queue import deque
from collections import deque

q = Queque()

q.put(1)
q.put(2)
q.put(3)

print(q.get())
print(q.get())




'''
Uma Queue (Fila) em Python é uma estrutura de dados linear do tipo FIFO (First-In, First-Out), ou seja, o primeiro elemento inserido é o primeiro a ser removido. Filas são amplamente utilizadas em algoritmos, sistemas operacionais, processamento de tarefas e gerenciamento de recursos.

Características principais:

Inserção (enqueue) ocorre no final da fila.
Remoção (dequeue) ocorre no início da fila.
Útil para processamento sequencial, buffers, impressão, etc.
Implementação básica de uma fila em Python usando listas:

fila = []
# Inserir elementos (enqueue)
fila.append('A')
fila.append('B')
fila.append('C')

# Remover elementos (dequeue)
primeiro = fila.pop(0)  # Remove 'A'

Limitação: Usar listas pode ser ineficiente para grandes filas, pois pop(0) é O(n).

Implementação eficiente com collections.deque:

from collections import deque

fila = deque()
fila.append('A')
fila.append('B')
fila.append('C')
print(fila)  # deque(['A', 'B', 'C'])

primeiro = fila.popleft()  # Remove 'A'
print(primeiro)  # 'A'
print(fila)     

Métodos principais:

append(x): insere no final.
popleft(): remove do início.
len(fila): retorna o tamanho da fila.
Exemplo de implementação de uma fila personalizada:

 class Queue:
    def __init__(self):
        self.items = deque()
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        if not self.is_empty():
            return self.items.popleft()
        raise IndexError("Fila vazia")
    def is_empty(self):
        return len(self.items) == 0
    def size(self):
        return len(self.items)

# Exemplo de uso:
q = Queue()
q.enqueue(10)
q.enqueue(20)
print(q.dequeue())  # 10
print(q.size())   

Resumo:

Fila é FIFO.
Ideal usar deque para eficiência.
Muito utilizada em algoritmos e sistemas. 

''' # 1# deque(['B', 'C'])