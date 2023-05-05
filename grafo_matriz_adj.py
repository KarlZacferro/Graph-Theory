def mostrar_lista(lista_adj):
    print("\nVetor de Adjacência: ")
    for v in lista_adj:
        print(f"{v}: ", end="")
        for k in lista_adj[v]:
            print(f"{k} ", end="")
        print()


def carregar_matriz(matriz_adj, lines):
    n = int(lines[0].split()[0])
    m = int(lines[0].split()[1])
    for i in range(n):
        matriz_adj.append([0] * n)
    k = 1
    while k <= m:
        a = int(lines[k].split()[0])
        b = int(lines[k].split()[1])
        matriz_adj[a-1][b-1] = 1
        matriz_adj[b - 1][a - 1] = 1
        k += 1
    for linha in matriz_adj:
        print(linha)


def main():
    lines = list()
    matriz_adj = list()
    with open('grafo.txt', 'r') as file:
        lines = [line.strip() for line in file if line.strip()]
    print(lines)
    carregar_matriz(matriz_adj, lines)

if __name__ == "__main__":
    main()