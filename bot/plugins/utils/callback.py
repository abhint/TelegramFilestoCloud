from logging import fatal
from ...filetocloud import CloudBot
from pyrogram.types import CallbackQuery
from ...helpers import download_media
from ...helpers.servers import anonfiles


@CloudBot.on_callback_query()
async def selecting_server(client: CloudBot, message: CallbackQuery) -> None:
    callback_data = message.data
    if callback_data.startswith('transfersh'):
        await anonfiles(client, message)
    elif callback_data.startswith('fileio'):
        pass
    elif callback_data.startswith('gofileio'):
        pass
    elif callback_data.startswith('anonymfiles'):
        pass
