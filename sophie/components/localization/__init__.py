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

from sophie.utils.logging import log


from .config import __config__


async def __setup__() -> bool:
    from .loader import __setup__ as load_all_languages
    from .db import __setup__ as database

    log.debug('Loading localizations...')
    load_all_languages()
    log.debug('...Done!')

    log.debug('Loading database...')
    await database()
    log.debug('...Done!')

    return True


__all__ = [
    '__config__'
]
