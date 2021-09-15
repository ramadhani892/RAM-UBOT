from userbot.events import register
from userbot import CMD_HELP, bot


@register(outgoing=True, pattern="^.gcast (.*)")
async def gcast(event):
    xx = event.pattern_match.group(1)
    if not xx:
        return await event.edit("`Pesannya Mana kak?`")
    tt = event.text
    msg = tt[6:]
    kk = await event.edit("`Sabar Lg gua kirim kak, Limit jangan salain gua...`")
    er = 0
    done = 0
    async for x in bot.iter_dialogs():
        if x.is_group:
            chat = x.id
            try:
                done += 1
                await bot.send_message(chat, msg)
            except BaseException:
                er += 1
    await kk.edit(f"**Berhasil Mengirim Pesan Ke** `{done}` **Grup, Gagal Mengirim Pesan Ke** `{er}` **Grup**")


@register(outgoing=True, pattern=r"^\.gucast(?: |$)(.*)")
async def gucast(event):
    xx = event.pattern_match.group(1)
    if not xx:
        return await event.edit("`Pesan nya Mana kak?`")
    tt = event.text
    msg = tt[7:]
    kk = await event.edit("`Sedang Mengirim pesan secara global...`")
    er = 0
    done = 0
    async for x in bot.iter_dialogs():
        if x.is_user and not x.entity.bot:
            chat = x.id
            try:
                done += 1
                await bot.send_message(chat, msg)
            except BaseException:
                er += 1
    await kk.edit(f"Berhasil Mengirim Pesan Ke `{done}` obrolan, kesalahan dalam `{er}` obrolan(s)")


CMD_HELP.update(
    {
        "gcast": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.gcast`\
         \n↳ : Mengirim Pesan Group Secara Global."})

CMD_HELP.update(
    {
         "gucast": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.gucast`\
         \n↳ : Mengirim Pesan Pribadi Secara Global."
    }
)
