def ident():
    print("=#" * 30)

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
    
    # def substituirAluno(self):
    #     ident()
    #     Ra = input("entre com novo dado de RA:")
    #     if Ra != "" :
    #         self.setRA(Ra)
    #     else:
    #         print("nenhum valor foi entrado")
    #     ident()
    #     Nome = str(input("entre com o novo nome:"))
    #     self.setNome(Nome)
    #     idade = int(input("entre com novo valor da idade:"))
    #     self.setIdade(idade)
        
    
        
        

    
    def MostraDados(self):
        dados = "[RA:" + str(self.RA) + ", nome:" + self.nome + " , idade:" + str(self.idade) + "]"
        return dados
    
    def __str__(self):
        dados = "[RA:" + str(self.RA) + ", nome:" + self.nome + " , idade:" + str(self.idade) + "]"
        return dados