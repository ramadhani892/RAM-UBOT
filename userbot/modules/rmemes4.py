# RAM-UBOT
from time import sleep
from userbot import ALIVE_NAME, CMD_HELP, IG_ALIVE, REPO_NAME, GROUP_LINK, bot
from userbot.events import register
from telethon import events
import asyncio

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname()
# ============================================


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.1

    animation_ttl = range(117)

    input_str = event.pattern_match.group(1)

    if input_str == "bulan":

        await event.edit(input_str)

        animation_chars = [
            "🌗",
            "🌘",
            "🌑",
            "🌒",
            "🌓",
            "🌔",
            "🌕",
            "🌖",
            "🌗",
            "🌘",
            "🌑",
            "🌒",
            "🌓",
            "🌔",
            "🌕",
            "🌖",
            "🌗",
            "🌘",
            "🌑",
            "🌒",
            "🌓",
            "🌔",
            "🌕",
            "🌖",
            "🌗",
            "🌘",
            "🌑",
            "🌒",
            "🌓",
            "🌔",
            "🌕",
            f"🌖"]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 32])


@register(outgoing=True, pattern='^.heli(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("▬▬▬.◙.▬▬▬ \n"
                     "═▂▄▄▓▄▄▂ \n"
                     "◢◤ █▀▀████▄▄▄▄◢◤ \n"
                     "█▄ █ █▄ ███▀▀▀▀▀▀▀╬ \n"
                     "◥█████◤ \n"
                     "══╩══╩══ \n"
                     "╬═╬ \n"
                     "╬═╬ \n"
                     "╬═╬ \n"
                     "╬═╬ \n"
                     "╬═╬ \n"
                     "╬═╬ \n"
                     "╬═╬ HALO MANTAN,AKU DATANG :) \n"
                     "╬═╬☻/ \n"
                     "╬═╬/▌ \n"
                     "╬═╬/ \\ \n")


@register(outgoing=True, pattern='^.tembak(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("_/﹋\\_\n"
                     "(҂`_´)\n"
                     "<,︻╦╤─ ҉\n"
                     r"_/﹋\_"
                     "\n**Mau Jadi Pacarku Gak?!**")


@register(outgoing=True, pattern='^.bundir(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`DIDUGA BUNDIR KARNA DI GHOSTING...`          \n　　　　　|"
                     "\n　　　　　| \n"
                     "　　　　　| \n"
                     "　　　　　| \n"
                     "　　　　　| \n"
                     "　　　　　| \n"
                     "　　　　　| \n"
                     "　　　　　| \n"
                     "　／￣￣＼| \n"
                     "＜ ´･ 　　 |＼ \n"
                     "　|　３　 | 丶＼ \n"
                     "＜ 、･　　|　　＼ \n"
                     "　＼＿＿／∪ _ ∪) \n"
                     "　　　　　 Ｕ Ｕ\n")


@register(outgoing=True, pattern='^.tawa(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("────██──────▀▀▀██\n"
                     "──▄▀█▄▄▄─────▄▀█▄▄▄\n"
                     "▄▀──█▄▄──────█─█▄▄\n"
                     "─▄▄▄▀──▀▄───▄▄▄▀──▀▄\n"
                     "─▀───────▀▀─▀───────▀▀\n`Awkwokwokwok lariii ada dia. . .`")


@register(outgoing=True, pattern='^.ular(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("░░░░▓\n"
                     "░░░▓▓\n"
                     "░░█▓▓█\n"
                     "░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░░██▓▓███\n"
                     "░░░░██▓▓████\n"
                     "░░░░░██▓▓█████\n"
                     "░░░░░░██▓▓██████\n"
                     "░░░░░░███▓▓███████\n"
                     "░░░░░████▓▓████████\n"
                     "░░░░█████▓▓█████████\n"
                     "░░░█████░░░█████●███\n"
                     "░░████░░░░░░░███████\n"
                     "░░███░░░░░░░░░██████\n"
                     "░░██░░░░░░░░░░░████\n"
                     "░░░░░░░░░░░░░░░░███\n"
                     "░░░░░░░░░░░░░░░░░░░\n")


@register(outgoing=True, pattern='^.y(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("‡‡‡‡‡‡‡‡‡‡‡‡▄▄▄▄\n"
                     "‡‡‡‡‡‡‡‡‡‡‡█‡‡‡‡█\n"
                     "‡‡‡‡‡‡‡‡‡‡‡█‡‡‡‡█\n"
                     "‡‡‡‡‡‡‡‡‡‡█‡‡‡‡‡█\n"
                     "‡‡‡‡‡‡‡‡‡█‡‡‡‡‡‡█\n"
                     "██████▄▄█‡‡‡‡‡‡████████▄\n"
                     "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
                     "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
                     "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
                     "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
                     "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
                     "▓▓▓▓▓▓█████‡‡‡‡‡‡‡‡‡‡‡‡██\n"
                     "█████‡‡‡‡‡‡‡██████████\n")


