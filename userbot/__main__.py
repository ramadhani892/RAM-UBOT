# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot start point """

import sys
from importlib import import_module

from telethon.tl.functions.channels import InviteToChannelRequest
from userbot import BOTLOG_CHATID, BOTLOG_MSG, BOT_USERNAME, BOT_VER, LOGS, bot, ramblacklist
from userbot.modules import ALL_MODULES
from userbot.utils.utils import autobot 
from userbot.utils.tools import hadeh_ajg
try:
    for module_name in ALL_MODULES:
        imported_module = import_module("userbot.modules." + module_name)
    bot.start()
    user = bot.get_me()
    if user.id in ramblacklist:
        LOGS.warning(
            "MAKANYA GA USAH BERTINGKAH GOBLOK, USERBOTnya GUA MATIIN NAJIS BANGET DIPAKE JAMET KEK LU.\nCredits: @merdhni"
        )
        sys.exit(1)
    LOGS.info(f"⚡AMI - iBOT⚡ ⚙️ V{BOT_VER} [ TELAH DIAKTIFKAN! ]")
except BaseException as e:
    LOGS.info(str(e), exc_info=True)
    sys.exit(1)


async def ram_ubot_on():
    try:
        if BOTLOG_CHATID != 0:
            await bot.send_message(
                BOTLOG_CHATID,
                f"{BOTLOG_MSG}",
            )
    except Exception as e:
        LOGS.info(str(e))
    try:
        await bot(InviteToChannelRequest(int(BOTLOG_CHATID), [BOT_USERNAME]))
    except BaseException:
        pass

bot.loop.run_until_complete(ram_ubot_on())
bot.loop.run_until_complete(autobot())
bot.loop.run_until_complete(hadeh_ajg())
if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
