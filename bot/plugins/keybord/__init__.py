#!/usr/bin/env python3
# This is bot coded by Abhijith-cloud and used for educational purposes only
# https://github.com/Abhijith-cloud
# Copyright ABHIJITH N T
# Thank you https://github.com/pyrogram/pyrogram

from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)


def server_select():
    upload_selection = [
        [
            InlineKeyboardButton(
                "MixDrop",
                callback_data="MixDrop"
            ),
            InlineKeyboardButton(
                "File.io",
                callback_data="File.io"
            )
        ],
    ]
    return InlineKeyboardMarkup(upload_selection)
