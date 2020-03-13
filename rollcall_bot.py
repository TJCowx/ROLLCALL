import os

from discord.ext import commands
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name='howto')
async def list_help(ctx):

    response = 'Here is a list of commands you can use me for!\n' \
                '**!rollcall** - Starts a rollcall for Siege! Defaults to ' \
                '8PM\n' \
                '**!in** - If there is a rollcall, use this to show you\'re' \
                ' in for Siege tonight\n' \
                '**!out** - If you changed your mind and are now out\n' \
                '**!whosin** - Gives you a list of people who are in for Siege'\
                ''
    await ctx.send(response)


@bot.command(name='rollcall', pass_context=True)
async def start_rollcall(ctx):
    sender = str(ctx.message.author.mention)
    await ctx.send(f'@here {sender} has initiated a Siege Roll Call for 8PM!')
    await send_whos_in(ctx)


async def send_whos_in(ctx):
    await ctx.send('Lets try this')

bot.run(TOKEN)