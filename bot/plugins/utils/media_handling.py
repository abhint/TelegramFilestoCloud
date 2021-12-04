#!/usr/bin/env python3
# This is bot coded by Abhijith N T and used for educational purposes only
# https://github.com/AbhijithNT
# Copyright ABHIJITH N T
# Thank you https://github.com/pyrogram/pyrogram


from ...filetocloud import CloudBot, filters
from bot import LOGGER
from hurry.filesize import size
from ...helpers import server_select
# from ..use import VIDEO, DOCUMENT, AUDIO

BOT_USE = False
AUTH_USER: list

if BOT_USE:
    AUTH_USER.append(429320566)
    VIDEO = filters.video & filters.user(AUTH_USER)
    DOCUMENT = filters.document & filters.user(AUTH_USER)
    AUDIO = filters.audio & filters.user(AUTH_USER)
else:
    VIDEO = filters.video
    DOCUMENT = filters.document
    AUDIO = filters.audio


logger = LOGGER(__name__)


@CloudBot.on_message(VIDEO)
async def userVideo(client, bot):
    logger.info(f"{bot.chat.id} - {bot.video.file_name}")
    file_name = bot.video.file_name
    file_size = size(bot.video.file_size)
    await client.send_message(
        chat_id=bot.chat.id,
        text=(
            f"File Name: `{file_name}`"
            f"File Size: `{file_size}`"
        ),
        reply_markup=server_select(file_name,file_size),
        reply_to_message_id=bot.message_id
    )


@CloudBot.on_message(DOCUMENT)
async def userDocument(client, bot):
    logger.info(f"{bot.chat.id} - {bot.document.file_name}")
    file_name = bot.document.file_name
    file_size = size(bot.document.file_size)
    await client.send_message(
        chat_id=bot.chat.id,
        text=(
            f"File Name: `{file_name}`"
            f"File Size: `{file_size}`"
        ),
        reply_markup=server_select(file_name,file_size),
        reply_to_message_id=bot.message_id
    )


@CloudBot.on_message(AUDIO)
async def userAudio(client, bot):
    logger.info(f"{bot.chat.id} - {bot.audio.file_name}")
    file_name = bot.audio.file_name
    file_size = size(bot.audio.file_size)
    await client.send_message(
        chat_id=bot.chat.id,
        text=(
            f"File Name: <code>`{file_name}`</code>"
            f"\nFile Size: <code>{file_size}</code>"
        ),
        reply_markup=server_select(file_name,file_size),
        reply_to_message_id=bot.message_id
    )
