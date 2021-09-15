# From vckyou Geez-Userbot
# WOI NGENTOT, KALO FORK KASIH BINTANG
# Yang apus kredit Lo ngentot!

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import bot, CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern=r"^\.limit(?: |$)(.*)")
async def _(event):
    await event.edit("`Proses Ngecek Limit akun, Gausah panik Tuan!...`")
    async with bot.conversation("@SpamBot") as conv:
        try: 
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=178220800)
            )
            await conv.send_message("/start")
            response = await response
            await bot.sen gad_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit("`Boss! Please Unblock @SpamBot`")
            return
        await event.edit(f"~ {response.message.message}")


CMD_HELP.update({"limit": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.limit`"
                 "\n•: ngecek akun kena limit atau gak"})
