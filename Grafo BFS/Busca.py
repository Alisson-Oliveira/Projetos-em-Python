#coding:utf8
from ViewBusca import ViewBusca

class Busca:
    def __init__(self, grafo):
        self.grafo = grafo
        self.viewBusca = ViewBusca()
        self.posicoes = []
        self.cor = []
        self.distancia = []
        self.anterior = []
        self.fila = []

    def is_empty(self):
        return self.fila != []

    def enqueue(self, number):
        self.fila.append(number)

    def dequeue(self):
        return self.fila.pop(0)

    def BFS(self, grafo):
        for vertice in range(len(grafo)):
            self.posicoes.append(vertice)
            self.cor.insert(vertice, "branco")
            self.distancia.insert(vertice, 0)
            self.anterior.insert(vertice, -1)
            self.viewBusca.add_vertice(vertice)
        self.show_busca()
        for vertice in range(len(grafo)):
            if(self.cor[vertice] == "branco"):
                self.BFS_VISIT(vertice)
        self.show_busca()

    def BFS_VISIT(self, vertice):
        self.cor[vertice] = "cinza"
        self.distancia[vertice] = 0
        self.enqueue(vertice)
        while(self.is_empty()):
            adjacente = self.dequeue()
            listaAdjacente = self.grafo.get_vertice(adjacente)
            for value in listaAdjacente:
                if(self.cor[value] == "branco"):
                    self.cor[value] = "cinza"
                    self.distancia[value] = self.distancia[adjacente] + 1
                    self.anterior[value] = adjacente
                    self.viewBusca.add_aresta(self.anterior[value], self.posicoes[value])
                    self.enqueue(value)
                    self.show_busca()
            self.cor[adjacente] = "preto"     

    def show_busca(self):
        print('---------------------')
        print('posições: ', self.posicoes)
        print('anterior: ', self.anterior)
        print('distancia: ', self.distancia)
        print('cor: ', self.cor)
        print('---------------------')

    def visualizar_busca(self):
        self.viewBusca.view_tree()
