from pyrogram import Client
from pyrogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

# Create a client using your bot token
app = Client("my_bot", bot_token="1306098991:AAHoWExoOUPE85OVpXFc8X0cs7gEqLmlV6g")

with app:
    app.send_message(
        "haskell",  # Edit this
        "This is a ReplyKeyboardMarkup example",
        reply_markup=ReplyKeyboardMarkup(
            [
                ["A", "B", "C", "D"],  # First row
                ["E", "F", "G"],  # Second row
                ["H", "I"],  # Third row
                ["J"]  # Fourth row
            ],
            resize_keyboard=True  # Make the keyboard smaller
        )
    )

    app.send_message(
        "haskell",  # Edit this
        "This is a InlineKeyboardMarkup example",
        reply_markup=InlineKeyboardMarkup(
            [
                [  # First row
                    InlineKeyboardButton(  # Generates a callback query when pressed
                        "Button",
                        callback_data="data"
                    ),
                    InlineKeyboardButton(  # Opens a web URL
                        "URL",
                        url="https://docs.pyrogram.org"
                    ),
                ],
                [  # Second row
                    InlineKeyboardButton(  # Opens the inline interface
                        "Choose chat",
                        switch_inline_query="pyrogram"
                    ),
                    InlineKeyboardButton(  # Opens the inline interface in the current chat
                        "Inline here",
                        switch_inline_query_current_chat="pyrogram"
                    )
                ]
            ]
        )
    )