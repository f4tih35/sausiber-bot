from discord.ext import tasks
from cogs.utils.feed import FeedUtils
from discord.ext.commands import Cog
from cogs.utils import db


class Task(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.engine = db.engine

    @tasks.loop(seconds=2.0)
    async def get_feed(self, ctx):
        await FeedUtils.get_reddit(ctx=ctx)


def setup(bot):
    bot.add_cog(Task(bot))
