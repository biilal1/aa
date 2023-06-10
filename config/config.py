import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

if os.path.exists("Internal"):
   load_dotenv("Internal")

aiohttpsession = aiohttp.ClientSession()
que = {}
admins = {}

#------------------------ Important Stuff 🤎 -----------------------

API_ID = int(getenv("API_ID", "28981662"))
API_HASH = getenv("API_HASH", "a21bb968cf40c2d86c21a376f5f3d32c")
BOT_TOKEN = getenv("BOT_TOKEN", "5589349935:AAH9KpA1ITepg8crzEIvsc9iAMv1Qqkh4mk")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "600"))
STRING_SESSION = getenv("STRING_SESSION", "AgBXIT-9LrSeXBrBSlm_zNbn0G-o0pEYpGe8HOYLN4Ps8vASipV2f83ElOQMGgPH8ts4wt8pewhfEFR_J-Ii8NPeYVKsmuLmzH8kqhzDHfYly0q2DVqUYpuBGCzyQHEt5RiI8spAl_n1odn4iy3m5P8G6HLPZkp-wMBR-dcMiP9R1pqngyXVr5pupBmnNT1UP5apgW_ayHm9bhyN88I4vGYxHYWhw4SpjCDT2tZSIh4vNGIhnCtoewKxljVE5Rn6xaexfwZA_6QQQ6z_I82mvwpQvBCk-z49yRuEDPTMQL9zgtGV14eKttxgiLwrcDqTqyJBPyv-_NDnnI0QnVshk-_MAAAAAVK2aQ0A")
BOT_USERNAME = getenv("BOT_USERNAME", "LROBOT")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1854384004").split()))
OWNER_ID = list(
    map(int, getenv("OWNER_ID", "1854384004").split())
)  # Input type must be interger
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "30"))

#•••••••••••••••••••••••• Mongodb Url Stuff & Loggroupid •••••••••••
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001847569598")) 

MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority")
#________________________ Updates  & Music bot name________________
NETWORK = getenv("NETWORK", "E9N99")
GROUP = getenv("GROUP", "E9N99")
BOT_NAME = getenv("BOT_NAME", "Music")
BANNED_USERS = filters.user()

#************************* Image Stuff  ****************************

IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/5fdd8da2461c05d893189.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/5fdd8da2461c05d893189.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/5fdd8da2461c05d893189.jpg") 
YOUTUBE_IMG_URL = getenv("YOUTUBE_IMG_URL", "https://te.legra.ph/file/5fdd8da2461c05d893189.png")

aiohttpsession = aiohttp.ClientSession()


