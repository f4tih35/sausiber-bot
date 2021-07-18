from discord.ext.commands import Cog
from discord.ext import commands

from cogs.task import Task
from cogs.utils import db


class Command(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.engine = db.engine
        self.task = Task(bot=self.bot)

    @commands.command()
    async def feed_start(self,ctx):
        await ctx.send('Feeds are coming!')
        self.task.get_feed.start(ctx=ctx)

    @commands.command()
    async def feed_stop(self, ctx):
        await ctx.send('Stopped!')
        self.task.get_feed.stop()


def setup(bot):
    bot.add_cog(Command(bot))