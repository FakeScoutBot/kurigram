#  Pyrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present Dan <https://github.com/delivrance>
#
#  This file is part of Pyrogram.
#
#  Pyrogram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrogram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import annotations as _annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable


def normalize_prefixes(prefixes: str | Iterable[str] | None) -> list[str]:
    """Turn a prefix, a collection of prefixes or None into a de-duplicated list of strings.

    None and an empty string both mean "no prefix", which is represented by a single empty string.
    """
    if prefixes is None or prefixes == "":
        return [""]

    if isinstance(prefixes, str):
        return [prefixes]

    return list(dict.fromkeys(prefixes)) or [""]
