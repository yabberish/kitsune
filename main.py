import sys, traceback
import discord
from discord.ext import commands
import json




def get_prefix(bot, message):


    prefixes = ['>?', 'lol ', 'k!']


    if not message.guild:
        return '?'


    return commands.when_mentioned_or(*prefixes)(bot, message)



utilities_extensions = ['cogs.utilities.help', 'cogs.utilities.serverinfo', 'cogs.utilities.userinfo', 'cogs.utilities.ping']
moderation_extensions = []
reddit_extensions = []
fun_extensions = ['cogs.fun.eightball']
bot = commands.Bot(command_prefix=get_prefix, description='kitsune! Rewrite')

bot.remove_command("help")

if __name__ == '__main__':
    for extension in utilities_extensions:
        bot.load_extension(extension)
    for extension in moderation_extensions:
        bot.load_extension(extension)
    for extension in reddit_extensions:
        bot.load_extension(extension)
    for extension in fun_extensions:
        bot.load_extension(extension)

@bot.event
async def on_ready():
    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')



bot.run('Nzc2NTQ2ODc4ODYzMDQ4NzY1.X62dow.OhoYKyrRT3xuDTtm2GN-wD4w3yY', bot=True, reconnect=True)

