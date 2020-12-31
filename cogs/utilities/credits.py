# -*- coding: utf-8 -*-

import discord
from discord.ext import commands


class Cog(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.command()
    async def credits(self, ctx):
        embed=discord.Embed(
            title='Credits',
            color=0xffa500,
        )
        embed.add_field(name='Elflanded#0004', value='Owner and main developer of kitsune!.', inline=False)

        embed.add_field(name='Funnylimericks#6967', value='Helped with the creation of the warning system.', inline=False)
        
        embed.add_field(name='iWillBanU#2247', value='Worked on the kitsune! dashboard. (in progress)', inline=False)

        embed.add_field(name='Shadow Is Gone#7949', value='Kitsune! avatar artist', inline=False)
        
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Cog(bot))