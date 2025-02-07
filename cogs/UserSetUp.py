import logging
import discord
from discord import app_commands
from discord.ext import commands
from data.database.dbOperations import DBOperations
from data.riotData.PlayerData import PlayerData

logger = logging.getLogger()
db = DBOperations()
playerData = PlayerData()


class UserSetUp(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        logger.info("Users ready to be set up!")

    @app_commands.command(name="register", description="register user")
    @app_commands.describe(riotid="Enter RiotID here: ex. JohnDoe#NA1")
    async def register(self, interaction: discord.Interaction, riotid: str):
        if playerData.checkRiotIDisValid(riotid):
            if db.registerUser(interaction, riotid):
                await interaction.response.send_message(f"{interaction.user.mention} has been registered successfully!")
            else:
                await interaction.response.send_message(f"{interaction.user.mention} there was an issue registering you.")

    @app_commands.command(name="remove", description="remove user")
    async def remove(self, interaction: discord.Interaction):
        if db.removeUser(interaction):
            await interaction.response.send_message(f"{interaction.user.mention} has been deleted successfully!")
        else:
            await interaction.response.send_message(f"{interaction.user.mention} there was an issue removing you.")


async def setup(bot):
    await bot.add_cog(UserSetUp(bot))
