import discord
import re
from calculester import Calculester
from env import Env


env = Env()
client = discord.Client()
cal = Calculester()

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=env.GUILD)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome friend'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    print(message)
    print(message.content)

    if re.search('calculester', message.content, re.IGNORECASE) :
        res = cal.parse_message(message)
        if res != '':
            await message.channel.send(res)

client.run(env.TOKEN)