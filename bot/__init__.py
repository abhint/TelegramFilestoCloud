#!/usr/bin/env python3
# This is bot coded by Abhijith-cloud and used for educational purposes only
# https://github.com/Abhijith-cloud
# (c) Abhijith N T ;-)
# Thank you https://github.com/pyrogram/pyrogram :-)

import logging

logging.basicConfig(
    level=logging.INFO,
    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class msg():
    source = "\nsource:https://github.com/Abhijith-cloud/Telegram-MixDrop-Bot"
    start = "\n<b>This bot uploads telegram files to mixdrop.co @thankappan369</b>"
    error = "something is went wrong\n{error} \ncontact admin @thankappan369"
    help = "Usage: <b>Send any file or URL and the bot will upload it to mixdrop.co</b>"
