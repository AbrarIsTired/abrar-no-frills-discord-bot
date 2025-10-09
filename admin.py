# admin.py

import discord
from discord.ext import commands
import os
import sys

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Shutdown Command
    @commands.command()
    @commands.is_owner()
    async def shutdown(self, ctx):
        await ctx.send("Shutting down... Goodbye, Commander.")
        await self.bot.close()

    # Clear Chat
    @commands.command()
    @commands.is_owner()
    async def clear(self, ctx, amount: int = 0):
        if amount < 2 or amount > 100: # Guard for invalid values
            await ctx.send("Please specify an amount between **2** and **100**.")
            return None
        deleted = await ctx.channel.purge(limit=amount + 1) # +1 to account for the command message
        await ctx.send(f"{ctx.author.mention} Cleared {len(deleted) - 1} messages.")
# Cog seutp
async def setup(bot):
    await bot.add_cog(Admin(bot))