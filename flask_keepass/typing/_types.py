from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pykeepass import Entry


type Any = any
type ReturnFindEntries = list[Entry] | None
type ReturnFindEntry = Entry | None
