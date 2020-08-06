# Copyright (C) 2018 - 2020 MrYacha.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# This file is part of Sophie.

import typing

from sophie.components.caching.cached import cached
from sophie.utils.config import config
from .db.locale import get_lang, set_lang

if typing.TYPE_CHECKING:
    from .db.locale import LocalizationDB


@cached()
async def get_chat_locale(chat_id: int) -> str:
    lang = await get_lang(chat_id)
    if not lang:
        return config.localization.default_language

    return lang.locale_code


async def set_chat_locale(chat_id: int, locale_code: str) -> typing.Optional[LocalizationDB]:
    return await set_lang(chat_id, locale_code)
