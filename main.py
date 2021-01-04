# -*- coding: utf-8 -*-

import time
import asyncpg
import json
import os

from discord.ext import commands
from datetime import datetime
from cogs.helpful import KitsuneHelpMenu


class BotCore(commands.Bot):
    def __init__(self, **kwargs):
        self.token = kwargs.pop('token')
        self.ignored_cogs = kwargs.pop('ignored_cogs')
        self.uptime = None
        self.db = None
        self.db_user = kwargs.pop('db_user')
        self.db_name = kwargs.pop('db_name')
        self.db_pass = kwargs.pop('db_pass')
        super().__init__(**kwargs)
    #
    # async def get_prefix(self, message):
    #     if message.author.id in self.owner_ids and message.channel.id == 767905805764132885:
    #         return ['', 'k!']
    #     else:
    #         return 'k!'

    def load_cogs(self):
        if __name__ == '__main__':
            for cog in os.listdir('cogs'):
                if cog.endswith('.py') and cog not in self.ignored_cogs:
                    self.load_extension(f'cogs.{cog[:-3]}')
            self.load_extension('jishaku')

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
            self.help_command = KitsuneHelpMenu()
            os.environ["JISHAKU_NO_UNDERSCORE"] = "True"
            os.environ["JISHAKU_NO_DM_TRACEBACK"] = "True"
            os.environ["JISHAKU_HIDE"] = "True"
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
    'token': token,
    'command_prefix': 'k!',
    'db_user': pg_user,
    'db_pass': pg_pass,
    'db_name': pg_name,
    'owner_ids': [701494621162963044, 738604939957239930],
    'ignored_cogs': []}

bot = BotCore(**bot_creds)


@bot.event
async def on_ready():
    print(f'Bot connected on {time.strftime("%m/%d/%Y, %H:%M:%S")}')

if __name__ == '__main__':
    bot.start_bot()
