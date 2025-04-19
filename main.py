
from os import listdir, mkdir, path, system
rs = open('./requirements.txt', 'r').readlines()
for i in rs:
    try:
        __a = __import__(i.strip())
        del __a
    except ImportError:
        system(f'python -m pip install -r requirements.txt')
        break
from nextcord.ext import commands
from nextcord import Intents
import logging
import sys
from json import load

if not path.exists('./cogs'):
    mkdir('./cogs')
if not path.exists('./data'):
    mkdir('./data')
if not path.exists('./config.json'):
    print('Config file not found. Please create a config.json file in the root directory.')
    sys.exit(1)
config = load(open('./config.json', 'r'))

logging.basicConfig(level=logging.ERROR)

intents = Intents.all()
client = commands.Bot(command_prefix=config['prefix'], intents=intents, help_command=None, case_insensitive=True)
client.cfg = config
client.default_guild_ids.append(config['guildId'])


async def cmd_error_handler(ctx, error):
    async def respond(msg):
        try:
            await ctx.reply(msg)
        except commands.CommandError:
            try:
                await ctx.send(msg)
            except commands.CommandError:
                pass

    if isinstance(error, commands.CommandNotFound):
        return
    if isinstance(error, commands.MissingRequiredArgument):
        await respond('Missing required argument')
    elif isinstance(error, commands.BadArgument):
        await respond('Bad argument')
    elif isinstance(error, commands.MissingPermissions):
        await respond('Missing permissions')
    elif isinstance(error, commands.BotMissingPermissions):
        await respond('Bot missing permissions')
    elif isinstance(error, commands.CheckFailure):
        await respond('Check failure')
    else:
        try:
            await respond('An error occurred')
        except Exception as e2:
            print(f'Error while trying to respond: {e2}')
            pass
        print(f'Error: {error}')
        raise error


@client.event
async def on_command_error(ctx, error):
    await cmd_error_handler(ctx, error)


@client.command(name='ping')
async def ping(ctx: commands.Context):
    ms = round(client.latency * 1000)
    await ctx.reply(f'Pong! {ms}ms')


@client.event
async def on_ready():
    print(f'{client.user.name} is ready!')


extensions = []
for i in listdir(r'./cogs'):
    if i == 'config.py':
        continue
    if i.endswith('.py'):
        name = i[:-3]
        extensions.append(f'cogs.{name}')
client.load_extensions(extensions)


def handle_exception(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return

    logging.error("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))
    if client.is_ready():
        client.loop.run_until_complete(client.close())
        client.loop.run_until_complete(client.start(config['token'], reconnect=True))
    else:
        sys.exit(1)


sys.excepthook = handle_exception

if __name__ == '__main__':
    try:
        client.run(config['token'], reconnect=True)
    except Exception as e:
        logging.error("Exception occurred", exc_info=e)
