from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar, Unpack, cast

from pykeepass import PyKeePass

from flask_keepass.common.exceptions import AppRequiredError
from flask_keepass.typing import ReturnFindEntries, typed_wrap
from flask_keepass.typing.kwargs import KeePassConfig

if TYPE_CHECKING:
    from flask_keepass.typing.manager import FindEntriesKwargs


@typed_wrap
class KeepassManager(PyKeePass):
    _has_init: ClassVar[bool] = False

    def __init__(self, **kwargs: Unpack[KeePassConfig]) -> None:

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


KeepassManager()
