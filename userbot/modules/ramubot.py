from time import sleep
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern='^.sadboy(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("`Pertama-tama kamu cantik`")
    sleep(2)
    await typew.edit("`Kedua kamu manis`")
    sleep(1)
    await typew.edit("`Dan yang terakhir adalah kamu bukan jodohku`")
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
                     "\n**Permisi Aku mau nimbrung Kk..**")


@register(outgoing=True, pattern='^.geez(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**JAE Peler☑️**")
    await typew.edit("**JAE Peler✅**")
    sleep(1)
    await typew.edit("**SISKA Gilaa☑️**")
    await typew.edit("**SISKA Gilaa✅**")
    sleep(2)
    await typew.edit("**PUTRI Depresi☑️**")
    await typew.edit("**PUTRI Depresi✅**")
    sleep(2)
    await typew.edit("**VITA Gajelas☑️**")
    await typew.edit("**VITA Gajelas✅**")
    sleep(2)
    await typew.edit("**BUDI GJM!☑️**")
    await typew.edit("**BUDI GJM!✅**")
    sleep(2)
    await typew.edit("**DELA GJB!☑️**")
    await typew.edit("**DELA GJB!✅**")
    sleep(2)
    await typew.edit("**VERA,MengRibet☑️**")
    await typew.edit("**VERA,MengRibet✅**")
    sleep(2)
    await typew.edit("**ADIN,Mengintil☑️**")
    await typew.edit("**ADIN,Mengintil✅**")
    sleep(3)
    await typew.edit("**CUMA KIM YANG BENER!**")


@register(outgoing=True, pattern='^.lahk(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Lah ?`")
    sleep(1)
    await typew.edit("`Apa lo dungu?`")
    sleep(1)
    await typew.edit("`iya lu emng gblk kok`")
    sleep(1)
    await typew.edit("`gaush di jelsin gw tau lu gblk !`")


@register(outgoing=True, pattern='^.wah(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Wahh, War ya bang?`")
    sleep(2)
    await typew.edit("`buat apa sih bang`")
    sleep(2)
    await typew.edit("`lu kira keren? `")
    sleep(2)
    await typew.edit("`yang ada lu keliatan bego`")
    sleep(2)
    await typew.edit("`udhlh ngapain sok jago gitu.`")
    sleep(2)
    await typew.edit("`hdeeeh koar" mulu ga malu apa`")
    sleep(3)
    await typew.edit("`gw aja yang tinggal dengerin malu`")

CMD_HELP.update({
    "rambot":
    "`.rambot`\
    \nUsage: menampilkan alive bot.\
    \n\n`.sadboy`\
    \nUsage: hiks\
    \n\n`.punten` ; `.geez`\
    \nUsage: misi."
})
