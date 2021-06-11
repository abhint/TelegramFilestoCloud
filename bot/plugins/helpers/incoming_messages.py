#!/usr/bin/env python3
# This is bot coded by Abhijith N T and used for educational purposes only
# https://github.com/AbhijithNT
# Copyright ABHIJITH N T
# Thank you https://github.com/pyrogram/pyrogram


from ...filetocloud import CloudBot
from bot import LOGGER
from hurry.filesize import size
from ..keyboard import server_select
from ..use import VIDEO, DOCUMENT, AUDIO


@CloudBot.on_message(VIDEO)
async def userVideo(client, bot):
    LOGGER.info(f"{bot.chat.id} - {bot.video.file_name}")
    await client.send_message(
        chat_id=bot.chat.id,
        text=(
            f"File Name: <code>{bot.video.file_name}</code>"
            f"\nFile Size: <code>{size(bot.video.file_size)}</code>"
        ),
        reply_markup=server_select(),
        reply_to_message_id=bot.message_id
    )


@CloudBot.on_message(DOCUMENT)
async def userDocument(client, bot):
    LOGGER.info(f"{bot.chat.id} - {bot.document.file_name}")
    await client.send_message(
        chat_id=bot.chat.id,
        text=(
            f"File Name: <code>{bot.document.file_name}</code>"
            f"\nFile Size: <code>{size(bot.document.file_size)}</code>"
        ),
        reply_markup=server_select(),
        reply_to_message_id=bot.message_id
    )


@CloudBot.on_message(AUDIO)
async def userAudio(client, bot):
    LOGGER.info(f"{bot.chat.id} - {bot.audio.file_name}")
    await client.send_message(
        chat_id=bot.chat.id,
        text=(
            f"File Name: <code>{bot.audio.file_name}</code>"
            f"\nFile Size: <code>{size(bot.audio.file_size)}</code>"
        ),
        reply_markup=server_select(),
        reply_to_message_id=bot.message_id
    )
