import discord
from discord.ext import commands
from datetime import datetime
import feedparser
import time
import os
from cogs import embed_message

last_ctftime_entry = ""


async def get_ctftime_feed(ctx):
    global last_ctftime_entry
    news_feed = feedparser.parse("https://ctftime.org/event/list/upcoming/rss/")
    if last_ctftime_entry == news_feed.entries[0]:
        print("x")
    else:
        entry = news_feed.entries[0]
        thumbnail_url = "https://ctftime.org/" + entry.logo_url
        start_date = datetime.strptime(entry.start_date, "%Y%m%dT%H%M%S")
        finish_date = datetime.strptime(entry.finish_date, "%Y%m%dT%H%M%S")
        field_1 = embed_message.Field("Start", start_date.strftime("%d/%m/%Y %H:%M"), True)
        field_2 = embed_message.Field("Finish", finish_date.strftime("%d/%m/%Y %H:%M"), True)
        if datetime.now() > start_date and datetime.now() < finish_date:
            field_3 = embed_message.Field("Status", "Active", True)
        else:
            field_3 = embed_message.Field("Status", "Incoming", True)

        embed = embed_message.get(entry, "CTFtime.org", "https://ctftime.org/event/list/upcoming/", thumbnail_url, "", field_1, field_2, field_3)
        await ctx.send(embed=embed)

        last_ctftime_entry = news_feed.entries[0]
