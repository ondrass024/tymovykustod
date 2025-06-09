# Týmový Kustod – Discord bot pro esport hokejový tým

import os
import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
import datetime
import json
import asyncio

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
DATA_FILE = "data.json"

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

# ... (celý obsah z canvasu pokračuje dál – byl vložen předtím) ...
