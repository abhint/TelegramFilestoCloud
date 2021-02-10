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
from pyrogram.errors import FloodWait
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
from bot.plugins.display.time import time_data
from bot import (
    API_KEY,
    API_EMAIL
)

env_email, env_api_key = API_EMAIL, API_KEY


async def mixFileup(file, client, bot, s_time):
    # https://github.com/odysseusmax/uploads/blob/master/mixdrop.py
    file_size = size(os.path.getsize(file))
    file_name = file.split('/')[-1]
    try:
        await client.edit_message_text(
            chat_id=bot.from_user.id,
            message_id=bot.message_id,
            text="Uploading to MixDrop..."
        )
        email = env_email
        api_key = env_api_key
        upload_url = "https://ul.mixdrop.co/api"
        async with aiohttp.ClientSession() as session:
            data = {
                'file': open(file, 'rb'),
                'email': email,
                'key': api_key
            }
            response = await session.post(upload_url, data=data)
            link = await response.json()
            await client.edit_message_text(
                chat_id=bot.from_user.id,
                message_id=bot.message_id,
                text=f"Uploaded...100% in {time_data(s_time)}"
            )
            dl_b = f"https://mixdrop.co/f/{link['result']['fileref']}"
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
    except FloodWait as e:
        LOGGER.info(f"FILE UPLOAD ERROR: {e}")
        print(time.sleep(e.x))
