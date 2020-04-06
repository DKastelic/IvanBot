# bot.py
import os
import asyncio

import discord
from discord.ext import commands
from dotenv import load_dotenv

import const

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix="ivan ")


# @bot.command(name='music', help='M U S I C')
# async def info(ctx):
#    await ctx.send('@dobi svoj info ni tezko pogledat mail pa nova.vegova pa moodle pa ekm pa discord pa teams')


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if 'a je kdo ' in message.content.lower() or 'ali je kdo ' in message.content.lower():
        await message.channel.send('ne')

    if 'a bo ' in message.content.lower() or 'a bo?' in message.content.lower() or message.content.lower() == 'a bo':
        await message.channel.send('ne')

    if 'koliko' in message.content.lower() or 'kolk' in message.content.lower() or 'kok' in message.content.lower() or 'kolko' in message.content.lower():
        await message.channel.send('dva')

    if 'zakaj' in message.content.lower() or 'zakva' in message.content.lower():
        await message.channel.send('zato')

    if 'lmao' in message.content.lower():
        await message.channel.send('lmao')

    if message.tts and message.author.id != const.MY_ID:
        await message.channel.send('shut the fuck up')

    if "info" in [x.name for x in message.role_mentions]:
        await message.channel.send('<@&696418671723151381>')

    if 'dela!' in message.content.lower() and 'ne' not in message.content.lower():
        await message.channel.send('YAY!')

    if message.content.upper() == "F":
        await message.channel.send('respect')

    if message.content.upper() == "X":
        await message.channel.send('doubt')

    if message.content == "test":
        print(f'{message.author.guild.channels}')

    await bot.process_commands(message)


crt_was_on = False


@bot.event
async def on_typing(channel, user, when):
    global crt_was_on
    if not crt_was_on and user.id == const.CRT_ID and channel.guild.id == const.OUR_GUILD:
        await channel.send(f'look! {user.nick} decided to show up')
        crt_was_on = True
        await asyncio.sleep(6 * 3600)  # 1h = 3600s
        crt_was_on = False
    # elif user.id == const.CRT_ID:



@bot.event
async def on_message_delete(message):
    print(f'`{message.content}` by {message.author.nick} was deleted')
    # await message.channel.send(f'\`{message.content}`" by {message.author.nick} was deleted')


@bot.event
async def on_message_edit(before, after):
    if before.content != '':
        print(f'`{before.content}` was changed to `{after.content}` by {before.author.nick}')
        # await on_message(after)


@bot.event
async def on_member_remove(member):
    if member.guild.id == const.OUR_GUILD:
        try:
            await member.unban()
        except:
            print(f'{member.name} not banned')

        for x in member.guild.channels:
            if isinstance(x, discord.TextChannel):
                invite = await x.create_invite(max_uses=1)
                await member.send(invite)
                break


bot.run(TOKEN)
