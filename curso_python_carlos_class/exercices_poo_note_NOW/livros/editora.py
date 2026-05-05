from abc import ABC, abstractmethod            # Classes abstratas
from dataclasses import dataclass              # Para Editora (estrutura simples)
 
 
# =============================================================================
# EDITORA (existência independente — Agregação com Livro)
# =============================================================================
 
@dataclass
class Editora:
    """
    Representa uma editora que publica livros.
    CONCEITO: Data Classes - @dataclass gera __init__, __repr__ e __eq__ automaticamente.
    CONCEITO: Agregação - Editora pode existir sem um Livro específico.
    """
    nome: str                                   # Nome da editora
    cnpj: str                                   # CNPJ único da editora
 
    def __str__(self) -> str:
        return f"Editora: {self.nome} (CNPJ: {self.cnpj})"