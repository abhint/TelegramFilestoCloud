#!/usr/bin/env python3
# This is bot coded by Abhijith N T and used for educational purposes only
# https://github.com/abhint
# Copyright ABHIJITH N T
# Thank you https://github.com/pyrogram/pyrogram

from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)


def server_select():

    # upload_selection = [
    #     [
    #         InlineKeyboardButton(
    #             "transfer.sh",
    #             callback_data=f'transfers'
    #         ),
    #         InlineKeyboardButton(
    #             "File.io",
    #             callback_data=f"fileio"
    #         )
    #     ],
    #     [
    #         InlineKeyboardButton(
    #             "gofile.io",
    #             callback_data=f"gofileio"
    #         ),
    #         InlineKeyboardButton(
    #             "anonymfiles.com",
    #             callback_data=f"anonymfiles"
    #         )
    #     ]
    # ]
    upload_selection = [
        [
            InlineKeyboardButton(
                "anonymfiles.com",
                callback_data=f"anonymfiles"
            )
        ],
        [
            InlineKeyboardButton(
                "gofile.io",
                callback_data=f"gofileio"
            )
        ],
        [
            InlineKeyboardButton(
                "File.io",
                callback_data=f"fileio"
            )
        ]
    ]
    return InlineKeyboardMarkup(upload_selection)
