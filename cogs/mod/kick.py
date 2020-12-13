from discord.ext import commands
import discord

def get_prefix(client, message):
    with open('./json/prefixes.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]


bot = commands.Bot(command_prefix=get_prefix, case_insensitive=True)


class kickCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    @commands.cooldown(1, 7, commands.BucketType.user)
    async def kick(self, ctx, member : discord.Member):

     await member.kick()
     await ctx.message.add_reaction("✅")

     await ctx.send(f"{member.name} has been kicked by {ctx.author.name}!")

def setup(bot):
    bot.add_cog(kickCog(bot))
    # Adds the Basic commands to the bot

