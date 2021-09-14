

from time import sleep
from userbot import CMD_HELP, bot
from userbot.events import register
from telethon import events
import asyncio


@register(outgoing=True, pattern="^.hua$")
async def koc(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("Aku di ghosting")
        sleep(1)
        await e.edit("😭😭😭")
        sleep(1)
        await e.edit("Aku Sedihhh")
        sleep(1)
        await e.edit("AKU JUGA ")
        sleep(1)
        await e.edit("PNGN DI GHOSTING ")
        sleep(1)
        await e.edit("KENAPA GA ADA YANG MAU GHOSTING GW")
        sleep(1)
        await e.edit("TAI BANGET ASLI")
        sleep(1)
        await e.edit("PARAH SI")
        sleep(1)
        await e.edit("GHOSTING GW DOOONG")
        sleep(1)
        await e.edit("GA ADA YANG MAU AMA GW YA")
        sleep(1)
        await e.edit("WALAUPUN CUMA GHOSTING?")
        sleep(1)
        await e.edit("GA ADA YANG MAU?")
        sleep(1)
        await e.edit("PNGN BNGT DI GHOSTING INI")
        sleep(1)
        await e.edit("WOIIIIII")
        sleep(1)
        await e.edit("GHOSTING GW!!!")
        sleep(1)
        await e.edit("😡😡😡")
        sleep(1)
        await e.edit("🥴🥴🥴")
        sleep(1)
        await e.edit("TAPI KALO MAU GHOSTING BILANG BILANG YA ༼")
        sleep(1)
        await e.edit("BIAR AKU GA KAGET")
        sleep(1)
        await e.edit("AKUBPNGN NGRASAIN DI GHOSTING")
        sleep(1)
        await e.edit("TAPI GA MAU SAKIT ATI")
        sleep(1)
        await e.edit("GUA STRESS")
        sleep(1)
        await e.edit("😭😭😭😭😭😭")
        sleep(1)
        await e.edit("🥴🥴🥴🥴")
        sleep(1)
        await e.edit("ADA YG MAU SAMA GUA?")
        sleep(1)
        await e.edit("PLISS GUA BUTUH")
        sleep(1)
        await e.edit("SESEORANG YG MAU NERIMA GUA")
        sleep(1)
        await e.edit("😔😔😔😔")
        sleep(1)
        await e.edit("MAU GAK JADI PACAR GUA??༼")
        sleep(1)
        await e.edit("TAPI BOONG ༼!!༽KWKW😊")


@register(outgoing=True, pattern='^.huh(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`\n(\\_/)`"
                     "`\n(●_●)`"
                     "`\n />❤️ *NIH GUA KASIH BUAT LU!!`")
    sleep(3)
    await typew.edit("`\n(\\_/)`"
                     "`\n(●_●)`"
                     "`\n/>💔  *E GAK DEH,UDH DI KSH GRATIS KAMU RUSAKIN`")
    sleep(2)
    await typew.edit("`\n(\\_/)`"
                     "`\n(●_●)`"
                     "`\n💔<\\  *MAAP AKU AMBIL LAGI`")


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 3

    animation_ttl = range(0, 103)

    input_str = event.pattern_match.group(1)

    if input_str == "story":

        await event.edit(input_str)

        animation_chars = [
            "`Cerita ❤️ Cinta` ",
            "  😐             😕 \n/👕\\         <👗\\ \n 👖               /|",
            "  😉          😳 \n/👕\\       /👗\\ \n  👖            /|",
            "  😚            😒 \n/👕\\         <👗> \n  👖             /|",
            "  😍         ☺️ \n/👕\\      /👗\\ \n  👖          /|",
            "  😍          😍 \n/👕\\       /👗\\ \n  👖           /|",
            "  😘   😊 \n /👕\\/👗\\ \n   👖   /|",
            " 😳  😁 \n /|\\ /👙\\ \n /     / |",
            "😈    /😰\\ \n<|\\      👙 \n /🍆    / |",
            "😅 \n/(),✊😮 \n /\\         _/\\/|",
            "😎 \n/\\_,__😫 \n  //    //       \\",
            "😖 \n/\\_,💦_😋  \n  //         //        \\",
            "  😭      ☺️ \n  /|\\   /(👶)\\ \n  /!\\   / \\ ",
            "`TAMAT 😅`"]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 103])


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 1

    animation_ttl = range(0, 11)

    input_str = event.pattern_match.group(1)

    if input_str == "canda":

        await event.edit(input_str)

        animation_chars = [
            "`⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀\n ⠀⣴⠿⠏⠀⠀⠀⠀⠀   ⢳⡀⠀⡏⠀⠀⠀   ⠀⢷\n⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀⠀⠀  ⠀   ⡇\n⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿  ⣸ Kamu    ⡇\n ⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀⠀  ⣿  ⢹⠀        ⡇\n  ⠙⢿⣯⠄⠀⠀⠀__⠀⠀⡿ ⠀⡇⠀⠀⠀⠀    ⡼\n⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀   ⠘⠤⣄⣠⠞⠀\n⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀\n⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀\n⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀ ⠀⣄⢸⠀⠀⠀⠀⠀⠀`",
            "`⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀\n ⠀⣴⠿⠏⠀⠀⠀⠀⠀  ⠀⢳⡀⠀⡏⠀⠀⠀   ⠀⢷\n⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀⠀⠀      ⡇\n⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿  ⣸ Pasti   ⡇\n ⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀⠀  ⣿  ⢹⠀        ⡇\n  ⠙⢿⣯⠄⠀⠀|__|⠀⠀⡿ ⠀⡇⠀⠀⠀⠀    ⡼\n⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀   ⠘⠤⣄⣠⠞⠀\n⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀\n⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀\n⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀ ⠀⣄⢸⠀⠀⠀⠀⠀⠀`",
            "`⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀\n ⠀⣴⠿⠏⠀⠀     ⠀⢳⡀⠀⡏⠀⠀    ⠀⢷\n⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀⠀⠀⠀     ⡇\n⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿  ⣸ Belum   ⡇\n ⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀⠀  ⣿  ⢹⠀         ⡇\n  ⠙⢿⣯⠄⠀⠀(x)⠀⠀⡿ ⠀⡇⠀⠀⠀⠀    ⡼\n⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀   ⠘⠤⣄⣠⠞⠀\n⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀\n⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀\n⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀ ⠀⣄⢸⠀⠀⠀⠀⠀⠀`",
            "`⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀\n ⠀⣴⠿⠏⠀⠀     ⠀⢳⡀⠀⡏⠀⠀    ⠀⢷\n⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀   ⠀     ⡇\n⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿  ⣸ Mandi Wajib  ⡇\n ⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀   ⣿  ⢹⠀        ⡇\n  ⠙⢿⣯⠄⠀⠀⠀__ ⠀⠀⡿ ⠀⡇⠀⠀⠀⠀    ⡼\n⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀   ⠘⠤⣄⣠⠞⠀\n⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀\n⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀\n⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀ ⠀⣄⢸⠀⠀⠀⠀⠀⠀`",
            "`⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀\n ⠀⣴⠿⠏⠀⠀⠀⠀⠀   ⢳⡀⠀⡏⠀⠀    ⠀⢷\n⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀⠀ ⠀     ⡇\n⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿  ⣸ Bwhaha  ⡇\n ⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀⠀  ⣿  ⢹⠀        ⡇\n  ⠙⢿⣯⠄⠀⠀|__| ⠀⡿ ⠀⡇⠀⠀⠀⠀    ⡼\n⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀   ⠘⠤⣄⣠⠞⠀\n⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀\n⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀\n⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀ ⠀⣄⢸⠀⠀⠀⠀⠀⠀`",
            "`⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀\n ⠀⣴⠿⠏⠀⠀⠀⠀⠀  ⠀⢳⡀⠀⡏⠀⠀    ⠀⢷\n⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀  ⠀     ⡇\n⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿  ⣸ GOBLOK   ⡇\n ⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀   ⣿  ⢹⠀        ⡇\n  ⠙⢿⣯⠄⠀⠀****⠀⠀⡿ ⠀⡇⠀⠀⠀⠀    ⡼\n⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀   ⠘⠤⣄⣠⠞⠀\n⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀\n⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀\n⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀ ⠀⣄⢸⠀⠀⠀⠀⠀⠀`"]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 11])


