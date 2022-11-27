from aluno import Aluno

class HashTable:

    #método construtor
    def __init__(self, lista = [],nome = "hashi",tamanhomax = 11,maxdeitens = 3, totalitens = 0):
        self.lista = lista
        self.nome = nome
        self.tamanhomax = tamanhomax
        self.maxdeitens = maxdeitens
        self.totalitens = totalitens
    
    def setlista(self, lista):
        self.lista = lista
        
    def getlista(self):
        return self.lista 
    
    def addLista(self, index , val):
        self.getlista()[index].append(val)
        pass
    
    def hashtable(self, obj):
        a = (obj.getRA() % self.tamanhomax)
        
        if self.getlista()[a] == []:
            print("a chave estava vazia, o aluno:",obj.getNome(),"vai ser adicionado a :", self.nome,"[",a,"]")
            self.getlista()[a].append(obj)
        else:
            print("o aluno:", obj.getNome()," está sendo comparado dentro da chave")
            
            for t in range(len(self.getlista()[a])):
                
                if self.getlista()[a][t].getRA() != obj.getRA() and (t+1) == len(self.getlista()[a]):
                    
                    print(obj.getNome(),"vai ser adicionada a posição self.getlista()[",a,"][",t+1,"] por não ter colisão")
                    
                    self.getlista()[a].append(obj)

                elif self.getlista()[a][t].getRA() == obj.getRA():
                    print("não pode adicionar", obj.getNome(), "por ter o mesmo RA que:", self.getlista()[a][t].getNome())
                    break
                else:
                    print(obj.getNome(),"foi passado para próxima etapa")
    
    def busca(self,RA):
        a = (RA % self.tamanhomax)
        busca = False
        aluno = 0
        for x in self.getlista()[a]:
            if x.getRA() == RA:
                busca = True
                aluno = x
            else:
                busca = False
        if busca:
            coordenada = self.getlista()[a].index(aluno)
            print("o aluno está alocado na posição")
            print(self.nome,"[",a,"][",coordenada,"]" )
        else:
            print("não existe o ",RA,"na hashtable")
    
    def settamanhomax(self, tamanhomax):
        self.tamanhomax = tamanhomax

    def gettamanhomax(self):
        return self.tamanhomax 
    
    def setmaxdeitens(self, maxdeitens):
        self.maxdeitens = maxdeitens

    def getmaxdeitens(self):
        return self.maxdeitens 
    
    def settotalitens(self, totalitens):
        self.totalitens = totalitens

    def gettotalitens(self):
        return self.totalitens 
    
    # métodos da classe
    def deletaraluno(self,RA):
        a = (RA % self.tamanhomax)
        busca = False
        aluno = 0
        for x in self.getlista()[a]:
            if x.getRA() == RA:
                busca = True
                aluno = x
            else:
                busca = False
        if busca:
            self.getlista()[a].remove(aluno)        
        else:
            print("não existe o ",RA,"na hashtable")

    
    # def hash(tam_vetor,max):
    #     quant_itens = 0
    #     maxdeitens = max
    #     tamanhomax = tam_vetor
    #     estrutura = Aluno[tam_vetor]
        
    # def Dhash(aluno):
    #     for x in aluno:
    #         aluno.pop()
        
    # def getSize(self):
    #     return self.totalitens
        
    # def imprimir(self):
    #     estrutura = Aluno[self.maxdeitens]
    #     print("tabelaHash:\n")
    #     for x in range(0,x<self.tamanhomax):
    #         if estrutura[x].getRA() != -1:
    #             print(x , " :", estrutura[x].getRA())

    def imprimir(self):
        print("tabelaHash:")
        for x in range(0,self.tamanhomax):
            print("index[",x,"]")
            if self.getlista()[x] == []:
                print("[]")
                pass
            else:
                for n in range(len(self.getlista()[x])):
                    print(self.getlista()[x][n-1].MostraDados())