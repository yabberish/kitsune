import discord
import traceback
import sys
from discord.ext import commands
import logging

error_messages = {
    "NotOwner": "Unfortunately this command is restricted to owners only. Sorry.",
    "Forbidden": "You or the bot do not have permissions to run this command.",
    "NotFound": "Error: 404 not found, are you sure you even exist???"
}


class ErrorHandler(commands.Cog, command_attrs=dict(hidden=True)):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if hasattr(ctx.command, 'on_error'):
            return

        cog = ctx.cog
        if cog:
            if cog._get_overridden_method(cog.cog_command_error) is not None:
                return

        ignored = (commands.CommandNotFound, )

        if isinstance(error, discord.HTTPException):
            pass

        elif isinstance(error, ignored):
            return

        else:
            print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
            traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)


def setup(bot):
    bot.add_cog(ErrorHandler(bot))
