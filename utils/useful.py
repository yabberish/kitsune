import discord
from discord.ext import commands
import datetime


# base embed
class BaseEmbed(discord.Embed):
    def __init__(self, color=0xffa500, timestamp=None, **kwargs):
        super().__init__(color=color, timestamp=timestamp or datetime.datetime.utcnow(), **kwargs)

    @classmethod
    def default(cls, ctx, **kwargs):
        instance = cls(**kwargs)
        instance.set_footer(text=f"Executed by {ctx.author}", icon_url=ctx.author.avatar_url)
        return instance