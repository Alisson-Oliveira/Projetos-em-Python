#coding:utf8
import networkx as nx
import matplotlib.pyplot as plt

class ViewGrafo:
    def __init__(self):
        self.viewGrafo = nx.Graph()

    def viewAddVertices(self, tamanho):
        vertices = []
        for number in range(tamanho):
            vertices.append(number)
        self.viewGrafo.add_nodes_from(vertices)

    def viewAddAdjacentes(self, vertice, adjacente):
        self.viewGrafo.add_edge(vertice, adjacente)
    
    def viewRemoveAdjacente(self, vertice, adjacente):
        self.viewGrafo.remove_edge(vertice, adjacente)

    def viewGraph(self):
        nx.draw(self.viewGrafo, with_labels=True)
        plt.show()
        print('Grafo Successful')