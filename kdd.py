import time

# Cria uma variável do tipo lista
lista_palavras = []

# Lê o conteúdo do arquivo "txt" linha a linha
with open("txt", "r") as arquivo:
    for linha in arquivo:
        # Separa cada linha em palavras
        palavras = linha.split()
        # Adiciona as palavras à lista
        lista_palavras.extend(palavras)

# --- Bubble Sort ---
inicio_bubble = time.time()
n = len(lista_palavras)
for i in range(n):
    for j in range(0, n - i - 1):
        if lista_palavras[j] > lista_palavras[j + 1]:
            lista_palavras[j], lista_palavras[j + 1] = lista_palavras[j + 1], lista_palavras[j]
fim_bubble = time.time()
tempo_bubble = fim_bubble - inicio_bubble
print(f"Bubble Sort: {lista_palavras}")
print(f"Tempo de execução do Bubble Sort: {tempo_bubble:.6f} segundos")

# --- Selection Sort ---
inicio_selection = time.time()
n = len(lista_palavras)
for i in range(n):
    min_idx = i
    for j in range(i + 1, n):
        if lista_palavras[min_idx] > lista_palavras[j]:
            min_idx = j
    lista_palavras[i], lista_palavras[min_idx] = lista_palavras[min_idx], lista_palavras[i]
fim_selection = time.time()
tempo_selection = fim_selection - inicio_selection
print(f"Selection Sort: {lista_palavras}")
print(f"Tempo de execução do Selection Sort: {tempo_selection:.6f} segundos")

# --- Sort nativo do Python ---
inicio_sort = time.time()
lista_palavras.sort()
fim_sort = time.time()
tempo_sort = fim_sort - inicio_sort
print(f"Sort nativo: {lista_palavras}")
print(f"Tempo de execução do Sort nativo: {tempo_sort:.6f} segundos")

# --- Escolha o algoritmo de melhor performance e remova os outros ---
# ... (Escreva o código para escolher o algoritmo mais rápido e remover os outros)

# --- Crie um novo arquivo txt com as palavras ordenadas ---
with open("palavras_ordenadas.txt", "w") as arquivo:
    for palavra in lista_palavras:
        arquivo.write(palavra + " ")
