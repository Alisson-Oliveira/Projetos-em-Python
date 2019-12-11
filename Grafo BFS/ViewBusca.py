#coding:utf8
import networkx as nx
import matplotlib.pyplot as plt

class ViewBusca:
    def __init__(self):
        self.viewBusca = nx.Graph()

    def add_vertice(self, vertice):
        self.viewBusca.add_node(vertice)

    def add_aresta(self, vertice, adjacente):
        self.viewBusca.add_edge(vertice, adjacente)

    def view_tree(self):
        nx.draw(self.viewBusca, with_labels=True)
        plt.show()
        print('Árvore Successful')
