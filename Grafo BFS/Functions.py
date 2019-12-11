#coding:utf8
from ViewGrafo import ViewGrafo
from Busca import Busca
from Grafo import Grafo

class Functions:
    def __init__(self):
        self.grafo = Grafo()
        self.viewGrafo = ViewGrafo()
        self.busca = Busca(self.grafo)
	
    def criar_grafo(self):
        tamanho = int(input('Quantidade de vertices: '))
        self.viewGrafo.viewAddVertices(tamanho)
        self.grafo.criar_grafo(tamanho)
	
    def add_adjacente(self):
        vertice = int(input('Vertice: '))
        novo_grafo = self.grafo.get_vertice(vertice)
        confirm1 = self.grafo.exite_vertice(self.grafo.get_grafo(), vertice)
        if(confirm1):
            qtd_adjacente = int(input('Quantidade de adjacentes: '))
            for number in range(qtd_adjacente):
                adjacente = int(input('%iº Adjacente: ' %(number + 1)))
                confirm2 = self.grafo.exite_adjacente(adjacente)
                if(confirm2):
                    self.viewGrafo.viewAddAdjacentes(vertice, adjacente)
                    confirm3 = self.grafo.ajdacentes_iguais(adjacente, novo_grafo)
                    if(confirm3):
                        novo_grafo.append(adjacente)
                        novo_vertice = self.grafo.get_vertice(adjacente)
                        confirm3 = self.grafo.ajdacentes_iguais(vertice, novo_vertice) 
                        if(confirm3):
                            novo_vertice.append(vertice)
                    else:
                        print('Adjacente já existe no grafo')
                else:
                    print('Não existe o adjacente', adjacente, 'no grafo')
        else:
            print('Não existe o vertice', vertice, 'no grafo')
	
    def remover_adjacente(self):
        vertice = int(input('Informe o vertice: '))
        novo_grafo = self.grafo.get_vertice(vertice)
        confirm1 = self.grafo.exite_vertice(self.grafo.get_grafo(), vertice)
        if(confirm1):
            qtd_adjacente = int(input('Quantidade de adjacentes: '))
            for number in range(qtd_adjacente):
                adjacente = int(input('%iº Adjacente: ' %(number + 1)))
                self.viewGrafo.viewRemoveAdjacente(vertice, adjacente)
                novo_grafo.remove(adjacente)
                novo_vertice = self.grafo.get_vertice(adjacente)
                confirm2 = self.grafo.remover_vertice_adjacente(vertice, novo_vertice)
                if(confirm2):
                    novo_vertice.remove(vertice)
        else:
            print('Não existe o vertice', vertice, 'no grafo')

    def verificar_adjacente(self):
        vertice = int(input('Informe o vertice: '))
        adjacentes = self.grafo.get_vertice(vertice)
        print('Adjacentes do vértice', vertice, ': ', adjacentes)
	
    def imprimir_grafo(self):
        vertices = "["
        tamanhoGrafo = len(self.grafo.get_grafo())
        for t in range(tamanhoGrafo):
            if(t < (tamanhoGrafo - 1)):
                vertices = vertices + ("%i, " %t)
            else:
                vertices = vertices + ("%i]" %t)
        print("POSIÇÕES: " + vertices)
        print(self.grafo.get_grafo())
	
    def visualizar_grafo(self):
        self.viewGrafo.viewGraph()
	
    def busca_largura(self):
        self.busca.BFS(self.grafo.get_grafo())
	
    def busca_view(self):
        self.busca.visualizar_busca()