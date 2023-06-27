import os
import discord
import datetime
import pytz
import random
import asyncio
from dotenv import load_dotenv
from discord.ext import commands,tasks

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    guild = discord.utils.get(bot.guilds, name=GUILD)
    print(f'{bot.user} has entered {guild.name}, let the stinking commence!')

bot.run(TOKEN)