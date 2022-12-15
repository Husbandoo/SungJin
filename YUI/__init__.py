import os
import logging
import sys
import time
#from YUI.config import OWNER_ID, DEV_USERS, DEMONS, DRAGONS, TOKEN, WORKERS, API_HASH, API_ID, WOLVES, ARQ_API_KEY, TIGERS
from pyrogram import Client, filters
from aiohttp import ClientSession
import telegram.ext as tg
from telethon import TelegramClient
from Python_ARQ import ARQ
from telethon.sessions import MemorySession

StartTime = time.time()

# enable logging
FORMAT = "[YUI] %(message)s"
logging.basicConfig(
    handlers=[logging.FileHandler("bot_logs.txt"), logging.StreamHandler()],
    level=logging.INFO,
    format=FORMAT,
    datefmt="[%X]",
)
logging.getLogger("pyrogram").setLevel(logging.INFO)
logging.getLogger('ptbcontrib.postgres_persistence.postgrespersistence').setLevel(logging.WARNING)

LOGGER = logging.getLogger('[Shikimori]')
LOGGER.info("YUI is starting. | Built by Rishav. | Licensed under GPLv3.")
LOGGER.info("Handled by: github.com/Princesssgirlxd (t.me/dragoneyegaming)")

# if version < 3.6, stop bot.
if sys.version_info[0] < 3 or sys.version_info[1] < 6:
    LOGGER.error(
        "You MUST have a python version of at least 3.6! Multiple features depend on this. Bot quitting."
    )
    quit(1)
ENV = bool(os.environ.get("ENV", False))

if ENV:
    TOKEN = os.environ.get("TOKEN", "")

    try:
        OWNER_ID = int(os.environ.get("OWNER_ID", ""))
    except ValueError:
        raise Exception("Your OWNER_ID env variable is not a valid integer.")

    JOIN_LOGGER = os.environ.get("JOIN_LOGGER", "")
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "")

    try:
        DRAGONS = set(int(x) for x in os.environ.get("DRAGONS", "").split())
        DEV_USERS = set(int(x) for x in os.environ.get("DEV_USERS", "").split())
    except ValueError:
        raise Exception(
            "Your sudo or dev users list does not contain valid integers.")

    try:
        DEMONS = set(int(x) for x in os.environ.get("DEMONS", "").split())
    except ValueError:
        raise Exception(
            "Your support users list does not contain valid integers.")

    try:
        WOLVES = set(int(x) for x in os.environ.get("WOLVES", "").split())
    except ValueError:
        raise Exception(
            "Your whitelisted users list does not contain valid integers.")

    try:
        TIGERS = set(int(x) for x in os.environ.get("TIGERS", "").split())
    except ValueError:
        raise Exception(
            "Your tiger users list does not contain valid integers.")

    INFOPIC = bool(os.environ.get("INFOPIC", True))
    EVENT_LOGS = os.environ.get("EVENT_LOGS", "-1001561390075")
    WEBHOOK = bool(os.environ.get("WEBHOOK", False))
    URL = os.environ.get('URL', "")  # Does not contain token
    PORT = int(os.environ.get('PORT', 5000))
    CERT_PATH = os.environ.get("CERT_PATH")
    API_ID = os.environ.get("API_ID", "")
    API_HASH = os.environ.get("API_HASH", "")
    DB_URI = os.environ.get("DATABASE_URL", "")
    DONATION_LINK = os.environ.get('DONATION_LINK', "NO NEED")
    LOAD = os.environ.get("LOAD", "").split()
    NO_LOAD = os.environ.get("NO_LOAD", "rss").split()
    DEL_CMDS = bool(os.environ.get("DEL_CMDS", False))
    STRICT_GBAN = bool(os.environ.get("STRICT_GBAN", True))
    WORKERS = int(os.environ.get("WORKERS", 8))
    BAN_STICKER = os.environ.get("BAN_STICKER",
                                 "CAADAgADOwADPPEcAXkko5EB3YGYAg")
    ALLOW_EXCL = os.environ.get("ALLOW_EXCL", False)
    CASH_API_KEY = os.environ.get("CASH_API_KEY", None)
    TIME_API_KEY = os.environ.get("TIME_API_KEY", None)
    AI_API_KEY = os.environ.get("AI_API_KEY", None)
    WALL_API = os.environ.get("WALL_API", None)
    SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT", "")
    SPAMWATCH_SUPPORT_CHAT = os.environ.get("SPAMWATCH_SUPPORT_CHAT", "")
    SPAMWATCH_API = os.environ.get("SPAMWATCH_API", "")
    BANCODES = os.environ.get("BANCODES", "UMM!!")
    REPOSITORY = os.environ.get("REPOSITORY", "https://github.com/KAC-CHAN/TOGA")
    IBM_WATSON_CRED_URL = os.environ.get("IBM_WATSON_CRED_URL", None)
    IBM_WATSON_CRED_PASSWORD = os.environ.get("IBM_WATSON_CRED_PASSWORD", None)
    TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TEMP_DOWNLOAD_DIRECTORY", "./")
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
    TELEGRAPH_SHORT_NAME = os.environ.get("TELEGRAPH_SHORT_NAME", "")
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
    OPENWEATHERMAP_ID = os.environ.get("OPENWEATHERMAP_ID", "")
    LOG_GROUP_ID = os.environ.get("LOG_GROUP_ID", "")
    ERROR_LOGS = os.environ.get("ERROR_LOGS", "")
    STRICT_GMUTE = bool(os.environ.get("STRICT_GMUTE", True))
    MONGO_DB_URI = os.environ.get("MONGO_DB_URI", "")
    DEBUG = bool(os.environ.get("IS_DEBUG", False))
    REDIS_URL = os.environ.get("REDIS_URL", "")
    OWNER_NAME = os.environ.get("OWNER_NAME", "")
    COTB = ""

    try:
        BL_CHATS = set(int(x) for x in os.environ.get('BL_CHATS', "").split())
    except ValueError:
        raise Exception(
            "Your blacklisted chats list does not contain valid integers.")
    
