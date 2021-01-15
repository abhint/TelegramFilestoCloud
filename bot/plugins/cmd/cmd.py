#!/usr/bin/env python3
# This is bot coded by Abhijith-cloud and used for educational purposes only
# https://github.com/Abhijith-cloud
# Copyright ABHIJITH N T
# Thank you https://github.com/pyrogram/pyrogram

from pyrogram import Client, filters
from bot import msg


@Client.on_message(filters.command("start"))
async def start(client, message):
    await client.send_message(
        chat_id=message.chat.id,
        text=f"Hey {message.from_user.first_name},{msg.start}{msg.source}",
        reply_to_message_id=message.message_id,
        parse_mode="html",
    )


@Client.on_message(filters.command(["help", "h"]))
async def help(client, message):
    await client.send_message(
        chat_id=message.chat.id,
        text=f"Hey {message.from_user.first_name},{msg.help}{msg.source}",
        reply_to_message_id=message.message_id,
        parse_mode="html",
    )
