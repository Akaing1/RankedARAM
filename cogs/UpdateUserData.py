from discord import app_commands
from discord.ext import commands

from data.LPManagement.LPManagement import *
from data.database.dbOperations import *

db = DBOperations()


class UpdateUserData(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Data ready to be updated!")

    @app_commands.command(name="update_lp", description="updates user current LP status")
    async def updateLPStatus(self, interaction):
        # TO DO: call riot api to get match history here <------
        if updateLPinDB(interaction, db, -4):
            await interaction.response.send_message(f"{interaction.user.mention}'s lp has been updated!")
        else:
            await interaction.response.send_message(f"{interaction.user.mention}'s lp had a problem while updating.")


async def setup(bot):
    await bot.add_cog(UpdateUserData(bot))
