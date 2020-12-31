# -*- coding: utf-8 -*-

import time
import asyncpg
import json

from discord.ext import commands
from datetime import datetime

utilities_extensions = [
    'cogs.utilities.serverinfo',
    'cogs.utilities.userinfo', 'cogs.utilities.help', 'cogs.utilities.embeds',
    'cogs.error.errorHandler', 'cogs.utilities.credits',
    'cogs.utilities.owner', 'cogs.utilities.ping'
]
moderation_extensions = ['cogs.mod.kick', 'cogs.mod.ban', 'cogs.mod.tempmute', 'cogs.mod.mute', 'cogs.mod.unmute',
                         'cogs.mod.slowmode', 'cogs.mod.warn', 'cogs.mod.purge']
reddit_extensions = ['cogs.reddit.meme', 'cogs.reddit.aww', 'cogs.reddit.gaming']
fun_extensions = ['cogs.fun.eightball']


class BotCore(commands.Bot):
    def __init__(self, **kwargs):
        self.token = kwargs.pop('token')
        self.uptime = None
        self.db = None
        self.db_user = kwargs.pop('db_user')
        self.db_name = kwargs.pop('db_name')
        self.db_pass = kwargs.pop('db_pass')
        super().__init__(**kwargs)

    def load_cogs(self):
        if __name__ == '__main__':
            # self.remove_command("help")
            for extension in utilities_extensions:
                self.load_extension(extension)
            for extension in moderation_extensions:
                self.load_extension(extension)
            for extension in reddit_extensions:
                self.load_extension(extension)
            for extension in fun_extensions:
                self.load_extension(extension)

    def start_bot(self):
        try:
            print('Connecting to database...')
            start = time.time()
            db = self.loop.run_until_complete(
                asyncpg.create_pool(database=self.db_name, user=self.db_user, password=self.db_pass))
            print(f'Connected to database. ({round(time.time() - start, 2)})s')
            self.db = db
        except Exception as e:
            print('Could not connect to database.')
            print(e)
        else:
            self.uptime = datetime.now()
            self.load_cogs()
            self.run(self.token)

    async def db_latency(self):
        start = time.time()
        await self.db.execute('SELECT 1;')
        return round((time.time() - start) * 1000, 2)


with open('secrets.json', 'r') as tf:
    tf = json.load(tf)
    token = tf['token']
    pg_user = tf['db_user']
    pg_pass = tf['db_pass']
    pg_name = tf['db_name']

bot_creds = {
    "token": token,
    'command_prefix': '~',
    'db_user': pg_user,
    'db_pass': pg_pass,
    'db_name': pg_name}

bot = BotCore(**bot_creds)


@bot.event
async def on_ready():
    print(f'Bot connected on {time.strftime("%m/%d/%Y, %H:%M:%S")}')

if __name__ == '__main__':
    bot.start_bot()