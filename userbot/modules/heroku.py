"""
   Heroku manager for your userbot
"""

import codecs
import heroku3
import aiohttp
import math
import os
import requests
import asyncio

from userbot import (
    HEROKU_APP_NAME,
    HEROKU_API_KEY,
    BOTLOG,
    BOTLOG_CHATID,
    CMD_HELP,
    ALIVE_NAME,
    REPO_NAME,
    GROUP_LINK)
from userbot.events import register

heroku_api = "https://api.heroku.com"
if HEROKU_APP_NAME is not None and HEROKU_API_KEY is not None:
    Heroku = heroku3.from_key(HEROKU_API_KEY)
    app = Heroku.app(HEROKU_APP_NAME)
    heroku_var = app.config()
else:
    app = None


"""
   ConfigVars setting, get current var, set var or delete var...
"""


@register(outgoing=True,
          pattern=r"^.(get|del) var(?: |$)(\w*)")
async def variable(var):
    exe = var.pattern_match.group(1)
    if app is None:
        await var.edit("`[HEROKU]"
                       "\nHarap Siapkan`  **HEROKU_APP_NAME**.")
        return False
    if exe == "get":
        await var.edit("`Mendapatkan Informasi...`")
        variable = var.pattern_match.group(2)
        if variable != '':
            if variable in heroku_var:
                if BOTLOG:
                    await var.client.send_message(
                        BOTLOG_CHATID, "#ConfigVars\n\n"
                        "**Config Vars**:\n"
                        f"`{variable}` **=** `{heroku_var[variable]}`\n"
                    )
                    await var.edit("`Diterima Ke BOTLOG_CHATID...`")
                    return True
                else:
                    await var.edit("`Mohon Ubah BOTLOG Ke True...`")
                    return False
            else:
                await var.edit("`Informasi Tidak Ditemukan...`")
                return True
        else:
            configvars = heroku_var.to_dict()
            msg = ''
            if BOTLOG:
                for item in configvars:
                    msg += f"`{item}` = `{configvars[item]}`\n"
                await var.client.send_message(
                    BOTLOG_CHATID, "#CONFIGVARS\n\n"
                    "**Config Vars**:\n"
                    f"{msg}"
                )
                await var.edit("`Diterima Ke BOTLOG_CHATID`")
                return True
            else:
                await var.edit("`Mohon Ubah BOTLOG Ke True`")
                return False
    elif exe == "del":
        await var.edit("`Menghapus Config Vars...`")
        variable = var.pattern_match.group(2)
        if variable == '':
            await var.edit("`Mohon Tentukan Config Vars Yang Mau Anda Hapus`")
            return False
        if variable in heroku_var:
            if BOTLOG:
                await var.client.send_message(
                    BOTLOG_CHATID, "#MenghapusConfigVars\n\n"
                    "**Menghapus Config Vars**:\n"
                    f"`{variable}`"
                )
            await var.edit("`Config Vars Telah Dihapus`")
            del heroku_var[variable]
        else:
            await var.edit("`Tidak Dapat Menemukan Config Vars, Kemungkinan Telah Anda Hapus.`")
            return True


@register(outgoing=True, pattern=r'^.set var (\w*) ([\s\S]*)')
async def set_var(var):
    await var.edit("`Sedang Menyetel Config Vars ヅ`")
    variable = var.pattern_match.group(1)
    value = var.pattern_match.group(2)
    if variable in heroku_var:
        if BOTLOG:
            await var.client.send_message(
                BOTLOG_CHATID, "#SetelConfigVars\n\n"
                "**Mengganti Config Vars**:\n"
                f"`{variable}` = `{value}`"
            )
        await var.edit("`Sedang Di Proses, Mohon Menunggu Dalam Beberapa Detik `")
    else:
        if BOTLOG:
            await var.client.send_message(
                BOTLOG_CHATID, "#MenambahkanConfigVar\n\n"
                "**Menambahkan Config Vars**:\n"
                f"`{variable}` **=** `{value}`"
            )
        await var.edit("`Menambahkan Config Vars...`")
    heroku_var[variable] = value


"""
    Check account quota, remaining quota, used quota, used app quota
"""


