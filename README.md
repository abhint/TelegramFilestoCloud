## What is about this bot ?

### This bot uploads telegram files to mixdrop.co. Usage: Send any file or URL and the bot will upload it to mixdrop.co

# Installation

#### Install Requirements

```sh
pip3 install -U -r requirements.txt
```
#### Edite sample_config.py

##### Replace with your bot details

```python3
class config():
    BOT_TOKEN = '1051231515:AAGv9yJbkpqQBx5nPnSRTNjF66Y5C9u4u3E'  # from @botfather
    APP_ID = 1234567                                              # from https://my.telegram.org/apps
    API_HASH = 'a6ec7e2ead26d1bcac4a3997780a864c'                 # from https://my.telegram.org/apps
```

#### Run this bot
```sh
python3 -m bot
```
