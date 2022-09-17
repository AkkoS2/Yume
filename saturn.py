# bibliotecas
from helpers.phrases import status, dont_exist
from discord.ext import commands, tasks
from helpers.envkeys import saturn_key
from dotenv import load_dotenv
from itertools import cycle
import discord
import random
import os


# prefixo padrão & ciclo de status
load_dotenv()
saturn = commands.Bot(command_prefix='!s.', case_insensitive=True)
saturn.remove_command('help')
status = cycle(status())


# bloqueia comandos conforme o ID do usuário
def whitelist(ctx):
    return ctx.author.id == 337765056970358784


# inicializações
@saturn.event
async def on_ready():
    saturn_status.start()
    print('Online e Funcional!')


# altera o status da saturn
@tasks.loop(seconds=5)
async def saturn_status():
    await saturn.change_presence(status=discord.Status.online, activity=discord.Game(next(status)))


# ativa uma categoria do cogs (developer only)
@saturn.command(aliases=['ativar'])
@commands.check(whitelist)
async def active(ctx, extension):
    saturn.load_extension(f'cogs.{extension}')
    await ctx.reply(f'Ativei a categoria {extension} assim como pediu.', mention_author=False)


# desativa uma categoria do cogs (‘developer’ only)
@saturn.command(aliases=['desativar'])
@commands.check(whitelist)
async def disable(ctx, extension):
    saturn.unload_extension(f'cogs.{extension}')
    await ctx.reply(f'Desativei a categoria {extension} assim como pediu.', mention_author=False)


# recarrega uma categoria do cogs (developer only)
@saturn.command(aliases=['recarregar'])
@commands.check(whitelist)
async def reload(ctx, extension):
    saturn.reload_extension(f'cogs.{extension}')
    await ctx.reply(f'Recarreguei a categoria {extension} assim como pediu.', mention_author=False)


# comando não existente
@saturn.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.reply(f'{random.choice(dont_exist())}', mention_author=False)


# inicializa os arquivos do diretório cogs
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        saturn.load_extension(f'cogs.{filename[:-3]}')

saturn.run(saturn_key())
