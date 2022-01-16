from logging import fatal
from ...filetocloud import CloudBot
from pyrogram.types import CallbackQuery
from ...helpers import download_media
from ...helpers.servers import upload_handler


@CloudBot.on_callback_query()
async def selecting_server(client: CloudBot, message: CallbackQuery) -> None:
    callback_data = message.data
    if callback_data.startswith('fileio'):
        await upload_handler(client, message, callback_data)
    elif callback_data.startswith('gofileio'):
        await upload_handler(client, message, callback_data)
    elif callback_data.startswith('anonymfiles'):
        await upload_handler(client, message, callback_data)
