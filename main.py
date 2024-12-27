from pyrogram import Client

class Bot(Client):
    async def start(self):
        await super().start()
        print("Bot has started!")

    async def stop(self, *args):
        await super().stop()
        print("Bot has stopped!")

if __name__ == "__main__":
    # Initialize the Bot with appropriate parameters
    bot = Bot("my_bot")  # Replace "my_bot" with the correct session name or parameters
    bot.run()  # No extra arguments passed here
