# Graziele Fagundes e Rafael Freitas - M1

class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0]*self.vertices for i in range(self.vertices)]
        
    def adiciona_aresta(self, partida, chegada, peso):
        self.grafo[partida][chegada] = peso;
        print("Aresta adicionada com sucesso!")

    def calcula_caminho_minimo(self, vertice_raiz, vertice_destino):
        linhas = 4;
        colunas = self.vertices;
        caminhos = [[column for column in range(colunas)] for row in range(linhas)];

        for i in range(linhas):
            for j in range(colunas):
                if (i == 0):
                    caminhos[i][j] = j;
                
                elif (i == 1):
                    caminhos[i][j] = 1;
                
                elif (i == 2) and (j != vertice_raiz):
                    caminhos[i][j] = 1000;
                elif (i == 2) and (j == vertice_raiz):
                    caminhos[i][j] = 0;
                
                elif (i == 3) and (j != vertice_raiz):
                    caminhos[i][j] = 0;
                elif (i == 3) and (j == vertice_raiz):
                    caminhos[i][j] = j;
        
        while True:
            achou_vertice_aberto = 0;
            vertice_aberto_estimativa_minima = 0;

            for j in range(colunas):
                if (caminhos[1][j] == 1):       # Se o vertice estiver aberto    
                    achou_vertice_aberto = 1;            
                    if (caminhos[2][j] < caminhos[2][vertice_aberto_estimativa_minima]) or (caminhos[1][vertice_aberto_estimativa_minima] == 0):    # Se a estimativa for menor
                        vertice_aberto_estimativa_minima = caminhos[0][j];

            if (achou_vertice_aberto == 0):
                break;
            else:
                caminhos[1][vertice_aberto_estimativa_minima] = 0;                                      # Fecha vertice
                for i in range(self.vertices):                              
                    if (self.grafo[vertice_aberto_estimativa_minima][i] != 0) and (caminhos[1][i] == 1):     # Acha os vertices adjacentes abertos
                        if (self.grafo[vertice_aberto_estimativa_minima][i] < caminhos[2][i]):          # Se a estimativa for menor, atualiza
                            caminhos[2][i] = caminhos[2][vertice_aberto_estimativa_minima] + self.grafo[vertice_aberto_estimativa_minima][i];   # Atualiza estimativa
                            caminhos[3][i] = vertice_aberto_estimativa_minima;                  # Atualiza precedente

        print()
        for i in range(linhas):
            if (i == 0):
                print("Verti.", end=" ")
            elif (i == 1):
                print("Aberto", end=" ")
            elif (i == 2):
                print("Estim.", end=" ")
            elif (i == 3):
                print("Prece.", end=" ")   
            
            for j in range(colunas):
                print('{:5d}'.format(caminhos[i][j]), end=" ")
            print();
    
        
        print("\nCaminho minimo do vertice " + str(vertice_raiz) + " ao vertice " + str(vertice_destino) + ": ");
        
        caminho_minimo = []
        caminho_minimo.append(vertice_destino)
        vertice_atual = caminhos[3][vertice_destino];
        while True:
            caminho_minimo.append(vertice_atual);
            if (vertice_atual == vertice_raiz):
                break
            vertice_atual = caminhos[3][vertice_atual];
        
        for i in range(int(len(caminho_minimo)/2)):         # Inverter vetor pq o caminho fica de tras pra frente
            temp = caminho_minimo[i];
            caminho_minimo[i] = caminho_minimo[len(caminho_minimo)-i-1];
            caminho_minimo[len(caminho_minimo)-i-1] = temp;
            
        for j in range(len(caminho_minimo)):                # Imprimir vetor com caminho minimo
            print(caminho_minimo[j], end=" ")
            if j != len(caminho_minimo)-1:
                print(" -> ", end=" ")
        print()

    def imprime_matriz(self):
        print("\n   ", end=" ")

        for i in range(self.vertices):
            print('{:3d}'.format((i)), end=" ");
        print()

        for i in range(self.vertices):
            print('{:3d}'.format((i)), end=" ");
            for j in range(self.vertices):
                print('{:3d}'.format(self.grafo[i][j]), end=" ")
            print();
             
    
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
    print("2 - Calcular caminho minimo")
    print("3 - Imprima a matriz")
    print("4 - Sair") 
    opcao = int(input("Digite a opcao que deseja: "));
    print("__________________________________________")
    
    if (opcao == 1):
        vertice_partida = int(input("\nQual vertice será a partida? (0-" + str(g.vertices-1) + "): "))
        vertice_chegada = int(input("Qual vertice será a chegada? (0-" + str(g.vertices-1) + "): "))
        if (vertice_partida < 0 or vertice_chegada > g.vertices-1) or (vertice_chegada < 0 or vertice_chegada > g.vertices-1):
            print("Vertice(s) incorretos!")
        else:
            peso = int(input("Qual é o peso desta aresta?: "))
            g.adiciona_aresta(vertice_partida, vertice_chegada, peso)

    elif (opcao == 2):
        vertice_raiz = int(input("\nQual vertice será a raiz? (0-" + str(g.vertices-1) + "): "))
        vertice_destino = int(input("Qual vertice será o destino? (0-" + str(g.vertices-1) + "): "))
        if (vertice_raiz < 0 or vertice_raiz > g.vertices-1) or (vertice_destino < 0 or vertice_destino > g.vertices-1):
            print("Vertice(s) incorretos!")
        else:
            g.calcula_caminho_minimo(vertice_raiz,vertice_destino)

    elif (opcao == 3):
        g.imprime_matriz()

    elif (opcao == 4):
        print("Saindo...")
        
    else:
        print("Opcao invalidada. Tente Novamente!")