"""
Assumindo já temos uma palavra 

histórico = letras que já foram tentadas 
tentativas = número de tentativas que ainda pode entrar 
número de letras que faltam?? 
pontos?
número das posições onde a letra certa está na palavra? 
"""

class Forca: 
    def __init__ (self, palavra, tamanho, tentativas, historico):
        self._palavra: str = palavra
        self._tamanho: int = tamanho
        self._tentativas: int = tentativas
        self._historico: dict[str, str] = historico


    def jogada(self, palavra, tamanho, tentativas, historico):
        l = (input("Digite uma letra")).capitalize
        if l in historico:
            print("Tente outra letra")
        elif self.letracerta(palavra, l):
            historico.append(l)
        else:
            if (tentativas-1 == 0):
                print("Você perdeu")
            else:
                self.jogada(palavra, tamanho, tentativas -1, historico + [l])
    

    def letracerta(palavra, letra):
        for x in palavra:
            x == letra

    


#    def tenta(c):
#        for x in 