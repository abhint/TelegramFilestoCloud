from json import decoder
from ..filetocloud import CloudBot
import aiohttp
from .upload import server_upload
from ..helpers import download_media
from pyrogram.types import CallbackQuery


async def anonfiles(client: CloudBot, message: CallbackQuery):

    try:
        FILE_PATH = await download_media(client, "message")
    except Exception as e:
        print(e)
        
        return
    try:
        url = 'https://api.anonfiles.com/upload'
        d = await server_upload(file="filetocloud_log.txt", url=url)
        print(d)
    except Exception as e:
        print(f"ERROR: {e}")
