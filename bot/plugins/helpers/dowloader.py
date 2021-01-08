from pyrogram import Client
import time
from bot.plugins.upload_servers.fileio_upload import fileIO
from bot.plugins.upload_servers.mixdrop_upload import mixFileup
from bot.plugins.display import progress

async def fileDownload(client, bot):
    file_path = ''
    now = time.time()
    upload_server = bot.data
    userMsg = await client.edit_message_text(
        chat_id=bot.from_user.id,
        message_id=bot.message.message_id,
        text="processing your request...please wait",
    )
    user_progress = userMsg
    try:
        file_path = await client.download_media(
        message = userMsg.reply_to_message,
        progress=progress,
        progress_args=(
            "Downloading...",
            user_progress,
            now
        )
    )
    except Exception as error:
        print(error)
    print(file_path)
    if upload_server == "MixDrop":
        await mixFileup(file_path,client, bot, now)
    if upload_server == "File.io":
        await fileIO(file_path, client, bot, now)

    # file_path = await client.download_media(
    #     message=bot.reply_to_message,
    #     progress=progress,
    #     progress_args=(
    #         "Downloading...",
    #         userMsg,
    #         now
    #     )
    # )
    # await client.edit_message_text(
    #     chat_id=bot.from_user.id,
    #     message_id=bot.message.message_id,
    #     text="hello"
    #     )
