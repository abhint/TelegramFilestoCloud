#!/usr/bin/env python3
# This is bot coded by Abhijith-cloud and used for educational purposes only
# https://github.com/Abhijith-cloud
# Copyright ABHIJITH N T
# Thank you https://github.com/pyrogram/pyrogram


import aiohttp
import os
import time
from bot import LOGGER
from hurry.filesize import size
from bot.plugins.display.time import time_data
from pyrogram.errors import FloodWait
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
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
            print(response)
            link = await response.json()
            dl_b = link['link']
            await client.edit_message_text(
                chat_id=bot.from_user.id,
                message_id=bot.message_id,
                text=f"Uploaded...100% in {time_data(s_time)}"
            )
            print(f"{bot}")
            await client.send_message(
                chat_id=bot.chat.id,
                text=(
                    f"File Name: <code>{file_name}</code>"
                    f"\nFile Size: <code>{file_size}</code>"
                ),
                reply_markup=InlineKeyboardMarkup(
                    [[
                        InlineKeyboardButton(
                            "🔗 DOWNLOAD URL",
                            url=f"{dl_b}"
                        )
                    ],
                        [
                            InlineKeyboardButton(
                                "🗂 SOURCE",
                                url="https://github.com/Abhijith-cloud/"
                            )
                        ]])
            )
    except FloodWait as error:
        LOGGER.info(f"FILE UPLOAD ERROR: {error}")
        print(time.sleep(error.x))
