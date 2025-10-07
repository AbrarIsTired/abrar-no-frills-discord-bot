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

    # Rock Paper Scissors Command
    @commands.command()
    async def rps(self, ctx, user_choice: str = None):
        if user_choice is None: # Check for no input
            await ctx.send("Please choose rock, paper, or scissors.")
            return None

        choices = ["rock", "paper", "scissors"] # Available choices for Bot and User
        user_choice = user_choice.lower()

        if user_choice not in choices: # Check for invalid value
            await ctx.send("Invalid choice! Please choose rock, paper, or scissors.")
            return None

        # Bot Choice
        bot_choice = random.choice(choices)
        result = ""

        # Winner Logic
        if user_choice == bot_choice:
            result = "It's a tie!"
        if(user_choice == "rock" and bot_choice == "scissors") or (user_choice == "paper" and bot_choice == "rock") or (user_choice == "scissors" and bot_choice == "paper"):
            result = "You win!"
        elif user_choice != bot_choice:
            result = "I win!"
        
        # Result Output
        await ctx.send(f"You chose {user_choice}, I chose {bot_choice}. {result}")

    # Dice Roll Command
    @commands.command()
    async def dice(self, ctx, sides: int = 6):
        # Guard for anything less than 2 sides
        if(sides <= 1):
            await ctx.send("Number of sides must be a minimum of 2.")
            return None
        
        # Dice Roll Logic
        result = random.randint(1, sides)
        
        # For Nat-Values
        if(result == sides):
            await ctx.send(f"🎲 Nat-{sides}! You rolled a {result}!")
            return None
        # Roll Result    
        await ctx.send(f"🎲 You rolled a {result} on a {sides}-sided dice!")


    # Event Listener for messages containing specific words
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        if "vector" in message.content.lower():
            await message.channel.send(f"Yo Commander, what do you want? I'm busy right now")

    


# Cog seutp
async def setup(bot):
    await bot.add_cog(Core(bot))