""" Userbot module which contains afk-related commands """

from datetime import datetime
import time
from random import choice, randint

from telethon.events import StopPropagation
from telethon.tl.functions.account import UpdateProfileRequest

from userbot import (  # noqa pylint: disable=unused-import isort:skip
    AFKREASON,
    BOTLOG,
    BOTLOG_CHATID,
    CMD_HELP,
    ALIVE_NAME,
    COUNT_MSG,
    ISAFK,
    PM_AUTO_BAN,
    USERS,
    PM_AUTO_BAN,
    REPO_NAME,
    bot,
)
from userbot.events import register

# ========================= CONSTANTS ============================
AFKSTR = [
    f"{REPO_NAME} 𝗔𝗙𝗞\n╭✠╼━━━━━━━━━━━━ \n┣ {ALIVE_NAME} 𝐋𝐚𝐠𝐢 𝐀𝐅𝐊\n╰✠╼━━━━━━━━━",
    f"{REPO_NAME} 𝗔𝗙𝗞\n╭✠╼━━━━━━━━━━━━ \n┣ {ALIVE_NAME} 𝐋𝐚𝐠𝐢 𝐀𝐅𝐊\n╰✠╼━━━━━━━━━",
    f"{REPO_NAME} 𝗔𝗙𝗞\n╭✠╼━━━━━━━━━━━━ \n┣ {ALIVE_NAME} 𝐋𝐚𝐠𝐢 𝐀𝐅𝐊\n╰✠╼━━━━━━━━━",
    f"{REPO_NAME} 𝗔𝗙𝗞\n╭✠╼━━━━━━━━━━━━ \n┣ {ALIVE_NAME} 𝐋𝐚𝐠𝐢 𝐀𝐅𝐊\n╰✠╼━━━━━━━━━",
]


global USER_AFK  # pylint:disable=E0602
global afk_time  # pylint:disable=E0602
global afk_start
global afk_end
USER_AFK = {}
afk_time = None
afk_start = {}

# =================================================================


@register(outgoing=True, pattern="^.afk(?: |$)(.*)", disable_errors=True)
async def set_afk(afk_e):
    """ For .afk command, allows you to inform people that you are afk when they message you """
    message = afk_e.text  # pylint:disable=E0602
    string = afk_e.pattern_match.group(1)
    global ISAFK
    global AFKREASON
    global USER_AFK  # pylint:disable=E0602
    global afk_time  # pylint:disable=E0602
    global afk_start
    global afk_end
    user = await bot.get_me()  # pylint:disable=E0602
    global reason
    USER_AFK = {}
    afk_time = None
    afk_end = {}
    start_1 = datetime.now()
    afk_start = start_1.replace(microsecond=0)
    if string:
        AFKREASON = string
        await afk_e.edit(f"{REPO_NAME}\n╭✠╼━━━━━━❖━━━━━━━✠╮\n┣ {ALIVE_NAME} __𝙨𝙚𝙙𝙖𝙣𝙜 𝘼𝙁𝙆__\n┣ ᴀʟᴀꜱᴀɴ : {AFKREASON}\n╰✠╼━━━━━━❖━━━━━━━✠╯")
    else:
        await afk_e.edit("⏱️ 𝘼 𝙁 𝙆\n╭✠╼━━━━━━❖━━━━━━━✠╮ \n┣ __𝙨𝙚𝙙𝙖𝙣𝙜 𝘼𝙁𝙆__ \n╰✠╼━━━━━━❖━━━━━━━✠╯")
    if user.last_name:
        await afk_e.client(UpdateProfileRequest(first_name=user.first_name, last_name=user.last_name + " ⏱️𝐀 𝐅 𝐊⏱️ "))
    else:
        await afk_e.client(UpdateProfileRequest(first_name=user.first_name, last_name=" ⏱️𝐀 𝐅 𝐊⏱️ "))
    if BOTLOG:
        await afk_e.client.send_message(BOTLOG_CHATID, "#AFK\n__𝙨𝙚𝙙𝙖𝙣𝙜 𝘼𝙁𝙆 𝙨𝙖𝙮𝙖𝙣𝙜__")
    ISAFK = True
    afk_time = datetime.now()  # pylint:disable=E0602
    raise StopPropagation


