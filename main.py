from pyrogram import Client

bot = Client(
    "my_bot",
    api_id=26300022,  # Your API ID
    api_hash="def44e13defba9d104323e821955dfa3"  # Your API Hash
)

bot.run()