@register(outgoing=True, pattern='^.tank(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("█۞███████]▄▄▄▄▄▄▄▄▄▄▃ \n"
                     "▂▄▅█████████▅▄▃▂…\n"
                     "[███████████████████]\n"
                     "◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙◤\n")


@register(outgoing=True, pattern='^.babi(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("┈┈┏━╮╭━┓┈╭━━━━╮\n"
                     "┈┈┃┏┗┛┓┃╭┫😧ha ┃\n"
                     "┈┈╰┓▋▋┏╯╯╰━━━━╯\n"
                     "┈╭━┻╮╲┗━━━━╮╭╮┈\n"
                     "┈┃▎▎┃╲╲╲╲╲╲┣━╯┈\n"
                     "┈╰━┳┻▅╯╲╲╲╲┃┈┈┈\n"
                     "┈┈┈╰━┳┓┏┳┓┏╯┈┈┈\n"
                     "┈┈┈┈┈┗┻┛┗┻┛┈┈┈┈\n")


@register(outgoing=True, pattern='^.ajg(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("╥━━━━━━━━╭━━╮━━┳\n"
                     "╢╭╮╭━━━━━┫┃▋▋━▅┣\n"
                     "╢┃╰┫┈┈┈┈┈┃┃┈┈╰┫┣\n"
                     "╢╰━┫┈┈┈┈┈╰╯╰┳━╯┣\n"
                     "╢┊┊┃┏┳┳━━┓┏┳┫┊┊┣\n"
                     "╨━━┗┛┗┛━━┗┛┗┛━━┻\n")


