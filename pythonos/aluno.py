class Aluno:
    def __init__(self, RA = 00,nome = "jão",idade = "18"):
        self.RA = RA
        self.nome = nome
        self.idade = idade

    def setIdade(self, idade):
        self.idade = idade

    def getIdade(self):
        return self.idade 
    
    def setNome(self, nome):
        self.nome = nome

    def getNome(self):
        return self.nome

    def setRA(self, RA):
        self.RA = RA
        
    def getRA(self):
        return self.RA 
    
    def adicionaraluno():
        while True:
            RA
            nome
            idade
    
    def MostraDados(self):
        dados = "[RA:" + str(self.RA) + ", nome:" + self.nome + " , idade:" + str(self.idade) + "]"
        return dados
    
    def __str__(self):
        dados = "[RA:" + str(self.RA) + ", nome:" + self.nome + " , idade:" + str(self.idade) + "]"
        return dados