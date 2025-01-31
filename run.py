import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
from commands import getPoints
from commands.getPoints import getLPFromUser

bot = commands.Bot(command_prefix=".", intents=discord.Intents.all())
load_dotenv()


@bot.event
async def on_ready():
    print("Booted up")


@bot.command()
async def getLP(ctx):
    await ctx.send(getLPFromUser(ctx))

@bot.command()
async def test(ctx):
    await ctx.send(f"test, {ctx.author.mention}")


botToken = os.getenv('DISCORD_TOKEN')
bot.run(botToken)
