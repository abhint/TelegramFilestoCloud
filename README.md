## What is about this bot ?

#### This bot uploads telegram files to a third-party server.
#### Usage: Send any file or bot. Then select the third-party server you want to upload to.

### Supported clouds
- [x] anonfiles.com
- [x] file.io
- [x] gofile.io
- [x] Transfer.sh
- [ ] mixdrop.co

### Installation
#### Clone

```sh
git clone https://github.com/AbhijithNT/TelegramFiletoCloud.git

cd TelegramFiletoCloud

```

#### Install Requirements

```sh
pip3 install -U -r requirements.txt
```
#### Edit Sample_config.py and replace it with your bot details like this

```python
class Config:
    BOT_USE = False                        # True is private use
    BOT_TOKEN = ''                         # from @botfather
    APP_ID = 1234567                       # from https://my.telegram.org/apps
    API_HASH = ''                          # from https://my.telegram.org/apps
    AUTH_USERS = []                        # Private users id
```

#### Run this bot
```sh
python3 -m bot
```

### Heroku Deploy
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## :clap:  Supporters

### Stargazers
[![Stargazers repo roster for @abhint/TelegramFilestoCloud](https://reporoster.com/stars/dark/abhint/TelegramFilestoCloud)](https://github.com/abhint/TelegramFilestoCloud/stargazers)
### Forkers
[![Forkers repo roster for @abhint/TelegramFilestoCloud](https://reporoster.com/forks/dark/abhint/TelegramFilestoCloud)](https://github.com/abhint/TelegramFilestoCloud/network/members)
