import discord
from discord.ext import commands
from datetime import datetime
import feedparser
import time
import os
from cogs import get_ctftime_feed, get_reddit_feed


TOKEN = os.getenv("DISCORD_TOKEN")
bot = commands.Bot(command_prefix='rakun/')


@bot.event
async def on_ready():
    print('ready')
    game = discord.Game("twitter.com/sausiber")
    await bot.change_presence(status=discord.Status.idle, activity=game)

@bot.command()
async def ping(ctx):


@bot.command()
async def feed(ctx):
    await get_ctftime_feed.get_ctftime_feed(ctx)
    await get_reddit_feed.get_reddit_feed(ctx)
    await feed(ctx)
    time.sleep(60)


if __name__ == "__main__":
    bot.run(TOKEN)
