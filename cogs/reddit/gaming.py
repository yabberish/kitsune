# -*- coding: utf-8 -*-

from discord.ext import commands
import discord
import random
import aiohttp

class gamingCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def gaming(self, ctx):
     embed = discord.Embed(title="r/Gaming", description=None, color=0xffa500)

     async with aiohttp.ClientSession() as cs:
         async with cs.get('https://www.reddit.com/r/gaming/new.json?sort=hot') as r:
             res = await r.json()
             embed.set_image(url=res['data']['children'] [random.randint(0, 250)] ['data']['url'])
             await ctx.send(embed=embed, content=None)
           

def setup(bot):
    bot.add_cog(gamingCog(bot))