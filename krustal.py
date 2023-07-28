class Aresta:
    def __init__(self, origem, destino, peso):
        self.origem = origem
        self.destino = destino
        self.peso = peso

class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0]*self.vertices for i in range(self.vertices)]
        self.arestas = []

    def adiciona_aresta(self, partida, chegada, peso):
        self.grafo[partida-1][chegada-1] = peso
        self.grafo[chegada-1][partida-1] = peso
        self.arestas.append(Aresta(partida, chegada, peso))
    
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

    def encontra_subconjunto(self, subconjuntos, vertice):
        if subconjuntos[vertice] == vertice:
            return vertice
        return self.encontra_subconjunto(subconjuntos, subconjuntos[vertice])

    def unir_subconjuntos(self, subconjuntos, vertice_origem, vertice_destino):
        vertice_origem_raiz = self.encontra_subconjunto(subconjuntos, vertice_origem)
        vertice_destino_raiz = self.encontra_subconjunto(subconjuntos, vertice_destino)
        subconjuntos[vertice_destino_raiz] = vertice_origem_raiz

    def kruskal(self):
        agm = []
        self.arestas = sorted(self.arestas, key=lambda aresta: aresta.peso)

        subconjuntos = [i for i in range(self.vertices)]

        for aresta in self.arestas:
            vertice_origem = aresta.origem - 1
            vertice_destino = aresta.destino - 1

            if self.encontra_subconjunto(subconjuntos, vertice_origem) != self.encontra_subconjunto(subconjuntos, vertice_destino):
                agm.append(aresta)
                self.unir_subconjuntos(subconjuntos, vertice_origem, vertice_destino)

        return agm

    def imprime_agm(self, agm):
        print("Árvore Geradora Mínima (Algoritmo de Kruskal):")
        for aresta in agm:
            print(f"{aresta.origem} -- {aresta.destino} : peso({aresta.peso})")

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
    print("3 - Encontre a Árvore Geradora Mínima (Algoritmo de Kruskal)")
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
        agm = g.kruskal()
        g.imprime_agm(agm)

    elif opcao == 4:
        print("Saindo...")

    else:
        print("Opção inválida. Tente novamente!")
