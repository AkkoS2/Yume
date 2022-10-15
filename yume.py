# bibliotecas
from helpers.texts import status, dont_exist
from helpers.envkeys import yume_key, app_id
from discord.ext import commands, tasks
from dotenv import load_dotenv
from itertools import cycle
import discord
import asyncio
import random
import os


# definição dos shards, prefixo e permissões da Yume
class YumeBot(commands.AutoShardedBot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        intents.members = True
        load_dotenv()

        super().__init__(command_prefix='y!', case_insensitive=True, intents=intents, application_id=app_id(), shards=3)

    # envia uma mensagem de erro caso o comando com prefixo não exista
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.reply(f'{random.choice(dont_exist())}', ephemeral=True)


# remove o comando help e define o status
yume = YumeBot()
yume.remove_command('help')
status = cycle(status())


# bloqueia a função com base no ID do usuário
def id_lock(ctx):
    return ctx.author.id == 337765056970358784


# inicializa os status da Yume
@yume.event
async def on_ready():
    yume_status.start()


# realiza a rotação do status da Yume
@tasks.loop(seconds=10)
async def yume_status():
    await yume.change_presence(activity=discord.Game(name=next(status)))


# inicializa os arquivos do diretório cogs
async def load_cog():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await yume.load_extension(f'cogs.{filename[:-3]}')


# realiza a sincronização dos comandos existentes com o discord
@yume.command()
@commands.check(id_lock)
async def synctree(ctx):
    await yume.tree.sync()
    await ctx.send('synced')


# realiza a inicialização da Yume
async def main():
    await on_ready()
    await load_cog()

    print("I'm Online!!")
    await yume.start(yume_key())


asyncio.run(main())
