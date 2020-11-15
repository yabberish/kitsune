import discord
from discord.ext import commands
import random

class eightballCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

 

    @commands.command(name='userinfo', aliases=['whois'])
    @commands.guild_only()
    async def userinfo(self, ctx):
     rpsa = ["As I see it, yes.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.", "It is certain.", "It is decidedly so."]
     rpsr = random.choice(rpsa)
     await ctx.send(rpsr)

    


# The setup fucntion below is neccesarry. Remember we give bot.add_cog() the name of the class in this case MembersCog.
# When we load the cog, we use the name of the file.
def setup(bot):
    bot.add_cog(eightballCog(bot))
