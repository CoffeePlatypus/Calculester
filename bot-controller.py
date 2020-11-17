# better bot controller

import re
import discord
from calculester import Calculester
from env import Env
from discord.ext import commands

ENV = Env()
cal = Calculester(ENV.IDs)

bot = commands.Bot(command_prefix='!')

@bot.command(name='mood', help='Returns a random mood')
async def mood(ctx):
    await ctx.send(cal.pick_mood())

@bot.command(name='street-side', help='Tells people which street side to park on at Julias')
async def street_side(ctx):
    await ctx.send(cal.street_side_to_park_on())

@bot.command(name='pick-person', help='picks a random person')
async def pick_person(ctx):
    await ctx.send(f'<@{cal.pick_friend()}>')

@bot.command(name='fuck', help=':P')
async def fuck(ctx):
    await ctx.send(f'fuck <@{cal.pick_friend()}>')
    await ctx.message.delete()

@bot.command(name='poop', help='💩')
async def poop(ctx):
    await ctx.send('💩')

@bot.command(name='unshit')
async def unshit(ctx, thing: str):
    if thing == 'pants': 
        await ctx.send('💩↩️👖')
    else:
        await ctx.send('💩↩️')

@bot.command(name='tell', help='person to tell followed by message')
async def tell(ctx, member: discord.Member, *, content):
    channel = await member.create_dm()
    await channel.send(content)
    await ctx.message.delete()

@bot.command(name='summon', help='summons the goon squad')
async def summon(ctx):
    mem = bot.get_user(cal.nard[0])
    print(mem)
    # channel = await mem.create_dm()
    # await channel.send('summon')
    await ctx.send('summon test')
    await ctx.message.delete()

@bot.command(name='printer')
async def printer(ctx):
    print(ctx.message)
    await ctx.send('tomato')
    await ctx.message.delete()

bot.run(ENV.TOKEN)