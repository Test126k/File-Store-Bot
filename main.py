import os
from pyrogram import Client
from flask import Flask

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
    bot_token=os.environ.get("7714466772:AAGX4YKqTQQQAro8lJoycxBGpv6QZ5IsEvs")
)

# Start the bot using a Flask thread-safe method
if __name__ == "__main__":
    from threading import Thread

    def start_bot():
        bot.run()

    # Run the Flask app in the main thread and the bot in the background
    thread = Thread(target=start_bot)
    thread.start()

    # Run the Flask app on port 8080
    app.run(host="0.0.0.0", port=8080)
