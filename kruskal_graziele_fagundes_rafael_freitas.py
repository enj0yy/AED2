# Graziele Fagundes e Rafael Freitas - M1

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
        self.grafo[partida][chegada] = peso
        self.grafo[chegada][partida] = peso
        self.arestas.append(Aresta(partida, chegada, peso))
    
    def imprime_matriz(self):
        print("\n   ", end=" ")

        for i in range(self.vertices):
            print('{:3d}'.format((i)), end=" ")
        print()

        for i in range(self.vertices):
            print('{:3d}'.format((i)), end=" ");
            for j in range(self.vertices):
                print('{:3d}'.format(self.grafo[i][j]), end=" ")
            print()

    # Encontra vértice raiz do subconjunto de um dado vertice
    # Indice = Vertice
    # Subconjuntos[Indice] = Vertice do mesmo subconjunto
    # Vertice == Vertice do mesmo subconjunto: Raiz do subconjunto
    def encontra_raiz_subconjunto(self, subconjuntos, vertice):
        if subconjuntos[vertice] == vertice:                
            return vertice
        else: 
            raiz = subconjuntos[vertice]
            while subconjuntos[raiz] != raiz:
                raiz = subconjuntos[raiz]
            return raiz

    # Une dois subconjuntos
    # Unir: Colocar as raizes dos subconjuntos em um unico subconjunto
    def unir_subconjuntos(self, subconjuntos, vertice_origem, vertice_destino):
        vertice_origem_raiz = self.encontra_raiz_subconjunto(subconjuntos, vertice_origem)
        vertice_destino_raiz = self.encontra_raiz_subconjunto(subconjuntos, vertice_destino)
        subconjuntos[vertice_destino_raiz] = vertice_origem_raiz

    # Algoritmo de Kruskal
    def kruskal(self):
        agm = []

        # Ordena as arestas de forma crescente segundo peso
        self.arestas = sorted(self.arestas, key=lambda aresta: aresta.peso)     

        # Cria um conjunto para cada vértice, inicialmente consistindo apenas do próprio vértice
        subconjuntos = [i for i in range(self.vertices)]    

        # Percorre as arestas ordenadas
        for aresta in self.arestas:
            vertice_origem = aresta.origem 
            vertice_destino = aresta.destino 

            # Se os vértices raízes de dois vértices são diferentes, então eles estão em subconjuntos diferentes
            if self.encontra_raiz_subconjunto(subconjuntos, vertice_origem) != self.encontra_raiz_subconjunto(subconjuntos, vertice_destino):    
                agm.append(aresta)                                                      # Adiciona na AGM
                self.unir_subconjuntos(subconjuntos, vertice_origem, vertice_destino)   # Une os dois subconjuntos

        return agm

    def imprime_agm(self, agm):
        print("Árvore Geradora Mínima (Algoritmo de Kruskal):")
        for aresta in agm:
            print(f"{aresta.origem} - {aresta.destino} : peso({aresta.peso})")

v = int(input("Digite a quantidade de vértices: "))

if (v > 20 or v <= 0):
    print("\nDigite um numero inteiro positivo que não ultrapasse 20 posicoes!")
    exit(0)
else:
    g = Grafo(v)
    
opcao = 0

while (opcao != 5):
    print("__________________________________________")
    print("\n1 - Adicione uma nova aresta")
    print("2 - Imprima a matriz")
    print("3 - Encontre a Árvore Geradora Mínima (Algoritmo de Kruskal)")
    print("4 - Exemplo")
    print("5 - Sair")
    
    opcao = int(input("Digite a opcao que deseja: "))
    print("__________________________________________")

    if opcao == 1:
        vertice_partida = int(input("\nQual vértice será a partida? (0-" + str(g.vertices-1) + "): "))
        vertice_chegada = int(input("Qual vértice será a chegada? (0-" + str(g.vertices-1) + "): "))
        if (vertice_partida < 0 or vertice_chegada >= g.vertices) or (vertice_chegada < 0 or vertice_chegada >= g.vertices):
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
        g = Grafo(6)
        g.adiciona_aresta(0, 1, 6)
        g.adiciona_aresta(0, 2, 5)
        g.adiciona_aresta(0, 3, 1)
        g.adiciona_aresta(1, 3, 5)
        g.adiciona_aresta(1, 4, 3)
        g.adiciona_aresta(2, 3, 5)
        g.adiciona_aresta(2, 5, 2)
        g.adiciona_aresta(3, 4, 6)
        g.adiciona_aresta(3, 5, 4)
        g.adiciona_aresta(4, 5, 6)
        print("Exemplo gerado!")

    elif opcao == 5:
        print("Saindo...")

    else:
        print("Opção inválida. Tente novamente!")
