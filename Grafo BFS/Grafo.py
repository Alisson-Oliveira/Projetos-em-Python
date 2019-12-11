#coding:utf8
import networkx as nx
import matplotlib.pyplot as plt

class Grafo:
    def __init__(self):
        self.grafo = []	

    def criar_grafo(self, tamanho):
        for number in range(tamanho):
            self.grafo.append([])

    def get_vertice(self, vertice):
        if(self.exite_vertice(self.grafo, vertice)):
            return self.grafo[vertice]
        return
	
    def get_grafo(self):
        return self.grafo
	
    def ajdacentes_iguais(self, adjacente, vertice):
        cont = 0
        for item in vertice:
            if(item == adjacente):
                cont += 1
        if(cont == 0):
            return True
        else:
            return False
	
    def remover_vertice_adjacente(self, adjacente, vertice):
        if(len(vertice) != 0):
            cont = 0
            for item in vertice:
                if(item == adjacente):
                    cont += 1
            if(cont == 0):
                return False
            else:
                return True
        else: 
            return False
	
    def exite_vertice(self, grafo, vertice):
        if(vertice < len(self.grafo)):
            return True
        else:
            return False
	
    def exite_adjacente(self, adjacente):
        if(adjacente < len(self.grafo)):
            return True
        else:
            return False
	
    def default_grafo(self):
        self.grafo = [[0, 1, 2, 3],[0],[0, 5],[0, 5],[5],[5, 4, 3, 2]]
	
    def default_grafo_view(self):
        self.viewDefault = nx.Graph()
        self.viewDefault.add_nodes_from([0, 1, 2, 3, 4, 5])
        self.viewDefault.add_edges_from([(0, 0), (0, 1), (0, 2), (0, 3)])
        self.viewDefault.add_edges_from([(5, 5), (5, 4), (5, 3), (5, 2)])
        nx.draw(self.viewDefault, with_labels=True)
        plt.show()
        print('Grafo Default Successful') 
