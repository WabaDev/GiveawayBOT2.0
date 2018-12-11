import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random
from random import randint
import datetime
bot = commands.Bot(command_prefix=commands.when_mentioned_or('+g'))

class Start():
    'Start a giveaway faster!'

    @bot.command()
    async def start(ctx, duration=None, winners=None, prize=None):
        'Create a giveaway but faster!'
        if duration == None:
            await ctx.send(':x: | No `Duration` Was Inputted!')
        if winners == None:
            await ctx.send(':x: | No `Amount Of Winners` Were Inputted!')
        if prize == None:
            await ctx.send(':x: | No `Prize` Was Inputted!')
        else:
            unit = duration[(- 1)]
            if unit == 's':
                time = int(duration[:(- 1)])
                longunit = 'seconds'
            elif unit == 'm':
                time = int(duration[:(- 1)]) * 60
                longunit = 'minutes'
            elif unit == 'h':
                time = (int(duration[:(- 1)]) * 60) * 60
                longunit = 'hours'
            winners = int(winners)
            color = ''.join([random.choice('0123456789ABCDEF') for x in range(6)])
            color = int(color, 16)
            embed = discord.Embed(title=':tada: __**{} Giveaway!**__ :tada:'.format(prize), colour=discord.Colour(value=color), timestamp=datetime.datetime.utcnow())
            embed.add_field(name='Prize: ', value='{}'.format(prize))
            embed.add_field(name='Winners: ', value='{} Winner(s)'.format(winners))
            embed.add_field(name='Time: ', value='{}'.format(duration), inline=True)
            embed.set_footer(text='Add The Reaction to join! Started @ ')
            give_away = await ctx.send(embed=embed)
            ga_message = await give_away.add_reaction('\U0001f389')
            await asyncio.sleep(time)
            ga_message = await give_away.channel.get_message(give_away.id)
            ga_users = []
            async for user in ga_message.reactions[0].users():
                ga_users.append(user.mention)
            ga_bot = ctx.guild.get_member(519733424387260416)
            ga_users.remove(ga_bot.mention)
            if len(ga_users) == 0:
                error = discord.Embed(title=':warning: Error!', description='The giveaway ended with no participants, could not chose a winner', color=16711680)
                await ctx.send(embed=error)
            else:
                winner_list = []
                for loop in range(winners):
                    winner = random.choice(ga_users)
                    ga_users.remove(winner)
                    winner_list.append(winner)
                    msg = ''
            color = ''.join([random.choice('0123456789ABCDEF') for x in range(6)])
            color = int(color, 16)
            embed = discord.Embed(title=':tada: __**Giveaway Ended!**__ :tada:', colour=discord.Colour(value=color), timestamp=datetime.datetime.utcnow())
            embed.add_field(name='Winners: ', value='{} Winner(s)'.format(winners))
            embed.add_field(name='Winner(s): ', value=',\n'.join(winner_list))
            embed.add_field(name='Prize: ', value='{}'.format(prize))
            embed.set_footer(text='Better Luck Next Time! Ended @ ')
            await give_away.edit(embed=embed)
            for winner in winner_list:
                msg += ', ' + winner
            await ctx.send((':tada: ' + ', '.join(winner_list)) + ' won **{}**'.format(prize))

def setup(bot):
    bot.add_cog(Start)
