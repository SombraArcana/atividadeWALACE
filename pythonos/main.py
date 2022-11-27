from aluno import Aluno
from hashtable import HashTable
from insertionsort import InsertionSort
hashi  = HashTable([[],[],[],[],[],[],[],[],[],[],[]],"hash1")
def ident():
    print("=#" * 30)
    
def main():
    while True:
        ident()
        print("MAIN")
        ident()
        print("Digite [1] para inserir aluno \nDigite [2] para usar funções da HasTable \nDigite <ENTER> para sair do while")
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
                search = int(input("Digite a RA do estudante a se Deletar:"))


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
    
    main()
    
    
    # while True:
    #     ident()
    #     print("MAIN")
    #     ident()
    #     print("Digite [1] para inserir aluno \nDigite [2] para usar funções da HasTable \nDigite <ENTER> para sair do while")
    #     opcao = input("escolha sua opção")
    #     if opcao == "":
    #         ident()
    #         print("==SESSÃO FINALIZADA==")
    #         break
    #     elif opcao == "1":
    #         ident()
    #         pass
    #     elif opcao == "2":
    #         ident()
    #         print("Digite [1] para exibir HasTable \nDigite [2] buscar Aluno com RA \nDigite [3] para remover Aluno com RA \nDigite <ENTER> para retornar ao menu")
    #         op =  input("escolha sua opção")
    #         if op = "":


    
    
    
    
    
    # ident()
    # # print(a5)
    # print(hashi.getlista())
    # ident()
    # print("printando objeto 1")
    # print(hashi.getlista()[0])
    # ident()
    # hashi.imprimir()
    # ident()
    # hashi.deletaraluno(12)
    # hashi.imprimir()
    
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
