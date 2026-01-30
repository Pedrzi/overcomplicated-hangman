class Jogador:

    def __init__(self, nome, pontos, lista):
        self._nome: str = nome
        self._pontos: int = pontos
        self._lista = lista

    @property
    def nome(self) -> str:
        return self.__nome 
    
    @nome.setter
    def nome(self, nome):
        if not nome:
            raise ValueError("Missing name")
        elif nome.isalnum() :
            raise ValueError("Nome não pode conter caracteres especias")
        self._nome = nome 
    
    @property
    def pontos(self) -> int :
        return self._pontos
    
    @pontos.setter
    def pontos(self, pontos):
        if pontos <0 :
            pontos = 0
        self._pontos = pontos

    @property
    def lista(self):
        return self._lista
    
    @lista.setter
    def lista(self,lista):
        self._lista
        