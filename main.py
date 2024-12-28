import os
from pyrogram import Client

bot = Client(
    "my_bot",
    api_id=int(os.environ.get("API_ID")),
    api_hash=os.environ.get("API_HASH")
)

bot.run()
