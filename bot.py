#!/usr/bin/env python3

import MySQLdb
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')
database = MySQLdb.connect('localhost', 'worms', '', 'leadership')
cursor = database.cursor()


@bot.event
async def on_ready():
    servers_list = ', '.join([server.name for server in bot.servers])
    print('Logged in as {} on:  {}'.format(bot.user.name, servers_list))


@bot.command(pass_context=True)
async def list(ctx):
    cursor.execute("SELECT user, role FROM members;")
    results = cursor.fetchall()
    result_str = 'Hey, you currently have all these leaders\n'
    for user_id, role in results:
        member = [user for user in ctx.message.server.members if user.id == user_id][0]
        result_str += '\n{} is a {}'.format(member.mention, role)
    await bot.say(result_str)


@bot.command(pass_context=True)
async def add(ctx, *args): # arg1:  user, arg2:  role
    try:
        users = ctx.message.mentions
        role = ctx.message.role_mentions[0]
        for user in users:
            await bot.add_roles(user, role)
            query = ("INSERT INTO members "
                     "(user, role) "
                     "VALUES (%s, %s)")
            cursor.execute(query, (user.id, role.name))
        database.commit()
        await bot.add_reaction(ctx.message, u'\u2705')
    except IndexError as e:
        print(e)
        await bot.add_reaction(ctx.message, '\U0001F1FD')
        await bot.say('Usage: `add user role`')
        return


@bot.command(pass_context=True)
async def test(ctx, *args):
    print(ctx.message.mentions)
    await bot.say('Tested with args {}'.format(', '.join(args)))


bot.run('NDQzNDIyNTA0NTI3MzMxMzQ4.DdNJKA.U_AvRod8AWJGBlvAVVrfd1iKZvE')
