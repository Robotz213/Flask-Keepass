from __future__ import annotations

from typing import TYPE_CHECKING, Protocol, TypedDict, Unpack, overload

if TYPE_CHECKING:
    from pathlib import Path
    from uuid import UUID

    from flask import Flask
    from pykeepass import Group

    from flask_keepass.typing._types import ReturnFindEntries, ReturnFindEntry


class KeepassManager(Protocol):
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

    def find_entries(self, **kwargs: Unpack[FindEntriesKwargs]) -> ReturnFindEntries:
        """Return entries which match all provided parameters.

        Args:
            path (`list` of (`str` or `None`), optional): full path to an entry
                (eg. `['foobar_group', 'foobar_entry']`).  This implies `first=True`.
                All other arguments are ignored when this is given.
                This is useful for handling user input.
            title (`str`, optional): title of entry to find
            username (`str`, optional): username of entry to find
            password (`str`, optional): password of entry to find
            url (`str`, optional): url of entry to find
            notes (`str`, optional): notes of entry to find
            otp (`str`, optional): otp string of entry to find
            string (`dict`): custom string fields.
                (eg. `{'custom_field1': 'custom value',
                'custom_field2': 'custom value'}`)
            uuid (`uuid.UUID`): entry UUID
            tags (`list` of `str`): entry tags
            autotype_enabled (`bool`, optional): autotype string is enabled
            autotype_sequence (`str`, optional): autotype string
            autotype_window (`str`, optional): autotype target window filter string
            group (`Group` or `None`, optional): search under this group
            first (`bool`, optional): return first match or `None` if no matches.
                Otherwise return list of `Entry` matches. (default `False`)
            history (`bool`): include history entries in results. (default `False`)
            recursive (`bool`): search recursively
            regex (`bool`): interpret search strings given above as
                [XSLT style](https://www.xml.com/pub/a/2003/06/04/tr.html) regexes
            flags (`str`): regex [search flags](https://www.w3.org/TR/xpath-functions/#flags)

            **kwargs: additional keyword arguments.

        Returns:
            `list` of `Entry` if `first=False`
            or (`Entry` or `None`) if `first=True`

        Examples:
        ``` python
        >>> kp.find_entries(title='gmail', first=True)
        Entry: "social/gmail (myusername)"

        >>> kp.find_entries(title='foo.*', regex=True)
        [Entry: "foo_entry (myusername)", Entry: "foobar_entry (myusername)"]

        >>> entry = kp.find_entries(
        ...     title='foo.*', url='.*facebook.*', regex=True, first=True
        ... )
        >>> entry.url
        'facebook.com'
        >>> entry.title
        'foo_entry'
        >>> entry.title = 'hello'

        >>> group = kp.find_group(name='social', first=True)
        >>> kp.find_entries(title='facebook', group=group, recursive=False, first=True)
        Entry: "social/facebook (myusername)"
        ```

        """
        ...


class FindEntriesKwargs(TypedDict):
    """Kwargs for FindEntries.

    Args:
        path (`list` of (`str` or `None`), optional): full path to an entry
                    (eg. `['foobar_group', 'foobar_entry']`).  This implies `first=True`.
                    All other arguments are ignored when this is given.
                    This is useful for handling user input.
        title (`str`, optional): title of entry to find
        username (`str`, optional): username of entry to find
        password (`str`, optional): password of entry to find
        url (`str`, optional): url of entry to find
        notes (`str`, optional): notes of entry to find
        otp (`str`, optional): otp string of entry to find
        string (`dict`): custom string fields.
            (eg. `{'custom_field1': 'custom value', 'custom_field2': 'custom value'}`)
        uuid (`uuid.UUID`): entry UUID
        tags (`list` of `str`): entry tags
        autotype_enabled (`bool`, optional): autotype string is enabled
        autotype_sequence (`str`, optional): autotype string
        autotype_window (`str`, optional): autotype target window filter string
        group (`Group` or `None`, optional): search under this group
        first (`bool`, optional): return first match or `None` if no matches.
            Otherwise return list of `Entry` matches. (default `False`)
        history (`bool`): include history entries in results. (default `False`)
        recursive (`bool`): search recursively
        regex (`bool`): interpret search strings given above as
            [XSLT style](https://www.xml.com/pub/a/2003/06/04/tr.html) regexes
        flags (`str`): regex [search flags](https://www.w3.org/TR/xpath-functions/#flags)

    """

    path: list[str]
    title: str
    username: str
    password: str
    url: str
    notes: str
    otp: str
    string: dict[str, str]
    uuid: UUID
    tags: list[str]
    autotype_enabled: bool
    autotype_sequence: str
    autotype_window: str
    group: Group
    first: bool
    history: bool
    recursive: bool
    regex: bool
    flags: str
