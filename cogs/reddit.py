import discord
import random
import aiohttp
from discord.ext import commands


class Reddit(commands.Cog, name='Reddit'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def aww(self, ctx):
        embed = discord.Embed(title="r/aww", description=None, color=0xffa500)

        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://www.reddit.com/r/aww/new.json?sort=hot') as r:
                res = await r.json()
                embed.set_image(url=res['data']['children'][random.randint(0, 250)]['data']['url'])
                await ctx.send(embed=embed, content=None)

    @commands.command()
    async def meme(self, ctx):
        embed = discord.Embed(title="r/dankmemes", description=None, color=0xffa500)

        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
                res = await r.json()
                embed.set_image(url=res['data']['children'][random.randint(0, 250)]['data']['url'])
                await ctx.send(embed=embed, content=None)


def setup(bot):
    bot.add_cog(Reddit(bot))