# Yaa begitu lah

""" Userbot initialization. """

import logging
import os
import time
import re
import redis

from platform import uname
from sys import version_info
from logging import basicConfig, getLogger, INFO, DEBUG
from distutils.util import strtobool as sb
from math import ceil

from pylast import LastFMNetwork, md5
from pySmartDL import SmartDL
from pymongo import MongoClient
from datetime import datetime
from redis import StrictRedis
from markdown import markdown
from dotenv import load_dotenv
from requests import get
from telethon.network.connection.tcpabridged import ConnectionTcpAbridged
from telethon.sync import TelegramClient, custom, events
from telethon.sessions import StringSession
from telethon import Button, events, functions, types
from telethon.utils import get_display_name

redis_db = None

load_dotenv("config.env")

StartTime = time.time()

CMD_LIST = {}
# for later purposes
CMD_HELP = {}
INT_PLUG = ""
LOAD_PLUG = {}

# Bot Logs setup:
CONSOLE_LOGGER_VERBOSE = sb(os.environ.get("CONSOLE_LOGGER_VERBOSE", "False"))

if CONSOLE_LOGGER_VERBOSE:
    basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=DEBUG,
    )
else:
    basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                level=INFO)
LOGS = getLogger(__name__)

if version_info[0] < 3 or version_info[1] < 8:
    LOGS.info("You MUST have a python version of at least 3.8."
              "Multiple features depend on this. Bot quitting.")
    quit(1)

# Check if the config was edited by using the already used variable.
# Basically, its the 'virginity check' for the config file ;)
CONFIG_CHECK = os.environ.get(
    "___________PLOX_______REMOVE_____THIS_____LINE__________", None)

if CONFIG_CHECK:
    LOGS.info(
        "Please remove the line mentioned in the first hashtag from the config.env file"
    )
    quit(1)

# Telegram App KEY and HASH
API_KEY = os.environ.get("API_KEY", "")
API_HASH = os.environ.get("API_HASH", "")

# Userbot Session String
STRING_SESSION = os.environ.get("STRING_SESSION", "")

# Logging channel/group ID configuration.
BOTLOG_CHATID = int(os.environ.get("BOTLOG_CHATID", ""))

# Userbot logging feature switch.
BOTLOG = sb(os.environ.get("BOTLOG", "True"))
LOGSPAMMER = sb(os.environ.get("LOGSPAMMER", "False"))

# Bleep Blop, this is a bot ;)
PM_AUTO_BAN = sb(os.environ.get("PM_AUTO_BAN", "False"))

# Send .chatid in any group with all your administration bots (added)
G_BAN_LOGGER_GROUP = os.environ.get("G_BAN_LOGGER_GROUP", "")
if G_BAN_LOGGER_GROUP:
    G_BAN_LOGGER_GROUP = int(G_BAN_LOGGER_GROUP)

# Heroku Credentials for updater.
HEROKU_MEMEZ = sb(os.environ.get("HEROKU_MEMEZ", "False"))
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", "")
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", "")

# JustWatch Country
WATCH_COUNTRY = os.environ.get("WATCH_COUNTRY", "ID")

# Github Credentials for updater and Gitupload.
GIT_REPO_NAME = os.environ.get("GIT_REPO_NAME", None)
GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN", None)

# Custom (forked) repo URL for updater.
UPSTREAM_REPO_URL = os.environ.get(
    "UPSTREAM_REPO_URL",
    "https://github.com/ramadhani892/RAM-UBOT")
UPSTREAM_REPO_BRANCH = os.environ.get(
    "UPSTREAM_REPO_BRANCH", "RAM-UBOT")

# Console verbose logging
CONSOLE_LOGGER_VERBOSE = sb(os.environ.get("CONSOLE_LOGGER_VERBOSE", "False"))

# SQL Database URI
DB_URI = os.environ.get("DATABASE_URL", None)

# OCR API key
OCR_SPACE_API_KEY = os.environ.get("OCR_SPACE_API_KEY", None)

# remove.bg API key
REM_BG_API_KEY = os.environ.get("REM_BG_API_KEY", None)

# Redis URI & Redis Password
REDIS_URI = os.environ.get('REDIS_URI', None)
REDIS_PASSWORD = os.environ.get('REDIS_PASSWORD', None)

if REDIS_URI and REDIS_PASSWORD:
    try:
        REDIS_HOST = REDIS_URI.split(':')[0]
        REDIS_PORT = REDIS_URI.split(':')[1]
        redis_connection = redis.Redis(
            host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD
        )
        redis_connection.ping()
    except Exception as e:
        LOGGER.exception(e)
        print()
        LOGGER.error(
            "Make sure you have the correct Redis endpoint and password "
            "and your machine can make connections."
        )

