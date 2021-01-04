# -*- coding: utf-8 -*-

import discord
from discord.ext import commands


class whoisCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

 

    @commands.command(name='userinfo', aliases=['whois'])
    async def userinfo(self, ctx, member: discord.Member = None):
      if not member:  # if member is no mentioned
          member = ctx.message.author  # set member as the author
      roles = [role for role in member.roles]
      embed = discord.Embed(colour=0xffa500, timestamp=ctx.message.created_at,
                          title=f"User Info - {member}")
      embed.set_thumbnail(url=member.avatar_url)
      embed.set_footer(text=f"Command sent by {ctx.author}")

      embed.add_field(name="ID:", value=member.id)
      embed.add_field(name="Display Name:", value=member.display_name)

      embed.add_field(name="Created Account On:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
      embed.add_field(name="Joined Server On:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))

      embed.add_field(name="Roles:", value="".join([role.mention for role in roles]))
      embed.add_field(name="Highest Role:", value=member.top_role.mention)
  
      await ctx.send(embed=embed)

    



def setup(bot):
    bot.add_cog(whoisCog(bot))