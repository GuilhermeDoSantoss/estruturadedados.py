'''
Um HashMap (ou tabela hash) em Python é uma estrutura de dados que armazena pares chave-valor, permitindo acesso, inserção e remoção eficientes (em média O(1)). Em Python, o tipo nativo dict implementa um hashmap.

Características principais:

Chaves são únicas e imutáveis (strings, números, tuplas imutáveis, etc.).
Valores podem ser de qualquer tipo.
Operações principais: inserção, busca, remoção e iteração.
Exemplo básico de uso:
'''
# Criação de um dicionário (hashmap)
alunos = {'Ana': 8.5, 'Bruno': 7.0, 'Carla': 9.2}

# Inserção/atualização
alunos['Daniel'] = 6.8

# Acesso
print(alunos['Ana'])  # 8.5

# Remoção
del alunos['Bruno']

# Verificação de existência
if 'Carla' in alunos:
    print('Carla está na lista')

# Iteração
for nome, nota in alunos.items():
    print(f'{nome}: {nota}')

'''
Principais métodos:

dict.get(chave, valor_padrao): busca segura.
dict.keys(), dict.values(), dict.items(): iteração sobre chaves, valores ou ambos.
dict.pop(chave): remove e retorna o valor da chave.
Exemplo prático:
'''
# Contando ocorrências de palavras
texto = "python é poderoso e python é fácil"
contagem = {}
for palavra in texto.split():
    contagem[palavra] = contagem.get(palavra, 0) + 1
print(contagem)  # {'python': 2, 'é': 2, 'poderoso': 1, 'fácil': 1}

'''
Resumo:

HashMap (dict) é essencial para buscas rápidas por chave.
Muito usado em algoritmos, contagem, indexação e armazenamento de dados relacionais.
Em Python, é seguro, eficiente e fácil de usar.
'''