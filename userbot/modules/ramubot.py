from time import sleep
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern='^.sadboy(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("`Pertama-tama Kamu cantik`")
    sleep(2)
    await typew.edit("`Kedua Kamu manis`")
    sleep(1)
    await typew.edit("`Dan yang terakhir aku dighosting kamu`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.punten(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`\n┻┳|―-∩`"
                     "`\n┳┻|     ヽ`"
                     "`\n┻┳|    ● |`"
                     "`\n┳┻|▼) _ノ`"
                     "`\n┻┳|￣  )`"
                     "`\n┳ﾐ(￣ ／`"
                     "`\n┻┳T￣|`"
                     "\n**Permisi Gua Mau Nimbrung Cuk..**")


@register(outgoing=True, pattern='^.geez(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Agaa Peler☑️**")
    await typew.edit("**Agaa Peler✅**")
    sleep(1)
    await typew.edit("**Caca Gilaa☑️**")
    await typew.edit("**Caca Gilaa✅**")
    sleep(2)
    await typew.edit("**Lia Depresi☑️**")
    await typew.edit("**Lia Depresi✅**")
    sleep(2)
    await typew.edit("**Rafi Gajelas☑️**")
    await typew.edit("**Rafi Gajelas✅**")
    sleep(2)
    await typew.edit("**Cece Tolol!☑️**")
    await typew.edit("**Cece Tolol!✅**")
    sleep(2)
    await typew.edit("**Agam Gabut!☑️**")
    await typew.edit("**Agam Gabut!✅**")
    sleep(2)
    await typew.edit("**Rian Jelek☑️**")
    await typew.edit("**Rian Jelek✅**")
    sleep(2)
    await typew.edit("**Alcoyy Kontol☑️**")
    await typew.edit("**Alcoyy Kontol✅**")
    sleep(3)
    await typew.edit("**CUMA DHIKA YANG BENER!**")

# Create by myself @localheart

CMD_HELP.update({
    "rambot":
    "`.rambot`\
    \nUsage: menampilkan alive bot.\
    \n\n`.sadboy`\
    \nUsage: hiks\
    \n\n`.punten` ; `.geez`\
    \nUsage: misi."
})
