from Banco import Banco

class Usuarios(object):
    def __init__(self, idusuario = 0, nome = "", cpf = "", telefone = "", endereco = "", email = "", usuario = "", senha = ""):
        self.info = {}
        self.idusuario = idusuario
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.endereco = endereco
        self.email = email
        self.usuario = usuario
        self.senha = senha
    
    def insertUser(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute(  "INSERT INTO usuarios(nome, cpf, telefone, endereco, email, usuario, senha)"
                        "VALUES (   '" + self.nome + '\n' "','"
                                    '' + self.cpf + '\n' "','"
                                    '' + self.telefone + '\n' "','"
                                    '' + self.endereco + '\n' "','"
                                    '' + self.email + '\n' "', '"
                                    '' + self.usuario + '\n' "','"
                                    '' + self.senha + '\n' "' " " )" )
            banco.conexao.commit()
            c.close()
            return "Usuário cadastrado com sucesso!"
        except:
            return "Ocorreu um erro na inserção do usuário"
        
    def updateUser(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute(  "UPDATE usuarios SET"
                        "nome = '" + self.nome + "',"
                        "cpf = '" + self.cpf + "',"
                        "telefone = '" + self.telefone + "',"
                        "endereco = '" + self.endereco + "',"
                        "email = '" + self.email + "',"
                        "usuario = '" + self.usuario + "',"
                        "senha = '" + self.senha + "'"
                        "WHERE idusuario = " + self.idusuario + " ")
            banco.conexao.commit()
            c.close()
            return "Usuário atualizado com sucesso!"
        except:
            return "Ocorreu um erro na alteração do usuário"
            
    def deleteUser(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("DELETE FROM usuarios WHERE idusuario = " + self.idusuario + " ")
            banco.conexao.commit()
            c.close()
            return "Usuário excluído com sucesso!"
        except:
            return "Ocorreu um erro na exclusão do usuário"
            
    def selectUser(self, id_usuario):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("SELECT * FROM usuarios WHERE idusuario = " + id_usuario + " ")
            for linha in c:
                self.idusuario = linha[0]
                self.nome = linha[1]
                self.cpf = linha[2]
                self.telefone = linha[3]
                self.endereco = linha[4]
                self.email = linha[5]
                self.usuario = linha[6]
                self.senha = linha[7]
            c.close() 
            return "Busca feita com sucesso!"
        except:
            return "Ocorreu um erro na busca do usuário"
