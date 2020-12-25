# -*- coding: utf-8 -*-

from discord.ext import commands


class ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ping')
    async def ping(self, ctx):
        await ctx.send(f'Pong!\nDatabase: {await self.bot.db_latency()}ms.\n\nWebsocket: {round(self.bot.latency * 1000, 2)}ms')


def setup(bot):
    bot.add_cog(ping(bot))
