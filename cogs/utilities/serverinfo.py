# -*- coding: utf-8 -*-

import discord
from discord.ext import commands


class serverinfoCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

 

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
     embed.set_footer(text=f'Command executed by {ctx.author.name}', icon_url = ctx.author.avatar_url)
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

    


# The setup fucntion below is neccesarry. Remember we give bot.add_cog() the name of the class in this case MembersCog.
# When we load the cog, we use the name of the file.
def setup(bot):
    bot.add_cog(serverinfoCog(bot))
