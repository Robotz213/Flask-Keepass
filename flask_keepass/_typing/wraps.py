"""Forneça funções utilitárias para tipagem do KeepassManager.

Este módulo contém funções para facilitar o uso de tipagem
com a classe KeepassManager.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .manager import KeePassManager


def typed_wrap(cls: type[KeePassManager]) -> type[KeePassManager]:
    """Retorne a própria classe KeePassManager tipada.

    Args:
        cls (KeePassManager): Classe do gerenciador KeePass.

    Returns:
        type[KeePassManager]: Tipo da classe KeePassManager.

    """
    return cls
