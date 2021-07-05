# Copyright (C) 2019 The Raphielscape Company LLC.
# RAM-UBOT MINTA
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License
""" Userbot module containing commands related to the \
    Information Superhighway (yes, Internet). """

import asyncio
import time
import redis

from datetime import datetime

from speedtest import Speedtest
from userbot import CMD_HELP, StartTime, ALIVE_NAME, REPO_NAME
from userbot.events import register


async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["Dtk", "Mnt", "Jam", "Hari"]

    while count < 4:
        count += 1
        remainder, result = divmod(
            seconds, 60) if count < 3 else divmod(
            seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time



@register(outgoing=True, pattern="^.pings$")
async def redis(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("`Connecting to server...`")
    await pong.edit("☠️")
    await asyncio.sleep(3)
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**`{ALIVE_NAME}`**\n"
                    f"✧ **-ꜱɪɢɴᴀʟ- :** "
                    f"`%sms` \n"
                    f"✧ **-ᴜᴘᴛɪᴍᴇ- :** "
                    f"`{uptime}` \n" % (duration))


@register(outgoing=True, pattern="^.ping$")
async def redis(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("SABAR!")
    await asyncio.sleep(1)
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**LAMA BAT!!**\n**KEKUATAN GUA NIH** : `%sms`\n**MASA HIDUP LU** : `{uptime}🕛`" % (duration))


@register(outgoing=True, pattern="^Ping$")
async def redis(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("PONG!!")
    await asyncio.sleep(2)
    await pong.edit(f"{REPO_NAME}")
    await asyncio.sleep(3)
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"{REPO_NAME}!!\n"
                    f"TUAN LU : {ALIVE_NAME}\n `%sms`\n"
                    f"`{uptime}` \n" % (duration))


@register(outgoing=True, pattern="^Speed$")
async def speedtst(spd):
    """ For .speed command, use SpeedTest to check server speeds. """
    await spd.edit("`Menjalankan Tes Kecepatan Coli lu, Sabar yeh...✨`")
    test = Speedtest()

    test.get_best_server()
    test.download()
    test.upload()
    test.results.share()
    result = test.results.dict()

    await spd.edit("**Kecepatan Tangan:\n**"
                   "✧ **Dimulai Pada :** "
                   f"`{result['timestamp']}` \n"
                   f" **━━━━━━━━━━━━━━━━━**\n\n"
                   "✧ **Download:** "
                   f"`{speed_convert(result['download'])}` \n"
                   "✧ **Upload:** "
                   f"`{speed_convert(result['upload'])}` \n"
                   "✧ **Signal:** "
                   f"`{result['ping']}` \n"
                   "✧ **ISP:** "
                   f"`{result['client']['isp']}` \n"
                   f"✧ **BOT:** {REPO_NAME}")


def speed_convert(size):
    """
    Hi human, you can't read bytes?
    """
    power = 2**10
    zero = 0
    units = {0: '', 1: 'Kb/s', 2: 'Mb/s', 3: 'Gb/s', 4: 'Tb/s'}
    while size > power:
        size /= power
        zero += 1
    return f"{round(size, 2)} {units[zero]}"


@register(outgoing=True, pattern="^Pong$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    start = datetime.now()
    await pong.edit("PONG")
    await asyncio.sleep(1)
    await pong.edit("✨")
    await asyncio.sleep(2)
    end = datetime.now()
    duration = (end - start).microseconds / 9000
    await pong.edit(f"**Majikan : {ALIVE_NAME}**\n`%sms`" % (duration))


CMD_HELP.update({
    "ping": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.ping` or `.pings`\
         \n↳ : Untuk Menunjukkan Ping Bot Anda.\
         \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `Speed`\
         \n↳ : Untuk Menunjukkan Kecepatan Coli Anda.\
         \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `Pong`\
         \n↳ : Sama Seperti Perintah Ping."})
