import os

class env_data():
    BOT_TOKEN = os.environ["BOT_TOKEN"]    # from @botfather
    API_ID = int(os.environ["API_ID"])     # from https://my.telegram.org/apps
    API_HASH = os.environ["API_HASH"]      # from https://my.telegram.org/apps
