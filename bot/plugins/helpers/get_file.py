#!/usr/bin/env python3
# This is bot coded by Abhijith-cloud and used for educational purposes only
# https://github.com/Abhijith-cloud
# (c) Abhijith N T ;-)
# Thank you https://github.com/pyrogram/pyrogram :-)

from pyrogram import Client,filters
from pyrogram.types.messages_and_media.message import Message
from bot.plugins.helpers.mixdrop_upload import mixFileup
from bot.plugins.display import progress
import time, os
from hurry.filesize import size
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
    )

@Client.on_message(filters.media)
async def userMedia(client, bot):
    now = time.time()
    link = ''
    f_size = ''
    f_name = ''
    file = ''
    userMsg = await client.send_message(
        chat_id=bot.chat.id,
        text = "processing your request...please wait"
    )
    try:
        file = await bot.download(
            progress = progress,
            progress_args = (
                'Downloading....',
                userMsg,
                now
            )
        )
        f_size = os.path.getsize(file)
        f_name = file.split('/')[-1]
        link = await mixFileup(file, userMsg, now)
        for i in link:
            pass
    except Exception as error:
        print(error)
    await bot.reply(
        text = f"File Name: {f_name}\nSIZE: {size(f_size)}",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "DOWNLOAD !",
                        url=f"{link}"
                    ),
                ],
            ]
        )
    )
    try:
        os.remove(file)
    except Exception as error:
        print(error)