# Chrome Driver and Headless Google Chrome Binaries
CHROME_DRIVER = os.environ.get("CHROME_DRIVER") or "/usr/bin/chromedriver"
GOOGLE_CHROME_BIN = os.environ.get(
    "GOOGLE_CHROME_BIN") or "/usr/bin/google-chrome"

# set to True if you want to log PMs to your PM_LOGGR_BOT_API_ID
NC_LOG_P_M_S = bool(os.environ.get("NC_LOG_P_M_S", False))
# send .get_id in any channel to forward all your NEW PMs to this group
PM_LOGGR_BOT_API_ID = int(os.environ.get("PM_LOGGR_BOT_API_ID", "-100"))

# OpenWeatherMap API Key
OPEN_WEATHER_MAP_APPID = os.environ.get("OPEN_WEATHER_MAP_APPID", None)
WEATHER_DEFCITY = os.environ.get("WEATHER_DEFCITY", None)

# Lydia API
LYDIA_API_KEY = os.environ.get("LYDIA_API_KEY", None)

# For MONGO based DataBase
MONGO_URI = os.environ.get("MONGO_URI", None)

# set blacklist_chats where you do not want userbot's features
UB_BLACK_LIST_CHAT = os.environ.get("UB_BLACK_LIST_CHAT", None)

# Anti Spambot Config
ANTI_SPAMBOT = sb(os.environ.get("ANTI_SPAMBOT", "False"))
ANTI_SPAMBOT_SHOUT = sb(os.environ.get("ANTI_SPAMBOT_SHOUT", "False"))

# Youtube API key
YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY", None)

# Untuk Perintah .rambot (alive)
RAM_TEKS_KOSTUM = os.environ.get("RAM_TEKS_KOSTUM") or "ㅤ"

# Untuk Melihat Repo
REPO_NAME = os.environ.get("REPO_NAME") or "⭐𝗥𝗔𝗠-𝗨𝗕𝗢𝗧⭐"

# DEVS only own id
DEVS = (
    5244176114,
    1826643972,
    5155140917,
)

# Default .alive Name
ALIVE_NAME = os.environ.get("ALIVE_NAME", None)

# Time & Date - Country and Time Zone
COUNTRY = str(os.environ.get("COUNTRY", "ID"))
TZ_NUMBER = int(os.environ.get("TZ_NUMBER", 1))

# Clean Welcome
CLEAN_WELCOME = sb(os.environ.get("CLEAN_WELCOME", "True"))

# Zipfile Module
ZIP_DOWNLOAD_DIRECTORY = os.environ.get("ZIP_DOWNLOAD_DIRECTORY", "./zips")

# bit.ly Module
BITLY_TOKEN = os.environ.get("BITLY_TOKEN", None)

# Bot Name
TERM_ALIAS = os.environ.get("TERM_ALIAS", "RAM-UBOT")

# Bot Version
BOT_VER = os.environ.get("BOT_VER", "7.0")

# Default .alive Username
ALIVE_USERNAME = os.environ.get("ALIVE_USERNAME", None)

# Sticker Custom Pack Name
S_PACK_NAME = os.environ.get("S_PACK_NAME", None)

# Default .alive Logo
ALIVE_LOGO = os.environ.get(
    "ALIVE_LOGO") or "https://telegra.ph/file/5e197cb47a4168c39f78f.jpg"

# Default .helpme logo
HELP_LOGO = os.environ.get(
   "HELP_LOGO") or "https://telegra.ph/file/5daa73aa6d1afbd1da353.jpg"

# Default .alive Instagram
IG_ALIVE = os.environ.get("IG_ALIVE") or "instagram.com/ramadh20"

# Default emoji help
EMOJI_HELP = os.environ.get("EMOJI_HELP") or "💫"

# Default .alive Group
GROUP_LINK = os.environ.get(
    "GROUP_LINK") or "t.me/geezsupport"

# Default .repo Bot
OWNER_BOT = os.environ.get(
    "OWNER_BOT") or "t.me/GeezProjectt"


# Last.fm Module
BIO_PREFIX = os.environ.get("BIO_PREFIX", None)
DEFAULT_BIO = os.environ.get("DEFAULT_BIO") or "⭐𝗥𝗔𝗠-𝗨𝗕𝗢𝗧⭐"

