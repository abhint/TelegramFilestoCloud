from pyrogram import Client
from bot import LOGGER
import pyrogram
from bot.plugins.helpers.dowloader import fileDownload
@Client.on_callback_query()
async def server_selection(client, server):
    # print(server)
    server_name = server.data
    if server_name == 'MixDrop':
        # LOGGER.info(server)
        await fileDownload(client, server)
    if server_name == 'File.io':
        await fileDownload(client, server)