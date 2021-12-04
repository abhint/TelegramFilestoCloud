from logging import fatal
from ...filetocloud import CloudBot
from pyrogram.types import CallbackQuery
from ...helpers import download_media


@CloudBot.on_callback_query()
async def selecting_server(client: CloudBot, message: CallbackQuery) -> None:
    callback_data = message.data
    if callback_data.startswith('transfersh'):
        f = await download_media(
            client,
            message
        )
