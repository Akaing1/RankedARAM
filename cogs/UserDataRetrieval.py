import discord
from discord.ext import commands

from commands.getPoints import *
from data.dbOperations import *

db = DBOperations()


class UserDataRetrieval(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Data ready to be retrieved!")

    @commands.command()
    async def getData(self, ctx):
        await ctx.send(db.getUserData(ctx))

    @commands.command()
    async def LP(self, ctx):
        await ctx.send(getLPFromUser(ctx, db))


async def setup(bot):
    await bot.add_cog(UserDataRetrieval(bot))
