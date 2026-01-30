
from dataclasses import dataclass, field


@dataclass
class Jogador:
    nome: str
    pontos: int
    palavras_acertadas: list = field(default_factory=list)
    
        