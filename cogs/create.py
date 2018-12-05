import discord
import time
import random
import datetime
import asyncio
from random import randint
from discord.ext import commands
from discord.ext.commands import Bot

bot=commands.Bot(command_prefix=commands.when_mentioned_or("s."))

class Create():
    
    @bot.command(pass_context=True)
    async def create(ctx):
        await ctx.send(":tada: Lets create your Giveaway! :tada:")
        await asyncio.sleep(1)
        await ctx.send("What channel shall i hold the giveaway in?\n"
                       "\n"
                       "`Ex. if you want to host it in a channel named #giveaways, reply giveaways`")
        def pred(m):
            return m.author==message.author and m.channel==message.channel
        try:
            channel_name=await bot.wait_for('message', check=pred, timeout=10.0)
        except asyncio.TimeoutError:
            await ctx.send("You took to long to reply, please start over.")
        else:
            g_channel=discord.utils.get(ctx.message.server.channels, name=channel_name.content)
            #Check if the channel exists (Currently Not working)
            if not g_channel:
                await ctx.send(":x: | Channel does not exist! | Start over") #Maybe add so that it dosent have to start over??!
            if g_channel:
                await ctx.send(":white_check_mark: | {} has been selected! :tada:")

def setup(bot):
    bot.add_cog(Create)
