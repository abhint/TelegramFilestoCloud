#!/usr/bin/env python3
# This is bot coded by Abhijith N T and used for educational purposes only
# https://github.com/AbhijithNT
# Copyright ABHIJITH N T
# Thank you https://github.com/pyrogram/pyrogram


from bot.plugins.display.time import time_data


async def progress(current, total, up_msg, message, start_time):

    try:
        percent = round(current * 100 // total)
        await message.edit(
            text="{0} {1}%".format(
                progressBar(percent),
                percent
            )
        )
    except Exception as e:
        await message.edit(
            text=f"ERROR: {e}"
        )


def progressBar(percent):
    done_block = '█'
    empty_block = '░'
    return f"{done_block * int(percent / 5)}{empty_block * int(20 - int(percent / 5))}"
