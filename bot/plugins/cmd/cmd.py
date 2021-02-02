#!/usr/bin/env python3
# This is bot coded by Abhijith-cloud and used for educational purposes only
# https://github.com/Abhijith-cloud
# Copyright ABHIJITH N T
# Thank you https://github.com/pyrogram/pyrogram

from bot.filetocloud import CloudBot, filters
from bot import Msg

@CloudBot.on_message(filters.command("start"))
async def start_message(client, message):
    await client.send_message(
        chat_id=message.chat.id,
        text=f"Hey {message.from_user.first_name},{Msg.start}{Msg.source}",
        reply_to_message_id=message.message_id,
        parse_mode="html"
    )
@CloudBot.on_message(filters.command(["help", "h"]))
async def help_message(client, message):
    await client.send_message(
        chat_id=message.chat.id,
        text=f"Hey {message.from_user.first_name},{Msg.help}{Msg.source}",
        reply_to_message_id=message.message_id,
        parse_mode="html"
    )
