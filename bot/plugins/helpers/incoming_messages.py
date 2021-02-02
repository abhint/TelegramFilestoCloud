#!/usr/bin/env python3
# This is bot coded by Abhijith-cloud and used for educational purposes only
# https://github.com/Abhijith-cloud
# Copyright ABHIJITH N T
# Thank you https://github.com/pyrogram/pyrogram


from bot.filetocloud import CloudBot, filters
from bot import (
    LOGGER,
    AUTH_USER
)
from hurry.filesize import size
from bot.plugins.keybord import server_select
AUTH_USER.append(429320566)

@CloudBot.on_message(filters.video & filters.user(AUTH_USER))
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


@CloudBot.on_message(filters.document & filters.user(AUTH_USER))
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


@CloudBot.on_message(filters.audio & filters.user(AUTH_USER))
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
