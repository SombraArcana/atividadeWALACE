from aluno import Aluno
from hashtable import HashTable
from insertionsort import InsertionSort

hashi  = HashTable([[],[],[],[],[],[],[],[],[],[],[]],"hash1")

pagica = [7,5,9,3,2,1]
def ident():
    print("=#" * 30)


def main():
    while True:
        ident()
        print("MAIN")
        ident()
        print("Digite [1] para inserir aluno \nDigite [2] para usar funções da HasTable \nDigite [3] para criar uma lista \nDigite <ENTER> para sair do while")
        opcao = input("escolha sua opção:")
        if opcao == "":
            ident()
            print("==SESSÃO FINALIZADA==")
            break
        elif opcao == "1":
            ident()
            array = []
            print("Dados do novo aluno:")
            RA = (input("insira o RA:"))
            if RA != "":
                array.append(int(RA))
            else:
                array.append(00)
            nome = (input("insirao Nome:"))
            if nome != "":
                array.append(nome)
            else:
                array.append("jão")
            idade = (input("insira a Idade:"))
            if idade != "":
                array.append(str(idade))
            else:
                array.append("18")
            
            alun = Aluno(array[0],array[1],array[2])
            hashi.hashtable(alun)
            
        elif opcao == "2":
            ident()
            print("Digite [1] para exibir HasTable \nDigite [2] buscar Aluno com RA \nDigite [3] para remover Aluno com RA \nDigite <ENTER> para retornar ao menu")
            op =  input("escolha sua opção:")
            if op == "":
                main()
            elif op == "1":
                ident()
                hashi.imprimir()
            elif op == "2":
                ident()
                search = int(input("Digite a RA do estudante a se Achar:"))
                hashi.busca(search)
            elif op == "3":
                ident()
                bu = int(input("Digite a RA do estudante a se Deletar:"))
                hashi.deletaraluno(bu)
        
        elif opcao == "3":
            pass
        else:
            main()


if __name__ == "__main__":
    a1 = Aluno(65,"anderson Nunes", 56)
    a2 = Aluno(78,"anclison clines", 56)
    a3 = Aluno(63,"adermilto fagundes", 56)
    a4 = Aluno(22,"jacinto jhonata", 56)
    a5 = Aluno(47,"katadéubis Nunes", 56)
    a6 = Aluno(12,"ana", 56)
    a7 = Aluno(13,"juana", 56)
    a8 = Aluno(17,"invanilson rodrigues", 90)
    
    print(hashi.getlista())
    ident()
    
    hashi.hashtable(a1)
    hashi.hashtable(a2)
    hashi.hashtable(a3)
    hashi.hashtable(a4)
    hashi.hashtable(a5)
    hashi.hashtable(a6)
    hashi.hashtable(a7)
    hashi.hashtable(a8)
    print(pagica)
    InsertionSort.ordenarVetor(pagica)
    print(pagica)
    # main()
    
    
    