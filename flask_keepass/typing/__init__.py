"""Forneça tipos e utilitários para tipagem estática no projeto.

Este pacote contém definições de tipos e funções auxiliares
relacionadas à tipagem estática utilizadas em todo o projeto.
"""

from ._types import ReturnFindEntries
from ._wraps import _typed

__all__ = ["ReturnFindEntries", "_typed"]
