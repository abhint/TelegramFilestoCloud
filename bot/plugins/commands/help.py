from bot.filetocloud import CloudBot, filters
from bot import HELP, SOURCE


@CloudBot.on_message(filters.command(["help", "h"]))
async def help_message(client, message):
    await client.send_message(
        chat_id=message.chat.id,
        text=f"Hey {message.from_user.first_name},{HELP}{SOURCE}",
        reply_to_message_id=message.message_id,
    )
