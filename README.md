## What is about this bot ?

### This bot uploads telegram files to MixDrop.co, File.io.
### Usage: Send any file, and the bot will upload it to MixDrop.co, File.io

### Heroku Deploy
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/Abhijith-cloud/Telegram-MixDrop-Bot/)

# Installation
#### Clone 

```sh
git clone https://github.com/Abhijith-cloud/TelegramFiletoCloud.git

cd TelegramFiletoCloud

```

#### Install Requirements

```sh
pip3 install -U -r requirements.txt
```
#### Edit Sample_config.py and replace it with your bot details like this

```python3
class Config:
    BOT_TOKEN = '1051231515:AAGv9yJbkpqQBx5nPnSRTNjF66Y5C9u4u3E'  # from @botfather
    APP_ID = 1234567                                              # from https://my.telegram.org/apps
    API_HASH = 'a6ec7e2ead26d1bcac4a3997780a864c'                 # from https://my.telegram.org/apps
    API_KEY = 'aoHq14CTUQyIPwltD1P'                               # from https://mixdrop.co
    API_EMAIL = 'mixdrop.login.mail.id@yourmail.com'              # from https://mixdrop.co
    AUTH_USERS = [1070202696, <YOUR TELEGRAM CHAT ID>]                                     # ADD YOUR USER ID
```

#### Run this bot
```sh
python3 -m bot
```
## :clap:  Supporters
[![Stargazers repo roster for @Abhijith-cloud/TelegramFiletoCloud](https://reporoster.com/stars/Abhijith-cloud/TelegramFiletoCloud)](https://github.com/Abhijith-cloud/TelegramFiletoCloud/stargazers)
[![Forkers repo roster for @Abhijith-cloud/TelegramFiletoCloud](https://reporoster.com/forks/Abhijith-cloud/TelegramFiletoCloud)](https://github.com/Abhijith-cloud/TelegramFiletoCloud/network/members)
