import asyncio

from telethon.tl.functions.channels import EditAdminRequest, InviteToChannelRequest
from telethon.tl.types import ChatAdminRights

from userbot import BOTLOG_CHATID, BOTLOG_MSG as star
from userbot import SEN2, SEN3, SEN4, SEN5, bot



async def sensi_ubot_on():
    new_rights = ChatAdminRights(
        add_admins=True,
        invite_users=True,
        change_info=True,
        ban_users=True,
        delete_messages=True,
        pin_messages=True,
        manage_call=True,
    )
    try:
        if bot and tgbot:
            RamUbot = await tgbot.get_me()
            BOT_USERNAME = SensiUbot.username
            await bot(InviteToChannelRequest(int(BOTLOG_CHATID), [BOT_USERNAME]))
            await asyncio.sleep(3)
    except BaseException:
        pass
    try:
        if bot and tgbot:
            RamUbot = await tgbot.get_me()
            BOT_USERNAME = SensiUbot.username
            await bot(EditAdminRequest(BOTLOG_CHATID, BOT_USERNAME, new_rights, "BOT"))
            await asyncio.sleep(3)
    except BaseException:
        pass
    try:
        if bot:
            if BOTLOG_CHATID != 0:
                await bot.send_message(
                    BOTLOG_CHATID,
                    f"{star}",
                )
    except BaseException:
        pass
    try:
        if RAM2:
            if BOTLOG_CHATID != 0:
                await SEN2.send_message(
                    BOTLOG_CHATID,
                    f"{star}",
                )
    except BaseException:
        pass
    try:
        if RAM3:
            if BOTLOG_CHATID != 0:
                await SEN3.send_message(
                    BOTLOG_CHATID,
                    f"{star}",
                )
    except BaseException:
        pass
    try:
        if RAM4:
            if BOTLOG_CHATID != 0:
                await SEN4.send_message(
                    BOTLOG_CHATID,
                    f"{star}",
                )
    except BaseException:
        pass
    try:
        if RAM5:
            if BOTLOG_CHATID != 0:
                await SEN5.send_message(
                    BOTLOG_CHATID,
                    f"{star}",
                )
    except BaseException:
        pass
    try:
        await bot(InviteToChannelRequest(int(BOTLOG_CHATID), [BOT_USERNAME]))
    except BaseException:
        pass
