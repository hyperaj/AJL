import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()


API_ID = int(getenv("API_ID", "22614057"))

API_HASH = getenv("API_HASH", "7f3199fc8aaa21f76a8f2ce35c21292b")

BOT_TOKEN = getenv("BOT_TOKEN", "6701671043:AAG8InzrwbYioNZWGqMTZ0f1P74dBoiQQIg")

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://musicheysiri:musicsiri123@cluster0.gozblfn.mongodb.net/?appName=Cluster0")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 54000))

SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "54000")
)

LOGGER_ID = int(getenv("LOGGER_ID", -1002066328009))

OWNER_ID = int(getenv("OWNER_ID", "6180148187"))

BOT_USERNAME = getenv("BOT_USERNAME" , "hey siri")

COMMAND_HANDLER = getenv("COMMAND_HANDLER", "! / .").split()

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/KRISHtg/queenmusicbot",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/tamilanexpress")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/tamil_anexpress_chat")

AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))
AUTO_SUGGESTION_MODE = getenv("AUTO_SUGGESTION_MODE", "True")
AUTO_SUGGESTION_TIME = int(
    getenv("AUTO_SUGGESTION_TIME", "500"))

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "19609edb1b9f4ed7be0c8c1342039362")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "409e31d3ddd64af08cfcc3b0f064fcbe")



PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))

CLEANMODE_DELETE_MINS = int(
    getenv("CLEANMODE_MINS", "5"))
DEEP_API = getenv("DEEP_API")

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))



# Get your pyrogram v2 session from @Shsusu_bot on Telegram
STRING1 = getenv("STRING_SESSION", "BQFZECkAt8HUNCMnYTdNikppb3jwXDnSt3vsNoFfYTYPQPnJB_0WEopp3E6qQ2K3ncN4ObASUFBQAM-PzeyQl2jmljJ_t61odG9ykFHLSTXsGN88auqFvB0sscYbEeNOpTvgaFadboBCbBWyPEXV8sgfoW89oIWXpFVeB7xGijuUPOBMhWsKHPKD2P4GUsbshj-pEOtnnci0ojTS-Ht_IZejLl2Js_zZi5hzEQIHHz0LqwzTL7ySWRSOau6kQkCvGbaBjkM6D-aucqkHvVFbMYiy-vN9b3oM7fvqStCq_Z6P6C8aJQbiIGG5YnncRFP8jgFEJTPcp8kmx1dL2I9OQ_iSGUB7PgAAAAGr5gXTAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

# Bot introduction messages - These can be customized as per your preference
AYU = [
    "💞", "🦋", "🔍", "🧪", "🦋", "⚡️", "🔥", "🦋", "🎩", "🌈", "🍷", "🥂", "🦋", "🥃", "🥤", "🕊️",
    "🦜", "🐝", "🕊️", "🧪", "🕊️", "🔎", "🦋", "🎶", "🪄", "💌", "🌡️", "🦜", "🧨"
]

AYUV = [
    "❖ нᴇʏ</b> {0}, ɴɪᴄᴇ ᴛᴏ ᴍᴇᴇᴛ ʏᴏᴜ !</b>\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n<b>● ʜᴇʏ, ɪ ᴀᴍ ᴀᴅᴠᴀɴᴄᴇᴅ ᴀɴᴅ ꜱᴜᴘᴇʀꜰᴀꜱᴛ ᴍᴜꜱɪᴄ ʙᴏᴛ</b>\n\n<b>● ꜰᴇᴇʟ ꜰʀᴇᴇ ᴛᴏ ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ/ɢʀᴏᴜᴘ, ᴀɴᴅ ᴇɴᴊᴏʏ... ɴᴏ ʟᴀɢ ᴀᴜᴅɪᴏ ᴀɴᴅ ᴠɪᴅᴇᴏ\n<b>● ᴢᴇʀᴏ ᴅᴏᴡɴᴛɪᴍᴇ ᴀɴᴅ ʟᴀɢ ꜰʀᴇᴇ ᴍᴜꜱɪᴄ 🎶\n\n<b>❖ ᴛʜɪs ɪs ᴘᴏᴡᴇʀғᴜʟ ᴍᴜsɪᴄ ʙᴏᴛ, ғᴏʀ ʏᴏᴜʀ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ ᴠᴄ",
    "❖ нᴇʏ</b> {0}, ɴɪᴄᴇ ᴛᴏ ᴍᴇᴇᴛ ʏᴏᴜ !</b>\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n<b>● ɪ ᴀᴍ {1} ʙᴏᴛ.</b>\n\n<b>● ᴘʏᴛʜᴏɴ ➥</b> 3.10.11\n<b>● ᴘʏʀᴏɢʀᴀᴍ ➥</b> 2.0.106\n<b>● ᴘʏ-ᴛɢᴄᴀʟʟs ➥</b> 0.9.7\n\n<b>❖ ᴛʜɪs ɪs ᴘᴏᴡᴇʀғᴜʟ ᴍᴜsɪᴄ ʙᴏᴛ, ғᴏʀ ʏᴏᴜʀ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ ᴠᴄ",
    "❖ нᴇʏ</b> {0}, ɴɪᴄᴇ ᴛᴏ ᴍᴇᴇᴛ ʏᴏᴜ !</b>\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n<b>● ɪ ᴀᴍ {1} ʙᴏᴛ.</b>\n\n<b>❖ ᴛʜɪs ɪs ᴘᴏᴡᴇʀғᴜʟ ᴍᴜsɪᴄ ʙᴏᴛ, ғᴏʀ ʏᴏᴜʀ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ ᴠᴄ",
]

BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
chatstats = {}
userstats = {}
clean = {}

autoclean = []

START_IMG_URL = getenv(
    "START_IMG_URL", "https://te.legra.ph/file/6d585197af34afd4bb740.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://te.legra.ph/file/f6b2e18ecae7ffb6a9c88.jpg"
)
PLAYLIST_IMG_URL = "https://te.legra.ph/file/6d585197af34afd4bb740.jpg"
STATS_IMG_URL = "https://telegra.ph/file/7adee139f0639c400e1b8.jpg"
TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/9e14789c344a3c983aca5.jpg"
TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/9e14789c344a3c983aca5.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/6d585197af34afd4bb740.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/6d585197af34afd4bb740.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/9e14789c344a3c983aca5.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/6d585197af34afd4bb740.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/6d585197af34afd4bb740.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/6d585197af34afd4bb740.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00"))

if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
        
