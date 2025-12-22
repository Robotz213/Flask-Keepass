"""Forneça tipos e utilitários para tipagem estática no projeto.

Este pacote contém definições de tipos e funções auxiliares
relacionadas à tipagem estática utilizadas em todo o projeto.
"""

from ._types import ReturnFindEntries
from .wraps import typed_wrap

__all__ = ["ReturnFindEntries", "typed_wrap"]
