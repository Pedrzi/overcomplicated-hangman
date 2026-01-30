
from dataclasses import dataclass, field


@dataclass
class Jogador:
    nome: str
    pontos: int
    palavras_acertadas: list = field(default_factory=list)


    def gastar_pontos(self, pontos_gastos: int) -> None:
        if pontos_gastos > self.pontos:
            raise ValueError("Pontos insuficientes")
        self.pontos -= pontos_gastos

        