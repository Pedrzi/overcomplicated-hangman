
from dataclasses import dataclass, field

@dataclass
class Jogador:
    nome: str
    pontos: int
    palavras_acertadas: list = field(default_factory=list)


    def gastar_pontos(self, pontos_gastos: int) -> bool:
        if pontos_gastos > self.pontos:
            print("Pontos insuficientes!")
            return False
        self.pontos -= pontos_gastos
        return True

    def ganhar_pontos(self, pontos_ganhos: int) -> None:
        self.pontos += pontos_ganhos
    
    def adicionar_palavra_acertada(self, palavra: str) -> None:
        self.palavras_acertadas.append(palavra)