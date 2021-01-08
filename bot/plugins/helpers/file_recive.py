#!/usr/bin/env python3
# This is bot coded by Abhijith-cloud and used for educational purposes only
# https://github.com/Abhijith-cloud
# (c) Abhijith N T ;-)
# Thank you https://github.com/pyrogram/pyrogram :-)

from pyrogram import Client,filters
from bot import LOGGER
from hurry.filesize import size
from bot.plugins.keybord import server_select

@Client.on_message(filters.video)
async def userVideo(client, bot):
    LOGGER.info(f"{bot.chat.id} - {bot.video.file_name}")
    await client.send_message(
        chat_id=bot.chat.id,
        text = (
        f"File Name: <code>{bot.video.file_name}</code>"
        f"\nFile Size: <code>{size(bot.video.file_size)}</code>"
        ),
        reply_markup=server_select(),
        reply_to_message_id=bot.message_id
    )
@Client.on_message(filters.document)
async def userDocument(client, bot):
    LOGGER.info(f"{bot.chat.id} - {bot.document.file_name}")
    await client.send_message(
        chat_id=bot.chat.id,
        text = (
        f"File Name: <code>{bot.document.file_name}</code>"
        f"\nFile Size: <code>{size(bot.document.file_size)}</code>"
        ),
        reply_markup=server_select(),
        reply_to_message_id=bot.message_id
    )
@Client.on_message(filters.audio)
async def userAudio(client, bot):
    LOGGER.info(f"{bot.chat.id} - {bot.audio.file_name}")
    await client.send_message(
        chat_id=bot.chat.id,
        text = (
        f"File Name: <code>{bot.audio.file_name}</code>"
        f"\nFile Size: <code>{size(bot.audio.file_size)}</code>"
        ),
        reply_markup=server_select(),
        reply_to_message_id=bot.message_id
    )












# @Client.on_message(filters.media)
# async def userMedia(client, bot):
#     now = time.time()
#     link = ''
#     f_size = ''
#     f_name = ''
#     file = ''

#     userMsg = await client.send_message(
#         chat_id=bot.chat.id,
#         text = "processing your request...please wait"
#     )

#     try:
#         file = await bot.download(
#             progress = progress,
#             progress_args = (
#                 'Downloading....',
#                 userMsg,
#                 now
#             )
#         )
#         f_size = os.path.getsize(file)
#         f_name = file.split('/')[-1]
#         link = await mixFileup(file, userMsg, now)
#         for i in link:
#             pass
#         LOGGER.info(f"""
#         Download:{bot.from_user.id}:
#         File Name:{f_name}
#         Link:{link}
#         """)
#     except Exception as error:
#         print(error)
#     await bot.reply(
#         text = f"""
#         File Name: {f_name}
#         \nSIZE: {size(f_size)}
#         """,
#         reply_markup=InlineKeyboardMarkup(
#             [
#                 [
#                     InlineKeyboardButton(
#                         "DOWNLOAD !",
#                         url=f"{link}"
#                     ),
#                 ],
#             ]
#         )
#     )
#     try:
#         os.remove(file)
#         LOGGER.info(f"{bot.from_user.id} {file} Remove")
#     except Exception as error:
#         LOGGER.info(f"{file} not Remove")
#         print(error)
