from pyrogram import Client

class Bot(Client):
    async def start(self):
        await super().start()
        print("Bot has started!")

    async def stop(self, *args):
        await super().stop()
        print("Bot has stopped!")

if __name__ == "__main__":
    bot = Bot(
        "my_bot",  # Replace with your bot's name/session string
        api_id=26300022,  # Replace with your Telegram API ID
        api_hash="def44e13defba9d104323e821955dfa3"  # Replace with your Telegram API hash
    )
    bot.run()  # No unsupported arguments like `use_qr`
