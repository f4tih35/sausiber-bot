import discord


class Field:
    def __init__(self, title, value, inline=False):
        self.title = title
        self.value = value
        self.inline = inline


def get(entry, feed_name, feed_url, thumbnail_url=None, description="", field_1=None, field_2=None, field_3=None, footer=None):

    embed = discord.Embed(title=entry.title, url=entry.link,
                          description=description,
                          color=0x0905fa)

    embed.set_author(name=feed_name, url=feed_url, icon_url="https://media.kommunity.com/communities/sausiber/20976/sausiber.png")

    embed.set_thumbnail(url=thumbnail_url)
    if field_1:
        embed.add_field(name=field_1.title, value=field_1.value, inline=field_1.inline)
    if field_2:
        embed.add_field(name=field_2.title, value=field_2.value, inline=field_2.inline)
    if field_3:
        embed.add_field(name=field_3.title, value=field_3.value, inline=field_3.inline)
    if footer:
        embed.set_footer(text=footer)
    return embed
