#!/usr/bin/env python3
# This is bot coded by Abhijith N T and used for educational purposes only
# https://github.com/AbhijithNT
# Copyright ABHIJITH N T
# Thank you https://github.com/pyrogram/pyrogram




import os
import aiohttp
from bot import LOGGER
from hurry.filesize import size
from ..keyboard import completedKeyboard
from bot.plugins.display.time import time_data

client_exceptions = (
    aiohttp.ClientResponseError,
    aiohttp.ClientConnectionError,
    aiohttp.ClientPayloadError,
)


async def fileIO(file, client, bot, s_time):
    file_size = size(os.path.getsize(file))
    file_name = file.split('/')[-1]
    try:
        await client.edit_message_text(
            chat_id=bot.from_user.id,
            message_id=bot.message_id,
            text="Uploading to File.IO"
        )
        async with aiohttp.ClientSession() as session:
            files = {
                'file': open(file, 'rb')
            }
            response = await session.post('https://file.io/', data=files)

            link = await response.json()
            dl = link['link']
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
                reply_markup=completedKeyboard(dl)
            )
    except client_exceptions as e:
        await client.edit_message_text(
            chat_id=bot.from_user.id,
            message_id=bot.message_id,
            text=f"{e}"
        )
        LOGGER.info(f"{bot.from_user.id} - fileIO - file_size - {e}")
