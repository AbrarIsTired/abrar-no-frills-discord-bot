import discord
from discord.ext import commands

class Core(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.count = 0

    #Latency of the Bot
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Current Latency: {round(self.bot.latency * 1000)}ms')


    #Word-Counter
    count = 0
    @commands.Cog.listener()
    async def on_message(self, message):
        # Ignore messages from the bot itself (to avoid infinite loops)
        if message.author == self.bot.user:
            return

        # If someone says "m4", reply
        if "m4" in message.content.lower():
            await message.channel.send(f"Hey, you said my name! Hello {message.author.mention}")
            return None

        # Word bank example
        word_bank = ["hello", "python"]
        # Loop through the words we want to track
        for i in word_bank:
            if i in message.content.lower():
                self.count += 1  # increase the counter
                await message.channel.send(f"Hey, you said {i}! That's from the word-bank. Total Count: {self.count}.")
                break  #Stops after first match


def setup(bot):
    bot.add_cog(Core(bot))