LASTFM_API = os.environ.get("LASTFM_API", None)
LASTFM_SECRET = os.environ.get("LASTFM_SECRET", None)
LASTFM_USERNAME = os.environ.get("LASTFM_USERNAME", None)
LASTFM_PASSWORD_PLAIN = os.environ.get("LASTFM_PASSWORD", None)
LASTFM_PASS = md5(LASTFM_PASSWORD_PLAIN)
if LASTFM_API and LASTFM_SECRET and LASTFM_USERNAME and LASTFM_PASS:
    lastfm = LastFMNetwork(api_key=LASTFM_API,
                           api_secret=LASTFM_SECRET,
                           username=LASTFM_USERNAME,
                           password_hash=LASTFM_PASS)
else:
    lastfm = None

# Google Drive Module
G_DRIVE_DATA = os.environ.get("G_DRIVE_DATA", None)
G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID", None)
G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", None)
G_DRIVE_AUTH_TOKEN_DATA = os.environ.get("G_DRIVE_AUTH_TOKEN_DATA", None)
G_DRIVE_FOLDER_ID = os.environ.get("G_DRIVE_FOLDER_ID", None)
TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TMP_DOWNLOAD_DIRECTORY",
                                         "./downloads")
# Google Photos
G_PHOTOS_CLIENT_ID = os.environ.get("G_PHOTOS_CLIENT_ID", None)
G_PHOTOS_CLIENT_SECRET = os.environ.get("G_PHOTOS_CLIENT_SECRET", None)
G_PHOTOS_AUTH_TOKEN_ID = os.environ.get("G_PHOTOS_AUTH_TOKEN_ID", None)
if G_PHOTOS_AUTH_TOKEN_ID:
    G_PHOTOS_AUTH_TOKEN_ID = int(G_PHOTOS_AUTH_TOKEN_ID)

# Genius Lyrics  API
GENIUS = os.environ.get("GENIUS_ACCESS_TOKEN", None)

# IMG Stuff
IMG_LIMIT = os.environ.get("IMG_LIMIT") or None
CMD_HELP = {}

# Quotes API Token
QUOTES_API_TOKEN = os.environ.get("QUOTES_API_TOKEN", None)

# Deezloader
DEEZER_ARL_TOKEN = os.environ.get("DEEZER_ARL_TOKEN", None)

# Photo Chat - Get this value from http://antiddos.systems
API_TOKEN = os.environ.get("API_TOKEN", None)
API_URL = os.environ.get("API_URL", "http://antiddos.systems")

# Inline bot helper
BOT_TOKEN = os.environ.get("BOT_TOKEN") or None
BOT_USERNAME = os.environ.get("BOT_USERNAME") or None

# Init Mongo
#MONGOCLIENT = MongoClient(MONGO_URI, 27017, serverSelectionTimeoutMS=1)
#MONGO = MONGOCLIENT.userbot


#def is_mongo_alive():
#    try:
#        MONGOCLIENT.server_info()
#    except BaseException:
#        return False
#    return True


# Init Redis
# Redis will be hosted inside the docker container that hosts the bot
# We need redis for just caching, so we just leave it to non-persistent
#REDIS = StrictRedis(host='localhost', port=6379, db=0)


#def is_redis_alive():
#    try:
#        REDIS.ping()
#        return True
#    except BaseException:
#        return False


# Setting Up CloudMail.ru and MEGA.nz extractor binaries,
# and giving them correct perms to work properly.
if not os.path.exists('bin'):
    os.mkdir('bin')

binaries = {
    "https://raw.githubusercontent.com/adekmaulana/megadown/master/megadown":
    "bin/megadown",
    "https://raw.githubusercontent.com/yshalsager/cmrudl.py/master/cmrudl.py":
    "bin/cmrudl"
}

for binary, path in binaries.items():
    downloader = SmartDL(binary, path, progress_bar=False)
    downloader.start()
    os.chmod(path, 0o755)

# 'bot' variable
if STRING_SESSION:
    # pylint: disable=invalid-name
    bot = TelegramClient(StringSession(STRING_SESSION), API_KEY, API_HASH)
else:
    # pylint: disable=invalid-name
    bot = TelegramClient("userbot", API_KEY, API_HASH)

async def check_botlog_chatid():
    if not BOTLOG_CHATID and LOGSPAMMER:
        LOGS.info(
            "You must set up the BOTLOG_CHATID variable in the config.env or environment variables, for the private error log storage to work."
        )
        quit(1)

    elif not BOTLOG_CHATID and BOTLOG:
        LOGS.info(
            "You must set up the BOTLOG_CHATID variable in the config.env or environment variables, for the userbot logging feature to work."
        )
        quit(1)

    elif not BOTLOG or not LOGSPAMMER:
        return

    entity = await bot.get_entity(BOTLOG_CHATID)
    if entity.default_banned_rights.send_messages:
        LOGS.info(
            "Your account doesn't have rights to send messages to BOTLOG_CHATID "
            "group. Check if you typed the Chat ID correctly.")
        quit(1)


