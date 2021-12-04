
from pyrogram import *
import datetime
from bot import (
    BOT_TOKEN,
    API_ID,
    API_HASH,
    LOGGER
)


class CloudBot(Client):
    def __init__(self):
        name = self.__class__.__name__.lower()
        self.logger = LOGGER(__name__)

        super().__init__(
            name,
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            plugins={
                "root": "bot/plugins"
            }
        )

    async def start(self):
        await super().start()
        self.logger.info(f"BOT IS STARTED {datetime.datetime.now()}")

    async def stop(self, *args):
        await super().stop()
        self.logger.info(f"BOT IS STOPPED {datetime.datetime.now()}")
