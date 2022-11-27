from aluno import Aluno
from hashtable import HashTable
from insertionsort import InsertionSort
hashi  = HashTable([[],[],[],[],[],[],[],[],[],[],[]],"hash1")
def ident():
    print("=#" * 30)


if __name__ == "__main__":
    a1 = Aluno(65,"anderson Nunes", 56)
    a2 = Aluno(78,"anclison clines", 56)
    a3 = Aluno(63,"adermilto fagundes", 56)
    a4 = Aluno(22,"jacinto jhonata", 56)
    a5 = Aluno(47,"katadéubis Nunes", 56)
    a6 = Aluno(1,"ana", 56)
    a7 = Aluno(1,"juana", 56)
    # atehnas = 1
    # HashTable.menu()
    # print(HashTable.functionHash("a",a1))
    print(hashi.getlista())
    ident()
    
    hashi.hashtable(a1)
    hashi.hashtable(a2)
    hashi.hashtable(a3)
    hashi.hashtable(a4)
    print(hashi.getlista()[0][0])
    hashi.hashtable(a6)
    hashi.hashtable(a7)
    ident()
    # print(a5)
    print(hashi.getlista())
    ident()
    print("printando objeto 1")
    print(hashi.getlista()[0])
    ident()
    hashi.imprimir()
    ident()
    hashi.deletaraluno(1)
    hashi.imprimir()
    hashi.busca(63)
    print("22 % 11 =", 22 % 11)
    # hashi.getlista()[0]
    # print("busca:")
    # hashi.busca(1)
    # hashi.busca(22)
    # print(hashi.getlista()[0][0])
    # print(hashi.getlista()[0][1])
    # print(hashi.getlista()[0][2])
    
    # print(hashi.getlista()[1])
    # print(hashi.getlista()[2])
    
    # hashi.imprimir()
    
    # hashi[1].append(a1)
    # hashi[1].append(a2)
    # hashi[3].append(a4)
    # hashi[5].append(a3)
    # print(a1)
    # print(hashi)
