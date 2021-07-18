from discord.ext.commands import Cog
from discord.ext import commands
from .utils import db


class Event(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.engine = db.engine

    @commands.Cog.listener()
    async def on_ready(self):
        print('Ready!')


def setup(bot):
    bot.add_cog(Event(bot))
