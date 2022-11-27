
print("sim")
class InsertionSort:

    def InsertionSort():
        pass

    def ordenarVetor(vetor):
        for i in range(1,len(vetor)):
            aux = vetor[i]
            indiceJ = i - 1
            while (indiceJ >= 0 and aux < vetor[indiceJ]):
                vetor[indiceJ + 1] = vetor[indiceJ]
                indiceJ = indiceJ - 1
            
            vetor[indiceJ + 1] = aux;

    def toString():
        return "InsertionSort";


