import os
from pyrogram import Client

bot = Client(
    "my_bot",
    api_id=int(os.environ.get("26300022")),
    api_hash=os.environ.get("def44e13defba9d104323e821955dfa3")
)

bot.run()
