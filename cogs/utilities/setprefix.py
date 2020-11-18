import discord
from discord.ext import commands
import random
import json

class prefixCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot




    

    async def determine_prefix(bot, message):
     guild = message.guild
     if guild:
        return custom_prefixes.get(guild.id, default_prefixes)
     else:
        return default_prefixes



    @commands.command()
    @commands.guild_only()
    async def cprefix(self, ctx, *, prefixes=""): 
      custom_prefixes = {}
      default_prefixes = ['k!']
      custom_prefixes[ctx.guild.id] = prefixes.split() or default_prefixes
      await ctx.send("Prefixes set!") 
      



def setup(bot):
   bot.add_cog(prefixCog(bot))