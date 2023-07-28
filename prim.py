class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0]*self.vertices for i in range(self.vertices)]

    def adiciona_aresta(self, partida, chegada, peso):
        self.grafo[partida-1][chegada-1] = peso
        self.grafo[chegada-1][partida-1] = peso
    
    def imprime_matriz(self):
        print("\n   ", end=" ")

        for i in range(self.vertices):
            print('{:3d}'.format((i+1)), end=" ")
        print()

        for i in range(self.vertices):
            print('{:3d}'.format((i+1)), end=" ");
            for j in range(self.vertices):
                print('{:3d}'.format(self.grafo[i][j]), end=" ")
            print()

    def prim(self):
        chave = [float('inf')] * self.vertices
        arvore = [None] * self.vertices
        chave[0] = 0
        incluidos = [False] * self.vertices

        for _ in range(self.vertices):
            min_chave = float('inf')
            u = 0

            for i in range(self.vertices):
                if chave[i] < min_chave and not incluidos[i]:
                    min_chave = chave[i]
                    u = i

            incluidos[u] = True

            for v in range(self.vertices):
                if self.grafo[u][v] > 0 and not incluidos[v] and self.grafo[u][v] < chave[v]:
                    chave[v] = self.grafo[u][v]
                    arvore[v] = u

        agm = []
        for i in range(1, self.vertices):
            agm.append((arvore[i]+1, i+1, self.grafo[i][arvore[i]]))

        return agm

    def imprime_agm(self, agm):
        print("Árvore Geradora Mínima (Algoritmo de Prim):")
        for aresta in agm:
            print(f"{aresta[0]} -> {aresta[1]} (Peso {aresta[2]})")

v = int(input("Digite a quantidade de vértices: "))

if (v > 20 or v <= 0):
    print("\nDigite um numero inteiro positivo que não ultrapasse 20 posicoes!")
    exit(0)
else:
    g = Grafo(v)
    
opcao = 0

while (opcao != 4):
    print("__________________________________________")
    print("\n1 - Adicione uma nova aresta")
    print("2 - Imprima a matriz")
    print("3 - Encontre a Árvore Geradora Mínima (Algoritmo de Prim)")
    print("4 - Sair")
    opcao = int(input("Digite a opcao que deseja: "))
    print("__________________________________________")

    if opcao == 1:
        vertice_partida = int(input("\nQual vértice será a partida? (1-" + str(g.vertices) + "): "))
        vertice_chegada = int(input("Qual vértice será a chegada? (1-" + str(g.vertices) + "): "))
        if (vertice_partida <= 0 or vertice_chegada > g.vertices) or (vertice_chegada <= 0 or vertice_chegada > g.vertices):
            print("Vértice(s) incorretos!")
        else:
            peso = int(input("Qual é o peso desta aresta?: "))
            g.adiciona_aresta(vertice_partida, vertice_chegada, peso)

    elif opcao == 2:
        g.imprime_matriz()

    elif opcao == 3:
        agm = g.prim()
        g.imprime_agm(agm)

    elif opcao == 4:
        print("Saindo...")

    else:
        print("Opção inválida. Tente novamente!")
