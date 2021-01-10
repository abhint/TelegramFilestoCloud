from pyrogram import Client
from bot import LOGGER
import pyrogram
from bot.plugins.helpers.dowloader import fileDownload
@Client.on_callback_query()
async def server_selection(client, server):
    await fileDownload(client, server)
