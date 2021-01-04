# -*- coding: utf-8 -*-

import discord
from discord.ext import commands
from datetime import datetime
import timeago

time_format = '%Y-%m-%d %H:%M:%S.%f'


class Cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group()
    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    async def warn(self, ctx, member: discord.Member, *, reason="None given."):
        invoker = ctx.author
        if member.id != ctx.author.id:
            if invoker.top_role > member.top_role:
                await self.bot.db.execute("INSERT INTO warns (user_id, guild_id, reason) VALUES ($1, $2, $3)",
                                          member.id, member.guild.id, reason)
                embed = discord.Embed(
                    description=f"You have been warned in {member.guild.name}. Reason: {reason}",
                    color=0xffa500
                )
                embed.set_author(name=f"Uh oh! {ctx.author.name} has warned you!", icon_url=str(ctx.author.avatar_url))
                await member.send(embed=embed)
                embed = discord.Embed(
                    color=0xffa500

                )
                embed.set_author(name=f"{member.name} has been warned by {ctx.author.name} for `{reason}",
                                 icon_url=str(member.avatar_url))
                await ctx.send(embed=embed)
            else:
                await ctx.send(f"You can't **{ctx.invoked_with}** someone with a higher role than you!")
        else:
            embed = discord.Embed(
                color=0xffa500,
            )
            embed.set_author(name="You can't warn yourself!")
            await ctx.send(embed=embed)

    @commands.group(aliases=['warns', 'infracts'])
    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    async def infractions(self, ctx, member: discord.Member):
        infracts = await self.bot.db.fetch("SELECT reason FROM warns WHERE $1 = user_id AND $2 = guild_id",
                                  member.id, member.guild.id,)

        warned_at = await self.bot.db.fetch(f"SELECT warned_at FROM warns WHERE $1 = user_id AND $2 = guild_id",
                                  member.id, member.guild.id,)

        descembed = f"Total infractions: {len(infracts)}"

        for infract, current_warn_inlist in zip(infracts, warned_at):
            current_warn = infract['reason']
            time_of_warn = current_warn_inlist['warned_at']
            descembed += f"\n**`{str(current_warn)}`** • {timeago.format(time_of_warn, datetime.now())}"
        if infracts != ():
            embed = discord.Embed(
                color=0xffa500,
                description=descembed
            )
            embed.set_author(name=f"{member.name}'s infractions:", icon_url=str(member.avatar_url))
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                color=0xffa500,
            )

            embed.set_author(name=f"{member.name} has no {ctx.invoked_with}!", icon_url=str(member.avatar_url))
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Cog(bot))
