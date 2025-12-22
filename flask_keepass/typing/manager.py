"""Modulo de tipagem para o gerenciador KeePass."""

from __future__ import annotations

from typing import TYPE_CHECKING, Unpack, overload

from pykeepass import PyKeePass

if TYPE_CHECKING:
    from pathlib import Path
    from uuid import UUID

    from flask import Flask
    from pykeepass import Group

    from flask_keepass.typing._types import ReturnFindEntries, ReturnFindEntry
    from flask_keepass.typing.kwargs import FindEntriesKwargs


class KeePassManager(PyKeePass):
    """Gerencie conexões e operações com arquivos KeePass.

    Esta classe permite inicializar, configurar e buscar
    entradas em bancos KeePass integrados ao Flask.

    Attributes:
        _has_init (bool): Indica se a instância já foi inicializada.

    """

    @overload
    def __init__(self, app: Flask | None) -> None: ...

    @overload
    def __init__(
        self,
        app: Flask | None,
        filename: str | Path | None,
        password: str | None,
        keyfile: str | Path | None,
        transformed_key: str | None,
        *,
        decrypt: bool | None,
    ) -> None: ...

    def __init__(self, **kwargs: Unpack[FindEntriesKwargs]) -> None:
        """Inicialize o gerenciador KeePass com configurações fornecidas."""

    @overload
    def init_app(self, app: Flask) -> None: ...

    @overload
    def init_app(
        self,
        app: Flask,
        filename: str | Path | None,
        password: str | None,
        keyfile: str | Path | None,
        transformed_key: str | None,
        *,
        decrypt: bool | None,
    ) -> None: ...

    def init_app(self, **kwargs: Unpack[FindEntriesKwargs]) -> None:
        """Inicialize a aplicação Flask com configurações KeePass."""

    @overload
    def find_entries(
        self,
        *,
        path: list[str] | None = None,
        title: str | None = None,
        username: str | None = None,
        password: str | None = None,
        url: str | None = None,
        notes: str | None = None,
        otp: str | None = None,
        string: dict[str, str] | None = None,
        uuid: UUID | None = None,
        tags: list[str] | None = None,
        autotype_enabled: bool | None = None,
        autotype_sequence: str | None = None,
        autotype_window: str | None = None,
        group: Group | None = None,
        history: bool | None = None,
        recursive: bool | None = None,
        regex: bool | None = None,
        flags: str | None = None,
    ) -> ReturnFindEntries: ...

    @overload
    def find_entries(
        self,
        *,
        path: list[str] | None = None,
        title: str | None = None,
        username: str | None = None,
        password: str | None = None,
        url: str | None = None,
        notes: str | None = None,
        otp: str | None = None,
        string: dict[str, str] | None = None,
        uuid: UUID | None = None,
        tags: list[str] | None = None,
        autotype_enabled: bool | None = None,
        autotype_sequence: str | None = None,
        autotype_window: str | None = None,
        group: Group | None = None,
        first: bool = True,
        history: bool | None = None,
        recursive: bool | None = None,
        regex: bool | None = None,
        flags: str | None = None,
    ) -> ReturnFindEntry: ...

    def find_entries(self) -> ReturnFindEntries:
        """Retorne entradas que correspondam a todos os parâmetros fornecidos.

        Args:
            path (list[str] | None): Caminho completo até a entrada.
            title (str | None): Título da entrada a ser encontrada.
            username (str | None): Nome de usuário da entrada.
            password (str | None): Senha da entrada.
            url (str | None): URL da entrada.
            notes (str | None): Notas da entrada.
            otp (str | None): Código OTP da entrada.
            string (dict[str, str] | None): Campos personalizados.
            uuid (UUID | None): UUID da entrada.
            tags (list[str] | None): Tags da entrada.
            autotype_enabled (bool | None): Autotype habilitado.
            autotype_sequence (str | None): Sequência de autotype.
            autotype_window (str | None): Filtro de janela para autotype.
            group (Group | None): Grupo para busca.
            first (bool | None): Retorne apenas a primeira correspondência.
            history (bool | None): Inclua histórico nas buscas.
            recursive (bool | None): Busque de forma recursiva.
            regex (bool | None): Interprete parâmetros como regex.
            flags (str | None): Flags para busca regex.

        """
