"""
credits to @mrconfused
dont edit credits
"""


from telethon.tl.types import (
    MessageEntityMentionName)
from telethon.tl.functions.contacts import BlockRequest, UnblockRequest

from userbot.events import register
from userbot import ALIVE_NAME, CMD_HELP


async def get_user_from_event(event):
    args = event.pattern_match.group(1).split(':', 1)
    extra = None
    if event.reply_to_msg_id and not len(args) == 2:
        previous_message = await event.get_reply_message()
        user_obj = await event.client.get_entity(previous_message.from_id)
        extra = event.pattern_match.group(1)
    elif len(args[0]) > 0:
        user = args[0]
        if len(args) == 2:
            extra = args[1]
        if user.isnumeric():
            user = int(user)
        if not user:
            await event.edit(f"`{ALIVE_NAME}`: **Kasih Gua nama pengguna,atau id nya kak!!**")
            return
        if event.message.entities is not None:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(probable_user_mention_entity,
                          MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        try:
            user_obj = await event.client.get_entity(user)
        except Exception as err:
            return await event.edit("Sepertinya Ada Kesalahan \n **Kesalahan**\n", str(err))
    return user_obj, extra


async def get_user_from_id(user, event):
    if isinstance(user, str):
        user = int(user)
    try:
        user_obj = await event.client.get_entity(user)
    except (TypeError, ValueError) as err:
        await event.edit(str(err))
        return None
    return user_obj

try:
    from userbot import client2, client3
except BaseException:
    client2 = client3 = None


@register(outgoing=True, pattern=r"^\.gkick(?: |$)(.*)")
async def gspide(rk):
    lazy = rk
    sender = await lazy.get_sender()
    me = await lazy.client.get_me()
    if not sender.id == me.id:
        rkp = await lazy.reply("`Proses global kick si e'ek !!!`")
    else:
        rkp = await lazy.edit("`Proses Global Kick si e'ek...!`")
    me = await rk.client.get_me()
    await rkp.edit(f"`{ALIVE_NAME}:` **Melakukan Aksi Global Kick..**")
    my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id)
    f"@{me.username}" if me.username else my_mention
    await rk.get_chat()
    a = b = 0
    if rk.is_private:
        user = rk.chat
        reason = rk.pattern_match.group(1)
    else:
        rk.chat.title
    try:
        user, reason = await get_user_from_event(rk)
    except BaseException:
        pass
    try:
        if not reason:
            reason = 'Private'
    except BaseException:
        return await rkp.edit(f"`{ALIVE_NAME}`, **Kesalahan! Pengguna tidak dikenal.**")
    if user:
        if user.id == 1547381425:
            return await rkp.edit(f"`ETTSSS, LU GABISA GKICK TUAN MUDA,GW SETIA SAMA TUAN MUDA..!!` ")
        try:
            await rk.client(BlockRequest(user))
            await rk.client(UnblockRequest(user))
        except BaseException:
            pass
        testrk = [d.entity.id for d in await rk.client.get_dialogs() if (d.is_group or d.is_channel)]
        for i in testrk:
            try:
                await rk.client.edit_permissions(i, user, view_messages=False)
                await rk.client.edit_permissions(i, user, send_messages=True)
                a += 1
                await rkp.edit(f"`{ALIVE_NAME} :` **Melakukan Aksi\nGlobal Kick dalam {a} obrolan.....**")

            except BaseException:
                b += 1
    else:
        await rkp.edit(f"`{ALIVE_NAME}:` **Balas ke pengguna !! **")

    return await rkp.edit(f"`{ALIVE_NAME}:` **Melakukan Aksi Global Kick Pada [{user.first_name}](tg://user?id={user.id}) Dalam {a} obrolan(s) **")

CMD_HELP.update({
    "gkick": "\
`.gkick <alasan>`\
\nUsage: Membantumu mengeluarkan seseorang secara global dari grup yang kamu masuki bersamanya."
})
