import os
from dotenv import load_dotenv
load_dotenv()

def get_env(name: str, terminal_action: bool = True) -> str:
    if name in os.environ:
        return os.environ[name]
    if terminal_action:
        value_name = input(f'Enter your {name}: ')
        return value_name
    else:
        return name