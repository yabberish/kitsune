from discord.ext import commands


def is_voter():
    async def predicate(ctx):
        # elf add an is_voter check using the python dbl module. (https://pypi.org/project/dblpy/)
        pass # return true or false
    return commands.check(predicate)