with bot:
    try:
        bot.loop.run_until_complete(check_botlog_chatid())
    except BaseException:
        LOGS.info(
            "BOTLOG_CHATID environment variable isn't a "
            "valid entity. Check your environment variables/config.env file.")
        quit(1)

if BOT_TOKEN is not None:
    tgbot = TelegramClient(
        "TG_BOT_TOKEN",
        api_id=API_KEY,
        api_hash=API_HASH,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    ).start(bot_token=BOT_TOKEN)
else:
    tgbot = None


# Global Variables
COUNT_MSG = 0
USERS = {}
COUNT_PM = {}
ENABLE_KILLME = True
LASTMSG = {}
CMD_HELP = {}
ISAFK = False
AFKREASON = None
ZALG_LIST = {}

#Import Userbot - Ported by RAMADHANI892
from userbot import (
    ALIVE_NAME
)

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


def paginate_help(page_number, loaded_modules, prefix):
    number_of_rows = 5
    number_of_cols = 2
    global lockpage
    lockpage = page_number
    helpable_modules = [p for p in loaded_modules if not p.startswith("_")]
    helpable_modules = sorted(helpable_modules)
    modules = [
        custom.Button.inline(
            "{} {} {} ".format(f"{EMOJI_HELP}", x, f"{EMOJI_HELP}"),
            data="ub_modul_{}".format(x),
        )
        for x in helpable_modules
    ]
    pairs = list(zip(modules[::number_of_cols], modules[1::number_of_cols]))
    if len(modules) % number_of_cols == 1:
        pairs.append((modules[-1],))
    max_num_pages = ceil(len(pairs) / number_of_rows)
    modulo_page = page_number % max_num_pages
    if len(pairs) > number_of_rows:
        pairs = pairs[
            modulo_page * number_of_rows: number_of_rows * (
                modulo_page + 1)] + [
            (custom.Button.inline(
                "<ʙᴀᴄᴋ​", data="{}_prev({})".format(
                    prefix, modulo_page)), custom.Button.inline(
                        "ᴍᴇɴᴜ", data="{}_close({})".format(
                            prefix, modulo_page)), custom.Button.inline(
                                "ɴᴇxᴛ>>", data="{}_next({})".format(
                                    prefix, modulo_page)), )]
    return pairs


