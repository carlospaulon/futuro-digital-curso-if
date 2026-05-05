from dataclasses import dataclass
from datetime import datetime

@dataclass
class Capitulo:
    title: str
    number: int
    date: datetime = datetime.now
    watched: bool = False

    def marcar_como_visto(self):
        self.visto = True