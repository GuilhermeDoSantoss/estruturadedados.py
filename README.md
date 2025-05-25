# Estruturas de Dados Fundamentais em Python

Este repositório apresenta um resumo técnico das estruturas de dados mais importantes utilizadas em ciência da computação, com foco em suas implementações e complexidades em Python.
O objetivo é oferecer uma referência clara e objetiva para estudantes e profissionais que desejam reforçar seus conhecimentos sobre Arrays, Hashmaps e Listas Ligadas (Linked Lists).


## 📚 Estruturas de Dados

### 📌 Array

- **Definição:** Estrutura linear que utiliza um espaço contíguo na memória, armazenando elementos sequencialmente.
  
- **Exemplo:** `[0, 3, 4, 5, 7, 1]`
  
- **Vantagens:**
  
  - Acesso por índice é muito rápido: **O(1)**
  
- **Desvantagens:**
  
  - Inserções/remoções no meio são custosas: **O(n)**, pois exigem deslocamento de elementos
  
  - Pode haver necessidade de realocação de memória

### 📌 Hashmap (Dicionário em Python)

- **Definição:** Estrutura que armazena pares chave/valor, com alta eficiência de acesso.
- **Operações principais:**
  - Inserção, remoção e busca geralmente em **O(1)** (tempo constante)
  - No pior caso, pode chegar a **O(n)** devido a colisões (múltiplas chaves no mesmo compartimento)

### 📌 Linked List (Lista Ligada)

- **Definição:** Estrutura onde cada nó aponta para o próximo, formando uma sequência encadeada.

- **Componentes principais:** `head` (início da lista), `tail` (fim da lista)
  
- **Vantagens:**
  
  - Inserção/remoção no início é eficiente: **O(1)**
    
- **Desvantagens:**
  
  - Acesso a elementos específicos é lento: **O(n)**
    
  - Inserções/remoções no meio ou fim também são **O(n)**, pois é necessário percorrer a lista

## 🔧 Tecnologias Utilizadas

- Python 3.x
- JavaScript


## 🧠 Objetivo

Servir como base de estudo para compreensão das principais estruturas de dados utilizadas no desenvolvimento de algoritmos e sistemas eficientes.