@register(outgoing=True, pattern='^.gbn(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Kita Gban Jamet duls!!...`")
    sleep(1)
    await typew.edit("`Memulai global banned...✅`")
    sleep(2)
    await typew.edit("`Proses Global banned...✅`")
    sleep(3)
    await typew.edit(f"╭✠╼━━━━━━❖━━━━━━━✠\n┣• **TUAN:** `{ALIVE_NAME}`\n┣• **PIBOONG:** [INSTAGRAM]({IG_ALIVE})\n┣• **Aksi:** `PROMOSI`\n╰✠╼━━━━━━❖━━━━━━━✠")

@register(outgoing=True, pattern='^.gkck(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Proses global kick!!...**")
    sleep(3)
    await typew.edit("__mengeluarkan dari (1) Group__")
    sleep(1)
    await typew.edit("__mengeluarkan dari (2) Group__")
    sleep(1)
    await typew.edit("__mengeluarkan dari (3) Group__")
    sleep(1)
    await typew.edit("__mengeluarkan dari (4) Group__")
    sleep(1)
    await typew.edit("__mengeluarkan dari (5) Group__")
    sleep(1)
    await typew.edit("__mengeluarkan dari (6) Group__")
    sleep(1)
    await typew.edit("__mengeluarkan dari (7) Group__")
    sleep(1)
    await typew.edit("__mengeluarkan dari (8) Group__")
    sleep(1)
    await typew.edit("__mengeluarkan dari (9) Group__")
    sleep(1)
    await typew.edit("__mengeluarkan dari (10) Group__")
    sleep(1)
    await typew.edit("__mengeluarkan dari (11) Group__")
    sleep(1)
    await typew.edit("__mengeluarkan dari (12) Group__")
    sleep(1)
    await typew.edit("__mengeluarkan dari (13) Group__")
    sleep(1)
    await typew.edit("__mengeluarkan dari (14) Group__")
    sleep(1)
    await typew.edit("__mengeluarkan dari (15) Group__")
    sleep(1)
    await typew.edit("__mengeluarkan dari (16) Group__")
    sleep(1)
    await typew.edit("__mengeluarkan dari (17) Group__")
    sleep(1)
    await typew.edit("__mengeluarkan dari (18) Group__")
    sleep(1)
    await typew.edit("__mengeluarkan dari (19) Group__")
    sleep(1)
    await typew.edit("__mengeluarkan dari (20) Group__")
    sleep(2)
    await typew.edit("**Pengguna berhasil di kick global dari (20) obrolan dalam grup.**")


@register(outgoing=True, pattern='^.gmt(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Memulai proses Global mute...`")
    sleep(3)
    await typew.edit("`Pengguna berhasil di Global mute...!`")


@register(outgoing=True, pattern='^.tolol(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`TOLOL...`")
    sleep(2)
    await typew.edit("`Pertama Kamu tolol....`")
    sleep(1)
    await typew.edit("`Kedua Kamu memang tolol...`")
    sleep(1)
    await typew.edit("`Ketiga Kamu benar benar tolol..`")
    sleep(1)
    await typew.edit("`Dan kamu di takdirkan tolol...`")
    sleep(1)
    await typew.edit("`Dasar kamu TOLOL...`")
    sleep(1)
    await typew.edit("`T`")
    await typew.edit("`TO`")
    await typew.edit("`TOL`")
    await typew.edit("`TOLO`")
    await typew.edit("`TOLOL`")
    await typew.edit("`Di baca`")
    sleep(2)
    await typew.edit("`GOBLOK`")


@register(outgoing=True, pattern='^.uasu(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Memeriksa dyno heroku anda...`")
    sleep(1)
    await typew.edit("🤴")
    sleep(2)
    await typew.edit(f"𝗜𝗡𝗙𝗢 𝗞𝗘𝗞𝗨𝗔𝗧𝗔𝗡!! {REPO_NAME}\n\n"
                     "╭✠╼━━━━━━❖━━━━━━━✠╮\n"
                     "┣•𝗣𝗘𝗡𝗚𝗚𝗨𝗡𝗔𝗔𝗡 𝗦𝗔𝗔𝗧 𝗜𝗡𝗜 :\n"
                     "┣• ▸ 999 ᴊᴀᴍ - 999 ᴍᴇɴɪᴛ.\n" 
                     "┣• ▸ ᴘʀᴇꜱᴇɴᴛᴀꜱᴇ : 999%\n" 
                     "╰✠╼━━━━━━❖━━━━━━━✠╯\n"
                     "▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰\n"
                     "╭✠╼━━━━━━❖━━━━━━━✠╮\n"
                     "┣•𝗣𝗘𝗡𝗚𝗚𝗨𝗡𝗔𝗔𝗡 𝗕𝗨𝗟𝗔𝗡 𝗜𝗡𝗜 :\n"
                     "┣• ▸ `999999` ᴊᴀᴍ - `999999` ᴍᴇɴɪᴛ.\n"
                     "┣• ▸ ᴘʀᴇꜱᴇɴᴛᴀꜱᴇ : 1000%.\n"
                     "╰✠╼━━━━━━❖━━━━━━━✠╯\n"
                     f"𝗣𝗘𝗠𝗜𝗟𝗜𝗞  : {ALIVE_NAME}\n"
                     f"**•JOIN•** : [MY GROUP]({GROUP_LINK})")


@register(outgoing=True, pattern='^.kickme(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(f"`{ALIVE_NAME}, goodbye, terimakasih untuk semunya...😣`")
    sleep(3)
    await typew.edit(f"`{ALIVE_NAME} Telah meninggalkan Group....`")


@register(outgoing=True, pattern='^.gi(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**MUTUALAG IG YUK!...**")
    sleep(2)
    await typew.edit(f"𝐈𝐍𝐒𝐓𝐀𝐆𝐑𝐀𝐌= [𝐓𝐄𝐊𝐀𝐍]({IG_ALIVE})")


@register(outgoing=True, pattern='^.fck(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(".                       /¯ )")
    await typew.edit(".                       /¯ )\n                      /¯  /")
    await typew.edit(".                       /¯ )\n                      /¯  /\n                    /    /")
    await typew.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸")
    await typew.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ ")
    await typew.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')")
    await typew.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /")
    await typew.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /\n          \\                _.•´")
    await typew.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /\n          \\                _.•´\n            \\              (")
    await typew.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /\n          \\                _.•´\n            \\              (\n              \\  ")

CMD_HELP.update({
    "memes7":
    "`.bulan` ; `.hati` ; `.gbn` ; `.tolol` ; `.gmt`\
    \nUsage: liat aja.\
    \n\n`.heli` ; `.tank` ; `.tembak`\n`.bundir`\
    \nUsage: liat sendiri."
})

CMD_HELP.update({
    "memes8":
    ".y` ; `.uasu` ; `.gkck`\
    \nUsage: jempol , Cek dyno & prank global kick\
    \n\n`.tawa` ; `.oy` ; `.fck`\
    \nUsage: ketawa lari , Nyuruh nimbrung , fvck & Coba sendiri.\
    \n\n`.ular` ; `.babi` ; `.ajg`\
    \nUsage: liat sendiri."
})
