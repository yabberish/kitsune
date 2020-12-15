import discord
from discord.ext import commands


class purge(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.group(name='purge')
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx):
        pass
        
    async def is_user(self, m):
        return m.author == user
    
    @purge.command(name='channel')
    @commands.bot_has_permissions(manage_messages=True)
    @commands.has_permissions(manage_messages=True)
    async def channel(self, ctx, limit=10):
        await ctx.channel.purge(limit=limit)

    @purge.command(name='user')
    @commands.bot_has_permissions(manage_messages=True)
    @commands.has_permissions(manage_messages=True)
    async def user(self, ctx, user : discord.Member, limit=10):
        def is_user(m):
            return m.author == user
        await ctx.channel.purge(limit=limit, check=is_user)
        
    @purge.command(name='keyword')
    @commands.bot_has_permissions(manage_messages=True)
    @commands.has_permissions(manage_messages=True)
    async def keyword(self, ctx, keyword : str, limit=10):
        def has_keyword(m):
            return keyword in m.content
        await ctx.channel.purge(limit=limit, check=has_keyword)

def setup(bot):
    bot.add_cog(purge(bot))