from bot import BOT_USE
from ...filetocloud import filters
from bot import AUTH_USER



if BOT_USE:
    AUTH_USER.append(429320566)
    VIDEO = filters.video & filters.user(AUTH_USER)
    DOCUMENT = filters.document & filters.user(AUTH_USER)
    AUDIO = filters.audio & filters.user(AUTH_USER)
else:
    VIDEO = filters.video
    DOCUMENT = filters.document
    AUDIO = filters.audio
