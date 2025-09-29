# fun.py
import discord
from discord.ext import commands
import random

class Core(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.count = 0


    # Simple Ping Command
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"Current Latency: {round(self.bot.latency*1000)}ms")

    # Dice Roll Command
    @commands.command()
    async def dice(self, ctx, sides: int = 6):
        # Guard for anything less than 2 sides
        if(sides <= 1):
            await ctx.send("Number of sides must be a minimum of 2.")
            return None
        
        # Dice Roll Logic
        result = random.randint(1, sides)
        
        # For Nat-20s
        if(sides == 20 and result == 20):
            await ctx.send(f"🎲 Nat-{sides}! You rolled a {result}!")
            return None
        # Roll Result    
        await ctx.send(f"🎲 You rolled a {result} on a {sides}-sided dice!")


    # Event Listener for messages containing specific words
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        if "m4" in message.content.lower():
            await message.channel.send(f"Hey, you said my name! Hiya {message.author.mention}")


# Cog seutp
async def setup(bot):
    await bot.add_cog(Core(bot))