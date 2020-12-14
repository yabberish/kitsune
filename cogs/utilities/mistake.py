import discord
from discord.ext import commands


class mistake(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.group(hidden=True)
    async def mistake(self, ctx):
        await ctx.send('https://cdn.discordapp.com/attachments/767905805764132885/788109880845795388/unknown.png')

def setup(bot):
    bot.add_cog(mistake(bot))