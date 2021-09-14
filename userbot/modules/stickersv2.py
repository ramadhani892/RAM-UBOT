from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
import io
from userbot import bot, CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern="^.itos$")
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("sir this is not a image message reply to image message")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        await event.edit("TUAN MUDA, ini bukan sebuah gambar ")
        return
    chat = "@buildstickerbot"
    await event.edit("Membuat Sticker...,sabar dulu tuan muda")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=164977173))
            msg = await event.client.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.reply("jangan blokir (@buildstickerbot) dan coba lagi")
            return
        if response.text.startswith("Hi!"):
            await event.edit("Can you kindly disable your forward privacy settings for good?")
        else:
            await event.delete()
            await bot.send_read_acknowledge(conv.chat_id)
            await event.client.send_message(event.chat_id, response.message)
            await event.client.delete_message(event.chat_id, [msg.id, response.id])


@register(outgoing=True, pattern="^.get$")
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("`Mohon Balas Ke Sticker.`")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        await event.edit("`Mohon Balas Ke Sticker.`")
        return
    chat = "@stickers_to_image_bot"
    await event.edit("`Mengubah Menjadi Gambar....`")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=611085086))
            msg = await event.client.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.reply("Buka Blokir @stickers_to_image_bot Lalu Coba Lagi")
            return
        if response.text.startswith("I understand only stickers"):
            await event.edit("`ngapunten,saya Tidak Bisa Mengubah Ini Menjadi Gambar, jajal delok neh opo iku Sticker Animasi?`")
        else:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=611085086))
            response = await response
            if response.text.startswith("..."):
                response = conv.wait_event(
                    events.NewMessage(
                        incoming=True,
                        from_users=611085086))
                response = await response
                await event.delete()
                await event.client.send_message(event.chat_id, response.message, reply_to=reply_message.id)
                await event.client.delete_message(event.chat_id, [msg.id, response.id])
            else:
                await event.edit("`jajal neh!!!`")
        await bot.send_read_acknowledge(conv.chat_id)


@register(outgoing=True, pattern="^.stoi$")
async def sticker_to_png(sticker):
    if not sticker.is_reply:
        await sticker.edit("`NULL information to feftch...`")
        return False

    img = await sticker.get_reply_message()
    if not img.document:
        await sticker.edit("`Maaf,Iki ora stiker Cok!! Matamu melek Ben roh`")
        return False

    await sticker.edit("`Berhasil Mengambil Sticker!`")
    image = io.BytesIO()
    await sticker.client.download_media(img, image)
    image.name = "sticker.png"
    image.seek(0)
    await sticker.client.send_file(
        sticker.chat_id, image, reply_to=img.id, force_document=True
    )
    await sticker.delete()
    return


CMD_HELP.update(
    {
        "stickers2": ">`.itos`"
        "\nUsage: Balas ke sticker atau gambar .itos untuk mengambil sticker bukan ke pack "
        "\n\n>`.get`"
        "\nUsage: Balas ke sticker untuk mendapatkan file 'PNG' sticker."
        "\n\n>`.stoi`"
        "\nUsage: Balas Ke sticker untuk mendapatkan file 'PNG' sticker."})
