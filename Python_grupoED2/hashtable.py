from aluno import Aluno
from insertionsort import InsertionSort

class HashTable:

    #método construtor
    def __init__(self, lista = [],nome = "hash",tamanhomax = 11,maxdeitens = 3, totalitens = 0):
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
    
    def hashtable(self,obj):
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
                    InsertionSort.ordenarHash(self.getlista()[a])
                elif self.getlista()[a][t].getRA() == obj.getRA():
                    print("não pode adicionar", obj.getNome(), "por ter o mesmo RA que:", self.getlista()[a][t].getNome())
                    break
                else:
                    print(obj.getNome(),"foi passado para próxima etapa")
    
    def busca(self,RA):
        a = (RA % self.tamanhomax)
        busca = False
        aluno = 0
        x = 0
        while x < len(self.getlista()[a]) and busca == False:
            print(self.getlista()[a][x].getRA()," == ",RA)
            if self.getlista()[a][x].getRA() != RA:
                busca = False
            else:
                busca = True
                aluno = self.getlista()[a][x]
            x += 1
            
        print(busca)
        if busca:
            coordenada = self.getlista()[a].index(aluno)
            print("o ",RA," está alocado na posição")
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
            print("o RA foi",RA," deletado com sucesso!")       
        else:
            print("não existe o ",RA,"na hashtable")


    def imprimir(self):
        print("tabelaHash:")
        for x in range(0,self.tamanhomax):
            print("index[",x,"]")
            if self.getlista()[x] == []:
                print("[]")
                pass
            else:
                for n in range(len(self.getlista()[x])):
                    print(self.getlista()[x][n].MostraDados())