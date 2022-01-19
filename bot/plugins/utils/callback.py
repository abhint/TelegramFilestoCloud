from ...filetocloud import CloudBot
from pyrogram.types import CallbackQuery
from ...helpers.servers import upload_handler


@CloudBot.on_callback_query()
async def selecting_server(client: CloudBot, message: CallbackQuery) -> None:
    callback_data = message.data
    await upload_handler(client, message, callback_data)
