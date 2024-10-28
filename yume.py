# Bibliotecas utilizadas para o arquivo principal funcionar corretamente
from utils.envkeys import yume_key, app_id
from discord.ext import commands, tasks
from utils.logger import YLogger
from dotenv import load_dotenv
import discord
import asyncio
import random
import os


# Definições de Shards, Prefixo, e Data Access
class YumeBot(commands.AutoShardedBot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.members = True
        intents.message_content = True
        load_dotenv()

        super().__init__(command_prefix='y!', case_insensitive=True, intents=intents, application_id=app_id(), shards=3)

    # Mensagem de erro para o usuário que tentar usar o prefixo
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.reply("You can't use this command.", ephemeral=True)


# Definindo status da Yume e removendo o comando help padrão
yume = YumeBot()
yume.remove_command('help')
status = open('./texts/status.txt').read().splitlines()


# Bloqueia o comando de acordo com o ID do usuário
def id_lock(ctx):
    return ctx.author.id == 337765056970358784


# Realiza a inicialização dos status da Yume
@tasks.loop(seconds=10)
async def yume_status():
    await yume.change_presence(activity=discord.Game(name=random.choice(status)), status=discord.Status.online)


@yume.event
async def on_ready():
    yume_status.start()


# Procura e carrega os arquivos do diretório cogs
async def load_cog():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await yume.load_extension(f'cogs.{filename[:-3]}')


# Comando para sincronizar e atualizar a lista de comandos que aparecem no discord
@yume.command()
@commands.check(id_lock)
async def synctree(ctx):
    await yume.tree.sync()
    await ctx.send('Synced')


# Realiza a inicialização da Yume e dos comandos
async def main():
    await on_ready()
    await load_cog()
    YLogger()

    print("Yume is Online!!")
    await yume.start(yume_key())


asyncio.run(main())
