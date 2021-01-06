#!/usr/bin/env python3
# This is bot coded by Abhijith-cloud and used for educational purposes only
# https://github.com/Abhijith-cloud
# (c) Abhijith N T ;-)
# Thank you https://github.com/pyrogram/pyrogram :-)


from pyrogram import Client
from env import ev_data
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
        bot_token = ev_data.BOT_TOKEN,
        api_id = ev_data.API_ID,
        api_hash = ev_data.API_HASH,
        plugins = {
            "root":"bot/plugins"
            }
        )
    LOGGER.info('Bot Started :)')
    bot.run()
    LOGGER.info('Somting is Wrong :(')
