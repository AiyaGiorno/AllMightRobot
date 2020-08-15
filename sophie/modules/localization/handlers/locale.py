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

from typing import Any

from sophie.components.localization.lanuages import get_language_name
from sophie.components.localization.strings import get_strings_dec
from sophie.modules.utils.message import MessageHandler

from .. import router


@router.message(commands=['lang'])  # type: ignore
@get_strings_dec
class GetLanguageMenu(MessageHandler):
    async def handle(self) -> Any:

        text = self.strings.get('current_lang', emoji=self.strings.emoji, language=get_language_name(self.strings.code))
        await self.event.reply(text)
