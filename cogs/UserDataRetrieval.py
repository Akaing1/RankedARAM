from discord import app_commands
from discord.ext import commands

from data.getPoints import *
from data.database.dbOperations import *

db = DBOperations()


class UserDataRetrieval(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Data ready to be retrieved!")

    @app_commands.command(name="get_data", description="gets user data from db")
    async def getData(self, interaction):
        await interaction.response.send_message(db.getUserData(interaction))

    @app_commands.command(name="lp", description="gets user current LP status")
    async def LP(self, interaction):
        await interaction.response.send_message(getLPFromUser(interaction, db))


async def setup(bot):
    await bot.add_cog(UserDataRetrieval(bot))
