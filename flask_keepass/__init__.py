"""Integração entre Flask e bancos de dados KeePass.

Este pacote permite gerenciar e acessar entradas KeePass
em aplicações Flask de forma segura e tipada.
"""

from ._main import KeepassManager

__all__ = ["KeepassManager"]
