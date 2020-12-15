"""
____  __.__  __                              
|    |/ _|__|/  |_  ________ __  ____   ____  
|      < |  \   __\/  ___/  |  \/    \_/ __ \ 
|    |  \|  ||  |  \___ \|  |  /   |  \  ___/ 
|____|__ \__||__| /____  >____/|___|  /\___  >
        \/             \/           \/     \/ 
"""

from discord.ext import commands
import traceback
import discord
import random
import json
import sys
import os

with open('secrets.json', 'r') as tf:
    tf = json.load(tf)
    TOKEN = tf['token']

utilities_extensions = [
    'cogs.utilities.serverinfo',
    'cogs.utilities.userinfo', 'cogs.utilities.help', 'cogs.utilities.embeds',
    'cogs.error.errorHandler', 'cogs.utilities.credits',
    'cogs.utilities.owner'
]
moderation_extensions = ['cogs.mod.kick', 'cogs.mod.ban', 'cogs.mod.tempmute','cogs.mod.mute','cogs.mod.unmute','cogs.mod.slowmode', 'cogs.mod.warn']
reddit_extensions = ['cogs.reddit.meme', 'cogs.reddit.aww', 'cogs.reddit.gaming']
fun_extensions = ['cogs.fun.eightball']

bot = commands.Bot(command_prefix='-')

bot.remove_command("help")

if __name__ == '__main__':
    for extension in utilities_extensions:
        bot.load_extension(extension)
    for extension in moderation_extensions:
        bot.load_extension(extension)
    for extension in reddit_extensions:
        bot.load_extension(extension)
    for extension in fun_extensions:
        bot.load_extension(extension)

@bot.command()
async def test(ctx):
   await ctx.send('<:kitsuneheart2:786989004272173106> __**Thank you for inviting me!**__\n<:kitsunethink:786984788095533069> My current prefix is **`k!`**, if you would like to view my commands, please type `k!help`!\n<:kitsuneheart:786984788761509908> If you like this bot, make sure to vote us on **top.gg!**, https://top.gg/bot/768967985326456874 ')

@bot.event
async def on_ready():
    print(
        f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n'
    )

@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def bal(ctx):
    await open_account(ctx.author)
    
    user = ctx.author

    users = await get_bank_data()

    wallet_amt = users[str(user.id)]["wallet"]

    bank_amt = users[str(user.id)]["bank"]
    total_amt = users[str(user.id)]["wallet"] + users[str(user.id)]["bank"]
    

    embed = discord.Embed(title=f"{ctx.author.name}'s Balance",description=f"**Wallet:** {wallet_amt}\n**Bank:** {bank_amt}\n**Total:** {total_amt}", color=0xffa500)
    await ctx.send(embed = embed)

@bot.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def beg(ctx):
    await open_account(ctx.author)

    user = ctx.author

    users = await get_bank_data()

    earnings = random.randrange(101)

    await ctx.send(f"**kitsune gave you {earnings} koins!!**")

    users[str(user.id)]["wallet"] += earnings

    with open("mainbank.json", "w") as f:
        json.dump(users,f)


@bot.command(aliases=["with",'w'])
@commands.cooldown(1, 5, commands.BucketType.user)
async def withdraw(ctx,amount = None):
    await open_account(ctx.author)
    if amount == None:
        await ctx.send("Please enter a amount of Koins to withdraw.")
        return

    bal = await update_bank(ctx.author)

    amount = int(amount)

    if amount>bal[1]:
        await ctx.send("Oof! You don't have that much money.")
        return
    if amount<0:
        await ctx.send("Amount must be positive.")
        return

    await update_bank(ctx.author,amount)
    await update_bank(ctx.author,-1*amount,"bank")

    await ctx.send(f"You've withdrew **{amount} Koins**!")

@bot.command()
async def dep(ctx,amount = None):
    await open_account(ctx.author)
    if amount == None:
        await ctx.send("Please enter a amount of Koins to deposit.")
        return

    bal = await update_bank(ctx.author)

    amount = int(amount)

    if amount>bal[0]:
        await ctx.send("You don't have that much money!")
        return
    if amount<=0:
        await ctx.send("Amount must be positive.")
        return

    await update_bank(ctx.author,-1*amount)
    await update_bank(ctx.author,amount,"bank")

    await ctx.send(f"**You've deposited **{amount}** Koins!")
@bot.command()
@commands.cooldown(1, 120, commands.BucketType.user)
async def rob(ctx,member: discord.Member):
    await open_account(ctx.author)
    await open_account(member)
   
    bal = await update_bank(member)

    

    if bal[0]<100:
        await ctx.send("Leave the poor alone...")
        return

    earnings = random.randrange(0, bal[0])
  

    await update_bank(ctx.author,earnings)
    await update_bank(member,-1*earnings)

    await ctx.send(f"You've robbed **{member.name}** and gained **{earnings} Koins**!")


async def open_account(user):

    users = await get_bank_data()
    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["wallet"] = 0
        users[str(user.id)]["bank"] = 0

    with open("mainbank.json", "w") as f:
        json.dump(users,f)
    return True
async def get_bank_data():
    with open("mainbank.json", "r") as f:
        users = json.load(f)

    return users

async def update_bank(user, change=0,mode = 'wallet'):

    users = await get_bank_data()

    users[str(user.id)][mode] += change

    with open("mainbank.json", "w") as f:
        json.dump(users,f)

    bal = users[str(user.id)]["wallet"],users[str(user.id)]["bank"]
    return bal

bot.run(TOKEN)