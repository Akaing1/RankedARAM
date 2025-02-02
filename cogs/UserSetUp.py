from discord.ext import commands
from data.database.dbOperations import DBOperations

db = DBOperations()


class UserSetUp(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Users ready to be set up!")

    @commands.command()
    async def register(self, ctx):
        if db.registerUser(ctx, 'Zaphkiel#stf'):
            await ctx.send(f"{ctx.author.mention} has been registered successfully!")
        else:
            await ctx.send(f"{ctx.author.mention} there was an issue registering you.")

    @commands.command()
    async def remove(self, ctx):
        if db.removeUser(ctx):
            await ctx.send(f"{ctx.author.mention} has been deleted successfully!")
        else:
            await ctx.send(f"{ctx.author.mention} there was an issue removing you.")


async def setup(bot):
    await bot.add_cog(UserSetUp(bot))
