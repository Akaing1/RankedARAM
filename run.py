import asyncio

import discord
from discord.ext import commands

from data.database.dbOperations import *

bot = commands.Bot(command_prefix=".", intents=discord.Intents.all())
load_dotenv()
db = DBOperations()
botToken = os.getenv('DISCORD_TOKEN')


@bot.event
async def on_ready():
    print("Booted up")


# @bot.command()
# async def register(ctx):
#     if db.registerUser(ctx, 'Zaphkiel#stf'):
#         await ctx.send(f"{ctx.author.mention} has been registered successfully!")
#     else:
#         await ctx.send(f"{ctx.author.mention} there was an issue registering you.")
#
#
# @bot.command()
# async def remove(ctx):
#     if db.removeUser(ctx):
#         await ctx.send(f"{ctx.author.mention} has been deleted successfully!")
#     else:
#         await ctx.send(f"{ctx.author.mention} there was an issue removing you.")


# @bot.command()
# async def getData(ctx):
#     await ctx.send(db.getUserData(ctx))
#
#
# @bot.command()
# async def LP(ctx):
#     await ctx.send(getLPFromUser(ctx, db))


@bot.command()
async def test(ctx):
    await ctx.send(f"test, {ctx.author.mention}")


async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")


async def main():
    async with bot:
        await load()
        await bot.start(botToken)


asyncio.run(main())
