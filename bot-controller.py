# better bot controller

import re
import discord
from calculester import Calculester
from env import Env
from discord.ext import commands

ENV = Env()
cal = Calculester()

bot = commands.Bot(command_prefix='!')

@bot.command(name='mood', help='Returns a random mood')
async def mood(ctx):
    await ctx.send(cal.pick_mood())

@bot.command(name='street-side', help='Tells people which street side to park on at Julias')
async def street_side(ctx):
    await ctx.send(cal.street_side_to_park_on())

@bot.command(name='pick-person', help='picks a random person')
async def pick_person(ctx):
    await ctx.send(cal.pick_friend())

@bot.command(name='fuck', help=':P')
async def fuck(ctx):
    await ctx.send(f'fuck @{cal.pick_friend()}')

@bot.command(name='poop', help='💩')
async def poop(ctx):
    await ctx.send('💩')

@bot.command(name='unshit')
async def unshit(ctx, thing: str):
    if thing == 'pants': 
        await ctx.send('💩↩️👖')
    else:
        await ctx.send('💩↩️')

@bot.command(pass_context = True, name='tell', help='')
async def tell(ctx, member: discord.Member, *, content):
    channel = await member.create_dm()
    await channel.send(content)

@bot.command(name='users')
async def users(ctx):
    for guild in bot.guilds:
        for member in guild.members:
            print(member) # why doesn't this work

@bot.command(name='printer')
async def printer(ctx, member: discord.Member):
    print(member)
    await ctx.send('print')


bot.run(ENV.TOKEN)