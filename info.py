import re, time
from os import environ
from Script import script 

id_pattern = re.compile(r'^.\d+$')

def is_enabled(value, default):
    if value.strip().lower() in ["on", "true", "yes", "1", "enable", "y"]: return True
    elif value.strip().lower() in ["off", "false", "no", "0", "disable", "n"]: return False
    else: return default


# PyroClient Setup 
API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
BOT_TOKEN = environ['BOT_TOKEN']

# Bot settings
WEB_SUPPORT = bool(environ.get("WEBHOOK", 'True')) # for web support on/off
PICS = (environ.get('PICS' ,'https://te.legra.ph/file/dde94e708129192bbbc3b.png https://te.legra.ph/file/5db7964438fa88fe66387.png https://te.legra.ph/file/7f9e7eaa567b3d66369f4.png https://te.legra.ph/file/95d58a10ddf136bc75b6f.png')).split()
UPTIME = time.time()

# Admins, Channels & Users
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '0').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# MongoDB information
DATABASE_URL = environ.get('DATABASE_URL', "mongodb+srv://user2002:abcd123@cluster0.gsdmp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
FILE_DB_URL = environ.get("FILE_DB_URL", DATABASE_URL)
FILE_DB_NAME = environ.get("FILE_DB_NAME", DATABASE_NAME)
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Filters Configuration 
MAX_RIST_BTNS = int(environ.get('MAX_RIST_BTNS', "10"))
START_MESSAGE = environ.get('START_MESSAGE', script.START_TXT)
BUTTON_LOCK_TEXT = environ.get("BUTTON_LOCK_TEXT", script.BUTTON_LOCK_TEXT)
FORCE_SUB_TEXT = environ.get('FORCE_SUB_TEXT', script.FORCE_SUB_TEXT)

WELCOM_PIC = environ.get("WELCOM_PIC", "")
WELCOM_TEXT = environ.get("WELCOM_TEXT", script.WELCOM_TEXT)
PMFILTER = is_enabled(environ.get('PMFILTER', "True"), True)
G_FILTER = is_enabled(environ.get("G_FILTER", "True"), True)
BUTTON_LOCK = is_enabled(environ.get("BUTTON_LOCK", "True"), True)
RemoveBG_API = environ.get("RemoveBG_API", "ftiwhaPS26Jx3HdQFT5gw3Mn")

# url shortner
SHORT_URL = environ.get("SHORT_URL")
SHORT_API = environ.get("SHORT_API")

# Others
IMDB_DELET_TIME = int(environ.get('IMDB_DELET_TIME', "300"))
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', 0))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'MovieTime_Movie_Request_Group')
P_TTI_SHOW_OFF = is_enabled(environ.get('P_TTI_SHOW_OFF', "True"), True)
PM_IMDB = is_enabled(environ.get('PM_IMDB', "False"), False)
IMDB = is_enabled(environ.get('IMDB', "False"), False)
SINGLE_BUTTON = is_enabled(environ.get('SINGLE_BUTTON', "True"), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "{file_name}\n•────•────────•────•\n📌 ᴊᴏɪɴ : <a href=\"https://t.me/MovieTime_Movie_Request_Group\">ᴍᴏᴠɪᴇᴛɪᴍᴇ</a> 🎬\n📌 ᴊᴏɪɴ : <a href=\"https://t.me/+prlX5HRWM-cyMmE1\">ᴍᴏᴠɪᴇꜰɪʟᴇꜱ</a> 📁\n📌 ᴊᴏɪɴ : <a href=\"https://t.me/+7D7GmraxuUY3Yzk1\">ᴡᴇʙꜱʜᴏᴡꜱ</a> 🍿\n📌 ꜱᴜʙꜱᴄʀɪʙᴇ ɴᴏᴡ : <a href=\"https://t.me/latest_hindi_movies_hub\">ᴄʟɪᴄᴋ</a> 👈🏻\n•────•────────•────•\n🎗 ʝσιи • ѕнαяє • ѕυρρσят 🎗")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", None)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", script.IMDB_TEMPLATE)
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled(environ.get('MELCOW_NEW_USERS', "True"), True)
PROTECT_CONTENT = is_enabled(environ.get('PROTECT_CONTENT', "False"), False)
PUBLIC_FILE_STORE = is_enabled(environ.get('PUBLIC_FILE_STORE', "True"), True)
LOG_MSG = "{} Iꜱ Rᴇsᴛᴀʀᴛᴇᴅ....✨\n\n🗓️ Dᴀᴛᴇ : {}\n⏰ Tɪᴍᴇ : {}\n\n🖥️ Rᴇᴏᴩ: {}\n🉐 Vᴇʀsɪᴏɴ: {}\n🧾 Lɪᴄᴇɴꜱᴇ: {}\n©️ Cᴏᴩʏʀɪɢʜᴛ: {}"
