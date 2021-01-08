import requests
import json
from bot.plugins.keybord import downloadButton
from bot.plugins.display.time import  time_data

async def fileIO(file_name, client, bot, s_time):
    print(1)
    try:
        await client.edit_message_text(
        chat_id=bot.from_user.id,
        message_id=bot.message.message_id,
        text="Uploadig to File.IO",
        )
        files = {
            'file': (file_name, open( file_name, 'rb')),
        }
        response = requests.post('https://file.io/', files=files)
        response = await json.loads(response.text)
        dl_b = response['link']
        await downloadButton(dl_b)
        await client.edit_message_text(
            chat_id=bot.from_user.id,
            message_id=bot.message.message_id,
            text=f"Uploaded...100% in {time_data(s_time)}",
        )
        await client.client.send_message(
            chat_id=bot.from_user.id,
            text=f"Enjoy Enjoy..",
            reply_markup=downloadButton()
            )
    except Exception as error:
        print(error)
