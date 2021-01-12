from discord.ext import commands


class NotVoterError(commands.CheckFailure):
    """Gets raised when someone hasnt voted for kitsune on https://top.gg"""
    pass