with bot:
    try:
        tgbot = TelegramClient(
            "TG_BOT_TOKEN",
            api_id=API_KEY,
            api_hash=API_HASH).start(
            bot_token=BOT_TOKEN)

        dugmeler = CMD_HELP
        user = bot.get_me()
        uid = user.id

        @ tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile("open")
            )
        )
        async def opeen(event):
            try:
                tgbotusername = BOT_USERNAME
                if tgbotusername is not None:
                    results = await event.client.inline_query(
                        tgbotusername, "@Ram_ubot"
                    )
                    await results[0].click(
                        event.chat_id, reply_to=event.reply_to_msg_id, hide_via=True
                    )
                    await event.delete()
                else:
                    await event.edit(
                        "`The bot doesn't work! Please set the Bot Token and Username correctly. The module has been stopped.`"
                    )
            except Exception:
                return await event.edit("⛔ **Kamu Tidak Diizinkan Untuk Menekan Nya**!")

        ramlogo = HELP_LOGO
        plugins = CMD_HELP
        vr = BOT_VER

        # ------------------------------ChatAction--------------->

        @tgbot.on(events.ChatAction)
        async def handler(event):
            if event.user_joined or event.user_added:
                u = await event.client.get_entity(event.chat_id)
                c = await event.client.get_entity(event.user_id)
                await event.reply(
                    f"** Selamat Datang Digrub **👋\n"
                    f"[{get_display_name(u)}](tg: // user?id={u.id})\n"
                    f"────────────────────\n"
                    f"📮 ** Nama: ** [{get_display_name(c)}](tg: // user?id={c.id})\n"
                    f"────────────────────\n"
                    f"✏️ ** ID: ** {c.id}\n"
                    f"────────────────────\n"
                    f"🤴 **ʙᴏᴛᴏꜰ: ** {DEFAULTUSER}\n\n"
                    f"➠ ** Ketik ** /rules supaya tahu peraturan Group ini\n"
                    f"➠ **Atau** Kalian Bisa Klik /notes Dibawah Jika Ada\n",
                    buttons=[
                        [Button.url("【﻿Ｃｈａｎｎｅｌ】",
                                    "https://t.me/geezprojectt")],
                    ],
                )

        # ====================================InlineHandler===================================== #

        @tgbot.on(events.NewMessage(pattern="/start"))
        async def handler(event):
            if event.message.from_id != uid:
                await event.client.get_entity(event.chat_id)
                await event.reply(
                    f"{START_WELCOME}\n\n**Powered By** : @Ram-ubot\n\n",
                    buttons=[
                        [
                            custom.Button.inline("ꜱᴇᴛᴛɪɴɢꜱ", data="settings"),
                            custom.Button.inline("ɪɴꜰᴏ", data="about"),
                        ],
                        [custom.Button.inline("ᴍᴇɴᴜ", data="kanan")],
                    ],
                )
            else:
                reply_pop_up_alert = f"🚫!WARNING!🚫 Jangan Menggunakan Milik {DEFAULTUSER} Nanti Kena Ghosting."
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @tgbot.on(events.NewMessage(pattern="/ping"))
        async def handler(event):
            if event.message.from_id != uid:
                start = datetime.now()
                end = datetime.now()
                ms = (end - start).microseconds / 1000
                await tgbot.send_message(
                    event.chat_id,
                    f"**PONG!!**\n `{ms}ms`",
                )

        @tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(f"open_plugin")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid:
                buttons = paginate_help(0, dugmeler, "helpme")
                text = f"Usᴇʀʙᴏᴛ Tᴇʟᴇɢʀᴀᴍ\n\n❥ **ʙᴏᴛ ᴏꜰ :** {DEFAULTUSER}\n❥ **ʙᴏᴛ ᴠᴇʀ :** 5.0\n❥ **ᴍᴏᴅᴜʟᴇꜱ :** {len(plugins)}\n❥ @GeezSupport "
                await event.edit(
                    text,
                    file=ramlogo,
                    buttons=buttons,
                    link_preview=False,
                )
            else:
                reply_pop_up_alert = f"❌ WARNINGS ❌\n\nAnda Tidak Mempunyai Hak Untuk Menekan Tombol Button Ini."
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"nepo")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            current_page_number = int(lockpage)
            buttons = paginate_help(current_page_number, plugins, "helpme")
            await event.edit(
                file=ramlogo,
                buttons=buttons,
                link_preview=False,
            )

        @tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"about")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid:
                text = (
                    f"❁ __Saya Adalah RAM-UBOT Yang Digunakan Banyak User Telegram__.\n\n"
                    f"❁ __Saya Dibuat Hanya Untuk Bersenang Senang Ditelegram__.\n\n"
                    f"❁ __Kelebihan Saya Banyak, Saya Mempunyai 180 Modules__.\n\n"
                    f"© @teervigroup")
                await event.edit(
                    text,
                    file=ramlogo,
                    link_preview=True,
                    buttons=[
                        [custom.Button.inline("ᴄʟᴏꜱᴇ", data="closed")],
                    ],
                )
            else:
                reply_pop_up_alert = f"🤴 Name : {DEFAULTUSER}\n🤖 Bot Ver : 7.0\n🛠 Modules : {len(plugins)}\n✨ Branch : RAM-UBOT"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"settings")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid:
                text = f"{DEFAULTUSER}Pilih dari opsi di bawah ini :"
                await event.edit(
                    text,
                    file=ramlogo,
                    link_preview=True,
                    buttons=[
                        [custom.Button.inline("ᴀʟɪᴠᴇ", data="alive")],
                        [custom.Button.inline("ᴘᴍᴘᴇʀᴍɪᴛ", data="permirt")],
                        [custom.Button.inline("ᴘᴍʙᴏᴛ", data="pmbot")],
                        [custom.Button.inline(
                            "ɪɴʟɪɴᴇ ᴍᴏᴅᴇ ", data="inline_mode")],
                        [custom.Button.inline("ᴍᴇɴᴜ", data="kanan")],
                    ],
                )
            else:
                reply_pop_up_alert = f"❌ DISCLAIMER ❌\n\nAnda Tidak Mempunyai Hak Untuk Menekan Tombol Button Ini"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"kanan")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid:
                text = f"Menu Lainnya ! Untuk {DEFAULTUSER}"
                await event.edit(
                    text,
                    file=ramlogo,
                    link_preview=True,
                    buttons=[
                        [custom.Button.inline("ᴜᴘᴅᴀᴛᴇ", data="pembaruan")],
                        [custom.Button.inline("ᴘɪɴɢ", data="ping")],
                        [custom.Button.inline("ᴄᴇᴋ ᴅʏɴᴏ", data="restart_bot")],
                        [custom.Button.inline("ʟᴇꜰᴛ", data="settings")],
                    ],
                )
            else:
                reply_pop_up_alert = f"❌ DISCLAIMER ❌\n\nAnda Tidak Mempunyai Hak Untuk Menekan Tombol Button Ini"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"alive")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid:
                text = (
                    f"Modules Name **Alive**\n\n"
                    f"× `.alive` × `.rambot` × `.xalive`\n"
                    f"°__Menampilkan Alive Punya Kamu__.\n\n"
                    f"× `.set var ALIVE_LOGO` [**LINK**]\n"
                    f"°__Mengubah Foto Alive Kamu, Yang Kamu Inginkan__.\n\n"
                    f"× `.set var RAM_TEKS_KOSTUM` [**TEKS**]\n"
                    f"°__Mengganti Teks Yang Ada Command ramalivie__.\n\n"
                    f"© @geezsupport"
                )
                await event.edit(
                    text,
                    file=ramlogo,
                    link_preview=True,
                    buttons=[
                        [
                            custom.Button.inline("ʙᴀᴄᴋ", data="settings"),
                            custom.Button.inline("ᴄʟᴏꜱᴇ", data="closed"),
                        ],
                    ],
                )
            else:
                reply_pop_up_alert = f"❌ DISCLAIMER ❌\n\nAnda Tidak Mempunyai Hak Untuk Menekan Tombol Button Ini"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"permirt")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid:
                text = (
                    f"Modules Name **pmpermit**\n\n"
                    f"× `.set var PM_AUTO_BAN True`\n"
                    f"°__Mengaktifkan Pmpermit Kalian Atau Disebut Pesan Otomatis__.\n\n"
                    f"× `.set pm_msg` [**REPLYCHAT**]\n"
                    f"°__Mengganti Teks Pmpermit Selera Kamu__.\n\n"
                    f"© @geezsupport")
                await event.edit(
                    text,
                    file=ramlogo,
                    link_preview=True,
                    buttons=[
                        [
                            custom.Button.inline("ʙᴀᴄᴋ", data="settings"),
                            custom.Button.inline("ᴄʟᴏꜱᴇ", data="closed"),
                        ],
                    ],
                )
            else:
                reply_pop_up_alert = f"❌ DISCLAIMER ❌\n\nAnda Tidak Mempunyai Hak Untuk Menekan Tombol Button Ini"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"inline_mode")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid:
                text = (
                    f"Modules Name **inline**\n\n"
                    f"× `.set var EMOJI_HELP` [**EMOJI**]\n"
                    f"°__Mengubah Emoji Inline Yang Ada Dicomand__ `.rhelp`\n\n"
                    f"× `.set var HELP_LOGO` [**LINK**]\n"
                    f"°__Mengubah Foto Yang Ada Dicomand__ `.rhelp`\n\n"
                    f"© @Geezprojectt")
                await event.edit(
                    text,
                    file=ramlogo,
                    link_preview=True,
                    buttons=[
                        [
                            custom.Button.inline("ʙᴀᴄᴋ", data="settings"),
                            custom.Button.inline("ᴄʟᴏꜱᴇ", data="closed"),
                        ],
                    ],
                )
            else:
                reply_pop_up_alert = f"❌ DISCLAIMER ❌\n\nAnda Tidak Mempunyai Hak Untuk Menekan Tombol Button Ini"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"pmbot")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid:
                text = (
                    f"Modules Name **pmbot**\n\n"
                    f"× `.set var START_WELCOME` [**TEKS**] \n"
                    f"°__Kamu Juga Bisa Mengubah Start Welcome Untuk Bot Kamu Yang Ini, Dengan Cara Diatas Dan Kata Kata Bebas__.\n\n"
                    f"© @geezsupport")
                await event.edit(
                    text,
                    file=ramlogo,
                    link_preview=True,
                    buttons=[
                        [
                            custom.Button.inline("ʙᴀᴄᴋ", data="settings"),
                            custom.Button.inline("ᴄʟᴏꜱᴇ", data="closed"),
                        ],
                    ],
                )
            else:
                reply_pop_up_alert = f"❌ DISCLAIMER ❌\n\nAnda Tidak Mempunyai Hak Untuk Menekan Tombol Button Ini"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"pembaruan")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid:
                text = (
                    f"Modules Name **Pembaruan**\n\n"
                    f"× **Pembaruan Data Untuk RAM-UBOT Command Untuk Pembaruan**.\n"
                    f"⚒Pembaruan Data :\n"
                    f"`.update all`\n"
                    f"`update`\n\n"
                    f"© @TeerviGroup")
                await event.edit(
                    text,
                    file=ramlogo,
                    link_preview=True,
                    buttons=[
                        [
                            custom.Button.inline("ʙᴀᴄᴋ", data="kanan"),
                            custom.Button.inline("ᴄʟᴏꜱᴇ", data="closed"),
                        ],
                    ],
                )
            else:
                reply_pop_up_alert = f"❌ DISCLAIMER ❌\n\nAnda Tidak Mempunyai Hak Untuk Menekan Tombol Button Ini"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"ping")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid:
                start = datetime.now()
                end = datetime.now()
                ms = (end - start).microseconds / 1000
                text = f"**PONG!!**\n `{ms}ms`"
                await event.edit(
                    text,
                    file=ramlogo,
                    link_preview=True,
                    buttons=[
                        [custom.Button.inline("ʙᴀᴄᴋ", data="kanan")],
                    ],
                )
            else:
                reply_pop_up_alert = f"PONG!!\n `{ms}ms`"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"dyno_usage")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if apps.get("app_uuid") == app.id:
                apps.get("quota_used") / 60
                AppPercentage = math.floor(
                    apps.get("quota_used") * 100 / quota)
                text = (
                    "✥ **ɪɴꜰᴏʀᴍᴀsɪ ᴅʏɴᴏ ʜᴇʀᴏᴋᴜ :**\n"
                    "╔════════════════════╗\n"
                    f" ✥ **ᴘᴇɴɢɢᴜɴᴀ ᴅʏɴᴏ sᴀᴀᴛ ɪɴɪ :**\n"
                    f"  ➠  `{AppHours}`**ᴊᴀᴍ**  `{AppMinutes}`**ᴍᴇɴɪᴛ**  "
                    f"**|**  [`{AppPercentage}`**%**]"
                    "\n◖════════════════════◗\n"
                    " ✥ **sɪsᴀ ᴋᴏᴜᴛᴀ ᴅʏɴᴏ ʙᴜʟᴀɴ ɪɴɪ :**\n"
                    f"  ➠  `{hours}`**ᴊᴀᴍ**  `{minutes}`**ᴍᴇɴɪᴛ**  "
                    f"**|**  [`{percentage}`**%**]\n"
                    f" ✥ **✦҈͜͡ᴘᴇᴍɪʟɪᴋ :** {ALIVE_NAME}  "
                    "\n╚════════════════════╝"
                    f"✥ **Sisa Dyno Heroku** `{day}` **Hari Lagi**"
                    f"© @GeezSupport"
                )
                await event.edit(
                    text,
                    file=ramlogo,
                    link_preview=True,
                    buttons=[
                        [custom.Button.inline("ʙᴀᴄᴋ", data="kanan")],
                    ],
                )
            else:
                reply_pop_up_alert = f"❌ DISCLAIMER ❌\n\nAnda Tidak Mempunyai Hak Untuk Menekan Tombol Button Ini"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"restart_bot")
            )
        )
        async def killdabot(event):
            if event.query.user_id == uid:
                text = f"**Restaring RAM-UBOT**..."
                await event.edit(
                    text,
                    file=ramlogo,
                    link_preview=True,
                    buttons=[
                        [custom.Button.inline("ʙᴀᴄᴋ", data="kanan")],
                    ],
                )

        @tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"closed")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid:
                text = f"Closed Menu!"
                await event.edit(
                    text,
                    file=ramlogo,
                    link_preview=True,
                    buttons=[
                        [Button.url("ᴄʜᴀɴɴᴇʟ", "t.me/GeezProjectt")],
                    ],
                )

        @tgbot.on(events.InlineQuery)  # pylint:disable=E0602
        async def inline_handler(event):
            builder = event.builder
            result = None
            query = event.text
            if event.query.user_id == uid and query.startswith(""):
                buttons = paginate_help(0, dugmeler, "helpme")
                result = builder.photo(
                    file=ramlogo,
                    link_preview=False,
                    text=f"Usᴇʀʙᴏᴛ Tᴇʟᴇɢʀᴀᴍ\n\n❥ **ʙᴏᴛ ᴏꜰ :** {DEFAULTUSER}\n❥ **ʙᴏᴛ ᴠᴇʀ :** 5.0\n❥ **ᴍᴏᴅᴜʟᴇꜱ :** {len(plugins)}\n❥ @geezsupport".format(
                        len(dugmeler),
                    ),
                    buttons=buttons,
                )
            elif query.startswith("tb_btn"):
                result = builder.article(
                    "Bantuan Dari **⚡RAM-UBOT⚡**",
                    text="Daftar Plugins",
                    buttons=[],
                    link_preview=True,
                )
            else:
                result = builder.article(" **⚡RAM-UBOT**",
                                         text="""•RAM-UBOT•""",
                                         buttons=[[custom.Button.url("RAM-UBOT",
                                                                     "https://github.com/ramadhani892/RAM-UBOT"),
                                                   custom.Button.url("ᴄʜᴀɴɴᴇʟ​",
                                                                     "t.me/geezprojectt"),
                                                   ],
                                                  [custom.Button.url("ʟɪᴄᴇɴsᴇ​",
                                                                     "https://github.com/ramadhani892/RAM-UBOT/LICENSE",
                                                                     )],
                                                  ],
                                         link_preview=False,
                                         )
            await event.answer([result] if result else None)

        @tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"helpme_next\((.+?)\)")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid:  # pylint:disable=E0602
                current_page_number = int(
                    event.data_match.group(1).decode("UTF-8"))
                buttons = paginate_help(
                    current_page_number + 1, dugmeler, "helpme")
                # https://t.me/TelethonChat/115200
                await event.edit(buttons=buttons)
            else:
                reply_pop_up_alert = (
                    f"🚫!WARNING!🚫 Jangan Menggunakan Milik {DEFAULTUSER}."
                )
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"helpme_close\((.+?)\)")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid:  # userbot
                # https://t.me/TelethonChat/115200
                await event.edit(
                    file=ramlogo,
                    link_preview=True,
                    buttons=[
                        [
                            Button.url("❈ꜱᴜᴘᴘᴏʀᴛ❈", "t.me/geezsupport"),
                            Button.url("❈ᴄʜᴀɴɴᴇʟ❈", "t.me/geezprojectt"),
                        ],
                        [custom.Button.inline(
                            "°ᴏᴘᴇɴ ᴍᴇɴᴜ°", data="open_plugin")],
                        [custom.Button.inline("°ᴄʟᴏꜱᴇ ɪɴʟɪɴᴇ°", b"close")],
                    ],
                )

        @tgbot.on(events.CallbackQuery(data=b"close"))
        async def close(event):
            buttons = [
                (custom.Button.inline("Open Menu", data="open_plugin"),),
            ]
            await event.edit(f"Menu Ditutup! ", buttons=buttons)

        @tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"helpme_prev\((.+?)\)")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid:  # pylint:disable=E0602
                current_page_number = int(
                    event.data_match.group(1).decode("UTF-8"))
                buttons = paginate_help(
                    current_page_number - 1, dugmeler, "helpme"  # pylint:disable=E0602
                )
                # https://t.me/TelethonChat/115200
                await event.edit(buttons=buttons)
            else:
                reply_pop_up_alert = (
                    f"🚫!WARNING!🚫 Jangan Menggunakan Milik {DEFAULTUSER}."
                )
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"ub_modul_(.*)")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid:  # pylint:disable=E0602
                modul_name = event.data_match.group(1).decode("UTF-8")

                cmdhel = str(CMD_HELP[modul_name])
                if len(cmdhel) > 180:
                    help_string = (
                        str(CMD_HELP[modul_name]).replace("`", "")[:180]
                        + "..."
                        + "\n\nBaca Text Berikutnya Ketik .help "
                        + modul_name
                        + " "
                    )
                else:
                    help_string = str(CMD_HELP[modul_name]).replace("`", "")

                reply_pop_up_alert = (
                    help_string
                    if help_string is not None
                    else "{} No document has been written for module.".format(
                        modul_name
                    )
                )
            else:
                reply_pop_up_alert = (
                    f"🚫!WARNING!🚫 Jangan Menggunakan Milik {DEFAULTUSER}."
                )

            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

    except BaseException:
        LOGS.info(
            "Mode Inline Bot Mu Nonaktif. "
            "Untuk Mengaktifkannya, Silahkan Pergi Ke @BotFather Lalu, Settings Bot > Pilih Mode Inline > Turn On. "
        )
    try:
        bot.loop.run_until_complete(check_botlog_chatid())
    except BaseException:
        LOGS.info(
            "BOTLOG_CHATID Environment Variable Isn't a "
            "Valid Entity. Please Check Your Environment variables/config.env File.")
        quit(1)
