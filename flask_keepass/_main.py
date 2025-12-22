from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING, ClassVar, Unpack, cast

from pykeepass import PyKeePass, create_database

from flask_keepass._typing import ReturnFindEntries, typed_wrap
from flask_keepass._typing.kwargs import KeePassConfig
from flask_keepass.common.exceptions import AppRequiredError

if TYPE_CHECKING:
    from flask import Flask

    from flask_keepass._typing.manager import FindEntriesKwargs


@typed_wrap
class KeepassManager(PyKeePass):
    _has_init: ClassVar[bool] = False

    def __init__(self, **kwargs: Unpack[KeePassConfig]) -> None:

        if kwargs.get("app") or kwargs.get("filename"):
            self._has_init = True

            if kwargs.get("app"):
                self.app: Flask = kwargs.get("app")

            config = self.load_config(kwargs)
            if not Path(config["filename"]).exists():
                create_database(
                    filename=config["filename"],
                    password=config["password"],
                    keyfile=config["keyfile"],
                    transformed_key=config["transformed_key"],
                )

            super().__init__(**config)

    def load_config(self, kwargs: KeePassConfig) -> KeePassConfig:
        app: Flask = self.app

        if app:
            filename: str = str(app.config.get("KEEPASS_FILENAME"))
            password: str = str(app.config.get("KEEPASS_PASSWORD"))
            keyfile: str = app.config.get("KEEPASS_KEYFILE")
            transformed_key = app.config.get("KEEPASS_TRANSFORMED_KEY")

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
        keyfile: str = kwargs.get("KEEPASS_KEYFILE")
        transformed_key = kwargs.get("KEEPASS_TRANSFORMED_KEY")

        decrypt_ = str(kwargs.get("KEEPASS_DECRYPT", "True"))
        decrypt = decrypt_.lower() in ["true", "1"]

        return KeePassConfig(
            filename=filename,
            password=password,
            keyfile=keyfile,
            transformed_key=transformed_key,
            decrypt=decrypt,
        )

    def init_app(self, *args: Flask, **kwargs: Unpack[KeePassConfig]) -> None:

        self.app = kwargs.get("app") or args[0] if args else None

        if not self.app:
            raise AppRequiredError

        if not self._has_init:
            config = self.load_config(kwargs)
            if not Path(config["filename"]).exists():
                create_database(
                    filename=config["filename"],
                    password=config["password"],
                    keyfile=config["keyfile"],
                    transformed_key=config["transformed_key"],
                )

            super().__init__(**config)

        self.app.extensions["keepass"] = self

    def find_entries(
        self,
        **kwargs: Unpack[FindEntriesKwargs],
    ) -> ReturnFindEntries:
        return cast(
            "ReturnFindEntries",
            super().find_entries(**kwargs),
        )
