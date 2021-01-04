# -*- coding: utf-8 -*-

from discord.ext import commands
import discord


class banCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(ban_members=True)
    @commands.cooldown(1, 7, commands.BucketType.user)
    async def ban(self, ctx, member : discord.Member):

     await member.ban()
     await ctx.message.add_reaction("✅")
     await ctx.send(f"**{member.name}** has been banned by **{ctx.author.name}**!")


def setup(bot):
    bot.add_cog(banCog(bot))
    # Adds the Basic commands to the bot

