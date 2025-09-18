# Abrar's Discord Bot: M4 SOPMOD II

# Bot character based on the mobile gacha game, Girl's Frontline in where a character is named M4-SOPMOD II. Art is also from said game

#Imports
import discord
from discord.ext import commands
from dotenv import load_dotenv
import os


#Commands are distributed across files to not "overfill" a file
import admin
import core

#Loading Token from enviroment file (.env)
load_dotenv()
discord_token = os.getenv('DISCORD_TOKEN')

#Intents + Perms
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

#Declaring Prefix as m! and setting Playing Status 
bot = commands.Bot(command_prefix = "m!", activity=discord.Game('with LEGOs'),intents=intents)

#Launch Status in the Terminal
@bot.event
async def on_ready():
    print(f"Heyo! {bot.user.name} Reporting In!")

cog_extensions = ["core","admin"]
for i in cog_extensions:
    bot.load_extension(i)
    print(f"Loaded {i}")

#Using Bot Token from the enviroment file it runs the bot
bot.run(discord_token)