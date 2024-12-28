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

# Start the bot and the Flask app in the same thread
if __name__ == "__main__":
    from threading import Thread
    
    # Start the Flask app
    def start_flask():
        app.run(host="0.0.0.0", port=8080)  # Ensure this is on port 8080 for Koyeb health check
    
    # Run both the bot and Flask in the main thread
    bot.run()  # This will block the main thread and run the bot
    start_flask()  # Flask will start after the bot