@register(outgoing=True)
async def type_afk_is_not_true(notafk):
    """ This sets your status as not afk automatically when you write something while being afk """
    global ISAFK
    global COUNT_MSG
    global USERS
    global AFKREASON
    global USER_AFK  # pylint:disable=E0602
    global afk_time  # pylint:disable=E0602
    global afk_start
    global afk_end
    user = await bot.get_me()  # pylint:disable=E0602
    last = user.last_name
    if last and last.endswith(" ⏱️𝐀 𝐅 𝐊⏱️ "):
        last1 = last[:-12]
    else:
        last1 = ""
    back_alive = datetime.now()
    afk_end = back_alive.replace(microsecond=0)
    if ISAFK:
        ISAFK = False
        msg = await notafk.respond("🌱𝐎𝐍𝐋𝐈𝐍𝐄")
        time.sleep(3)
        await msg.delete()
        await notafk.client(UpdateProfileRequest(first_name=user.first_name, last_name=last1))
        if BOTLOG:
            await notafk.client.send_message(
                BOTLOG_CHATID,
                "Anda Mendapatkan " + str(COUNT_MSG) + " Pesan dari " +
                str(len(USERS)) + " Obrolan Saat Anda AFK",
            )
            for i in USERS:
                name = await notafk.client.get_entity(i)
                name0 = str(name.first_name)
                await notafk.client.send_message(
                    BOTLOG_CHATID,
                    "[" + name0 + "](tg://user?id=" + str(i) + ")" +
                    " Mengirim Mu " + "`" + str(USERS[i]) + " Pesan`",
                )
        COUNT_MSG = 0
        USERS = {}
        AFKREASON = None


@register(incoming=True, disable_edited=True)
async def mention_afk(mention):
    """ This function takes care of notifying the people who mention you that you are AFK."""
    global COUNT_MSG
    global USERS
    global ISAFK
    global USER_AFK  # pylint:disable=E0602
    global afk_time  # pylint:disable=E0602
    global afk_start
    global afk_end
    user = await bot.get_me()  # pylint:disable=E0602
    back_alivee = datetime.now()
    afk_end = back_alivee.replace(microsecond=0)
    afk_since = "**Terakhir Aktif**"
    if mention.message.mentioned and not (await mention.get_sender()).bot:
        if ISAFK:
            now = datetime.now()
            datime_since_afk = now - afk_time  # pylint:disable=E0602
            time = float(datime_since_afk.seconds)
            days = time // (24 * 3600)
            time = time % (24 * 3600)
            hours = time // 3600
            time %= 3600
            minutes = time // 60
            time %= 60
            seconds = time
            if days == 1:
                afk_since = "**Kemarin**"
            elif days > 1:
                if days > 6:
                    date = now + \
                        datetime.timedelta(
                            days=-days, hours=-hours, minutes=-minutes)
                    afk_since = date.strftime("%A, %Y %B %m, %H:%I")
                else:
                    wday = now + datetime.timedelta(days=-days)
                    afk_since = wday.strftime('%A')
            elif hours > 1:
                afk_since = f"`{int(hours)} Jam {int(minutes)} Menit`"
            elif minutes > 0:
                afk_since = f"`{int(minutes)} Menit {int(seconds)} Detik`"
            else:
                afk_since = f"`{int(seconds)} Detik`"
            if mention.sender_id not in USERS:
                if AFKREASON:
                    await mention.reply(f"⏱️ 𝐀 𝐅 𝐊\n╭✠╼━━━━━━━━━━━━ \n┣ {ALIVE_NAME} ꜱᴇᴅᴀɴɢ ᴀꜰᴋ\n┣ ꜱᴇᴊᴀᴋ: {afk_since}\n┣ ᴀʟᴀꜱᴀɴ: {AFKREASON}\n╰✠╼━━━━━━━━━")
                else:
                    await mention.reply(str(choice(AFKSTR)))
                USERS.update({mention.sender_id: 1})
                COUNT_MSG = COUNT_MSG + 1
            elif mention.sender_id in USERS:
                if USERS[mention.sender_id] % randint(2, 4) == 0:
                    if AFKREASON:
                        await mention.reply(f"{REPO_NAME} 𝗔𝗙𝗞\n╭✠╼━━━━━━━━━━━━ \n┣ {ALIVE_NAME} ꜱᴇᴅᴀɴɢ ᴀꜰᴋ\n┣ ꜱᴇᴊᴀᴋ: {afk_since}\n┣ ᴀʟᴀꜱᴀɴ: {AFKREASON}\n╰✠╼━━━━━━━━━")
                    else:
                        await mention.reply(str(choice(AFKSTR)))
                    USERS[mention.sender_id] = USERS[mention.sender_id] + 1
                    COUNT_MSG = COUNT_MSG + 1
                else:
                    USERS[mention.sender_id] = USERS[mention.sender_id] + 1
                    COUNT_MSG = COUNT_MSG + 1


