import discord
from discord.ext import commands
import asyncio
from datetime import datetime
import timeago

time_format = '%Y-%m-%d %H:%M:%S.%f'


class Moderation(commands.Cog, name='Moderation'):
    def __init__(self, bot):
        self.bot = bot

    # ban commands
    @commands.command(name='ban', help='Use this command to ban a member, they will get a dm with the reason they have been banned.',
                      brief='Ban someone.')
    @commands.has_permissions(ban_members=True)
    @commands.cooldown(1, 7, commands.BucketType.user)
    async def ban(self, ctx, member: discord.Member, reason='None given.'):
        await member.send(f'You have been banned from {ctx.guild.name}, reason: {reason}')
        await member.ban()
        await ctx.message.add_reaction("✅")
        await ctx.send(f"**{member.name}** has been banned by **{ctx.author.name}** for **{reason}**!")

    # kick
    @commands.command(name='kick', help='Use this command to kick a member, they will get a dm with the reason they have been banned.',
                      brief='Kick someone.')
    @commands.has_permissions(kick_members=True)
    @commands.cooldown(1, 7, commands.BucketType.user)
    async def kick(self, ctx, member: discord.Member, reason='None given.'):
        await member.send(f'You have been banned from {ctx.guild.name}, reason: {reason}')
        await member.kick()
        await ctx.message.add_reaction("✅")
        await ctx.send(f"{member.name} has been kicked by **{ctx.author.name}** for **{reason}**!")

    # mute command
    @commands.command(name='mute')
    @commands.has_permissions(manage_messages=True)
    async def mute(self, ctx, member: discord.Member, reason=None):
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        await member.add_roles(role)
        await ctx.send(f'**Muted** {member.mention}\n**Reason: **{reason}')
        embed = discord.Embed(color=discord.Color.green())
        embed.add_field(name=f"You've been **Muted** in {ctx.guild.name}.",
                        value=f"**Action By: **{ctx.author.mention}\n**Reason: **{reason}\n**Duration: ∞**")
        await member.send(embed=embed)

    # purge commands TODO: Add flags instead of subcommands.
    @commands.group(name='purge', invoke_without_command=True)
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, limit: int):
        await ctx.channel.purge(limit=limit)

    @purge.command(name='user')
    @commands.bot_has_permissions(manage_messages=True)
    @commands.has_permissions(manage_messages=True)
    async def user(self, ctx, user: discord.Member, limit=10):
        def is_user(m):
            return m.author == user

        await ctx.channel.purge(limit=limit, check=is_user)

    @purge.command(name='keyword')
    @commands.bot_has_permissions(manage_messages=True)
    @commands.has_permissions(manage_messages=True)
    async def keyword(self, ctx, keyword: str, limit=10):
        def has_keyword(m):
            return keyword in m.content

        await ctx.channel.purge(limit=limit, check=has_keyword)

    # slow mode
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def slowmode(self, ctx, seconds: int):
        await ctx.channel.edit(slowmode_delay=seconds)
        await ctx.send(f"I've set the slowmode to **{seconds}** seconds in {ctx.channel.mention}!")

    # tempmute FIXME
    @commands.command(aliases=["tmute"])
    @commands.has_permissions(manage_messages=True)
    async def tempmute(self, ctx, member: discord.Member, mute_time: int, *, reason=None):
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        await member.add_roles(role)
        ctx.send(f'**Muted** {member.mention}\n**Reason: **{reason}\n**Duration:** {mute_time}')

        embed = discord.Embed(color=discord.Color.green())
        embed.add_field(name=f"You've been **Muted** in {ctx.guild.name}.",
                        value=f"**Action By: **{ctx.author.mention}\n**Reason: **{reason}\n**Duration:** {mute_time}")
        await member.send(embed=embed)

        await asyncio.sleep(mute_time)
        await member.remove_roles(role)
        await ctx.send(f"**Unmuted {member.mention} for: `Timeout ended`**")

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def unmute(self, ctx, member: discord.Member):
        role = discord.utils.get(ctx.guild.roles, name="Muted")

        embed = discord.Embed(color=discord.Color.green())
        embed.add_field(name=f"You've been **Unmuted** in {ctx.guild.name}.",
                        value=f"**Action By: **{ctx.author.mention}")
        await member.send(embed=embed)

        await member.remove_roles(role)

    # warn commands.
    @commands.command()
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

    @commands.command(aliases=['warns', 'infracts'])
    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    async def infractions(self, ctx, member: discord.Member):
        infracts = await self.bot.db.fetch("SELECT reason FROM warns WHERE $1 = user_id AND $2 = guild_id",
                                           member.id, member.guild.id, )

        warned_at = await self.bot.db.fetch(f"SELECT warned_at FROM warns WHERE $1 = user_id AND $2 = guild_id",
                                            member.id, member.guild.id, )

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
    bot.add_cog(Moderation(bot))