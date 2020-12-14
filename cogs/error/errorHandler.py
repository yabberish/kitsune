import discord
from discord.ext import commands


class ErrorHandler(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            embed = discord.Embed(
                color = 0xffa500,
                description=str(error),
            )
            embed.set_author(name='You are on cooldown!')
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                color = 0xffa500,
                description=str(error),
            )
            embed.set_author(name='You are missing permissions!')
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color = 0xffa500,
                description=str(error),
            )
            embed.set_author(name='You are missing a required argument!')
            await ctx.send(embed=embed)
        elif isinstance(error, commands.CommandNotFound):
            await ctx.message.add_reaction(":kitsunethink:786984788095533069>")
            
        elif isinstance(error, commands.DisabledCommand):
            embed = discord.Embed(
                color = 0xffa500,
                description=str(error),
            )
            embed.set_author(name='Command is disabled!')
            await ctx.send(embed=embed)
        elif isinstance(error, commands.BotMissingPermissions):
            embed= discord.Embed(
                color = 0xffa500,
                desciption=str(error)
            )
            embed.set_author(name='Bot missing permissions!')
            await ctx.send(embed=embed)
        elif isinstance(error, commands.BotMissingRole):
            embed= discord.Embed(
                color = 0xffa500,
                desciption=str(error)
            )
            embed.set_author(name='Bot missing roles!')
            await ctx.send(embed=embed)
        elif isinstance(error, commands.UserNotFound):
            embed= discord.Embed(
                color = 0xffa500,
                desciption=str(error)
            )
            embed.set_author(name='User Not found!')
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MemberNotFound):
            embed= discord.Embed(
                color = 0xffa500,
                desciption=str(error)
            )
            embed.set_author(name='Member Not found!')
            await ctx.send(embed=embed)
        elif isinstance(error, commands.ChannelNotFound):
            embed= discord.Embed(
                color = 0xffa500,
                desciption=str(error)
            )
            embed.set_author(name='Channel Not found!')
            await ctx.send(embed=embed)
        elif isinstance(error, commands.RoleNotFound):
            embed= discord.Embed(
                color = 0xffa500,
                desciption=str(error)
            )
            embed.set_author(name='Role Not found!')
            await ctx.send(embed=embed)
def setup(bot):
    bot.add_cog(ErrorHandler(bot))