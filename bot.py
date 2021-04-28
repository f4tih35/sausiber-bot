from discord.ext import commands
from datetime import datetime
import feedparser
import time
import os


TOKEN = os.getenv("DISCORD_TOKEN")
bot = commands.Bot(command_prefix='rakun/')

@bot.command()
async def feed(ctx):
    await get_ctftime_feed(ctx)
    await get_reddit_feed(ctx)
    time.sleep(60)
    await feed(ctx)


last_ctftime_entry = ""
last_reddit_trsec_entry = ""
last_reddit_netsec_entry = ""

async def get_ctftime_feed(ctx):
    global last_ctftime_entry

    NewsFeed = feedparser.parse("https://ctftime.org/event/list/upcoming/rss/")

    if last_ctftime_entry == NewsFeed.entries[0]:
        print("x")
    else:
        entry = NewsFeed.entries[0]

        print("Title = " + entry.title)
        await ctx.send("Title = " + entry.title)
        start_date = datetime.strptime(entry.start_date, "%Y%m%dT%H%M%S")
        finish_date = datetime.strptime(entry.finish_date, "%Y%m%dT%H%M%S")

        print("Start date = " + start_date.strftime("%d/%m/%Y %H:%M"))
        print("Finish date = " + finish_date.strftime("%d/%m/%Y %H:%M"))
        print("Link = " + entry.link)
        print("Logo = " + "https://ctftime.org/" + entry.logo_url)

        last_ctftime_entry = NewsFeed.entries[0]

async def get_reddit_feed(ctx):
    async def get_trsec():
        global last_reddit_trsec_entry

        NewsFeed = feedparser.parse("https://www.reddit.com/r/trsec/new/.rss")

        if last_reddit_trsec_entry == NewsFeed.entries[0]:
            print("x")
        else:
            entry = NewsFeed.entries[0]

            await ctx.send("Title = " + entry.title)

            last_reddit_trsec_entry = NewsFeed.entries[0]

    async def get_netsec():
        global last_reddit_netsec_entry

        NewsFeed = feedparser.parse("https://www.reddit.com/r/netsec/new/.rss")

        if last_reddit_netsec_entry == NewsFeed.entries[0]:
            print("x")
        else:
            entry = NewsFeed.entries[0]

            await ctx.send("Title = " + entry.title)

            last_reddit_netsec_entry = NewsFeed.entries[0]

    await get_trsec()
    await get_netsec()






if __name__ == "__main__":
    bot.run(TOKEN)


