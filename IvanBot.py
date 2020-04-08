# bot.py
import asyncio
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
OUR_GUILD = int(os.getenv('DISCORD_OUR_GUILD'))
CAKA_ID = int(os.getenv('DISCORD_CAKA_ID'))
CRT_ID = int(os.getenv('DISCORD_CRT_ID'))
MY_ID = int(os.getenv('DISCORD_MY_ID'))

bot = commands.Bot(command_prefix="ivan ")


# @bot.command(name='music', help='M U S I C')
# async def info(ctx):
#    await ctx.send('@dobi svoj info ni tezko pogledat mail pa nova.vegova pa moodle pa ekm pa discord pa teams')


# connection confirmation
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


# auto reply
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if ((message.content.lower().startswith('a ') or message.content.lower().startswith('ali '))
            and 'kdo' in message.content.lower()):
        await message.channel.send('ne')

    elif message.content.lower().startswith('a bo?') or message.content.lower().startswith('a bo '):
        await message.channel.send('ne')

    if ('koliko ' in message.content.lower() or 'kolk ' in message.content.lower()
            or 'kok ' in message.content.lower() or 'kolko ' in message.content.lower()):
        await message.channel.send('dva')

    if 'zakaj ' in message.content.lower() or 'zakva ' in message.content.lower():
        await message.channel.send('zato')

    if 'dela!' in message.content.lower() and 'ne' not in message.content.lower():
        await message.channel.send('YAY!')

    if 'ivan' in message.content.lower():
        await message.channel.send('ja?')

    if 'lmao' in message.content.lower():
        await message.channel.send('lmao')

    if message.content.lower().startswith('nice') or ' nice ' in message.content.lower() or message.content.lower().endswith(' nice'):
        await message.channel.send('nice')

    if message.tts and message.author.id != MY_ID:
        await message.channel.send('shut the fuck up')

    if "info" in [x.name for x in message.role_mentions]:
        await message.channel.send('<@&696418671723151381>')

    if message.content.lower().startswith('good bot'):
        await message.channel.send('hvala')

    if message.content.upper() == "F":
        await message.channel.send('respect')

    if message.content.upper() == "X":
        await message.channel.send('doubt')

    if message.content == "test":
        print(f'{message}')

    if message.author.id == CAKA_ID:
        await message.channel.send('fuck you caka')

    await bot.process_commands(message)


crt_was_on = False


# crt check
@bot.event
async def on_typing(channel, user, when):
    # await channel.send('fuck you caka')
    global crt_was_on
    if not crt_was_on and user.id == CRT_ID and channel.guild.id == OUR_GUILD:
        await channel.send(f'look! {user.nick} decided to show up')
        crt_was_on = True
        await asyncio.sleep(6 * 3600)  # 1h = 3600s
        crt_was_on = False
    # elif user.id == CRT_ID:


# auto unban
@bot.event
async def on_member_remove(member):
    if member.guild.id == OUR_GUILD:
        try:
            await member.unban()
        except:
            print(f'{member.name} not banned')

        for x in member.guild.channels:
            if isinstance(x, discord.TextChannel):
                invite = await x.create_invite(max_uses=1)
                await member.send(invite)
                break


# logging
@bot.event
async def on_message_delete(message):
    print(f'`{message.content}` by {message.author.nick} was deleted')
    # await message.channel.send(f'\`{message.content}`" by {message.author.nick} was deleted')


# logging
@bot.event
async def on_message_edit(before, after):
    if before.content != '':
        print(f'`{before.content}` was changed to `{after.content}` by {before.author.nick}')
        # await on_message(after)

bot.run(TOKEN)
