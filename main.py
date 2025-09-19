# main.py
# Abrar's Discord Bot: M4 SOPMOD II

# Bot character based on the mobile gacha game, Girl's Frontline in where a character is named M4-SOPMOD II. Art is also from said game

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
status = ["with LEGOs", "in the armory", "with IEDs", "with 556"]

# Declaring Prefix as m! and setting Playing Status 
bot = commands.Bot(command_prefix="m!", help_command=None, activity=discord.Game(random.choice(status)), intents=intents)

# Async function to load cogs
async def load_cogs():
    cog_extensions = ["core"]
    for extension in cog_extensions:
        await bot.load_extension(extension)
        print(f"Loaded {extension}")

#Status Changer Task/Function - changes status every 30 minutes
@tasks.loop(minutes=30) 
async def change_status():
    new_status = random.choice(status)
    await bot.change_presence(activity=discord.Game(new_status))
    print(f"Status changed to:{new_status}")  # Optional: see status changes in console

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
    M4 SOPMOD II Bot Commands:
    - m!help | Display this help message.
    - m!ping | Check the bot's latency.

    Special/Fun Features:
    - The bot will respond if you mention "m4" in your message.
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