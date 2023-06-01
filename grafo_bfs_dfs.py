def mostrar_grafo(G):
    print("\nVetor de Adjacência: ")
    for v in G:
        print(f"{v}: ", end="")
        for k in G[v]:
            print(f"{k} ", end="")
        print()

def mostrar_lista(lista, texto):
    print(texto)
    for item in lista:
        print(f"{item}", end="")
    print()


def gerar_grafo(G, lines):
    n = int(lines[0].split()[0])
    m = int(lines[0].split()[1])
    for v in range(1, n+1):
        G[v] = []
    i = 1
    while i <= m:
        a = int(lines[i].split()[0])
        b = int(lines[i].split()[1])
        G[a].append(b)
        G[b].append(a)
        i += 1


def bfs(G, raiz):
    arvore, queue = [], []
    # Desmarcando todos os vértices
    verts = {}.fromkeys(list(G.keys()), 0)
    while verts:
        queue.append(raiz)
        verts[raiz] = 1
        while queue:
            v = queue[0]
            for w in G[v]:
                if w in verts and verts[w] == 0:
                    queue.append(w)
                    verts[w] = 1    # Descoberto
                    # Árvore Geradora a partir da BFS
                    arvore.append((v,w))
            queue.remove(v)
            verts[v] = 1    # Explorado
        lista = []
        for k in verts:
            if verts[k] == 1:
                lista.append(k)
        for i in lista:
            verts.pop(i)
        if verts:
            raiz = min(verts.keys())
    return arvore


def dfs(G, raiz):
    pilha = []
    verts = {}.fromkeys(list(G.keys()), 0)

    def dfs_i(G, v):
        verts[v] = 1
        pilha.append(v)
        while pilha:
            v = pilha.pop()
            for u in G[v]:
                if u in verts.keys() and verts[u] == 0:
                    verts[u] = 1
                    pilha.append(u)
    while verts:
        dfs_i(G, raiz)
        print(verts)
        lista = list(verts.keys())
        for k in lista:
            if k in verts.keys() and verts[k] == 1:
                    verts.pop(k)
        if verts:
            raiz = min(verts.keys())


def contar_comp(G):
    cont = 0
    pilha = []
    verts = {}.fromkeys(list(G.keys()), 0)

    def dfs_i(G, v):
        verts[v] = 1
        pilha.append(v)
        while pilha:
            v = pilha.pop()
            for u in G[v]:
                if u in verts.keys() and verts[u] == 0:
                    verts[u] = 1
                    pilha.append(u)
    while verts:
        raiz = min(verts.keys())
        dfs_i(G, raiz)
        print(verts)
        lista = list(verts.keys())
        for k in lista:
            if k in verts.keys() and verts[k] == 1:
                    verts.pop(k)
        cont += 1
    return cont


def menu():
    while True:
        print("==============================")
        print("======= MENU PRINCIPAL =======")
        print("==============================")
        print("1. Mostrar Lista de Adjacência")
        print("2. Executar BFS")
        print("3. Executar DFS")
        print("4. Contar Componentes Conexas")
        print("5. Mostrar Componentes Conexas")
        print("0. Sair")
        try:
            op = int(input("Informe a opção: "))
        except:
            print("================\nOpção inválida!!\n================")
            op = 99
        if 0 > op or op > 5:
            continue
        return op


def main():
    lines = list()
    G = dict()
    with open('grafo5.txt', 'r') as file:
        lines = [line.strip() for line in file if line.strip()]
        file.close()
    gerar_grafo(G, lines)
    while True:
        op = menu()
        if op == 1:
            mostrar_grafo(G)
        elif op == 2:
            while True:
                print("=======================")
                print("Para sair, informe ZERO")
                raiz = int(input("Informe a raiz...: "))
                if raiz == 0:
                    break
                if raiz in G.keys():
                    mostrar_lista(bfs(G, raiz), "Árvore Geradora: ")
        elif op == 3:
            while True:
                print("=======================")
                print("Para sair, informe ZERO")
                raiz = int(input("Informe a raiz...: "))
                if raiz == 0:
                    break
                if raiz in G.keys():
                    dfs(G, raiz)
            pass
        elif op == 4:
            k = contar_comp(G)
            print(f"Componentes conexas: {k}")
        elif op == 5:
            pass
            #mostrar_cc(G)
        elif op == 0:
            break


if __name__ == "__main__":
    main()