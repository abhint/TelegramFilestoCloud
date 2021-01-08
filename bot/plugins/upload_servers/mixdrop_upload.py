from logging import error
import aiohttp
from bot.plugins.display.time import  time_data
from bot import (
    API_KEY,
    API_EMAIL
)

env_email = API_EMAIL
env_api_key = API_KEY

async def mixFileup(file, bot, s_time):
    #https://github.com/odysseusmax/uploads/blob/master/mixdrop.py
    try:
        await bot.edit(
            text = "Uploadig to MixDrop.."
        )
        email = env_email
        api_key = env_api_key
        upload_url = "https://ul.mixdrop.co/api"
        async with aiohttp.ClientSession() as session:
            file_to_upload = file
            data = {
                'file': open(file_to_upload, 'rb'),
                'email': email,
                'key': api_key
            }
            response = await session.post(upload_url, data=data)
            link = await response.json()
            await bot.edit(
                text = f"Uploaded...100% in {time_data(s_time)}"
            )
            return f"https://mixdrop.co/f/{link['result']['fileref']}"
    except Exception as eror:
        print(error)


