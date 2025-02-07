import asyncio
import logging

import discord
from discord.ext import commands

from data.database.dbOperations import *

bot = commands.Bot(command_prefix=".", intents=discord.Intents.all())

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

load_dotenv()
db = DBOperations()
botToken = os.getenv('DISCORD_TOKEN')


@bot.event
async def on_ready():
    logger.info("Booted up")

    try:
        synced_commands = await bot.tree.sync()
        logger.info(f"Synced {len(synced_commands)} commands.")
    except Exception as e:
        logger.info("An error with syncing application commands has occurred: ", e)


@bot.tree.command(name="test", description="test")
async def test(interaction: discord.Interaction):
    await interaction.response.send_message(f"{interaction.user.mention} test")


async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")


async def main():
    async with bot:
        await load()
        await bot.start(botToken)


asyncio.run(main())
