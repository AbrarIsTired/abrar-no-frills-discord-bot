import discord
from discord.ext import commands

class Core(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.count = 0

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"Pong! {round(self.bot.latency*1000)}ms")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        if "m4" in message.content.lower():
            await message.channel.send(f"Hey, you said my name! Hello {message.author.mention}")

        word_bank = ["hello", "python"]
        for word in word_bank:
            if word in message.content.lower():
                self.count += 1
                await message.channel.send(f"Hey, you said {word}! Count: {self.count}")
                break

        # allow commands to still work
        await self.bot.process_commands(message)

def setup(bot):
    bot.add_cog(Core(bot))
