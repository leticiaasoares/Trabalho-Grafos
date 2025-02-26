# Grupo 10
# Intergrantes: CAIO CÉZAR MIRANDA CARVALHO, LETÍCIA DE OLIVEIRA SOARES, MATHEUS MONTEIRO HUEBRA PERDIGÃO

import sys
sys.setrecursionlimit(10**6)  # Para evitar limites de recursão em grandes grafos

def dfs(x):
    for v in lista[x]:
        if componente[v] == -1:  # Verifica se ainda não foi visitado
            componente[v] = componente[x]
            dfs(v)

# Leitura da entrada
def main():
    global lista, componente, n, m
    n, m = map(int, input().split())

    # Inicializando as estruturas
    componente = [-1] * (n + 1)
    lista = [[] for _ in range(n + 1)]

    # Construção do grafo
    for _ in range(m):
        a, b = map(int, input().split())
        lista[a].append(b)
        lista[b].append(a)

    # Contagem de componentes conexos
    numero_componentes = 0
    for i in range(1, n + 1):
        if componente[i] == -1:  # Verifica se ainda não há componentes
            numero_componentes += 1
            componente[i] = numero_componentes
            dfs(i)

    # Exibe o resultado
    print(numero_componentes)

if __name__ == "__main__":
    main()
