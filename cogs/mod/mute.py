# -*- coding: utf-8 -*-

from discord.ext import commands
import discord


class muteCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def mute(self, ctx, member: discord.Member, reason=None):
      role = discord.utils.get(ctx.guild.roles, name="Muted")
      await member.add_roles(role)
      await ctx.send(f'**Muted** {member.mention}\n**Reason: **{reason}')

      embed = discord.Embed(color=discord.Color.green())
      embed.add_field(name=f"You've been **Muted** in {ctx.guild.name}.", value=f"**Action By: **{ctx.author.mention}\n**Reason: **{reason}\n**Duration: ∞**")
      await member.send(embed=embed)


def setup(bot):
    bot.add_cog(muteCog(bot))
    # Adds the Basic commands to the bot
