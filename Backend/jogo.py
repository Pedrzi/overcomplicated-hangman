"""
Assumindo já temos uma palavra 

histórico = letras que já foram tentadas 
tentativas = número de tentativas que ainda pode entrar 
numdeletras = numeros de letras distintas na palavra

"""

class Forca: 
    def __init__ (self, palavra, tamanho, numdeletras):
        self._palavra: str = palavra
        self._tamanho: int = tamanho
        self._tentativas: int = 6
        self._historico: dict[str: list[str]] = {"Acertos": [], "Erros":[]}


    def jogada(self, jogada: str):
        # Uni o histótico de erros e acertos 
        historico = self._historico["Acertos"] + self._historico["Erros"]
        if jogada in historico:
            print("Tente outra letra")
        elif self.letracerta(jogada):
            #Adiciona a jogada certa no histórico de acertos
            self._historico["Acertos"] += jogada 
            print(self._historico)
        else:
            #Adiciona a jogada errada no histórico de erros
            self._historico["Erros"] += jogada
            self._tentativas -= 1
            print(f"{self._historico} e tem {self._tentativas} tentativas")

    def verifica_vida(self):
        novaTentativa = self._tentativas - 1
        if self._tentativas > 0 :
            if novaTentativa <= 0:
                print("Você perdeu!")
            else :
                return novaTentativa
        else :
            print("Você perdeu!")
            
    def letras_diferentes(self):
        listaLetras = []
        for x in self._palavra:
            if not (x in listaLetras):
                listaLetras.apend(x)



    def letracerta(self, letra):
        for x in self._palavra:
            x == letra

    


def teste():
    forca = Forca("cachorro", 8)
    forca.jogada("u")



if __name__ == "__main__":
    teste()

