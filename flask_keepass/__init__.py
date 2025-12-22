"""Forneça integração entre Flask e bancos de dados KeePass.

Este pacote permite gerenciar e acessar entradas KeePass
em aplicações Flask de forma segura e tipada.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar, TypedDict, Unpack, cast

from pykeepass import PyKeePass

from flask_keepass.common.exceptions import AppRequiredError
from flask_keepass.typing import ReturnFindEntries, _typed

if TYPE_CHECKING:
    from pathlib import Path

    from flask import Flask

    from flask_keepass.typing._manager import FindEntriesKwargs


class KeePassConfig(TypedDict):
    app: Flask
    filename: str | Path
    password: str
    keyfile: str | Path
    transformed_key: str
    decrypt: bool


@_typed
class KeepassManager(PyKeePass):
    """Gerencie conexões e operações com arquivos KeePass.

    Esta classe permite inicializar, configurar e buscar
    entradas em bancos KeePass integrados ao Flask.

    Attributes:
        _has_init (bool): Indica se a instância já foi inicializada.

    """

    _has_init: ClassVar[bool] = False

    def __init__(self, **kwargs: Unpack[KeePassConfig]) -> None:
        """Inicialize o gerenciador KeePass com configurações fornecidas.

        Args:
            **kwargs (KeePassConfig): Parâmetros de configuração,
            podendo incluir app Flask, caminho do arquivo, senha,
            keyfile, chave transformada e opção de descriptografia.

        """
        if kwargs.get("app") or kwargs.get("filename"):
            self._has_init = True
            config = self.load_config(kwargs)
            super().__init__(**config)

    def load_config(self, kwargs: KeePassConfig) -> KeePassConfig:
        app = kwargs.get("app")

        if app:
            filename: str = str(app.config["KEEPASS_FILENAME"])
            password: str = str(app.config["KEEPASS_PASSWORD"])
            keyfile: str = str(app.config.get("KEEPASS_KEYFILE"))
            transformed_key = str(app.config.get("KEEPASS_TRANSFORMED_KEY"))

            decrypt_ = str(app.config.get("KEEPASS_DECRYPT", "True"))
            decrypt = decrypt_.lower() in ["true", "1"]

            return KeePassConfig(
                filename=filename,
                password=password,
                keyfile=keyfile,
                transformed_key=transformed_key,
                decrypt=decrypt,
            )

        filename: str = str(kwargs["KEEPASS_FILENAME"])
        password: str = str(kwargs["KEEPASS_PASSWORD"])
        keyfile: str = str(kwargs.get("KEEPASS_KEYFILE"))
        transformed_key = str(kwargs.get("KEEPASS_TRANSFORMED_KEY"))

        decrypt_ = str(kwargs.get("KEEPASS_DECRYPT", "True"))
        decrypt = decrypt_.lower() in ["true", "1"]

        return KeePassConfig(
            filename=filename,
            password=password,
            keyfile=keyfile,
            transformed_key=transformed_key,
            decrypt=decrypt,
        )

    def init_app(self, **kwargs: Unpack[KeePassConfig]) -> None:

        app = kwargs.get("app")

        if not app:
            raise AppRequiredError

        if not self._has_init:
            config = self.load_config(kwargs)
            super().__init__(**config)

        app.extensions["keepass"] = self

    def find_entries(
        self,
        **kwargs: Unpack[FindEntriesKwargs],
    ) -> ReturnFindEntries:
        return cast(
            "ReturnFindEntries",
            super().find_entries(**kwargs),
        )


__all__ = ["KeepassManager"]
