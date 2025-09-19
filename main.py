# main.py
# Abrar's Discord Bot: M4 SOPMOD II

# Bot character based on the mobile gacha game, Girl's Frontline in where a character is named M4-SOPMOD II. Art is also from said game

# Imports
import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import logging
import asyncio

# Loading Token from environment file (.env)
load_dotenv()
discord_token = os.getenv('DISCORD_TOKEN')

# Setting up Logging
handler = logging.FileHandler(filename='discord_bot.log', encoding='utf-8', mode='w')

# Intents + Perms
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

# Declaring Prefix as m! and setting Playing Status 
bot = commands.Bot(command_prefix="m!", activity=discord.Game('with LEGOs'), intents=intents)

# Async function to load cogs
async def load_cogs():
    cog_extensions = ["core"]
    for extension in cog_extensions:
            await bot.load_extension(extension)
            print(f"Loaded {extension}")


# Launch Status in the Terminal
@bot.event
async def on_ready():
    print(f"Heyo! {bot.user.name} Reporting In!")

# Main async function to run the bot
async def main():
    await load_cogs()
    await bot.start(discord_token)

# Run the bot
if __name__ == "__main__":
    asyncio.run(main())