from hashlib import new
from tkinter import N
from Grafo import Grafo
import math

file = "instancias/caminho_minimo/minimum.net"

def main():
    #Instanciar grafo
    grafo = Grafo(file)

    result = floydWarshall(grafo)
    printMatrix(result)
    

def floydWarshall(grafo: Grafo):

    # Pega a matriz de caminhos minimos
    matDist = grafo.matrizDistancias()

    # Algoritmo de floyd warshall, considerando todos os pares de vértices em um grafo
    for k in range(grafo.qtdVertices()):
        for i in range(grafo.qtdVertices()):
            for j in range(grafo.qtdVertices()):
                matDist[i][j] = min(matDist[i][j], matDist[i][k] + matDist[k][j])
        
    return matDist

def printMatrix(matriz):


    for itens in matriz: #Imprimi a matriz final organizando a leitura
        print("")   
        for item in itens:
            print("%s\t " % item, end="")
    print("\n")
            
main()