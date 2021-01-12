import dblpy
import discord
from discord.ext import commands

class NotVoterError(commands.CheckFailure):
  pass

def is_voter():
  async def predicate(ctx):
    topgg = dbl.DBLClient(bot=ctx.bot)
    if topgg.get_user_vote(ctx.author.id):
      return True
    else:
      raise NotVoterError
  return commands.check(predicate)