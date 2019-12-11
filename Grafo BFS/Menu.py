#coding:utf8
from Functions import Functions
from Grafo import Grafo

class Menu:
    def __init__(self):
        self.functions = Functions()
        self.grafo = Grafo()

    def informacoes(self):
        print(
                """
                *** O grafo é iniciado com 0, ou seja,
                    se você digitou para criar N
                    vertices, o grafo vai ser criado
                    com N-1.

                *** Exemplo:
                    criar grafo com 5 vertices

                    [[],[],[],[],[]]
                     0  1  2  3  4
                """
            )        
	
    def menu(self):
        menuOne = True
        menuTwo = False
        menuThree = False
        while menuOne:
            print(
                    """
                    ========================
                    1 - Criar Grafo
                    2 - Grafo Padrão
                    3 - Informações
                    0 - Sair
                    ========================
                    """
                )
            op = int(input('Selecione uma opção: ')) 
            if op == 0:
                break
            elif op == 1:
                self.functions.criar_grafo()
                menuOne = False 
                menuTwo = True
                menuThree = False
                break
            if op == 2:
                self.functions.grafo.default_grafo()
                menuOne = False 
                menuTwo = False
                menuThree = True
                break
            elif op == 3:
                self.informacoes()
            else:
                print('Opção Inválida')
                continue

        while menuTwo:
            print(
                    """
                    ========================
                    1 - Adicionar Adjacente
                    2 - Remover Adjacente
                    3 - Verificar Adjacente
                    4 - Imprimir Grafo
                    5 - Visualizar Grafo
                    6 - Busca em Largura
                    7 - Visualizar Busca
                    8 - Informações
                    0 - Sair
                    ========================
                    """
                )
            op = int(input('Selecione uma opção: ')) 
            if op == 0:
                break
            elif op == 1:
                self.functions.add_adjacente()
            elif op == 2:
                self.functions.remover_adjacente()
            elif op == 3:
                self.functions.verificar_adjacente()
            elif op == 4:
                self.functions.imprimir_grafo()
            elif op == 5:
                self.functions.visualizar_grafo()
            elif op == 6:
                self.functions.busca_largura()
            elif op == 7:
                self.functions.busca_view()
            elif op == 8:
                self.informacoes()
            else:
                print('Opção Inválida')
                continue    
	
        while menuThree:
            print(
                    """
                    ========================
                    1 - Imprimir Grafo
                    2 - Visualizar Grafo Padrão
                    3 - Busca em Largura
                    4 - Visualizar Busca
                    5 - Informações
                    0 - Sair
                    ========================
                    """
                )
            op = int(input('Selecione uma opção: ')) 
            if op == 0:
                break
            elif op == 1:
                self.functions.imprimir_grafo()
            elif op == 2:
                self.grafo.default_grafo_view()
            elif op == 3:
                self.functions.busca_largura()
            elif op == 4:
                self.functions.busca_view()
            elif op == 5:
                self.informacoes()
            else:
                print('Opção Inválida')
                continue
	
    def run(self):
        self.menu()
