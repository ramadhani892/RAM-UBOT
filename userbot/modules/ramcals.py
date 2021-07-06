# Thanks Full To Team Ultroid
# Ported By Vcky @VckyouuBitch + @MaafGausahSokap
# Copyright (c) 2021 Geez - Projects
# Geez - Projects https://github.com/Vckyou/Geez-UserBot
# RAM - UBOT https://github.com/ramadhani892/RAM-UBOT
# Ini Belum Ke Fix Ya Bg :')
# Ambil aja gapapa tp Gaguna kaya hidup lu Woakkakaka


from telethon.tl.functions.channels import GetFullChannelRequest as getchat
from telethon.tl.functions.phone import CreateGroupCallRequest as startvc
from telethon.tl.functions.phone import DiscardGroupCallRequest as stopvc
from telethon.tl.functions.phone import GetGroupCallRequest as getvc
from telethon.tl.functions.phone import InviteToGroupCallRequest as invitetovc

from telethon.tl.types import ChatAdminRights
from userbot import CMD_HELP
from userbot.events import register

NO_ADMIN = "`LU BUKAN ADMIN NGENTOT!!`"


async def get_call(event):
    rambot = await event.client(getchat(event.chat_id))
    rama = await event.client(getvc(rambot.full_chat.call))
    return rama.call


def user_list(l, n):
    for i in range(0, len(l), n):
        yield l[i: i + n]


@register(outgoing=True, pattern=r"^\.startvc$", groups_only=True)
async def _(rambot):
    chat = await rambot.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not admin and not creator:
        return await rambot.edit(NO_ADMIN)
    new_rights = ChatAdminRights(invite_users=True)
    try:
        await rambot.client(startvc(rambot.chat_id))
        await rambot.edit("`OBROLAN SUARA DIMULAI, YANG ONCAM GUA KEPLAK PALA LU...`")
    except Exception as ex:
        await rambot.edit(f"`{str(ex)}`")


@register(outgoing=True, pattern=r"^\.stopvc$", groups_only=True)
async def _(rambot):
    chat = await rambot.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not admin and not creator:
        return await rambot.edit(NO_ADMIN)
    new_rights = ChatAdminRights(invite_users=True)
    try:
        await rambot.client(stopvc(await get_call(rambot)))
        await rambot.edit("`OBROLAN SUARA DIHENTIKAN, JANGAN KAYA JAMET VCG MULU...`")
    except Exception as ex:
        await rambot.edit(f"`{str(ex)}`")


@register(outgoing=True, pattern=r"^\.vcinvite", groups_only=True)
async def _(rambot):
    await rambot.edit("`Memulai Invite member group...`")
    users = []
    z = 0
    async for x in rambot.client.iter_participants(rambot.chat_id):
        if not x.bot:
            users.append(x.id)
    hmm = list(user_list(users, 6))
    for p in hmm:
        try:
            await rambot.client(invitetovc(call=await get_call(rambot), users=p))
            z += 6
        except BaseException:
            pass
    await rambot.edit(f"`Menginvite {z} Member`")


CMD_HELP.update(
    {
        "ramcalls": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.startvc`\
         \n↳ : Memulai Obrolan Suara dalam Group.\
         \n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.stopvc`\
         \n↳ : `Menghentikan Obrolan Suara Pada Group.`\
         \n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.vcinvite`\
         \n↳ : Invite semua member yang berada di group. (Kadang bisa kadang kaga)."
    }
)
