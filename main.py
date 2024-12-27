from pyrogram import Client

class Bot(Client):
    async def start(self):
        # Replace 'use_qr' logic with an alternative if needed
        await super().start()
        print("Bot has started!")

    async def stop(self, *args):
        await super().stop()
        print("Bot has stopped!")

if __name__ == "__main__":
    Bot("my_bot").run()
