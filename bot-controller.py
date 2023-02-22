# better bot controller

import discord,  praw , random, re
from calculester import Calculester
from env import Env
from calsreddit import CalsReddit
from discord.ext import commands, tasks
from datetime import datetime

ENV = Env()
cal = Calculester(ENV.fIDs)
calsReddit = CalsReddit(ENV)

bot = commands.Bot(command_prefix='!')

@bot.command(name='mood', help='Returns a random mood')
async def mood(ctx):
    await ctx.send(cal.pick_mood())

@bot.command(name='street-side', help='Tells people which street side to park on at Julias')
async def street_side(ctx):
    await ctx.send(cal.street_side_to_park_on())

@bot.command(name='pick-person', help='picks a random person')
async def pick_person(ctx):
    if ctx.guild.name == 'Actual friends' :
        await ctx.send(f'<@{cal.pick_friend()}>')
    else:
        await ctx.send('no friends here')

@bot.command(name='fuck', help=':P')
async def fuck(ctx):
    if ctx.guild.name == 'Actual friends' :
        await ctx.send(f'fuck <@{cal.pick_friend()}>')
        await ctx.message.delete()
    else:
        await ctx.send('im sorry that is nsfw ;)')

@bot.command(name='poop', help='💩')
async def poop(ctx):
    await ctx.send('💩')

@bot.command(name='unshit', help='we all need help')
async def unshit(ctx, thing: str):
    if thing == 'pants': 
        await ctx.send('💩↩️👖')
    else:
        await ctx.send('💩↩️')

@bot.command(name='tell', help='person to dm followed by message')
async def tell(ctx, member: discord.Member, *, content):
    channel = await member.create_dm()
    await channel.send(content)
    await ctx.message.delete()

@bot.command(name='summon', help='summons the goon squad')
async def summon(ctx):
    if ctx.guild.name == 'Actual friends' :
        await ctx.send('Summon the goon squad')
        ats = ''
        for f in cal.friends :
            ats += f'<@{f}> '
        await ctx.send(ats)

@bot.command(name='simp', help='🍆')
async def simp(ctx):
    await ctx.message.add_reaction('🍆')

@bot.command(name='porn')
async def porn(ctx):
    await ctx.send(calsReddit.getRandomRedditPost('wireporn'))

@bot.command(name='cat', help='r/blep')
async def cat(ctx):
    await ctx.send(calsReddit.getRandomRedditPost('Blep'))

@bot.command(name='dog')
async def dog(ctx):
    await ctx.send(calsReddit.getRandomRedditPost('rarepuppers'))

# testing function
@bot.command(name='printer')
async def printer(ctx):
    # chan = bot.get_channel(734945466982203526)
    # chan = bot.get_channel(777634476972572693)
    # print(chan)
    print(ctx.channel.id)
    cal.check_events()
    await ctx.message.add_reaction('🍆')

@tasks.loop(hours=24)
async def called_once_a_day():
    message_channel = bot.get_channel(ENV.genId)
    print(f"Got channel {message_channel}")
    todayEvents = cal.check_events()
    if todayEvents:
        await message_channel.send(todayEvents)
    lateNit = bot.get_channel(ENV.lateNightId)
    print(f"Got channel {lateNit}")
    
    todayEvents = cal.check_roomate_events()
    if todayEvents:
        await lateNit.send(todayEvents)
    


@called_once_a_day.before_loop
async def before():
    await bot.wait_until_ready()
    print("Finished waiting for cal to wake up")

called_once_a_day.start()
bot.run(ENV.TOKEN)