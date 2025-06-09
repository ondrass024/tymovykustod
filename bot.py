# Týmový Kustod – Discord bot pro esport hokejový tým s web serverem pro Render Free plán

import os
import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
import datetime
import json
import threading
from flask import Flask

# Flask web server pro udržení portu
app = Flask(__name__)

@app.route('/')
def index():
    return "Týmový Kustod běží!"

def run_web():
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))

# Discord část
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
DATA_FILE = "data.json"

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"✅ Týmový Kustod je online jako {bot.user}")

# (příkazy zůstávají stejné...)

# Spuštění Flask serveru v paralelním vlákně
threading.Thread(target=run_web).start()

# Spuštění bota
bot.run(TOKEN)
