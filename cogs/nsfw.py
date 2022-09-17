# bibliotecas
from helpers.envkeys import api_key, user_id
from discord.ext import commands
from pygelbooru import Gelbooru
from helpers import searchers
import requests
import discord
import random


# inicializa o cog
class NSFW(commands.Cog):
    def __init__(self, saturn):
        self.saturn = saturn

    # avisa se a classe iniciou
    @commands.Cog.listener()
    async def on_ready(self):
        print('Lewd is Ready!')

    # rule34
    @commands.command(aliases=['r34'])
    @commands.is_nsfw()
    async def rule34(self, ctx, *, search: str):

        search = search.replace(' ', '_')

        r = requests.get(f'https://api.rule34.xxx/index.php?page=dapi&s=post&q=index&limit=50&pid='
                         f'{random.randint(1, 5)}&tags={search}&json=1')

        if r.status_code == 200:

            data = r.json()
            if len(data) < 1:
                await ctx.send('Não consegui achar nada :c', mention_author=False)
                return

            lewd = discord.Embed(color=discord.Colour.random())
            url = data[random.randint(0, 49)]['file_url']
            lewd.set_image(url=url)
            lewd.set_footer(text='Rule34.xxx')

            await ctx.send(embed=lewd)

        else:
            await ctx.reply('Parece que deu algum problema com a API, desculpa :c', mention_author=False)

    # Yande.re
    @commands.command(aliases=['yande.re'])
    @commands.is_nsfw()
    async def yandere(self, ctx, *, search: str):

        search = search.replace(' ', '_')

        r = requests.get(f'https://yande.re/post.json?tags={search}&3Afalse&limit=50&api_version=2&filter=1&'
                         f'include_tags=1&include_votes=1&include_pools=1')

        if r.status_code == 200:

            data = r.json()
            if len(data['posts']) < 1:
                await ctx.reply('Não consegui achar nada :c')
                return

            lewd = discord.Embed(color=discord.Colour.random())
            url = data['posts'][random.randint(0, 50)]['file_url']
            lewd.set_image(url=url)
            lewd.set_footer(text='Yande.re')

            await ctx.send(embed=lewd)

        else:
            await ctx.reply('Parece que deu algum problema com a API, desculpa :c', mention_author=False)

    # r/Paizuri
    @commands.command()
    @commands.is_nsfw()
    async def paizuri(self, ctx):

        searchers.reddit = 'paizuri'
        result = searchers.reddit_searcher()

        lewd = discord.Embed(description=f'**{str(result[0])}**', color=discord.Colour.random())
        lewd.set_author(name=f'r/{result[3]}', url=str(result[2]))
        lewd.set_image(url=str(result[1]))
        await ctx.send(embed=lewd)

    # r/hentai
    @commands.command()
    @commands.is_nsfw()
    async def hentai(self, ctx):

        searchers.reddit = 'hentai'
        result = searchers.reddit_searcher()

        lewd = discord.Embed(description=f'**{str(result[0])}**', color=discord.Colour.random())
        lewd.set_author(name=f'/r{result[3]}', url=str(result[2]))
        lewd.set_image(url=str(result[1]))
        await ctx.send(embed=lewd)

    # r/ecchi
    @commands.command()
    @commands.is_nsfw()
    async def ecchi(self, ctx):

        searchers.reddit = 'ecchi'
        result = searchers.reddit_searcher()

        lewd = discord.Embed(description=f'**{str(result[0])}**', color=discord.Colour.random())
        lewd.set_author(name=f'/r{result[3]}', url=str(result[2]))
        lewd.set_image(url=str(result[1]))
        await ctx.send(embed=lewd)

    # r/HQHentai
    @commands.command()
    @commands.is_nsfw()
    async def hqhentai(self, ctx):

        searchers.reddit = 'HQHentai'
        result = searchers.reddit_searcher()

        lewd = discord.Embed(description=f'**{str(result[0])}**', color=discord.Colour.random())
        lewd.set_author(name=f'/r{result[3]}', url=str(result[2]))
        lewd.set_image(url=str(result[1]))
        await ctx.send(embed=lewd)

    # r/almosthentai
    @commands.command()
    @commands.is_nsfw()
    async def almosthentai(self, ctx):

        searchers.reddit = 'almosthentai'
        result = searchers.reddit_searcher()

        lewd = discord.Embed(description=f'**{str(result[0])}**', color=discord.Colour.random())
        lewd.set_author(name=f'/r{result[3]}', url=str(result[2]))
        lewd.set_image(url=str(result[1]))
        await ctx.send(embed=lewd)

    # r/uncensoredhentai
    @commands.command()
    @commands.is_nsfw()
    async def uncensoredhentai(self, ctx):

        searchers.reddit = 'uncensoredhentai'
        result = searchers.reddit_searcher()

        lewd = discord.Embed(description=f'**{str(result[0])}**', color=discord.Colour.random())
        lewd.set_author(name=f'/r{result[3]}', url=str(result[2]))
        lewd.set_image(url=str(result[1]))
        await ctx.send(embed=lewd)

    # r/SubwayHentai
    @commands.command(aliases=['subhentai'])
    @commands.is_nsfw()
    async def subwayhentai(self, ctx):

        searchers.reddit = 'SubwayHentai'
        result = searchers.reddit_searcher()

        lewd = discord.Embed(description=f'**{str(result[0])}**', color=discord.Colour.random())
        lewd.set_author(name=f'/r{result[3]}', url=str(result[2]))
        lewd.set_image(url=str(result[1]))
        await ctx.send(embed=lewd)

    # r/TrapHentai
    @commands.command()
    @commands.is_nsfw()
    async def traphentai(self, ctx):

        searchers.reddit = 'TrapHentai'
        result = searchers.reddit_searcher()

        lewd = discord.Embed(description=f'**{str(result[0])}**', color=discord.Colour.random())
        lewd.set_author(name=f'/r{result[3]}', url=str(result[2]))
        lewd.set_image(url=str(result[1]))
        await ctx.send(embed=lewd)

    # r/tightdeology
    @commands.command(aliases=['tightdeo'])
    @commands.is_nsfw()
    async def tightdeology(self, ctx):

        searchers.reddit = 'tights'
        result = searchers.reddit_searcher()

        lewd = discord.Embed(description=f'**{str(result[0])}**', color=discord.Colour.random())
        lewd.set_author(name=f'/r{result[3]}', url=str(result[2]))
        lewd.set_image(url=str(result[1]))
        await ctx.send(embed=lewd)

    # r/HentaiWorldInfo
    @commands.command(aliases=['hri'])
    @commands.is_nsfw()
    async def hentaiworldinfo(self, ctx):

        searchers.reddit = 'HentaiWorldInfo'
        result = searchers.reddit_searcher()

        lewd = discord.Embed(description=f'**{str(result[0])}**', color=discord.Colour.random())
        lewd.set_author(name=f'/r{result[3]}', url=str(result[2]))
        lewd.set_image(url=str(result[1]))
        await ctx.send(embed=lewd)

    # r/HENTAI_GIF
    @commands.command()
    @commands.is_nsfw()
    async def hentaigif(self, ctx):

        searchers.reddit = 'HENTAI_GIF'
        result = searchers.reddit_searcher()

        lewd = discord.Embed(description=f'**{str(result[0])}**', color=discord.Colour.random())
        lewd.set_author(name=f'/r{result[3]}', url=str(result[2]))
        lewd.set_image(url=str(result[1]))
        await ctx.send(embed=lewd)

    # r/ElegantR34
    @commands.command(aliases=['er34'])
    @commands.is_nsfw()
    async def elegantr34(self, ctx):

        searchers.reddit = 'ElegantR34'
        result = searchers.reddit_searcher()

        lewd = discord.Embed(description=f'**{str(result[0])}**', color=discord.Colour.random())
        lewd.set_author(name=f'/r{result[3]}', url=str(result[2]))
        lewd.set_image(url=str(result[1]))
        await ctx.send(embed=lewd)

    # Gelbooru
    @commands.command(aliases=['gbooru'])
    @commands.is_nsfw()
    async def gelbooru(self, ctx, *, search: str):

        gbooru = Gelbooru(f'{api_key()}', f'{user_id()}')
        search = search.replace(' ', '_')

        results = await gbooru.search_posts(tags=[f'{search}'])
        url = str(results[random.randint(0, 50)])

        lewd = discord.Embed(color=discord.Colour.random())
        lewd.set_image(url=url)
        lewd.set_footer(text='Gelbooru')
        await ctx.send(embed=lewd)

    # Danbooru
    # Safebooru
    # Konachan
    # Sankaku Complex


# registra a classe no cogs
def setup(saturn):
    saturn.add_cog(NSFW(saturn))