@register(outgoing=True, pattern=r"^Usage(?: |$)")
async def dyno_usage(dyno):
    """
        Get your account Dyno Usage
    """
    await dyno.edit("`Memeriksa Dyno Heroku anda...`")
    await asyncio.sleep(3)
    await dyno.edit("🍁")
    await asyncio.sleep(2)
    useragent = (
        'Mozilla/5.0 (Linux; Android 10; SM-G975F) '
        'AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/81.0.4044.117 Mobile Safari/537.36'
    )
    user_id = Heroku.account().id
    headers = {
        'User-Agent': useragent,
        'Authorization': f'Bearer {HEROKU_API_KEY}',
        'Accept': 'application/vnd.heroku+json; version=3.account-quotas',
    }
    path = "/accounts/" + user_id + "/actions/get-quota"
    async with aiohttp.ClientSession() as session:
        async with session.get(heroku_api + path, headers=headers) as r:
            if r.status != 200:
                await dyno.client.send_message(
                    dyno.chat_id,
                    f"`{r.reason}`",
                    reply_to=dyno.id
                )
                await dyno.edit("`Tidak Bisa Mendapatkan Informasi Dyno Anda`")
                return False
            result = await r.json()
            quota = result['account_quota']
            quota_used = result['quota_used']

            """ - User Quota Limit and Used - """
            remaining_quota = quota - quota_used
            percentage = math.floor(remaining_quota / quota * 100)
            minutes_remaining = remaining_quota / 60
            hours = math.floor(minutes_remaining / 60)
            minutes = math.floor(minutes_remaining % 60)

            """ - User App Used Quota - """
            Apps = result['apps']
            for apps in Apps:
                if apps.get('app_uuid') == app.id:
                    AppQuotaUsed = apps.get('quota_used') / 60
                    AppPercentage = math.floor(
                        apps.get('quota_used') * 100 / quota)
                    break
            else:
                AppQuotaUsed = 0
                AppPercentage = 0

            AppHours = math.floor(AppQuotaUsed / 60)
            AppMinutes = math.floor(AppQuotaUsed % 60)

            await dyno.edit(
                f"𝗜𝗡𝗙𝗢 𝗞𝗘𝗞𝗨𝗔𝗧𝗔𝗡 {REPO_NAME}!!\n\n"
                "╭✠╼━━━━━━❖━━━━━━━✠╮\n"
                "┣•𝗣𝗘𝗡𝗚𝗚𝗨𝗡𝗔𝗔𝗡 𝗦𝗔𝗔𝗧 𝗜𝗡𝗜 : \n"
                f"┣•   ▸ {AppHours} ᴊᴀᴍ - {AppMinutes} ᴍᴇɴɪᴛ. \n"
                f"┣•   ▸ ᴘʀᴇꜱᴇɴᴛᴀꜱᴇ : {AppPercentage}% \n"
                "╰✠╼━━━━━━❖━━━━━━━✠╯\n"
                "▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰ \n"
                "╭✠╼━━━━━━❖━━━━━━━✠╮ \n"
                "┣•𝗣𝗘𝗡𝗚𝗚𝗨𝗡𝗔𝗔𝗡 𝗕𝗨𝗟𝗔𝗡 𝗜𝗡𝗜 : \n"
                f"┣•  ▸ {hours} ᴊᴀᴍ - {minutes} ᴍᴇɴɪᴛ. \n"
                f"┣•  ▸ ᴘʀᴇꜱᴇɴᴛᴀꜱᴇ : {percentage}%. \n"
                "╰✠╼━━━━━━❖━━━━━━━✠╯\n"
                f"• 𝗣𝗘𝗠𝗜𝗟𝗜𝗞  : {ALIVE_NAME} \n"
                f"**•JOIN•** : [MY GROUP]({GROUP_LINK}) \n"
            )
            await asyncio.sleep(5)
            await event.delete()
            return True


@register(outgoing=True, pattern=r"^\.logs")
async def _(dyno):
    try:
        Heroku = heroku3.from_key(HEROKU_API_KEY)
        app = Heroku.app(HEROKU_APP_NAME)
    except BaseException:
        return await dyno.reply(
            "`Please make sure your Heroku API Key, Your App name are configured correctly in the heroku var.`"
        )
    await dyno.edit("`Sedang Mengambil Logs Anda`")
    with open("logs.txt", "w") as log:
        log.write(app.get_log())
    fd = codecs.open("logs.txt", "r", encoding="utf-8")
    data = fd.read()
    key = (requests.post("https://nekobin.com/api/documents",
                         json={"content": data}) .json() .get("result") .get("key"))
    url = f"https://nekobin.com/raw/{key}"
    await dyno.edit(f"`Ini Logs Heroku Anda :`\n\nPaste Ke: [Nekobin]({url})")
    return os.remove("logs.txt")


CMD_HELP.update({"herokuapp": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `Usage`"
                 "\n↳ : Check Quota Dyno Heroku"
                 "\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.set var <NEW VAR> <VALUE>`"
                 "\n↳ : Tambahkan Variabel Baru Atau Memperbarui Variabel"
                 "\nSetelah Menyetel Variabel Tersebut, Geez-Userbot Akan Di Restart."
                 "\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.get var atau .get var <VAR>`"
                 "\n↳ : Dapatkan Variabel Yang Ada, !!PERINGATAN!! Gunakanlah Di Grup Privasi Anda."
                 "\nIni Mengembalikan Semua Informasi Pribadi Anda, Harap berhati-hati."
                 "\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.del var <VAR>`"
                 "\n↳ : Menghapus Variabel Yang Ada"
                 "\nSetelah Menghapus Variabel, Bot Akan Di Restart."})
