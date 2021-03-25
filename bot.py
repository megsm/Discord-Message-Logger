import discord
from discord.ext import commands
import csv
import os
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Prepare the client
client = commands.Bot(command_prefix=':')

# Event Listeners
@client.event
async def on_ready():
    print("Bot Ready, Listening for Messages")

# Main Message Listener
@client.event
async def on_message(msg):
    if msg.author == client.user: return

    # Append to CSV
    with open(os.environ["OUTPUT_FILENAME"], "a+", newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([msg.content])
    print("[{}] Saved: {}".format(datetime.now(), msg.content))

# Run the bot
client.run(os.environ["DISCORD_TOKEN"])