import discord
from discord.ext import commands
import typing
import re
from datetime import datetime


class Utilities(commands.Cog, name='Utilities'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def credits(self, ctx):
        embed = discord.Embed(
            title='Credits',
            color=0xffa500,
        )
        embed.add_field(name='Elflanded#0004', value='Owner and main developer of kitsune!.', inline=False)

        embed.add_field(name='Funnylimericks#6967', value='Helped with the creation of the warning system.',
                        inline=False)

        embed.add_field(name='iWillBanU#2247', value='Worked on the kitsune! dashboard. (in progress)', inline=False)

        embed.add_field(name='Shadow Is Gone#7949', value='Kitsune! avatar artist', inline=False)

        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def embed(
            self,
            ctx: commands.Context,
            role: typing.Optional[typing.Union[discord.Role, str]] = None,
    ):

        # TODO: Enable use of reactions
        def check(msg: discord.Message):
            return ctx.author == msg.author and ctx.channel == msg.channel

        # def check_reaction(reaction: discord.Reaction, user: discord.Member):
        #     return ctx.author == user and (str(reaction.emoji == "✅") or str(reaction.emoji) == "❌")

        def title_check(msg: discord.Message):
            return (
                    ctx.author == msg.author
                    and ctx.channel == msg.channel
                    and (len(msg.content) < 256)
            )

        def description_check(msg: discord.Message):
            return (
                    ctx.author == msg.author
                    and ctx.channel == msg.channel
                    and (len(msg.content) < 2048)
            )

        def footer_check(msg: discord.Message):
            return (
                    ctx.author == msg.author
                    and ctx.channel == msg.channel
                    and (len(msg.content) < 2048)
            )

        # def author_check(msg: discord.Message):
        #     return (
        #             ctx.author == msg.author and ctx.channel == msg.channel and (len(msg.content) < 256)
        #     )

        def cancel_check(msg: discord.Message):
            if msg.content == "cancel" or msg.content == f"{ctx.prefix}cancel":
                return True
            else:
                return False

        if isinstance(role, discord.Role):
            role_mention = f"<@&{role.id}>"
            guild: discord.Guild = ctx.guild
            grole: discord.Role = guild.get_role(role.id)
            await grole.edit(mentionable=True)
        elif isinstance(role, str):
            if role == "here" or role == "@here":
                role_mention = "@here"
            elif role == "everyone" or role == "@everyone":
                role_mention = "@everyone"
        else:
            role_mention = ""

        await ctx.send("Starting an interactive process to create an embed.")

        await ctx.send(
            embed=await self.generate_embed("Do you want it to be an embed? `[y/n]`")
        )

        embed_res: discord.Message = await self.bot.wait_for("message", check=check)
        if cancel_check(embed_res) is True:
            await ctx.send("Cancelled!")
            return
        elif cancel_check(embed_res) is False and embed_res.content.lower() == "n":
            await ctx.send(
                embed=await self.generate_embed(
                    "Okay, let's do a no-embed announcement."
                    "\nWhat's the announcement?"
                )
            )
            announcement = await self.bot.wait_for("message", check=check)
            if cancel_check(announcement) is True:
                await ctx.send("Cancelled!")
                return
            else:
                await ctx.send(
                    embed=await self.generate_embed(
                        "To which channel should I send the announcement?"
                    )
                )
                channel: discord.Message = await self.bot.wait_for(
                    "message", check=check
                )
                if cancel_check(channel) is True:
                    await ctx.send("Cancelled!")
                    return
                else:
                    if channel.channel_mentions[0] is None:
                        await ctx.send("Cancelled as no channel was provided")
                        return
                    else:
                        await channel.channel_mentions[0].send(
                            f"{role_mention}\n{announcement.content}"
                        )
        elif cancel_check(embed_res) is False and embed_res.content.lower() == "y":
            embed = discord.Embed()
            await ctx.send(
                embed=await self.generate_embed(
                    "Should the embed have a title? `[y/n]`"
                )
            )
            t_res = await self.bot.wait_for("message", check=check)
            if cancel_check(t_res) is True:
                await ctx.send("Cancelled")
                return
            elif cancel_check(t_res) is False and t_res.content.lower() == "y":
                await ctx.send(
                    embed=await self.generate_embed(
                        "What should the title of the embed be?"
                        "\n**Must not exceed 256 characters**"
                    )
                )
                tit = await self.bot.wait_for("message", check=title_check)
                embed.title = tit.content
            await ctx.send(
                embed=await self.generate_embed(
                    "Should the embed have a description?`[y/n]`"
                )
            )
            d_res: discord.Message = await self.bot.wait_for("message", check=check)
            if cancel_check(d_res) is True:
                await ctx.send("Cancelled")
                return
            elif cancel_check(d_res) is False and d_res.content.lower() == "y":
                await ctx.send(
                    embed=await self.generate_embed(
                        "What do you want as the description for the embed?"
                        "\n**Must not exceed 2048 characters**"
                    )
                )
                des = await self.bot.wait_for("message", check=description_check)
                embed.description = des.content

            await ctx.send(
                embed=await self.generate_embed(
                    "Should the embed have a thumbnail?`[y/n]`"
                )
            )
            th_res: discord.Message = await self.bot.wait_for("message", check=check)
            if cancel_check(th_res) is True:
                await ctx.send("Cancelled")
                return
            elif cancel_check(th_res) is False and th_res.content.lower() == "y":
                await ctx.send(
                    embed=await self.generate_embed(
                        "What's the thumbnail of the embed? Enter a " "valid URL"
                    )
                )
                thu = await self.bot.wait_for("message", check=check)
                embed.set_thumbnail(url=thu.content)

            await ctx.send(
                embed=await self.generate_embed("Should the embed have a image?`[y/n]`")
            )
            i_res: discord.Message = await self.bot.wait_for("message", check=check)
            if cancel_check(i_res) is True:
                await ctx.send("Cancelled")
                return
            elif cancel_check(i_res) is False and i_res.content.lower() == "y":
                await ctx.send(
                    embed=await self.generate_embed(
                        "What's the image of the embed? Enter a " "valid URL"
                    )
                )
                i = await self.bot.wait_for("message", check=check)
                embed.set_image(url=i.content)

            await ctx.send(
                embed=await self.generate_embed("Will the embed have a footer?`[y/n]`")
            )
            f_res: discord.Message = await self.bot.wait_for("message", check=check)
            if cancel_check(f_res) is True:
                await ctx.send("Cancelled")
                return
            elif cancel_check(f_res) is False and f_res.content.lower() == "y":
                await ctx.send(
                    embed=await self.generate_embed(
                        "What do you want the footer of the embed to be?"
                        "\n**Must not exceed 2048 characters**"
                    )
                )
                foo = await self.bot.wait_for("message", check=footer_check)
                embed.set_footer(text=foo.content)

            await ctx.send(
                embed=await self.generate_embed(
                    "Do you want it to have a color?`[y/n]`"
                )
            )
            c_res: discord.Message = await self.bot.wait_for("message", check=check)
            if cancel_check(c_res) is True:
                await ctx.send("Cancelled!")
                return
            elif cancel_check(c_res) is False and c_res.content.lower() == "y":
                await ctx.send(
                    embed=await self.generate_embed(
                        "What color should the embed have? "
                        "Please provide a valid hex color"
                    )
                )
                colo = await self.bot.wait_for("message", check=check)
                if cancel_check(colo) is True:
                    await ctx.send("Cancelled!")
                    return
                else:
                    match = re.search(
                        r"^#(?:[0-9a-fA-F]{3}){1,2}$", colo.content
                    )  # uwu thanks stackoverflow
                    if match:
                        embed.colour = int(
                            colo.content.replace("#", "0x"), 0
                        )  # Basic Computer Science
                    else:
                        await ctx.send(
                            "Failed! Not a valid hex color, get yours from "
                            "https://www.google.com/search?q=color+picker"
                        )
                        return

            await ctx.send(
                embed=await self.generate_embed(
                    "In which channel should I send the announcement?"
                )
            )
            channel: discord.Message = await self.bot.wait_for("message", check=check)
            if cancel_check(channel) is True:
                await ctx.send("Cancelled!")
                return
            else:
                if channel.channel_mentions[0] is None:
                    await ctx.send("Cancelled as no channel was provided")
                    return
                else:
                    schan = channel.channel_mentions[0]
            await ctx.send(
                "Here is how the embed looks like: Send it? `[y/n]`", embed=embed
            )
            s_res = await self.bot.wait_for("message", check=check)
            if cancel_check(s_res) is True or s_res.content.lower() == "n":
                await ctx.send("Cancelled")
                return
            else:
                await schan.send(f"{role_mention}", embed=embed)
        if isinstance(role, discord.Role):
            guild: discord.Guild = ctx.guild
            grole: discord.Role = guild.get_role(role.id)
            if grole.mentionable is True:
                await grole.edit(mentionable=False)

    @commands.command(aliases=["native", "n", "q"])
    @commands.has_permissions(manage_messages=True)
    async def quick(
            self,
            ctx: commands.Context,
            channel: discord.TextChannel,
            role: typing.Optional[typing.Union[discord.Role, str]],
            *,
            msg: str,
    ):
        """
        An old way of making announcements
        **Usage:**
        {prefix}announcement quick #channel <OPTIONAL role> message
        """
        if isinstance(role, discord.Role):
            guild: discord.Guild = ctx.guild
            grole: discord.Role = guild.get_role(role.id)
            await grole.edit(mentionable=True)
            role_mention = f"<@&{role.id}>"
        elif isinstance(role, str):
            if role == "here" or role == "@here":
                role_mention = "@here"
            elif role == "everyone" or role == "@everyone":
                role_mention = "@everyone"
            else:
                msg = f"{role} {msg}"
                role_mention = ""

        await channel.send(f"{role_mention}\n{msg}")
        await ctx.send("Done")

        if isinstance(role, discord.Role):
            guild: discord.Guild = ctx.guild
            grole: discord.Role = guild.get_role(role.id)
            if grole.mentionable is True:
                await grole.edit(mentionable=False)

    @staticmethod
    async def generate_embed(description: str):
        embed = discord.Embed()
        embed.colour = 0xffa500
        embed.description = description

        return embed

    @commands.command(name='invite')
    async def _invite(self, ctx):
        await ctx.send(
            'Invite me to your server here!\nhttps://discord.com/api/oauth2/authorize?client_id=768967985326456874&permissions=470281318&scope=bot')

    @commands.command(name='ping')
    async def ping(self, ctx):
        await ctx.send(
            f'Pong!\nDatabase: {await self.bot.db_latency()}ms.\n\nWebsocket: {round(self.bot.latency * 1000, 2)}ms')

    @commands.command(name='sinfo', aliases=['serverinfo'])
    @commands.guild_only()
    async def serverinfo(self, ctx):
        guild = ctx.guild
        create_server = guild.created_at
        owner_server = guild.owner_id
        icon = guild.icon_url
        members = guild.member_count
        embed = discord.Embed(
            title="Server info",
            description=f'Information about the guild: **{guild.name}**',
            color=0xffa500
        )
        embed.set_thumbnail(url=f'{icon}')
        embed.set_footer(text=f'Command executed by {ctx.author.name}', icon_url=ctx.author.avatar_url)
        embed.add_field(
            name='Server creation date:',
            value=f'{create_server}',
        )
        embed.add_field(
            name='Server owner:',
            value=f'<@{owner_server}>',
        )
        embed.add_field(
            name='Members count:',
            value=f'{members}',
        )
        await ctx.send(embed=embed)

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

    @commands.command(name='uptime', help='Check the uptime of the bot.', brief='Uptime.')
    async def _uptime(self, ctx):
        delta_uptime = datetime.utcnow() - self.bot.uptime
        hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)
        await ctx.send(f"This bot has been online for {days} days, {hours} hours, {minutes} minutes and {seconds} seconds.")

    @commands.group(name='dev')
    async def _dev(self, ctx):
        pass

    @_dev.command(name='reboot')
    async def _reboot(self, ctx):
        await ctx.send('Rebooting.')
        await self.bot.close()


def setup(bot):
    bot.add_cog(Utilities(bot))
