"""Forneça funções utilitárias para tipagem do KeepassManager.

Este módulo contém funções para facilitar o uso de tipagem
com a classe KeepassManager.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .manager import KeepassManager


def typed_wrap(cls: KeepassManager) -> type[KeepassManager]:
    """Retorne a própria classe KeepassManager tipada.

    Args:
        cls (KeepassManager): Classe do gerenciador Keepass.

    Returns:
        type[KeepassManager]: Tipo da classe KeepassManager.

    """
    return cls
