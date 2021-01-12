from discord.ext import commands
import dblpy
from utils.errors import NotVoterError



class TopGG():

  def __init__(self, bot)
    self.bot = bot
    self.token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6Ijc2ODk2Nzk4NTMyNjQ1Njg3NCIsImJvdCI6dHJ1ZSwiaWF0IjoxNjEwNDczNDUyfQ.Ro-kwtzfbcPcbBSpijtvBe1kKkB9mBj2xSUts670JtE'
    self.dblpy = dbl.DBLClient(self.bot, self.token)


  
  def is_voter():
     async def predicate(ctx):
      if dblpy.get_user_vote(ctx.author.id):
        return True
      else:
        raise NoVoterError
       

    return commands.check(predicate)

