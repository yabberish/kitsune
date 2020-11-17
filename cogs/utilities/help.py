import discord
from discord.ext import commands
import random

class helpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

 

    @commands.command(name='help', aliases=['Help'])
    @commands.guild_only()
    async def help(self, ctx):
     embed = discord.Embed(title="Help", description="Prefix: **k!**", color=0xffa500)
    
     embed.set_thumbnail(url="https://images.discordapp.net/avatars/768967985326456874/0c0c081f777c871826e48d7e63c64c3a.png?size=512")

     embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Command executed by {ctx.author.name}")
   

     embed.add_field(name="Moderation", value="kick, ban, mute, unmute, warn, warns", inline=False)

     embed.add_field(name="Reddit", value="meme, memes, minecraft, fortnite", inline=False)



     embed.add_field(name="Utility", value="whois, ping, serverinfo, help", inline=False)
 
     embed.add_field(name="Fun", value="tictactoe, hangman, numgame, trivia, 8ball", inline=False)
    
    
     await ctx.send(embed=embed)

    


# The setup fucntion below is neccesarry. Remember we give bot.add_cog() the name of the class in this case MembersCog.
# When we load the cog, we use the name of the file.
def setup(bot):
    bot.add_cog(helpCog(bot))