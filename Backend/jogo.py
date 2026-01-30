
## Assumindo já temos uma palavra 

#histórico = letras que já foram tentadas 
#tentativas = número de tentativas que ainda pode entrar 
#número de letras que faltam?? 
##pontos?
#número das posições onde a letra certa está na palavra? 

class Forca: 
    def __init__ (self, palavra, tamanho, tentativas, historico):
        self._palavra = palavra
        self._tamanho = tamanho
        self._tentativas: int = tentativas
        self._historico = historico


    def jogada(self, palavra, tamanho, tentativas, historico):
        l = (input("Digite uma letra")).capitalize
        if l in historico:
            print("Tente outra letra")
            jogada(self, palavra, tamanho, tentativas, historico)
        elif letracerta(palavra, l):
            historico.append(l)
        else:
            case (tentativas-1 == 0) : print ("You Lose!")
            _ : jogada(self, palavra, tamanho, tentaivas -1, historico.append(l))
    

def letracerta(palavra, letra):
    for x in palavra:
        x == letra

    


#    def tenta(c):
#        for x in 