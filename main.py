# Abrar's Discord Bot: M4 SOPMOD II

# Bot character based on the mobile gacha game, Girl's Frontline in where a character is named M4-SOPMOD II. Art is also from said game

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

#Declaring Prefix as m! and setting Playing Status 
bot = commands.Bot(command_prefix = "m!", activity=discord.Game('with LEGOs'),intents=intents)

#Launch Status in the Terminal
@bot.event
async def on_ready():
    print(f"Heyo! {bot.user.name} Reporting In!")


#Prefix Based Commands (ex. m!command)

#Latency of the Bot
@bot.command
async def ping(ctx):
    await ctx.send(f'Current Latency: {round(bot.latency * 1000)}ms')


#Context Based Commands (ex. Triggers on specific words outside of command)

#Word-Counter
count = 0
@bot.event
async def on_message(message):
    global count
    if(message.author == bot.user):
        return None
    
    if("m4" in message.content.lower()):
        await message.channel.send(f"Hey, you said my name! Hello {message.author.mention}")
        return None
    
    word_bank = ["hello", "python"]
    for i in word_bank:
        if(i in message.content.lower()):
            count += 1
            await message.channel.send(f"Hey, you said {i}! That's from the word-bank. Total Count: {count}.")
            break


#Using Bot Token from the enviroment file it runs the bot
bot.run(discord_token)