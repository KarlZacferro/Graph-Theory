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


def gerar_digrafo(D, lines):
    n = int(lines[0].split()[0])
    m = int(lines[0].split()[1])
    for v in range(n):
        D[v] = []
    i = 1
    while i <= m:
        a = int(lines[i].split()[0])
        b = int(lines[i].split()[1])
        D[a].append(b)
        i += 1


def ord_topologica(D):
    ordem = []
    de = [0] * len(D.keys())
    for v in D.keys():
        for w in D[v]:
            de[w] += 1
    fila = []
    for i, grau in enumerate(de):
        if grau == 0:
            fila.append(i)
    while fila:
        v = fila.pop(0)
        ordem.append(v)
        for w in D[v]:
            de[w] -= 1
            if de[w] == 0:
                fila.append(w)
    print(ordem)


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
        print("6. Mostrar Ordenação Topológica")
        print("0. Sair")
        try:
            op = int(input("Informe a opção: "))
        except:
            print("================\nOpção inválida!!\n================")
            op = 99
        if 0 > op or op > 6:
            continue
        return op


def main():
    lines = list()
    D = dict()
    with open('grafo5.txt', 'r') as file:
        lines = [line.strip() for line in file if line.strip()]
        file.close()
    gerar_digrafo(D, lines)
    while True:
        op = menu()
        if op == 1:
            mostrar_grafo(D)
            input("Tecle ENTER para continuar...")
        elif op == 2:
            while True:
                print("=======================")
                print("Para sair, informe ZERO")
                raiz = int(input("Informe a raiz...: "))
                if raiz == 0:
                    break
                if raiz in D.keys():
                    #mostrar_lista(bfs(D, raiz), "Árvore Geradora: ")
                    pass
        elif op == 3:
            while True:
                print("=======================")
                print("Para sair, informe ZERO")
                raiz = int(input("Informe a raiz...: "))
                if raiz == 0:
                    break
                if raiz in D.keys():
                    #dfs(D, raiz)
                    pass
            pass
        elif op == 4:
            #k = contar_comp(G)
            #print(f"Componentes conexas: {k}")
            pass
        elif op == 5:
            pass
            #mostrar_cc(G)
        elif op == 6:
            ord_topologica(D)
            input("Tecle ENTER para continuar...")
        elif op == 0:
            break


if __name__ == "__main__":
    main()