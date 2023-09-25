from Grafo import Grafo
import math

file = "instancias/caminho_minimo/fln_pequena.net"

def main():
    grafo = Grafo(file)

    D, A = dijkstra(grafo, 2)
    printPaths(D, A)

# Encontrar o caminho mais curto em um grafo ponderado com arestas positivas
def dijkstra(grafo: Grafo, s: int):
    s = s - 1
    D: list[float] = [math.inf] * grafo.qtdVertices() # Guarda a distância mínima do vértice de origem até cada vértice do grafo
    A: list[int] = [-1] * grafo.qtdVertices() # Guarda o antecessor de cada vértice no caminho mais curto a partir do vértice de origem
    C: list[bool] = [False] * grafo.qtdVertices() # Guarda um valor booleano que indica se o vértice já foi visitado ou não

    D[s] = 0 # Distância do vértice de origem até ele mesmo é zero.

    while not all(C): #  Enquanto nem todos os vértices forem visitados
        u = -1
        for i in range(grafo.qtdVertices()):
            if (C[i] == False) and (D[i] < D[u] or u == -1):
                u = i
        C[u] = True # Vértice "u" é marcado como visitado
        
        # Atualiza as distâncias e os vértices anteriores de cada vértice adjacente a "u" que ainda não foi visitado
        for v in [x for x in grafo.vizinhos(u) if C[x] == False]: 
            if D[v] > D[u] + grafo.peso(u, v):
                D[v] = D[u] + grafo.peso(u, v)
                A[v] = u

    return D, A

# Imprimi os caminhos mais curtos de cada vértice do grafo até o vértice inicial 
def printPaths(D, A):
    for v in range(len(D)):
        print(v+1, ": ", sep="", end="")

        # Percorre a lista "A" a partir do vértice "v" até encontrar o vértice anterior no caminho mais curto
        path = [v]
        a = A[v]
        while a != -1:
            path.append(a)
            a = A[a]

        pathLen = len(path)
        for index, i in enumerate(path[::-1]):
            print(i+1, end='')
            if index != pathLen-1:
                print(",", end="")

        print("; d=", D[v], sep="")

main()
            
