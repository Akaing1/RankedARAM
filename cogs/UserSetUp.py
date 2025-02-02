import discord
from discord import app_commands
from discord.ext import commands
from data.database.dbOperations import DBOperations
from data.riotData.RiotData import RiotData

db = DBOperations()
riotData = RiotData()


class UserSetUp(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Users ready to be set up!")

    @app_commands.command(name="register", description="register user")
    @app_commands.describe(riotid="Enter RiotID here: ex. JohnDoe#NA1")
    async def register(self, interaction: discord.Interaction, riotid: str):
        if riotData.checkRiotIDisValid(riotid):
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
