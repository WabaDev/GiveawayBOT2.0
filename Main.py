import discord
import random
import time
import datetime
import asyncio
import aiohttp

from discord.ext import commands
from discord.ext.commands import Bot
from random import randint

tu = datetime.now()
bot=commands.Bot(command_prefix=commands.when_mentioned_or("+g"))
startup_extensions=["cogs.create", "cogs.start"]

for extension in startup_extensions:
    try:
        bot.load_extension(extension)
        print(f'{extension} Loaded')
    except Exception as e:
        print(f"Failed to load extention {extension}\n{type(e).__name__}: {e}")

@bot.event
async def on_ready():
    print("===================================")
    print("Logged in as: %s"%bot.user.name)
    print("ID: %s"%bot.user.id)
    print("Py Lib Version: %s"%discord.__version__)
    print("===================================")

@bot.command()
async def support(ctx):
    color = ''.join([random.choice('0123456789ABCDEF') for x in range(6)])
    color = int(color, 16)
    embed=discord.Embed(title=":tada: Support Giveaway! :tada:", colour=discord.Colour(value=color))
    embed.add_field(name = "Official Server", value = '[Join Now](https://discord.gg/SfjCvMg)')
    embed.add_field(name = "Why Join?", value = "Join to stay up to date with the newest features, meet the Devs, and chill with others!")
    embed.set_footer(text = "Upvote us if you enjoy our bot!")
    await ctx.send(embed = embed)

@bot.command()
async def updates(ctx):
    color=''.join([random.choice('0123456789ABCDEF') for x in range(6)])
    color = int(color, 16)
    embed=discord.Embed(title=":tada: Recent Updates :tada:", colour=discord.Colour(value=color))
    embed.add_field(name="Dev News:", value="No Recent Updates as of 12/04/2018")
    await ctx.send(embed=embed)
@bot.command()
async def upvote(ctx):
    color=''.join([random.choice('0123456789ABCDEF') for x in range(6)])
    color=int(color, 16)
    embed=discord.Embed(title=":thumbsup: Upvote us to show some love! :thumbsup:", colour=discord.Colour(value=color))
    embed.add_field(name = "Upvotes us now!", value="Click [here](https://discordbots.org/bot/396464677032427530/vote)")
    embed.set_footer(text="Upvotes are greatly appreciated, Thank you!")
    await ctx.send(embed=embed)

@bot.command()
async def uptime(ctx):
    'Check bot uptime.'
    global tu
    colour = ''.join([random.choice('0123456789ABCDEF') for x in range(6)])
    colour = int(colour, 16)
    embed = discord.Embed(colour=discord.Colour(value=colour), timestamp=datetime.utcnow())
    embed.add_field(name='__**My Current Uptime :**__', value=timedelta_str(datetime.now() - tu))
    embed.set_footer(text='{} | Requested by: {}'.format(version, ctx.author))
    await ctx.send(embed=embed)

def timedelta_str(dt):
    days = dt.days
    (hours, r) = divmod(dt.seconds, 3600)
    (minutes, sec) = divmod(r, 60)
    if (minutes == 1) and (sec == 1):
        return '{0} days, {1} hours, {2} minute and {3} second.'.format(days, hours, minutes, sec)
    elif (minutes > 1) and (sec == 1):
        return '{0} days, {1} hours, {2} minutes and {3} second.'.format(days, hours, minutes, sec)
    elif (minutes == 1) and (sec > 1):
        return '{0} days, {1} hours, {2} minute and {3} seconds.'.format(days, hours, minutes, sec)
    else:
        return '{0} days, {1} hours, {2} minutes and {3} seconds.'.format(days, hours, minutes, sec)

bot.run("")