@register(incoming=True, disable_errors=True)
async def afk_on_pm(sender):
    """ Function which informs people that you are AFK in PM """
    global ISAFK
    global USERS
    global COUNT_MSG
    global COUNT_MSG
    global USERS
    global ISAFK
    global USER_AFK  # pylint:disable=E0602
    global afk_time  # pylint:disable=E0602
    global afk_start
    global afk_end
    user = await bot.get_me()  # pylint:disable=E0602
    back_alivee = datetime.now()
    afk_end = back_alivee.replace(microsecond=0)
    afk_since = "**Belum Lama**"
    if sender.is_private and sender.sender_id != 777000 and not (
            await sender.get_sender()).bot:
        if PM_AUTO_BAN:
            try:
                from userbot.modules.sql_helper.pm_permit_sql import is_approved
                apprv = is_approved(sender.sender_id)
            except AttributeError:
                apprv = True
        else:
            apprv = True
        if apprv and ISAFK:
            now = datetime.now()
            datime_since_afk = now - afk_time  # pylint:disable=E0602
            time = float(datime_since_afk.seconds)
            days = time // (24 * 3600)
            time = time % (24 * 3600)
            hours = time // 3600
            time %= 3600
            minutes = time // 60
            time %= 60
            seconds = time
            if days == 1:
                afk_since = "**Kemarin**"
            elif days > 1:
                if days > 6:
                    date = now + \
                        datetime.timedelta(
                            days=-days, hours=-hours, minutes=-minutes)
                    afk_since = date.strftime("%A, %Y %B %m, %H:%I")
                else:
                    wday = now + datetime.timedelta(days=-days)
                    afk_since = wday.strftime('%A')
            elif hours > 1:
                afk_since = f"`{int(hours)} Jam {int(minutes)} Menit`"
            elif minutes > 0:
                afk_since = f"`{int(minutes)} Menit {int(seconds)} Detik`"
            else:
                afk_since = f"`{int(seconds)} Detik`"
            if sender.sender_id not in USERS:
                if AFKREASON:
                    await sender.reply(f"{REPO_NAME} 𝗔𝗙𝗞\n╭✠╼━━━━━━━━━━━━ \n┣ {ALIVE_NAME} 𝙨𝙚𝙙𝙖𝙣𝙜 𝘼𝙁𝙆\n┣ ꜱᴇᴊᴀᴋ: {afk_since}\n┣ ᴀʟᴀꜱᴀɴ: {AFKREASON}\n╰✠╼━━━━━━━━━")
                else:
                    await sender.reply(str(choice(AFKSTR)))
                USERS.update({sender.sender_id: 1})
                COUNT_MSG = COUNT_MSG + 1
            elif apprv and sender.sender_id in USERS:
                if USERS[sender.sender_id] % randint(2, 4) == 0:
                    if AFKREASON:
                        await sender.reply(f"{REPO_NAME} 𝗔𝗙𝗞\n ╭✠╼━━━━━━━━━━━━ \n┣ {ALIVE_NAME} 𝙨𝙚𝙙𝙖𝙣𝙜 𝘼𝙁𝙆\n┣ ꜱᴇᴊᴀᴋ: {afk_since}\n┣ ᴀʟᴀꜱᴀɴ: {AFKREASON}\n╰✠╼━━━━━━━━━")
                    else:
                        await sender.reply(str(choice(AFKSTR)))
                    USERS[sender.sender_id] = USERS[sender.sender_id] + 1
                    COUNT_MSG = COUNT_MSG + 1
                else:
                    USERS[sender.sender_id] = USERS[sender.sender_id] + 1
                    COUNT_MSG = COUNT_MSG + 1


CMD_HELP.update({
    "afk":
    "`.afk` [Alasan]\
\nUsage: Lakukan ketika ingin OFF.\nSiapapun Yang Balas, Tag, Atau Chat Kamu \
Mereka Akan Tau Alasan Kamu OFF.\n\nAFK Bisa Dilakukan Dan Dibatalkan Dimanapun.\
"
})
