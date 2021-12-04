from bot import LOGGER
from ..filetocloud import CloudBot
from .upload import server_upload
from ..helpers import download_media
from pyrogram.types import CallbackQuery

logger = LOGGER(__name__)


async def upload_handler(client: CloudBot, message: CallbackQuery, file_name: str, file_size: str, callback_data: str):

    try:
        FILE_PATH = await download_media(client, message)
    except Exception as e:
        logger.error(f"{e}")
        await client.edit_message_text(
            chat_id=message.from_user.id,
            message_id=message.message.message_id,
            text=f"**File downloading error:** `{e}`",
        )
        return
    try:
        if callback_data.startswith('transfersh'):
            await client.edit_message_text(
                chat_id=message.message.chat.id,
                text="Temporarily down",
                message_id=message.message.message_id,
            )
            return

        elif callback_data.startswith('gofileio'):
            url = 'https://store1.gofile.io/uploadFile'
            response = await server_upload(file=FILE_PATH, url=url)
            _URL = await gofileIO(response)

        elif callback_data.startswith('fileio'):
            url = 'https://file.io/'
            response = await server_upload(file=FILE_PATH, url=url)
            _URL = await fileIO(response)

        elif callback_data.startswith('anonfiles'):
            url = 'https://api.anonfiles.com/upload'
            response = await server_upload(file=FILE_PATH, url=url)
            _URL = await anonfiles(response)

        await client.edit_message_text(
            chat_id=message.message.chat.id,
            text=(
                f"File Name: `{file_name}`"
                f"\nFile Size: `{file_size}`"
                f'\nURL: `{_URL}`'
            ),
            message_id=message.message.message_id
            # reply_markup=completedKeyboard(dl)
        )
    except Exception as e:
        logger.error(f'{e}')
        await client.edit_message_text(
            chat_id=message.from_user.id,
            message_id=message.message.message_id,
            text=f"**File uploading error:** `{e}`",
        )
        return


async def anonfiles(response):
    return response['data']['file']['url']['short']


async def fileIO(response):
    return response['link']


async def gofileIO(response):
    return response['data']['downloadPage']
