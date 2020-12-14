import discord
from discord.ext import commands
import sqlite3

conn = sqlite3.connect('./database/database.db')
c = conn.cursor()

def checkExists(user_id, guild_id):
    c.execute('SELECT bank FROM economy WHERE ? LIKE user_id AND ? LIKE guild_id', (user_id, guild_id,))
    bank = c.fetchone()
    c.execute('SELECT purse FROM economy WHERE ? LIKE user_id AND ? LIKE guild_id', (user_id, guild_id,))
    purse = c.fetchone()
    if bank == None or purse == None:
        return True


class economy(commands.Cog):
    def __init__(self, bot):
        self.bot=bot
    
    @commands.group()
    @commands.guild_only()
    async def bal2(self, ctx):
        user = ctx.author
        if checkExists(user.id, user.guild.id):
            c.execute('DELETE FROM economy WHERE ? LIKE user_id AND ? LIKE guild_id', (user.id, user.guild.id,))
            c.execute('INSERT INTO economy (user_id, guild_id) VALUES (?, ?)', (user.id, user.guild.id))
            conn.commit()
        else:
            print('test')
            c.execute('SELECT bank FROM economy WHERE ? LIKE user_id AND ? LIKE guild_id', (user.id, user.guild.id,))
            bank = c.fetchone()
            c.execute('SELECT purse FROM economy WHERE ? LIKE user_id AND ? LIKE guild_id', (user.id, user.guild.id,))
            purse = c.fetchone()
            embed = discord.Embed(title=f"{ctx.author.name}'s Balance",description=f"**Wallet:** {str(purse[0])}\n**Bank:** {str(bank[0])}\n**Total:** {str(purse[0] + bank[0])}", color=0xffa500)
            await ctx.send(embed=embed)
    
    @commands.group()
    @commands.guild_only()
    async def beg2(self, ctx):
        user = ctx.author



def setup(bot):
    bot.add_cog(economy(bot))