import discord
from discord.ext import commands


class NewContext(commands.Context):
    async def log(self, message, **kwargs):
        # elf do something here, make a logging command that logs bans and stuff. You can use this script by typing ctx.log(stuff)
        # if u need help with custom context here: https://discordpy.readthedocs.io/en/latest/migrating.html#subclassing-context
        await self.send(message, **kwargs)
        pass