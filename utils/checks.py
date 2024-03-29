from discord.ext import commands
import dbl
from utils.errors import NotVoterError
import aiohttp


def is_voter():
    async def predicate(ctx):
        top_gg = dbl.DBLClient(bot=ctx.bot, token='', session=aiohttp.ClientSession())
        print(await top_gg.get_user_vote(ctx.author.id))
        if await top_gg.get_user_vote(user_id=ctx.author.id):
            return True
        else:
            raise NotVoterError
    return commands.check(predicate)
