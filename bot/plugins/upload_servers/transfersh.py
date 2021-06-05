import aiohttp
from bot.plugins.display.time import time_data
from bot import LOGGER
from hurry.filesize import size
import os
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


# error
client_exceptions = (
    aiohttp.ClientResponseError,
    aiohttp.ClientConnectionError,
    aiohttp.ClientPayloadError,
)


async def transferSH(file, client, bot, s_time):
    file_size = size(os.path.getsize(file))
    file_name = file.split('/')[-1]
    await client.edit_message_text(
        chat_id=bot.from_user.id,
        message_id=bot.message_id,
        text="Uploading to Transfer.sh"
    )
    try:
        async with aiohttp.ClientSession() as session:
            files = {'file': open(file, 'rb')}
            response = await session.post('http://transfer.sh', data=files)
            dl = await response.text()
            await client.edit_message_text(
                chat_id=bot.from_user.id,
                message_id=bot.message_id,
                text=f"Uploaded...100% in {time_data(s_time)}"
            )
            await client.send_message(
                chat_id=bot.chat.id,
                text=(
                    f"File Name: <code>{file_name}</code>"
                    f"\nFile Size: <code>{file_size}</code>"
                ),
                reply_markup=InlineKeyboardMarkup(
                    [[
                        InlineKeyboardButton(
                            "DOWNLOAD URL",
                            url=f"{dl}"
                        )
                    ],
                        [
                        InlineKeyboardButton(
                            "🗂 SOURCE",
                            url="https://github.com/AbhijithNT/"
                        )
                    ]])
            )
    except client_exceptions as e:
        print(e)
