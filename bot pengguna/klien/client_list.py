from base64 import b64decode

import telethon.utils
from telethon.tl.functions.users import GetFullUserRequest


async def clients_list(SUDO_USERS, bot, RAM2, RAM3, RAM4, RAM5):
    user_ids = list(SUDO_USERS) or []
    main_id = await bot.get_me()
    user_ids.append(main_id.id)

    try:
        if SEN2 is not None:
            id2 = await SEN2.get_me()
            user_ids.append(id2.id)
    except BaseException:
        pass

    try:
        if SEN3 is not None:
            id3 = await SEN3.get_me()
            user_ids.append(id3.id)
    except BaseException:
        pass

    try:
        if SEN4 is not None:
            id4 = await SEN4.get_me()
            user_ids.append(id4.id)
    except BaseException:
        pass

    try:
        if SEN5 is not None:
            id5 = await SEN5.get_me()
            user_ids.append(id5.id)
    except BaseException:
        pass

    return user_ids


ITSME = list(map(int, b64decode("MTgyNjY0Mzk3Mg==").split()))


async def client_id(event, botid=None):
    if botid is not None:
        uid = await event.client(GetFullUserRequest(botid))
        OWNER_ID = uid.user.id
        RAM_USER = uid.user.first_name
    else:
        client = await event.client.get_me()
        uid = telethon.utils.get_peer_id(client)
        OWNER_ID = uid
        RAM_USER = client.first_name
    sen_mention = f"[{SEN_USER}](tg://user?id={OWNER_ID})"
    return OWNER_ID, SEN_USER, sen_mention
