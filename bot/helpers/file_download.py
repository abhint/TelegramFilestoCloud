import time
from bot import LOGGER
from ..filetocloud import CloudBot
from pyrogram.errors import RPCError
from pyrogram.types import CallbackQuery
from ..helpers.display import progress
# from ..helpers import progress


logger = LOGGER(__name__)


async def download_media(client: CloudBot, message: CallbackQuery, ) -> str:
    # client.download_media(message)
    now = time.time()
    user_message = await client.edit_message_text(
        chat_id=message.from_user.id,
        message_id=message.message.message_id,
        text="processing your request...please wait",
    )
    try:
        media_id = message.message.reply_to_message
        download_file_path = await client.download_media(media_id,
                                                         progress=progress,
                                                         progress_args=(
                                                             "Downloading...",
                                                             user_message,
                                                             now
                                                         )
                                                         )
        print(download_file_path)
        return download_file_path
    except RPCError as e:
        logger.error(e)
        client.edit_message_text(
            chat_id=message.from_user.id,
            message_id=message.message.message_id,
            text="Someting is error",
        )
        return