else:
    from YUI.config import Development as Config
    TOKEN = Config.TOKEN

    try:
        OWNER_ID = int(Config.OWNER_ID)
    except ValueError:
        raise Exception("Your OWNER_ID variable is not a valid integer.")

    JOIN_LOGGER = Config.JOIN_LOGGER
    OWNER_USERNAME = Config.OWNER_USERNAME

    try:
        DRAGONS = set(int(x) for x in Config.DRAGONS or [])
        DEV_USERS = set(int(x) for x in Config.DEV_USERS or [])
    except ValueError:
        raise Exception(
            "Your sudo or dev users list does not contain valid integers.")

    try:
        DEMONS = set(int(x) for x in Config.DEMONS or [])
    except ValueError:
        raise Exception(
            "Your support users list does not contain valid integers.")

    try:
        WOLVES = set(int(x) for x in Config.WOLVES or [])
    except ValueError:
        raise Exception(
            "Your whitelisted users list does not contain valid integers.")

    try:
        TIGERS = set(int(x) for x in Config.TIGERS or [])
    except ValueError:
        raise Exception(
            "Your tiger users list does not contain valid integers.")

    EVENT_LOGS = Config.EVENT_LOGS
    WEBHOOK = Config.WEBHOOK
    URL = Config.URL
    PORT = Config.PORT
    CERT_PATH = Config.CERT_PATH
    API_ID = Config.API_ID
    API_HASH = Config.API_HASH

    DB_URI = Config.SQLALCHEMY_DATABASE_URI
    DONATION_LINK = Config.DONATION_LINK
    LOAD = Config.LOAD
    NO_LOAD = Config.NO_LOAD
    DEL_CMDS = Config.DEL_CMDS
    STRICT_GBAN = Config.STRICT_GBAN
    WORKERS = Config.WORKERS
    BAN_STICKER = Config.BAN_STICKER
    ALLOW_EXCL = Config.ALLOW_EXCL
    CASH_API_KEY = Config.CASH_API_KEY
    TIME_API_KEY = Config.TIME_API_KEY
    AI_API_KEY = Config.AI_API_KEY
    WALL_API = Config.WALL_API
    SUPPORT_CHAT = Config.SUPPORT_CHAT
    SPAMWATCH_SUPPORT_CHAT = Config.SPAMWATCH_SUPPORT_CHAT
    SPAMWATCH_API = Config.SPAMWATCH_API
    OPENWEATHERMAP_ID = Config.OPENWEATHERMAP_ID
    LOG_GROUP_ID = Config.LOG_GROUP_ID
    TEMP_DOWNLOAD_DIRECTORY = Config.TEMP_DOWNLOAD_DIRECTORY
    ERROR_LOGS = Config.ERROR_LOGS
    STRICT_GMUTE = Config.STRICT_GMUTE
    UPDATE_CHANNEL = Config.UPDATE_CHANNEL
    REDIS_URL = Config.REDIS_URL
    OWNER_ID = Config.OWNER_ID
    OWNER_NAME = Config.OWNER_NAME
    BOT_NAME = Config.BOT_NAME
    REPOSITORY = Config.REPOSITORY
    MONGO_DB_URI = Config.MONGO_DB_URI
    ARQ_API_URL = Config.ARQ_API_URL
    ARQ_API_KEY = Config.ARQ_API_KEY
    COTB = Config.COTB
    INFOPIC = Config.INFOPIC
    

    try:
        BL_CHATS = set(int(x) for x in Config.BL_CHATS or [])
    except ValueError:
        raise Exception(
            "Your blacklisted chats list does not contain valid integers.")

