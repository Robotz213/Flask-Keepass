"""Modulo de tipagem para argumentos de palavra-chave."""

from __future__ import annotations

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    from pathlib import Path
    from uuid import UUID

    from flask import Flask
    from pykeepass import Group


class FindEntriesKwargs(TypedDict, total=False):
    """Defina os argumentos para busca de entradas.

    Args:
        path (list[str]): Caminho completo até a entrada
            (ex: ['grupo', 'entrada']). Implica first=True.
            Todos os outros argumentos são ignorados se este for fornecido.
            Útil para tratar entrada do usuário.
        title (str): Título da entrada a ser buscada.
        username (str): Nome de usuário da entrada a ser buscada.
        password (str): Senha da entrada a ser buscada.
        url (str): URL da entrada a ser buscada.
        notes (str): Notas da entrada a ser buscada.
        otp (str): Código OTP da entrada a ser buscada.
        string (dict[str, str]): Campos personalizados da entrada.
            Exemplo: {'campo1': 'valor', 'campo2': 'valor'}
        uuid (UUID): UUID da entrada.
        tags (list[str]): Tags da entrada.
        autotype_enabled (bool): Indica se autotype está habilitado.
        autotype_sequence (str): Sequência de autotype.
        autotype_window (str): Filtro de janela para autotype.
        group (Group): Grupo onde buscar a entrada.
        first (bool): Retorne apenas a primeira correspondência ou None.
            Caso contrário, retorna lista de entradas encontradas.
        history (bool): Inclua entradas do histórico nos resultados.
        recursive (bool): Busque de forma recursiva.
        regex (bool): Interprete os campos de busca como expressões regulares.
        flags (str): Flags para busca com regex.

    """

    path: list[str] = ...
    title: str = ...
    username: str = ...
    password: str = ...
    url: str = ...
    notes: str = ...
    otp: str = ...
    string: dict[str, str] = ...
    uuid: UUID = ...
    tags: list[str] = ...
    autotype_enabled: bool = ...
    autotype_sequence: str = ...
    autotype_window: str = ...
    group: Group = ...
    first: bool = ...
    history: bool = ...
    recursive: bool = ...
    regex: bool = ...
    flags: str = ...


class KeePassConfig(TypedDict):
    """Defina as opções de configuração para integração com KeePass.

    Args:
        app (Flask): Instância da aplicação Flask.
        filename (str | Path): Caminho para o arquivo do banco KeePass.
        password (str): Senha para desbloquear o banco KeePass.
        keyfile (str | Path): Caminho para o keyfile de segurança extra.
        transformed_key (str): Chave transformada para descriptografia, se houver.
        decrypt (bool): Indica se deve descriptografar o banco.

    """

    app: Flask = ...
    filename: str | Path = ...
    password: str = ...
    keyfile: str | Path = ...
    transformed_key: str = ...
    decrypt: bool = ...
