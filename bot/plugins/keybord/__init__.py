from yarl import URL
import bot
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
    )



def server_select():
    upload_selection = []
    upload_selection=[
        [
            InlineKeyboardButton(
                "MixDrop",
                callback_data = "MixDrop"
            ),
            InlineKeyboardButton(
            "File.io",
            callback_data = "File.io"
            )
        ],
    ]
    return InlineKeyboardMarkup(upload_selection)

def downloadButton(link):
    dl_button = []
    dl_button = [
        [
            InlineKeyboardButton(
                "DOWNLOAD URL",
                url=f"{link}"
            )
        ]
    ]
    return InlineKeyboardMarkup(dl_button)