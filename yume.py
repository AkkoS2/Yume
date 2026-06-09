# Bibliotecas e Inicializadores
from utils.envkeys import yume_key, app_id
from utils.localization import localizations, get_language
from discord.ext import commands, tasks
from workers.database import db_init
# from utils.logger import YLogger
from dotenv import load_dotenv
import discord
import asyncio
import random
import json
import os


# Definições de Shards, Prefixo, e Acesso a Dados
class YumeBot(commands.AutoShardedBot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.members = True
        intents.message_content = True
        load_dotenv()

        super().__init__(command_prefix='y!', case_insensitive=True, intents=intents, application_id=app_id(), shards=3)

    # Mensagem de erro para o usuário que tentar usar prefixo
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.reply("You can't use this command.", ephemeral=True)


# Definição de status e remoção do help padrão
yume = YumeBot()
yume.remove_command('help')

# Carrega o json de status na memória
try:
    with open('./utils/status.json', 'r', encoding='utf-8') as f:
        status = json.load(f)
except Exception as e:
    print(f"Algo deu errado :c \n{e}")
    status = []


# Bloqueio via ID do comando com prefixo
def id_lock(ctx):
    return ctx.author.id == 337765056970358784


# Realiza a inicialização dos status da Yume
@tasks.loop(seconds=30)
async def yume_status():
    if status:
        await yume.change_presence(activity=discord.Activity(type=discord.ActivityType.custom, name=random.choice(status)), status=discord.Status.online)


@yume.event
async def on_ready():
    if not yume_status.is_running():
        yume_status.start()


# Procura e carrega os arquivos do diretório cogs
async def load_cog():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            try:
                await yume.load_extension(f'cogs.{filename[:-3]}')
                print(f"{filename[:-3]} Funcionante.")
            except Exception as e:
                print(f"{filename[:-3]} Não Funcionante :c \n {e}")


# Sincronização e atualização da lista de comandos
@yume.command()
@commands.check(id_lock)
async def synctree(ctx):
    await yume.tree.sync()
    await ctx.send('Synced')


# Inicialização Geral: Idiomas, Personalidades, Bando de Dados, Cogs, Logger e API Discord
async def main():
    print("===============[ 🌸 ]===============")
    
    localizations()
    await db_init()
    await load_cog()
    # YLogger()
    
    print("Yume is Online!!")
    print("===============[ 🌸 ]===============")
    
    await yume.start(yume_key())


if __name__ == "__main__":
    asyncio.run(main())
