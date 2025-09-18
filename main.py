# Abrar's Discord Bot

#Imports
import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
import random

#Loading Secret Token
load_dotenv()
discord_token = os.getenv('DISCORD_TOKEN')

#Intents + Perms
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

#Prefix is m! for M4 SOPMOD II, my personal bot
bot = commands.Bot(command_prefix = "m!", activity=discord.Game('with IEDs'),intents=intents)

@bot.command
async def on_ready():
    print(f"Heyo! {bot.user.name} Reporting In!")


#Connection of the bot using f-strings
@bot.command()
async def ping(ctx):
    await ctx.send(f'Current Latency: {round(bot.latency * 1000)}ms')

bot.run(discord_token)