import feedparser
from cogs import embed_message


last_reddit_trsec_entry = ""
last_reddit_netsec_entry = ""


async def get_reddit_feed(ctx):

    async def get_trsec():
        global last_reddit_trsec_entry
        NewsFeed = feedparser.parse("https://www.reddit.com/r/trsec/new/.rss")
        if last_reddit_trsec_entry == NewsFeed.entries[0]:
            print("x")
        else:
            entry = NewsFeed.entries[0]
            thumbnail_url = "https://styles.redditmedia.com/t5_271aqi/styles/communityIcon_cprzumhc73u31.png?width=256&s=6795720fb86620dda4cc0d8a56f01d4af4f2a233"
            embed = embed_message.get(entry, "/r/trsec", "https://www.reddit.com/r/trsec/new/", thumbnail_url)
            await ctx.send(embed=embed)
            last_reddit_trsec_entry = NewsFeed.entries[0]

    async def get_netsec():
        global last_reddit_netsec_entry
        NewsFeed = feedparser.parse("https://www.reddit.com/r/netsec/new/.rss")
        if last_reddit_netsec_entry == NewsFeed.entries[0]:
            print("x")
        else:
            entry = NewsFeed.entries[0]
            thumbnail_url = "https://thenudesguy.com/wp-content/uploads/2020/08/logo-1.png"
            embed = embed_message.get(entry, "/r/netsec", "https://www.reddit.com/r/netsec/new/", thumbnail_url)
            await ctx.send(embed=embed)
            last_reddit_netsec_entry = NewsFeed.entries[0]

    await get_trsec()
    await get_netsec()
