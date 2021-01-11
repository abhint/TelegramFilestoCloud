#!/usr/bin/env python3
# This is bot coded by Abhijith-cloud and used for educational purposes only
# https://github.com/Abhijith-cloud
# Copyright ABHIJITH N T
# Thank you https://github.com/pyrogram/pyrogram


from bot import (
    BOT_TOKEN,
    APP_ID,
    API_HASH
)
from pyrogram import Client
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

if __name__ == "__main__":
    bot = Client(
        "Telegram MixDrop Bot",
        bot_token = BOT_TOKEN,
        api_id = APP_ID,
        api_hash = API_HASH,
        plugins = {
            "root":"bot/plugins"
            }
        )
    LOGGER.info('Bot Started :)')
    bot.run()
    LOGGER.info('Bot is Stopped Working :(')