@register(outgoing=True, pattern='^.nah(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`\n(\\_/)`"
                     "`\n(●_●)`"
                     "`\n />💖 *Ini Buat Kamu`")
    sleep(2)
    await typew.edit("`\n(\\_/)`"
                     "`\n(●_●)`"
                     "`\n💖<\\  *Tapi Bo'ong`")
# Alpinnnn Gans


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.5

    animation_ttl = range(0, 6)

    input_str = event.pattern_match.group(1)

    if input_str == "owner":

        await event.edit(input_str)

        animation_chars = [
            "**MAS 𝓚𝓲𝓶 ADALAH MANUSIA TERGANTENG DI HATI EMAK, KENALAN DULU SAMA MAS 𝓚𝓲𝓶 YUK**"
            "**PANGGIL AJA MAS 𝓚𝓲𝓶,ORANG NYA BAIK**"
            "**TINGGAL NYA DI PATI JAWA TENGAH INDONESIA**"
            "**KALO GA TAU CARI AJA DI GOOGLE MAPS, KALO DEKET KITA BIKIN INPO SANTUY**"
            "**POKOK NYA MAS 𝓚𝓲𝓶 ORNGNYA BIASA AJA🤭**"
            "**UDAH POKOK NYA ITU AJA SIH,INTINYA MAS 𝓚𝓲𝓶 GAK JAHAT**"]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 6])

CMD_HELP.update({
    "memes5":
    "`.nah` ; `.huh` ; `.owner`\
    \nUsage: cobain.\
    \n\n`.bunga` ; `.buah`\
    \nUsage: animasi.\
    \n\n`.waktu`\
    \nUsage: animasi."
})

CMD_HELP.update({
    "memes6":
    "`.hua`\
    \nUsage: nangis.\
    \n\n`.cinta` ; `.canda`\
    \nUsage: liat sendiri"
})
