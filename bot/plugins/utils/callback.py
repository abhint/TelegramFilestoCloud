from ...filetocloud import CloudBot
from pyrogram.types import CallbackQuery



@CloudBot.on_callback_query()
async def selecting_server(client: CloudBot, message: CallbackQuery) -> None:
    print(message)