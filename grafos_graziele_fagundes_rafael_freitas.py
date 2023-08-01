# Graziele Fagundes e Rafael Freitas - M1

class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0]*self.vertices for i in range(self.vertices)]
        
    def adiciona_aresta(self, partida, chegada, peso):
        self.grafo[partida-1][chegada-1] = peso
         
    def imprime_matriz(self):
        print("\n   ", end=" ")

        for i in range(self.vertices):
            print('{:3d}'.format((i+1)), end=" ");
        print("")

        for i in range(self.vertices):
            print('{:3d}'.format((i+1)), end=" ");
            for j in range(self.vertices):
                print('{:3d}'.format(self.grafo[i][j]), end=" ")
            print("");
             
    
v = int(input("Digite a quantidade de vértices: "))

if (v > 20 or v <= 0):
    print("\nDigite um numero inteiro positivo que não ultrapasse 20 posicoes!")
    exit(0)
else:
    g = Grafo(v)
    
opcao = 0
      
while (opcao != 3):
    print("__________________________________________")
    print("\n1 - Adicione uma nova aresta")
    print("2 - Imprima a matriz")
    print("3 - Sair") 
    opcao = int(input("Digite a opcao que deseja: "));
    print("__________________________________________")
    
    if (opcao == 1):
        vertice_partida = int(input("\nQual vertice será a partida? (1-" + str(g.vertices) + "): "))
        vertice_chegada = int(input("Qual vertice será a chegada? (1-" + str(g.vertices) + "): "))
        if (vertice_partida <= 0 or vertice_chegada > g.vertices) or (vertice_chegada <= 0 or vertice_chegada > g.vertices):
            print("Vertice(s) incorretos!")
        else:
            peso = int(input("Qual é o peso desta aresta?: "))
            g.adiciona_aresta(vertice_partida, vertice_chegada, peso)

    elif (opcao == 2):
        g.imprime_matriz()

    elif (opcao == 3):
        print("Saindo...")
        
    else:
        print("Opcao invalidada. Tente Novamente!")