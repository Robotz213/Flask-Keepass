from typing import Literal

type Any = any


type APP_REQUIRED = Literal["Flask or Quart instance required!"]
MESSAGE_APP_REQUIRED = "Flask or Quart instance required!"


class KpManagerExceptionBaseError(Exception):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class KpManagerRuntimeBaseError(RuntimeError):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class AppRequiredError(KpManagerRuntimeBaseError):
    def __init__(
        self,
        message: str | APP_REQUIRED = MESSAGE_APP_REQUIRED,
        *args: Any,
        **kwargs: Any,
    ) -> None:
        self.message = message
        super().__init__(*args, **kwargs)

    def __repr__(self) -> str:
        """Return a string representation of the AppRequiredError."""
        return f"AppRequiredError(message={self.message})"
