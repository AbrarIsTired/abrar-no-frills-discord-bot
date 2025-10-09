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
    cog_extensions = ["fun", "admin"] # Cog/File List
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
    print(f"Long time no see, Commander… Neural module nominal, all limbs accounted for, I’m not scraps yet… I’m glad to see you again, Commander, you’re like the sun after a storm.")
    if not change_status.is_running():
        change_status.start()
        print("Status changer started")



# Help Command. Overrides default help command. Learning Embeds
@bot.command()
async def help(ctx):
    # Create the Embed object
    embed = discord.Embed(
        title="🤖 Vector Bot Commands (v!)",
        description="Long time no see, Commander. Here's a list of my current protocols.",
        color=discord.Color.blue() # A nice blue color
    )

    # General/Fun Commands Field
    fun_commands = (
        "`v!help` | Display this help message.\n"
        "`v!ping` | Check the bot's latency.\n"
        "`v!dice [sides]` | Roll a dice (default 6 sides).\n"
        "`v!rps [r/p/s]` | Play Rock-Paper-Scissors."
    )
    embed.add_field(name="🛠️ General/Fun Commands", value=fun_commands, inline=False)

    # Admin Commands Field
    admin_commands = (
        "`v!shutdown` | Safely shut down the bot. (Owner Only)\n"
        "`v!clear [amount]` | Clear messages (2-100). (Owner Only)"
    )
    embed.add_field(name="⚙️ Admin Commands (Owner Only)", value=admin_commands, inline=False)
    
    # Special Features Field
    embed.add_field(
        name="⭐ Special Feature", 
        value="I'll respond if you mention my name, **Vector**, in a message!", 
        inline=False
    )

    await ctx.send(embed=embed)

# Main async function to run the bot
async def main():
    await load_cogs()
    await bot.start(discord_token)

# Run the bot
if __name__ == "__main__":
    asyncio.run(main())