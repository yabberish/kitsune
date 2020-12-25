# -*- coding: utf-8 -*-

from discord.ext import commands
import random


class eightballCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='8ball', aliases=['eightball'])
    @commands.guild_only()
    async def eight_ball(self, ctx):
     rpsa = ["As I see it, yes.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.", "It is certain.", "It is decidedly so."]
     rpsr = random.choice(rpsa)
     await ctx.send(rpsr)

    

def setup(bot):
    bot.add_cog(eightballCog(bot))
