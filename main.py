from pyrogram import Client

bot = Client(
    "my_bot",
    api_id=26300022,  # Your API ID
    api_hash="def44e13defba9d104323e821955dfa3",  # Your API Hash
    bot_token="7714466772:AAGX4YKqTQQQAro8lJoycxBGpv6QZ5IsEvs"  # Replace with your bot's token
)

bot.run()
