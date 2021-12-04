from bot.filetocloud import CloudBot, filters
from bot import START, SOURCE


@CloudBot.on_message(filters.command("start"))
async def start_message(client, message):
    await client.send_message(
        chat_id=message.chat.id,
        text=f"Hey {message.from_user.first_name},{START}{SOURCE}",
        reply_to_message_id=message.message_id,
        parse_mode="html"
    )
