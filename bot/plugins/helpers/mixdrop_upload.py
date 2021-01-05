from logging import error
import aiohttp
from bot.plugins.display.time import  time_data

async def mixFileup(file, bot, s_time):
    #https://github.com/odysseusmax/uploads/blob/master/mixdrop.py
    try:
        await bot.edit(
            text = "Uploadig to MixDrop.."
        )
        email = "veyopi9060@aomrock.com"
        api_key = "TUtD1QIPwPyaoHql14C"
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


