""" Userbot module for other small commands. """
from userbot import CMD_HELP, ALIVE_NAME
from userbot.events import register


# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.helpmy$")
async def usit(e):
    await e.edit(
        f"**Hai {DEFAULTUSER} Kalau Anda Tidak Tau Perintah Untuk Memerintah Ku Ketik** `.helpmek` Atau Bisa `.help` atau Minta Bantuan Ke:\n"
        "\n[AZEL🦔](t.me/Deadendzs)"
        "\n\n[SUPPORT](https://t.me/geezsupportgroup)"
        "\n\n[CHANNEL](https://t.me/ramubotinfo)")


@register(outgoing=True, pattern="^.mekvars$")
async def var(m):
    await m.edit(
        f"**Disini Daftar Vars Dari {DEFAULTUSER}:**\n"
        "\n[DAFTAR VARS](https://raw.githubusercontent.com/azelfirdaus/JEM-BOT/JEM-BOT/varshelper.txt)")


CMD_HELP.update({
    "ramhelper":
    "`.helpmy`\
\nPenjelasan: Bantuan Untuk JEM-BOT.\
\n`.mekvars`\
\nPenjelasan: Untuk Melihat Beberapa Daftar Vars."
})
