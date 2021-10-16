import sqlite3 #Importando o Banco de dados SQLite 3

class Banco(): # Criando a Classe do Banco
    def __init__(self): # Definindo primeira função que faz ligação do banco com o codigo
        self.conexao = sqlite3.connect('banco.db')
        self.createTable()
    
    def createTable(self): # Faz a conexão do banco com com o codigo
        c = self.conexao.cursor()
        c.execute("""create table if not exists usuarios (
                        idusuario integer primary key autoincrement,
                        nome text,
                        cpf text,
                        telefone text,
                        endereco text,
                        email text,
                        usuario text,
                        senha text)""")
        self.conexao.commit()
        c.close()