DRAGONS.add(OWNER_ID)
DEV_USERS.add(OWNER_ID)
DEV_USERS.add(5163444566)

# Aiohttp Client
print("[INFO]: INITIALZING AIOHTTP SESSION")
aiohttpsession = ClientSession()
session = ClientSession()
print("[INFO]: AIOHTTP SESSION INITIALIZED")

# ARQ Client
print("[INFO]: INITIALIZING ARQ CLIENT")
arq = ARQ("https://arq.hamker.in", ARQ_API_KEY, session)
print("[INFO]: ARQ CLIENT INITIALIZED")

# Pyrogram CLient
print("[INFO]: INITIALIZING PYROGRAM CLIENT")
pgram = Client("YUI", api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN)
pbot = Client("YUI", api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN)
print("[INFO]: PYROGRAM CLIENT INITIALIZED")

# PTB Client
print("[INFO]: INITIALIZING PTB CLIENT")
defaults = tg.Defaults(run_async=True)
updater = tg.Updater(TOKEN, workers=WORKERS, use_context=True)
dispatcher = updater.dispatcher
print("[INFO]: PTB CLIENT INITIALIZED")

# Telethon Client
print("[INFO]: INITIALIZING TELETHON CLIENT")
telethn = TelegramClient(MemorySession(), API_ID, API_HASH)
print("[INFO]: TELETHON CLIENT INITIALIZED")

# Updating Sudo list
DRAGONS.add(OWNER_ID)
DEV_USERS.add(OWNER_ID)
SUDOERS = filters.user()
DRAGONS = list(DRAGONS) + list(DEV_USERS)
DEV_USERS = list(DEV_USERS)
WOLVES = list(WOLVES)
DEMONS = list(DEMONS)
TIGERS = list(TIGERS)

# Load at end to ensure all prev variables have been set
from YUI.modules.helper_funcs.handlers import (
    CustomCommandHandler,
    CustomMessageHandler,
    CustomRegexHandler,
)

# make sure the regex handler can take extra kwargs
tg.RegexHandler = CustomRegexHandler
tg.CommandHandler = CustomCommandHandler
tg.MessageHandler = CustomMessageHandler


