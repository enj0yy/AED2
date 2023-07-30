# Definição da classe Grafo que representa um grafo não direcionado com matriz de adjacência.
class Grafo:
    def __init__(self, vertices):
        # Inicializa o grafo com o número de vértices fornecido.
        self.vertices = vertices
        self.grafo = [[0]*self.vertices for i in range(self.vertices)]

    # Adiciona uma nova aresta ao grafo, atualizando a matriz de adjacência com o peso da aresta.
    def adiciona_aresta(self, partida, chegada, peso):
        self.grafo[partida-1][chegada-1] = peso
        self.grafo[chegada-1][partida-1] = peso
    
    # Imprime a matriz de adjacência do grafo, mostrando as conexões entre os vértices e os pesos das arestas.
    def imprime_matriz(self):
        print("\n   ", end=" ")
        for i in range(self.vertices):
            print('{:3d}'.format((i+1)), end=" ")
        print()

        for i in range(self.vertices):
            print('{:3d}'.format((i+1)), end=" ")
            for j in range(self.vertices):
                print('{:3d}'.format(self.grafo[i][j]), end=" ")
            print()

    # Implementa o algoritmo de Prim para encontrar a Árvore Geradora Mínima (AGM) do grafo.
    def prim(self):
        chave = [float('inf')] * self.vertices # Inicializa as chaves (pesos) dos vértices como infinito.
        arvore = [None] * self.vertices # Inicializa a árvore que representará a AGM.
        chave[0] = 0 # Define a chave do primeiro vértice como 0 (raiz da AGM).
        incluidos = [False] * self.vertices # Inicializa um vetor para marcar os vértices incluídos na AGM.

        # Iteração para construir a AGM.
        for _ in range(self.vertices):
            min_chave = float('inf')
            u = 0

            # Encontra o vértice com a menor chave que ainda não foi incluído na AGM.
            for i in range(self.vertices):
                if chave[i] < min_chave and not incluidos[i]:
                    min_chave = chave[i]
                    u = i

            incluidos[u] = True # Marca o vértice como incluído na AGM.

            # Atualiza as chaves dos vértices vizinhos do vértice selecionado.
            for v in range(self.vertices):
                if self.grafo[u][v] > 0 and not incluidos[v] and self.grafo[u][v] < chave[v]:
                    chave[v] = self.grafo[u][v]
                    arvore[v] = u

        # Monta e retorna a lista de arestas que representa a AGM encontrada pelo algoritmo.
        agm = []
        for i in range(1, self.vertices):
            agm.append((arvore[i]+1, i+1, self.grafo[i][arvore[i]]))

        return agm

    # Imprime a Árvore Geradora Mínima (AGM) encontrada pelo algoritmo de Prim.
    def imprime_agm(self, agm):
        print("Árvore Geradora Mínima (Algoritmo de Prim):")
        for aresta in agm:
            print(f"{aresta[0]} -> {aresta[1]} (Peso {aresta[2]})")

# Solicita ao usuário a quantidade de vértices do grafo.
v = int(input("Digite a quantidade de vértices: "))

# Verifica se o número de vértices é válido e cria o grafo.
if (v > 20 or v <= 0):
    print("\nDigite um numero inteiro positivo que não ultrapasse 20 posicoes!")
    exit(0)
else:
    g = Grafo(v)
    
# Menu interativo para realizar operações com o grafo.
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
        # Adicionar uma nova aresta ao grafo, solicitando os vértices de partida, chegada e o peso.
        vertice_partida = int(input("\nQual vértice será a partida? (1-" + str(g.vertices) + "): "))
        vertice_chegada = int(input("Qual vértice será a chegada? (1-" + str(g.vertices) + "): "))
        if (vertice_partida <= 0 or vertice_chegada > g.vertices) or (vertice_chegada <= 0 or vertice_chegada > g.vertices):
            print("Vértice(s) incorretos!")
        else:
            peso = int(input("Qual é o peso desta aresta?: "))
            g.adiciona_aresta(vertice_partida, vertice_chegada, peso)

    elif opcao == 2:
        # Imprime a matriz de adjacência do grafo.
        g.imprime_matriz()

    elif opcao == 3:
        # Encontra e imprime a Árvore Geradora Mínima (AGM) utilizando o algoritmo de Prim.
        agm = g.prim()
        g.imprime_agm(agm)

    elif opcao == 4:
        print("Saindo...")

    else:
        print("Opção inválida. Tente novamente!")