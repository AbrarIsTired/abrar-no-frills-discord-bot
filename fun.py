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
        if sides < 1:
            await ctx.send("Number of sides must be at least 2.")
            return
        result = random.randint(1, sides)
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