import math
from Grafo import Grafo

file = "instancias/caminho_minimo/fln_pequena.net"
s = 1

def main(file, s: int):
    s = s - 1
    grafo = Grafo(file)

    # Vertice i já visitado
    C: list[bool] = [False] * grafo.qtdVertices()
    # Distância, em vértices, até o vértice i
    D: list[int] = [math.inf] * grafo.qtdVertices()
    # Vertice antecessor ao vertice i
    A: list[int] = [None] * grafo.qtdVertices()

    # Marca o vertice de origem como já visitado...
    C[s] = True
    # ... e seta sua distância para 0
    D[s] = 0
    
    # Fila de visitas - inicia com S
    Q:list[int] = [s]

    # Enquanto a fila Q não estiver vazia:
    while Q:
        u = Q.pop(0) # Retire o primeiro elemento u da fila Q

        for v in grafo.vizinhos(u): # Para cada vizinho v de u no grafo
            if not C[v]: # Se v ainda não foi visitado (C[v] é falso)
                C[v] = True # Marcar v como visitado (C[v] é verdadeiro).
                D[v] = D[u] + 1 # Definir a distância de v como a distância de u mais um (D[v] = D[u] + 1).
                A[v] = u # Defiir o antecessor de v como u (A[v] = u).
                Q.append(v) # Adicionar v ao final da fila Q.

    printD(D)

def printD(D): # Recebe como parâmetro o vetor D 
    for i in range(max(D)+1): # Para cada distância i no intervalo de 0 a max(D):
        print(f"{i}: ", end='')
        for vertice, distancia in enumerate(D): # Para cada vértice e sua distância no vetor D:
            if distancia == i: # Se a distância do vértice for igual a i:
                print(vertice + 1, end=' ') # Imprimir o número do vértice seguido de um espaço em branco
        print() # Imprima uma nova linha

main(file, s)