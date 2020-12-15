from discord.ext import commands
import discord
import asyncio

class tmuteCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["tmute"])
    @commands.has_permissions(manage_messages=True)
    async def tempmute(self, ctx, member: discord.Member, mute_time : int, *, reason=None):
      role = discord.utils.get(ctx.guild.roles, name="Muted")
      await member.add_roles(role)
      ctx.send(f'**Muted** {member.mention}\n**Reason: **{reason}\n**Duration:** {mute_time}')

      embed = discord.Embed(color=discord.Color.green())
      embed.add_field(name=f"You've been **Muted** in {ctx.guild.name}.", value=f"**Action By: **{ctx.author.mention}\n**Reason: **{reason}\n**Duration:** {mute_time}")
      await member.send(embed=embed)

      await asyncio.sleep(mute_time)
      await member.remove_roles(role)
      await ctx.send(f"**Unmuted {member.mention} for: `Timeout ended`**")


def setup(bot):
    bot.add_cog(tmuteCog(bot))
