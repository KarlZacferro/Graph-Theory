def mostrar_lista(vetor_adj):
    print("\nVetor de Adjacência: ")
    for v in vetor_adj:
        print(f"{v}: ", end="")
        for k in vetor_adj[v]:
            print(f"{k} ", end="")
        print()

def carregar_lista(vetor_adj, lines):
    n = int(lines[0].split()[0])
    m = int(lines[0].split()[1])
    for v in range(1, n+1):
        vetor_adj[v] = []
    i = 1
    while i <= m:
        a = int(lines[i].split()[0])
        b = int(lines[i].split()[1])
        vetor_adj[a].append(b)
        vetor_adj[b].append(a)
        i += 1

def main():
    lines = list()
    vetor_adj = dict()
    with open('grafo.txt', 'r') as file:
        lines = [line.strip() for line in file if line.strip()]
    carregar_lista(vetor_adj, lines)
    mostrar_lista(vetor_adj)

if __name__ == "__main__":
    main()