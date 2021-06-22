# Copyright (C) 2020 TeamDerUntergang.
#
# SedenUserBot is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# Rama ganteng
# SedenUserBot is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

# @Qulec tarafından yazılmıştır.
# Thanks @Spechide.

import logging


from userbot import BOT_USERNAME
from userbot.events import register

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s",
    level=logging.WARNING)


@register(outgoing=True, pattern=r"^\.helpmek")
async def yardim(event):
    try:
        tgbotusername = BOT_USERNAME
        if tgbotusername is not None:
            results = await event.client.inline_query(tgbotusername, "@Jem_urbot")
            await results[0].click(
                event.chat_id, reply_to=event.reply_to_msg_id, hide_via=True
            )
            await event.delete()
        else:
            await event.edit(
                "`Bot tidak berfungsi! Harap setel Token Bot dan Nama Pengguna dengan benar. Modul telah dihentikan.`"
            )
    except Exception:
        return await event.edit(
            "`Anda tidak dapat Menggunakan Perintah Helpme, Bisa Jadi Grup Ini tidak Mensupport nya (Mungkin Anda Belum Menghidupakan Inline Mode Dan Inline Location Data)`"
        )
