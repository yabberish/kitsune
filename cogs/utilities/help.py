import discord
from discord.ext import commands
import random
from time import time
class helpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

 

    @commands.command(name='help', aliases=['Help'])
    @commands.guild_only()
    async def help(self, ctx):
        embed = discord.Embed(title="Help", description="Prefix: **k!**", color=0xffa500)
    
        embed.set_thumbnail(url="https://images.discordapp.net/avatars/768967985326456874/0c0c081f777c871826e48d7e63c64c3a.png?size=512")

        embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Command executed by {ctx.author.name}")
   

        embed.add_field(name="Moderation", value="`kick`, `ban`, `mute`, `unmute`, `warn`, `warns`, `slowmode`", inline=False)

        embed.add_field(name="Reddit", value="`meme`, `gaming`, `aww`", inline=False)



        embed.add_field(name="Utility", value="`whois`, `embed`, `serverinfo`, `help`, `credits`", inline=False)
 
        embed.add_field(name="Fun", value="`8ball`", inline=False)
     
        embed.add_field(name="Economoy", value="`balance`, `rob`, `beg`, `deposit`, `withdraw`", inline=False)
        
        await ctx.send(embed=embed)

    @commands.command(name="ping")
    async def ping(self, ctx):
        start = time()
        message = await ctx.send(f"Pong! Latency: {self.bot.latency*1000:,.0f} ms.")
        end = time()

        await message.edit(content=f"Pong! Latency: {self.bot.latency*1000:,.0f} ms. Response time: {(end-start)*1000:,.0f} ms.")
    


def setup(bot):
    bot.add_cog(helpCog(bot))