import os
import asyncio
from pyrogram import Client
from flask import Flask
from threading import Thread

# Your Flask app
app = Flask(__name__)

@app.route('/')
def health_check():
    return "Bot is running!"

# Initialize your Pyrogram bot
bot = Client(
    "my_bot",
    api_id=26300022,
    api_hash="def44e13defba9d104323e821955dfa3",
    bot_token=os.environ.get("BOT_TOKEN")
)

# Start the bot in an async event loop
async def start_bot():
    await bot.start()

# Start the Flask app
def start_flask():
    app.run(host="0.0.0.0", port=8080)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()

    # Start both the Flask app and the bot
    loop.create_task(start_bot())
    thread = Thread(target=start_flask)
    thread.start()

    # Run the event loop
    loop.run_forever()
