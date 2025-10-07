# main.py
# Abrar's Discord Bot: Vector

# Bot character based on the mobile gacha game, Girl's Frontline 1/2 (Based on the Kriss Vector) in where a character is named Vector/Vivi . Art is also from said game

# Imports
import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv
import os
import logging
import asyncio
import random

# Loading Token from environment file (.env)
load_dotenv()
discord_token = os.getenv('DISCORD_TOKEN')

# Setting up Logging
handler = logging.FileHandler(filename='discord_bot.log', encoding='utf-8', mode='w')

# Intents + Perms
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

# Discord Status Options
status = ["with LEGOs", "in the armory", "with IEDs", "with .45","with 9mm", "with .22LR"]

# Declaring Prefix as m! and setting Playing Status 
bot = commands.Bot(command_prefix="v!", help_command=None, activity=discord.Game(random.choice(status)), intents=intents)

# Async function to load cogs
async def load_cogs():
    cog_extensions = ["fun"]
    for extension in cog_extensions:
        await bot.load_extension(extension)
        print(f"Loaded {extension}")

#Status Changer Task/Function - changes status every 30 minutes
@tasks.loop(minutes=30) 
async def change_status():
    new_status = random.choice(status)
    await bot.change_presence(activity=discord.Game(new_status))
    print(f"Status changed to: {new_status}")  # Status changes in console

# Launch Status in the Terminal
@bot.event
async def on_ready():
    print(f"Heyo! {bot.user.name} Reporting In!")
    if not change_status.is_running():
        change_status.start()
        print("Status changer started")

# Help Command + Documentation for commands
@bot.command()
async def help(ctx):
    help_text = """
    ```
    Vector Bot Commands:
    - v!help | Display this help message.
    - v!ping | Check the bot's latency.
    - v!dice [sides] | Roll a dice with the specified number of sides (default is 6)

    Special/Fun Features:
    - The bot will respond if you mention "Vector" in your message.
    - The bot counts and responds when you say "hello" or "python".
    ```
    """
    await ctx.send(help_text)

# Main async function to run the bot
async def main():
    await load_cogs()
    await bot.start(discord_token)

# Run the bot
if __name__ == "__main__":
    asyncio.run(main())