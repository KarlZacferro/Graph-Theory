def mostrar_grafo(G):
    print("\nG(V,A):\nV = [", end="")
    for v in G['V']:
        if G['V'].index(v) == len(G['V'])-1:
            print(f"{v}", end="")
            continue
        print(f"{v}, ", end="")
    print("]")
    print("A = [", end="")
    for a in G['A']:
        if G['A'].index(a) == len(G['A'])-1:
            print(f"{a}", end="")
            continue
        print(f"{a}, ", end="")
    print("]")

def carregar_grafo(G, lines):
    n = int(lines[0].split()[0])
    m = int(lines[0].split()[1])
    G['V'] = list()
    G['A'] = list()
    for v in range(1,n+1):
        G['V'].append(v)
    for i in range(1,m+1):
        a = int(lines[i].split()[0])
        b = int(lines[i].split()[1])
        G['A'].append((a,b))

def main():
    lines = list()
    G = dict()
    with open('grafo.txt', 'r') as file:
        lines = [line.strip() for line in file if line.strip()]
    carregar_grafo(G, lines)
    mostrar_grafo(G)

if __name__ == "__main__":
    main()